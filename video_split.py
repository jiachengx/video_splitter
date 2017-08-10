#!/usr/bin/python3
# multiple splitter for python 3 version
# 2017/08/10 

import subprocess,sys

if len(sys.argv) < 2:
    print("\nUsage:\n \t%s [clip text filename]\n" %(sys.argv[0]))
    sys.exit(1)

fn_clip = sys.argv[1]

with open(fn_clip) as fn:
    for line in fn.readlines():
        orig_video, output, start, end = line.strip().split(',')
        cmd = ["ffmpeg","-i",orig_video,"-flags","+global_header","-ss" ,start, "-to",end,"-c","copy", output]
        print("Process ... [%s]\n" %(output))
        subprocess.run(cmd,stderr=subprocess.STDOUT)
