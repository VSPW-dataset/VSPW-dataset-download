VIDEO_SAVE_PATH='/your/path/to/save/video/'

TARGET_PATH='/your/path/to/VSPW/folder'


python download_hd.py $VIDEO_SAVE_PATH ####download hd videos


python generate_frames_multiprocess.py $VIDEO_SAVE_PATH $TARGET_PATH ###extract frames to vspw data folder

