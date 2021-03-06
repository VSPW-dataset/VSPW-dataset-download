# VSPW-dataset-download


## We thank @sssdddwww2 who collected and extracted all frames. Please refer to her/his [page](https://github.com/sssdddwww2/vspw_dataset_download) to download the entire VSPW dataset.


## Download Ground Truth Masks
Download ground truth masks using [Google Drive](https://drive.google.com/file/d/1YnZvjYQyfWCpqTbyD5-MgfGZF3q_RK_6/view?usp=sharing) or [Baidu YunPan](https://pan.baidu.com/s/1K3SfFPpJ80GI-Lb5wDMLPg) (提取密码: tozq). Decompress it to *'/your/path/to/VSPW/folder/'*.




## Download and Extract Video Frames

Edit `video_download.sh`, change *VIDEO_SAVE_PATH* to *'/your/path/to/save/video'* and change *TARGET_PATH* to *'/your/path/to/VSPW/folder'*.

```sh video_download.sh```


## Instruction
![avatar](figures/figure1.png)
          
               




**Notice**:  Our ground truth mask contains values from 0 to 124 and 255.  0 indicates "others" and 255 indicates "void label". During evaluation, both 0 and 255 are void classes.  Thus we recommend using the following code:

```
label[label==0]=255
label=label-1
label[label==254]=255

```
