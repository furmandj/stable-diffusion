import time
import glob

import cv2
import numpy as np

image = None
old_image = None
old_image_dir = ''
while True:
    image_dirs = glob.glob('outputs/txt2img-samples/*')
    if len(image_dirs) < 2:
        time.sleep(1)
        continue
    image_dirs.sort()
    image_dir = image_dirs[-2]
    image_files = glob.glob(f'{image_dir}/*.png')
    image_files.sort()
    image_file = image_files[-1]
    image = cv2.imread(image_file)
    if old_image is None or image_dir == old_image_dir:
        # Display the image
        cv2.imshow('Real Time Image Display', image.astype(np.uint8))
        # Exit if 'q' key is pressed
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        # Do a smooth transition to the new image
        n_transition_frames = 100
        for i in range(1, n_transition_frames + 1):
            beta = i / n_transition_frames
            alpha = 1 - beta
            new_image = cv2.addWeighted(old_image, alpha, image, beta, 0)
            cv2.imshow('Real Time Image Display', new_image.astype(np.uint8))
            time.sleep(0.02)
            # Exit if 'q' key is pressed
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break
    old_image_dir = image_dir
    old_image = image.copy()
    time.sleep(0.1)


# close all windows
cv2.destroyAllWindows()
