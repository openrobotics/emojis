#!/usr/bin/env python3

import zulip

client = zulip.Client(config_file="./zuliprc")
result = client.get_realm_emoji()
names = []
for e in result["emoji"]:
    emoji = result["emoji"][e]
    names.append(emoji["name"])
names.sort()
for n in names:
    print(n)
