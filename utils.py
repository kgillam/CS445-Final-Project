import os
import cv2
import numpy as np


def get_reference_distances_from_renamed_files(dir):
    files = sorted(os.listdir(dir))
    reference_distances = [int(i.split('.')[0]) for i in files]
    list_max = max(reference_distances)
    reference_distances = [list_max - i for i in reference_distances]
    estimated_distances = np.interp(reference_distances, (min(reference_distances), max(reference_distances)),(0, +255))
    estimated_distances = estimated_distances.astype(int)
    return estimated_distances

def get_reference_distances_from_original_files(dir):
    files = sorted(os.listdir(dir))
    num_frames = len(files)
    estimated_distances = [num_frames - i for i in range(num_frames)]
    estimated_distances = np.interp(estimated_distances, (min(estimated_distances), max(estimated_distances)),
                                    (0, +255))
    estimated_distances = estimated_distances.astype(int)
    return estimated_distances

def resize_im(im, scale_percent):
    width = int(im.shape[1] * scale_percent / 100)
    height = int(im.shape[0] * scale_percent / 100)
    return cv2.resize(im, (width, height))

# video2imageFolder is from utils provided in proj5
def video2imageFolder(input_file, output_path):
    '''
    Extracts the frames from an input video file
    and saves them as separate frames in an output directory.
    Input:
        input_file: Input video file.
        output_path: Output directorys.
    Output:
        None
    '''
    cap = cv2.VideoCapture()
    cap.open(input_file)

    if not cap.isOpened():
        print("Failed to open input video")

    frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    frame_idx = 0

    while frame_idx < frame_count:
        ret, frame = cap.read()
        if not ret:
            print ("Failed to get the frame {}".format(frame_idx))
            continue

        out_name = os.path.join(output_path, 'f{:04d}.jpg'.format(frame_idx+1))
        ret = cv2.imwrite(out_name, frame)
        if not ret:
            print ("Failed to write the frame {}".format(frame_idx))
            continue

        frame_idx += 1
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)