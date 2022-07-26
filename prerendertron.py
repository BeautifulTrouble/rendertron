#!/usr/bin/env python

import requests

RENDERTRON_PORT = 3000

j = requests.get("https://api.beautifultrouble.org/api/v1/modules").json()

for tool in j:
    print(f"Fetching {tool['title']}...")
    requests.get(
        f"http://127.0.0.1:{RENDERTRON_PORT}/render/"
        f"https://beautifultrouble.org/toolbox/tool/{tool['slug']}?refreshCache=true"
    )
