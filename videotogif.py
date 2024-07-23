from moviepy.editor import *

video = VideoFileClip("f:/mummy phone's photos/mummy phone's photos/118bed22b326f47fa91eb0234d877451.mp4").subclip(00,5)
video.write_gif("Test2.gif")
