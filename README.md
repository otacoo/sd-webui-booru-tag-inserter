# SD WebUI Booru Tag Inserter
A small extension to extract the tags from `Danbooru` / `Gelbooru` posts and insert them into the positive prompt textarea.

## How work?

Simply insert a `Danbooru` or `Gelbooru` URL into the extension field and press the big `Get Tags and Append` button.

The extension will fetch the **general**, **artist** and **character tags** and append them to the end of the positive prompt.\
For `Danbooru` the **Copyright** and **meta** tags are ignored.

## Fetching from Gelbooru

To fetch the tags from Gelbooru requires using their *API* and thus you need to have an account.\
In the settings menu of SD WebUI you can insert your API key and Gelbooru ID.

Go [here](https://gelbooru.com/index.php?page=account&s=options) to get your API key.\
Nothing is sent anywhere but from your WebUI to Gelbooru to fetch the image info so your credentials are safe.


## Notes

Only `Danbooru` and `Gelbooru` URLs are compatible.
