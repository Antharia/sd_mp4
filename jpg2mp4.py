import ffmpeg

input_images = "*.jpg"

ffmpeg.input(input_images, pattern_type="glob", framerate=25).output("output.mp4").run()
