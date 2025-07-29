import re
import requests
import gradio as gr
from modules import scripts, script_callbacks, shared
import contextlib
import html


def on_ui_settings():
    section = ('booru-tag-inserter', "Booru Tag Inserter")
    shared.opts.add_option("booru_tag_inserter_gelbooru_user_id", shared.OptionInfo("", "Gelbooru User ID", section=section))
    shared.opts.add_option("booru_tag_inserter_gelbooru_api_key", shared.OptionInfo("", "Gelbooru API Key", section=section))


def get_gelbooru_tags(post_id):
    user_id = shared.opts.data.get("booru_tag_inserter_gelbooru_user_id")
    api_key = shared.opts.data.get("booru_tag_inserter_gelbooru_api_key")

    headers = {'User-Agent': 'Booru-Tag-Inserter-For-SD-WebUI/1.0'}
    params = {
        'page': 'dapi',
        's': 'post',
        'q': 'index',
        'json': '1',
        'id': post_id,
    }
    if api_key and user_id:
        params['user_id'] = user_id
        params['api_key'] = api_key

    response = requests.get("https://gelbooru.com/index.php", params=params, headers=headers)

    if response.status_code != 200 or not response.text:
        return f"Error: Could not fetch from Gelbooru (status code: {response.status_code})."

    try:
        data = response.json()
        if "post" not in data or not data["post"]:
            return "No post found on Gelbooru with that ID."
        tags = data['post'][0]['tags']
        processed_tags = [html.unescape(tag).replace("_", " ").replace("(", "\\(").replace(")", "\\)") for tag in tags.split()]
        return ", ".join(processed_tags)
    except (requests.exceptions.JSONDecodeError, KeyError, IndexError):
        return "Error: Could not parse Gelbooru API response."


def get_danbooru_tags(post_id):
    headers = {'User-Agent': 'Booru-Tag-Inserter-For-SD-WebUI/1.0'}
    api_url = f"https://danbooru.donmai.us/posts/{post_id}.json"
    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        return f"Error: Could not fetch from Danbooru (status code: {response.status_code})."

    try:
        data = response.json()
        
        tags_to_get = ["tag_string_general", "tag_string_character", "tag_string_artist"]
        all_tags = []
        for key in tags_to_get:
            tag_string = data.get(key, '')
            if tag_string:
                all_tags.extend(tag_string.split())

        if not all_tags:
            return "No tags found for this Danbooru post in the specified categories."

        processed_tags = [html.unescape(tag).replace("_", " ").replace("(", "\\(").replace(")", "\\)") for tag in all_tags]
        return ", ".join(processed_tags)
    except requests.exceptions.JSONDecodeError:
        return "Error: Could not parse Danbooru API response."


def fetch_and_append_tags(url, current_prompt):
    if not url:
        return current_prompt

    gelbooru_match = re.search(r"gelbooru\.com/index\.php\?page=post&s=view&id=(\d+)", url)
    danbooru_match = re.search(r"danbooru\.donmai\.us/posts/(\d+)", url)

    tags_or_error = ""
    if gelbooru_match:
        post_id = gelbooru_match.group(1)
        tags_or_error = get_gelbooru_tags(post_id)
    elif danbooru_match:
        post_id = danbooru_match.group(1)
        tags_or_error = get_danbooru_tags(post_id)
    else:
        raise gr.Error("URL is not a valid Gelbooru or Danbooru post URL.")

    if tags_or_error.startswith("Error:"):
        raise gr.Error(tags_or_error)

    if not current_prompt:
        return tags_or_error
    else:
        return f"{current_prompt}, {tags_or_error}"


class BooruPromptsScript(scripts.Script):
    def title(self):
        return "Booru Tag Inserter"

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion(self.title(), open=False):
                url_input = gr.Textbox(label="Gelbooru/Danbooru URL", placeholder="e.g. https://danbooru.donmai.us/posts/...")
                fetch_button = gr.Button(value="Get Tags and Append", variant="primary")

        with contextlib.suppress(AttributeError):
            prompt_textbox = self.boxxIMG if is_img2img else self.boxx
            
            fetch_button.click(
                fn=fetch_and_append_tags,
                inputs=[url_input, prompt_textbox],
                outputs=[prompt_textbox]
            )

        return [url_input, fetch_button]

    def after_component(self, component, **kwargs):
        if kwargs.get("elem_id") == "txt2img_prompt":
            self.boxx = component
        if kwargs.get("elem_id") == "img2img_prompt":
            self.boxxIMG = component

script_callbacks.on_ui_settings(on_ui_settings)
