import subprocess
import os
import sys
import whisper


def create_text_from_audio():
        model = whisper.load_model("base")
        options = { 'fp16': False, 'language': 'Yoruba', 'task': 'transcribe' }
        result = model.transcribe('video.mp3', **options)
        print(result["text"])

def convert_video_to_audio_ffmpeg(video_file, output_ext='mp3'):
    filename, ext = os.path.splitext(video_file)
    subprocess.call(['ffmpeg', '-y', '-i', video_file, f'{filename}.{output_ext}'],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT
                   )
    create_text_from_audio() #refactor to accept argument of file name


# if __name__ == '__main__':
#     vf = sys.argv[1]
convert_video_to_audio_ffmpeg('video.mp4')
