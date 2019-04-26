# 3D Pose Estimation Using Detectron and VideoPose3D

VideoPose3D: Dario Pavllo, Christoph Feichtenhofer, David Grangier, and Michael Auli. [3D human pose estimation in video with temporal convolutions and semi-supervised training](https://arxiv.org/abs/1811.11742). In Conference on Computer Vision and Pattern Recognition (CVPR), 2019. [Github here](https://github.com/facebookresearch/VideoPose3D)

Detectron: Ross Girshick, Ilija Radosavovic, Georgia Gkioxari, Piotr Dollár and Kaiming He. [Detectron](https://github.com/facebookresearch/detectron), 2018

Based on the fork of VideoPose3D [here](https://github.com/tobiascz/VideoPose3D)

## Installation
### Cloning this Repo
A standard git clone will not clone the submodules, so do this command instead
- git clone --recurse-submodules -j8 https://github.com/TrySickle/3d-pose-estimation.git

### Detectron
- NVIDIA GPU, Linux, Python2
- Caffe2, pip for installing packages, COCO API
- CUDA 8.0, cuDNN 6.0.21

Refer to the Detectron repo's instructions [here](https://github.com/facebookresearch/Detectron/blob/master/INSTALL.md)

For easy use of Detectron, try this [colab notebook](https://colab.research.google.com/drive/1F3dwAGV8Igin1-_RuuNLfG00hrPJ_k-i)  
Follow instructions below if you want to use this notebook (maybe you are on Windows)  

### VideoPose3D
- Python3+
- PyTorch >= 0.4.0
- ffmpeg
- OpenCV
- various downloadable models, weights, config files described below

## Setup
1. Download this model to the configs folder of Detectron: [Download](https://www.dropbox.com/sh/vi5byf0du9g50lw/AABGVezeuHuipOzaFGdGGvbaa?dl=0&preview=model_final.pkl)
	- Final directory from the root is Detectron/configs/model_final.pkl
2. Download this checkpoint file to checkpoint folder of VideoPose3D (make folder if needed): [Download](https://dl.fbaipublicfiles.com/video-pose-3d/d-pt-243.bin)
	- Final directory VideoPose3D/checkpoint/d-pt-243.bin
3. Prepare data_3d_h36m.npz file in the data directory as described in the VideoPose3D docs: [Help](https://github.com/facebookresearch/VideoPose3D/blob/master/DATASETS.md#setup-from-preprocessed-dataset)

## Running
1. Find video on youtube, copy URL.
2. Determine start and stop times for the video in seconds (e.g. time 2:43 is 163 seconds)
3. Run run.py youtube_url start_time_in_seconds end_time_in_seconds name_of_data frames_to_skip output_directory
	- for example: python3 run.py https://www.youtube.com/watch?v=HEXWRTEbj1I 163 173 love 0 output
	- the name_of_data parameter is used to distinguish between intermediate and final outputs
	- the frames_to_skip parameter can be used if the output reconstruction lags behind the video

## Results
- Output video should be in the VideoPose3D/outputs folder
- Output 3D coordinates should be in VideoPose3D root

## Troubleshooting
- Open an issue on Github or message jlee3331@gatech.edu
- Check internal parameters in run.py (the script calls other scripts with command line args that can be modified)
- Check all installations are working

## Colab
Using colab requires you to download the video, split the frames, download the detectron model, and upload to drive  
1. Download youtube video, rename it something to identify it with, like golf.mp4, skating.mp4, etc
2. Create empty folder called frames to store output frames
3. Split into frames using ffmpeg -i video_name.mp4 -r 25/1 frames/output%04d.png
4. Download this model: [Download](https://www.dropbox.com/sh/vi5byf0du9g50lw/AABGVezeuHuipOzaFGdGGvbaa?dl=0&preview=model_final.pkl)
5. Make a folder called detectron_assets in your drive
6. Upload the frames folder, model_final.pkl, and infer_simple.py (found in Detectron/tools) to detectron_assets
7. Run the notebook, make sure to change the video name in the Detectron cell
8. Download the data_2d_detections_name file to the data folder of VideoPose3D
9. Copy the video to InTheWildData
10. python3 run_wild.py -k detections_golf -arc 3,3,3,3,3 -c checkpoint --evaluate d-pt-243.bin --render --viz-subject S1 --viz-action Directions --viz-video InTheWildData/golf.mp4 --viz-camera 0 --viz-output output_golf.mp4 --viz-size 5 --viz-downsample 1 --viz-skip 0
11. Change golf to whatever is appropriate
12. Outputs in outputs folder and in root
