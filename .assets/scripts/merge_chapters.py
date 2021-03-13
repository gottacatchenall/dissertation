import subprocess
import json
import os
import glob

chapterFiles = sorted(glob.glob("./chapters/*.md"))

import yaml

def get_yaml(f):
  pointer = f.tell()
  if f.readline() != '---\n':
    f.seek(pointer)
    return ''
  readline = iter(f.readline, '')
  readline = iter(readline.__next__, '---\n')
  return ''.join(readline)




with open("manuscript.md", "a") as outfile:
    for cf in chapterFiles:
        with open(cf, "r") as f:
              config = list(yaml.load_all(get_yaml(f), Loader=yaml.SafeLoader))
              chTitle = config[0]["title"]
              chNum = int("".join(cf.split("/")[2]).split(".md")[0])    # python is a beautiful language
              header = ("# Chapter %d\n " % chNum) + "# " + (chTitle)
              text = f.read()

              this_chapter = header + "\n" + text + "\n\n"

              outfile.write(this_chapter)


    # interate over md files in chapters in order and put their title as a level 1 header
