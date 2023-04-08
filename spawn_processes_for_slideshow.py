import signal
import time
from subprocess import Popen


process1 = Popen(["python", "speech_to_text.py"])
process2 = Popen(["python", "produce_realtime_slideshow.py"])
process3 = Popen(["python", "show_slideshow.py"])

while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        process1.send_signal(signal.SIGINT)
        process2.send_signal(signal.SIGINT)
        process3.send_signal(signal.SIGINT)
        raise
