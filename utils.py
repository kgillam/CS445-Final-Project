import os
import cv2

# from utils provided in proj5
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