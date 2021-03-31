import os
import json
import sys
file_ = 'vspw_videolist.txt'

save_dir = sys.argv[1]
with open(file_) as f:
     lines= f.readlines()
count=0
videos=[]
for  line in lines:
    videos.append(line.split()[0])
print(len(videos))
#print(videos)
for v in videos:
    number = v.split('_')[0]   
    vname = v[len(number)+1:]
    print('downloading video:{}'.format(vname))
    for i in range(6): ##
        os.system("youtube-dl --ignore-errors --no-part  -o '{}/%(id)s.%(ext)s' '{}'".format(save_dir,vname))
    count+=1
print(count)
    

