# VSPW-dataset-download


## Download Ground Truth Masks
Download ground truth masks using [Google Drive]() or [Baidu YunPan](). Decompress it to '/your/path/to/VSPW/folder/'.

## Download and Extract Video Frames

Edit video_download.sh, change VIDEO_SAVE_PATH to '/your/path/to/save/video' and change TARGET_PATH to '/your/path/to/VSPW/folder'.

```sh video_download.sh```


## Instruction
![avatar](figures/figure1.png)
          
               




Notation:  Our ground truth mask contains values from 0 to 124 and 255.  0 indicates "others" and 255 indicates "void label". During evaluation, both 0 and 255 are void class.  Thus we recommend using the following code:

```
label[label==0]=255
label=label-1
label[label==254]=255

```
