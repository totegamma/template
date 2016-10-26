#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path
import re


args = sys.argv #コマンドライン引数
filename = extension = args[1].split(".")[0]
extension = args[1].split(".")[-1]

target = open(args[1], 'w')

if(os.path.isfile(extension + ".temp")):
    template = open(extension + ".temp", 'r')
    for line in template:
        replacedLine = line.replace("<#filename#>", filename)
        replacedLine = line.replace("<#FILENAME#>", filename.upper())
        target.write(replacedLine)
