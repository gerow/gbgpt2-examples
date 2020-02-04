#!/usr/bin/python3

import os
import sys

if __name__ == '__main__':
    out = 'examples'

    games = sys.stdin.read().split('====================')
    games = games[1:]

    os.mkdir(out)
    for i in range(len(games)):
        o = games[i].strip()
        o = o.strip('===')
        o = o.strip()
        o = "# "+o
        with open(os.path.join(out, str(i).zfill(3)+'.md'), 'w') as f:
            f.write(o)
