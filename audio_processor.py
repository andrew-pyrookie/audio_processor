#import cv2
#OpenCV to read the video file and extract the audio track.

#mport ffmpeg
#ffmpeg-python to extract audio from a video file.

from pydub import AudioSegment
#PyDub to load and manipulate audio data, and to concatenate audio data from multiple audio files.

from moviepy.editor import VideoFileClip,AudioFileClip,concatenate_audioclips

media = input("Enter path to media ; ")
#path or make sure  there are on same folder

print('')

def check_media(media):
    try:
        video = VideoFileClip(media)
        print("Input file is a video file.")
        print("Video duration:", video.duration, "seconds")
        return 'video'
    except OSError:
        audios = AudioFileClip(media)
        print("Input file is an audio file.")
        print("Audio duration:", audios.duration, "seconds")
        return 'audio'
check_media(media)

media_type = check_media(media)


print('')

if media_type=='video':
    audio = VideoFileClip(media).audio
    print('')
    ans = input("Do you want to save the Audio file 's' or go ahead and just concatenate with other audio 'enter' ? : ")
    print('')
    if ans.lower() == 's':

        name = input("How do you want to name the audio file : ")
        print('')
        destination = input("Enter destination path to save the audio file : ")
        print('')
        audio.write_audiofile(f'{destination}/{name}.mp3')

    else:
        audio1 = AudioFileClip(audio)
        print('')
        audios2 = input("Audio 2 path : ")
        audio2 = AudioFileClip(audios2)
        final_name = input("What do you want to name the audio : ")
        print('')
        destination = input("Enter destination path to save the audio file : ")
        print('')
        final_audio = concatenate_audioclips([audio1,audio2])
        final_audio.write_audiofile(f"{destination}/{final_name}.mp3")













