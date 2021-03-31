# VSPW-dataset-download


## Download Ground Truth Masks
Download ground truth masks using [Google Drive]() or [Baidu YunPan](). Decompress it to '/your/path/to/VSPW/folder/'.

## Download and Extract Video Frames

Edit video_download.sh, change VIDEO_SAVE_PATH to '/your/path/to/save/video' and change TARGET_PATH to '/your/path/to/VSPW/folder'.

```sh video_download.sh```


## Instruction

The structure of VSPW:
    |—— VSPW/
    |       |—— train.txt
    |       |—— val.txt
    |       |—— test.txt
    |       |—— label_num_dic_final.json
    |       |—— data/
    |           |—— video1/
    |               |—— origin/
    |                    |—— 00000001.jpg
    |                    |—— 00000002.jpg
    |                    ...
    |               |—— mask/
    |                    |—— 00000001.png
    |                    |—— 00000002.png
    |                    ...   
    |           |—— video2/
    |           ...      
          
               




Notation:  Our ground truth mask contains values from 0 to 124 and 255.  0 indicates "others" and 255 indicates "void label". During evaluation, both 0 and 255 are void class.  Thus we recommend using the following code:
