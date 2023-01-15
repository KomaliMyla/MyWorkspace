import moviepy
import moviepy.editor

video = moviepy.editor.VideoFileClip(r"C:\Users\mylak\Documents\mp4sample.mp4")
audio = video.audio
audio.write_audiofile("new_audio.mp3")
