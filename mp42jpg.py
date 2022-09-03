import sys
import ffmpeg

input_video = sys.argv[1]

ffmpeg.input(input_video).output("frame%003d.jpg").run()
