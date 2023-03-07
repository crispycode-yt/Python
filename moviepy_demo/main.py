import moviepy.editor as mp

clip1 = mp.VideoFileClip("video1.mp4")
clip2 = mp.VideoFileClip("video2.mp4")

merged = mp.concatenate_videoclips([clip1, clip2])
merged.write_videofile("merged_video.mp4")