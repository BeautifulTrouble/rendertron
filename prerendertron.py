#!/usr/bin/env python

import requests

RENDERTRON_PORT = 3000


j = requests.get("https://api.beautifultrouble.org/v2/en/toolbox.json").json()

for slug, tool in j["tools"].items():
    for lang in tool["langs"]:
        print(f"Rendering {tool['title']} ({lang})")
        requests.get(
            f"http://127.0.0.1:{RENDERTRON_PORT}/render/"
            + "https://beautifultrouble.org/toolbox/"
            + ("" if lang == "en" else f"{lang}/")
            + f"{slug}?refreshCache=true"
        )
