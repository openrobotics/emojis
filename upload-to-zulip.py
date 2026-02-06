#!python3

import os.path
import sys
import zulip

client = zulip.Client(config_file="./zuliprc")

if len(sys.argv) < 2:
    print("Please specify the emoji filename")
    sys.exit(1)

emoji_name = os.path.splitext(os.path.basename(sys.argv[1]))[0]
with open(sys.argv[1], "rb") as emoji_file:
    result = client.call_endpoint(
        f"realm/emoji/{emoji_name}", method="POST", files=[emoji_file])
print(result)
