#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import re


args = sys.argv #コマンドライン引数
if(len(sys.argv) == 1):
    print("ファイル名を書けつってんの")
    sys.exit()
filename = extension = args[1].split(".")[0]
extension = args[1].split(".")[-1]

target = open(args[1], 'w')


if(os.path.isfile(os.environ['HOME'] + "/.templates/" + extension + ".temp")):
    templatePath = os.environ['HOME'] + "/.templates/" + extension + ".temp"
elif(os.path.isfile("templates/" + extension + ".temp")):
    templatePath = "templates/" + extension + ".temp"

if 'templatePath' in locals():
    template = open(templatePath, 'r')
    for line in template:
        replacedLine = line.replace("<#filename#>", filename)
        replacedLine = replacedLine.replace("<#FILENAME#>", filename.upper())
        target.write(replacedLine)
