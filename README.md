# SD WebUI Booru Tag Inserter
A small extension to extract the tags from `Danbooru` / `Gelbooru` posts and insert them into the positive prompt textarea.

<img width="614" height="162" alt="Capture" src="https://github.com/user-attachments/assets/d818e504-6373-41cb-badd-25681c8f4bb6" />


## How work?

Simply insert a `Danbooru` or `Gelbooru` URL into the extension field and press the big `Get Tags and Append` button.

The extension will fetch the **general**, **artist** and **character tags** and append them to the end of the positive prompt.\
For `Danbooru` the **Copyright** and **meta** tags are ignored.

## Fetching from Gelbooru

To fetch the tags from Gelbooru requires using their *API* and thus you need to have an account.\
In the settings menu of SD WebUI you can insert your API key and Gelbooru ID.

<img width="506" height="300" alt="options" src="https://github.com/user-attachments/assets/b7e04224-8eb3-444f-a357-7cbc0a26a5c1" />

Go [here](https://gelbooru.com/index.php?page=account&s=options) to get your API key.\
Nothing is sent anywhere but from your WebUI to Gelbooru to fetch the image info so your credentials are safe.


## Notes

Only `Danbooru` and `Gelbooru` URLs are compatible.

