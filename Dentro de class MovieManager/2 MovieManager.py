import speech_recognition as sr
from moviepy.editor import VideoFileClip, AudioFileClip

def get_wav_audio(mp4_file, wav_file):
    vc = VideoFileClip(mp4_file)  # Pasar el archivo MP4 al constructor
    ac = vc.audio
    ac.write_audiofile(wav_file, codec='pcm_s16le')  # Corregir el codec
    ac.close()
    vc.close()

def audio_to_total_text(audio_file):
    r = sr.Recognizer()  # Corregir el nombre de la clase
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  # Corregir el método

    try:
        text = r.recognize_google(audio)  # Corregir el método
        return text
    except:  # Capturar la excepción correctamente
        return 'unknown'