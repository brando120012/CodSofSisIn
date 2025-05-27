import speech_recognition as sr
from moviepy.editor import VideoFileClip, AudioClip, CompositeAudioClip

class MovieManager:

    def get_wav_audio(self, mp4_file, wav_file):  # Indentar correctamente y agregar self
        vc = VideoFileClip(mp4_file)  # Pasar el archivo MP4 al constructor
        ac = vc.audio
        ac.write_audiofile(wav_file, codec='pcm_s16le')  # Corregir el codec
        ac.close()
        vc.close()

# Crear una instancia de MovieManager
mm = MovieManager()

# Llamar al método get_wav_audio con los archivos correspondientes
mm.get_wav_audio('input_video.mp4', 'output_audio.wav')  # Asegúrate de proporcionar los nombres de archivo correctos

def audio_to_total_text(audio_file):
    r = sr.Recognizer()  # Corregir el nombre de la clase
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)  # Corregir el método

    try:
        text = r.recognize_google(audio)  # Corregir el método
        return text
    except Exception as e:  # Capturar la excepción correctamente
        return 'unknown'
