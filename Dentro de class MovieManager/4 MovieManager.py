import speech_recognition as sr
from moviepy.editor import VideoFileClip

def extract_audio_from_video(mp4_file, wav_file):
    """
    Extract audio from video file and save as WAV.
    """
    video_clip = VideoFileClip(mp4_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(wav_file, codec='pcm_s16le')
    audio_clip.close()
    video_clip.close()

def transcribe_audio(wav_file):
    """
    Transcribe speech from audio file to text using Google's speech recognition API.
    """
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "No se pudo entender el audio."
    except sr.RequestError as e:
        return f"No se pudo solicitar resultados del servicio de reconocimiento de voz; {e}"

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Uso: python video_to_text.py <video_file.mp4>")
        sys.exit(1)

    video_path = sys.argv[1]
    wav_path = "extracted_audio.wav"

    print(f"Extrayendo audio de {video_path} ...")
    extract_audio_from_video(video_path, wav_path)
    print("Audio extraído.")

    print("Transcribiendo audio...")
    transcription = transcribe_audio(wav_path)
    print("Resultado de la transcripción:")
    print(transcription)


