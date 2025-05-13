import speech_recognition as sr
from moviepy.editor import VideoFileClip, AudioFileClip
class MovieManager:

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
        except Exception as e:  # Capturar la excepción correctamente
            return 'unknown'
        
    def get_wav_audio(self, mp4_file, wav_file):
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(wav_file, codec = 'pcm_s16le')
        ac.close()
        vc.close()

    def audio_total_text(self, audio_file):
        r = sr.Recognizer()
        with sr.AudioFile (audio_file) as source :
            audio = r.record(source)

        try:
            text = r.recognize_google(audio)
            return text
        except:
            return 'unknow'

mm = MovieManager()
#mm.get_wav_audio('video.mp4', 'audio.wav')
speech = mm.audio_total_text('audio.wav')
print(speech)