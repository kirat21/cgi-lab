#!/usr/bin/env python3

import os
import json

print("Content-Type: application/json")
print()

print(json.dumps(dict(os.environ)))
print()

# q = os.environ["QUERY_STRING"]
# print(q)
print()