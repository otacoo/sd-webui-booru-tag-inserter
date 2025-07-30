# SD WebUI Booru Tag Inserter :label:
A small extension to extract the tags from `Danbooru` / `Gelbooru` posts and insert them into the positive prompt textarea.

<img width="614" height="162" alt="Capture" src="https://github.com/user-attachments/assets/e5b47b0a-05e2-427f-b1c8-441d2a8648db" />


## How work?

Simply insert a `Danbooru` or `Gelbooru` URL into the extension field and press the big `Get Tags and Append` button.

### For Danbooru
The extension will fetch the **general**, **artist** and **character tags** and append them to the end of the positive prompt.\
The **copyright** and **meta** tags are ignored by default.

### For Gelbooru

To fetch the tags from Gelbooru requires using their *API* and thus you need to have an account.\
In the settings menu of SD WebUI you can insert your API key and Gelbooru ID.

Go [here](https://gelbooru.com/index.php?page=account&s=options) to get your Gelbooru API key.\
Nothing is sent anywhere but between your WebUI instance and Gelbooru to fetch the image info so your credentials are safe.

### Excluding Tags
The settings menu allows one to set any tags, separated by comma, to be excluded when fetching tags. This will work for both sites.

<img width="604" height="255" alt="options" src="https://github.com/user-attachments/assets/b5a7e886-0374-428f-b84c-45d0b51ee77c" />


## SD WebUI Installation

1. Go into `Extensions` tab > `Install from URL`
2. Paste `https://github.com/otacoo/sd-webui-booru-tag-inserter.git`
3. Press Install
4. Apply and Restart the UI


## Notes

Only `Danbooru` and `Gelbooru` URLs are compatible.

