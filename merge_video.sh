#!/bin/bash

#fix audio sync problem
for file in *.mp4; do
	ffmpeg -i $file -q 0 $file.mts
done

#generate file list
for file in *.mts;
	do echo "file $file" >> mylist.txt
done

#ffmpeg merge videos
ffmpeg -f concat -safe 0 -i mylist.txt -c copy output.mp4

rm *.mts