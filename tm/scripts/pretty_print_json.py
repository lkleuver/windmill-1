#!/usr/bin/env python

import json
import sys

json.dump(json.load(sys.stdin), sys.stdout, indent=4, separators=(',', ': '))
