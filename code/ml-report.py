#! /usr/bin/env python3

# Summarizes the content of pip wheels

import sys
import zipfile
import os
from collections import defaultdict
from typing import Dict, Tuple



def summarize(whl: str) -> Dict[str, Tuple[int,int,str]]:
    """Analyze the number and type of files in the zip file. """
    with zipfile.ZipFile(whl, "r") as f:
        exts = defaultdict(lambda : [0,0,""])
        for info in f.infolist():
            filename, ext = os.path.splitext(info.filename)
            exts[ext][0] += 1
            if info.file_size > exts[ext][1]:
                exts[ext][1] = info.file_size
                exts[ext][2] = info.filename
        return exts

if __name__ == "__main__":
    summary = summarize(sys.argv[1])
    discard = set(['.text', '.TXT', '.txt', '.md', '.MPL2', '.zip', '.typed'])
    print("[")

    for (i,(ext,(count,size,name))) in enumerate(summary.items()):
        if ext and not ext in discard:
            if i>0:
                print(",")
            print(f'{{ "ext":"{ext}", "count":{count}, "name": "{name}", "size": {size/1024:.2f} }}')
    print("]")
