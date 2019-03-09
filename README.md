Video_splitter
==============

Split one long video file into multiple shorter video clip using ffmpeg
-----------------------------------------------------------------------
# Usage
  In clip text file, please input your requirement and follow this format

Film file:

    format for bash: [original_video filename output filename start_time end_time]
  
    format for python: [original_video,filename,output,filename,start_time,end_time]

Example File (clip):

    [Bash] 2017-08-06-13-33-49.mp4 d8.mp4 00:40:25 01:02:40

    [Python] 2017-08-06-13-33-49.mp4,d8.mp4,00:40:25,01:02:40
