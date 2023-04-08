import os
import time

transcript_filename = 'outputs/transcript.txt'
last_output = 'A shiny black tesla model 3'
text = last_output
seed = 0
while True:
    if os.path.exists(transcript_filename):
        with open(transcript_filename, 'r') as f:
            lines = f.readlines()
            if len(lines) > 0:
                text = lines[-1].replace('\n', '')
    if text != last_output:
        print(text)
        last_output = text
        seed += 1
        cmd = f'python optimizedSD/optimized_txt2img.py --prompt "{text}" ' \
              f'--H 512 --W 512 --seed {seed} --n_iter 1 --n_samples 1 --ddim_steps 15'
        err = os.system(cmd)
        if err:
            raise RuntimeError(f'Error running command: {cmd}')
    else:
        print('Waiting for speech...')
        time.sleep(1)
