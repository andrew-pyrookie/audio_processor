import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_audioclips
from pydub import AudioSegment

media = input("Enter path to media: ")

def check_media(media):
    if not os.path.isfile(media):
        raise ValueError("File does not exist!")
    ext = os.path.splitext(media)[1].lower()
    if ext in ['.mp4', '.avi', '.mov', '.mkv']:
        return 'video'
    elif ext in ['.mp3', '.wav']:
        return 'audio'
    else:
        raise ValueError("Unsupported file format!")

media_type = check_media(media)

if media_type == 'video':
    audio = VideoFileClip(media).audio
    ans = input("Do you want to save the Audio file 's' or go ahead and just concatenate with other audio 'enter' ? : ")
    if ans.lower() == 's':
        name = input("How do you want to name the audio file: ")
        destination = input("Enter destination path to save the audio file: ")
        audio.write_audiofile(f'{destination}/{name}.mp3')
    else:
        audio1 = audio
        audio2 = AudioFileClip(input("Enter the path to the second audio file: "))
        final_name = input("Enter the name of the final audio file: ")
        destination = input("Enter the destination path to save the final audio file: ")
        final_audio = concatenate_audioclips([audio1, audio2])
        final_audio.write_audiofile(f"{destination}/{final_name}.mp3")
else:
    audio1 = AudioSegment.from_file(media)
    audio2 = AudioSegment.from_file(input("Enter the path to the second audio file: "))
    final_name = input("Enter the name of the final audio file: ")
    destination = input("Enter the destination path to save the final audio file: ")
    final_audio = audio1 + audio2
    final_audio.export(f"{destination}/{final_name}.mp3", format="mp3")
