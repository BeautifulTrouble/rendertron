#!/usr/bin/env python

import requests

RENDERTRON_PORT = 3000
TOOL_URL = "https://beautifultrouble.org/toolbox/tool"

j = requests.get("https://api.beautifulrising.org/api/v1/modules").json()

for tool in j:
    print(f"Fetching {tool['title']}...")
    requests.get(f"http://127.0.0.1:{RENDERTRON_PORT}/render/{TOOL_URL}/{tool['slug']}")