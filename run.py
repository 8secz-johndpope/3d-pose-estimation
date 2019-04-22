from __future__ import unicode_literals
from subprocess import call, check_output
import platform
import argparse
import youtube_dl
import os
import cv2
from utils import get_time_string

def preprocess_video(youtube, start, end, name):
    try:
        os.makedirs("temp")
    except FileExistsError:
        # directory already exists
        pass

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': 'temp/video.mp4'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube])

    start = get_time_string(int(start))
    end = get_time_string(int(end))
    print("Cutting video from {} to {}".format(start, end))
    call(['ffmpeg', '-ss', start, '-i', 'temp/video.mp4', '-to', end, '-c', 'copy', 'temp/' + name + '.mp4'])

    try:
        os.makedirs("frames")
    except FileExistsError:
        # directory already exists
        pass
    call(['ffmpeg', '-i', 'temp/' + name + '.mp4', '-r', '25/1', 'frames/output%04d.png'])

def detectron(name):
    call(['python3', 'Detectron/tools/infer_simple.py', 
        '--cfg', 'Detectron/configs/12_2017_baselines/e2e_keypoint_rcnn_R-101-FPN_s1x.yaml',
        '--output-dir', 'VideoPose3D/data',
        '--image-ext', 'png',
        '--wts', 'Detectron/configs/model_final.pkl',
        '--output-ext', 'jpg',
        '--name', name,
        'frames'])

def videopose(name, skip):
    file_path = "temp/" + name + ".mp4"
    vid = cv2.VideoCapture(file_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
    call(['python3', 'VideoPose3D/run_wild.py', 
        '-k', 'detections_' + name,
        '-arc', '3,3,3,3,3',
        '-c', 'checkpoint',
        '--evaluate', 'd-pt-243.bin',
        '--render',
        '--viz-subject', 'S1',
        '--viz-action', 'Directions',
        '--viz-video', 'InTheWildData/' + name + '.mp4',
        '--viz-camera', '0',
        '--viz-output', 'output_' + name + '.mp4',
        '--viz-size', '5',
        '--viz-downsample', '1',
        '--viz-skip', skip])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("youtube", help="youtube source video url")
    parser.add_argument("start", help="video start time in seconds, e.g. 2 minutes 24 seconds = 144")
    parser.add_argument("end", help="video end time in seconds")
    parser.add_argument("name", help="give files a tag, e.g. a video about golf can be named golf")
    parser.add_argument("skip", help="number of frames to skip in beginning")
    args = parser.parse_args()
    print(args)

    print("Beginning video preprocessing...")
    preprocess_video(args.youtube, args.start, args.end, args.name)
    print("Finished video preprocessing!")

    print("Beginning 2D detections...")
    detectron(args.name)
    print("Finished 2D detections!")

    print("Beginning 3D reconstruction")
    videopose(args.name, args.skip)
    print("Finished 3D reconstruction!")
