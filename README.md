# Paevireservini
This repository contains code for the Instagram page @paevireservini.
## Explanation
- Scrape a random background image from https://pildid.mil.ee
- Generate an image for the Instagram post.
- Upload it using the Meta Graph API for Instagram.

```docker build -t paevireservini .
docker run -p 8080:8080 --restart=always --env-file ./env.list -d paevireservini
```