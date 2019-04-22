# 3D Pose Estimation Using Detectron and VideoPose3D

VideoPose3D: Dario Pavllo, Christoph Feichtenhofer, David Grangier, and Michael Auli. [3D human pose estimation in video with temporal convolutions and semi-supervised training](https://arxiv.org/abs/1811.11742). In Conference on Computer Vision and Pattern Recognition (CVPR), 2019. [Github here](https://github.com/facebookresearch/VideoPose3D)

Detectron: Ross Girshick, Ilija Radosavovic, Georgia Gkioxari, Piotr Dollár and Kaiming He. [Detectron](https://github.com/facebookresearch/detectron), 2018

Based on the fork of VideoPose3D [here](https://github.com/tobiascz/VideoPose3D)

## Installation
### Detectron
- NVIDIA GPU, Linux, Python2
- Caffe2, pip for installing packages, COCO API
- CUDA 8.0, cuDNN 6.0.21

Refer to the Detectron repo's instructions [here](https://github.com/facebookresearch/Detectron/blob/master/INSTALL.md)

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