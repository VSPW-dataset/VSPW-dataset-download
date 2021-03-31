import os
import shutil
from multiprocessing import Pool
import sys
count=0
dic={}
with open('vspw_videolist.txt','r') as f:
    lines = f.readlines()
for line in sorted(lines):
    v_name_num = line.split()[0]

    num = v_name_num.split('_')[0]
    v_name =v_name_num[len(num)+1:]

    _,start_time,end_time = line.split()
    start_time = int(start_time)
    end_time = int(end_time)

    dic[v_name]=(start_time,end_time,v_name_num)

###
###
DIR=sys.argv[1]
TARGET_DIR=sys.argv[2]

def extract_frames(v):
    
    v_name,suf = v.split('.')
    print(v_name)
#    suf = suf[:-1]

    origin_dir = os.path.join(TARGET_DIR,'origin_frames',v_name)
    if not os.path.exists(origin_dir):
        os.makedirs(origin_dir)
    start_time,end_time,v_name_num = dic[v_name]
    os.system("ffmpeg -i {}/{}.{} -q:v 4 -r 15 -f image2 {}/origin_frames/{}/%08d.jpg".format(DIR,v_name,suf,TARGET_DIR,v_name))
    if not os.path.exists(os.path.join(TARGET_DIR,'data',v_name_num,'origin')):
        os.makedirs(os.path.join(TARGET_DIR,'data',v_name_num,'origin'))

    for img in sorted(os.listdir(origin_dir)):
        frame_count = int(img.split('.')[0])
        if frame_count>=start_time and frame_count<=end_time:
            shutil.copy(os.path.join(origin_dir,img),os.path.join(TARGET_DIR,'data',v_name_num,'origin'))

    shutil.rmtree(origin_dir)
    print('*'*100)


p = Pool(8)

videos = os.listdir(DIR)
for v in sorted(videos):
    p.apply_async(extract_frames, args=(v,))
print('Waiting for all subprocesses done...')
p.close()
p.join()
    
        
        
        
        
