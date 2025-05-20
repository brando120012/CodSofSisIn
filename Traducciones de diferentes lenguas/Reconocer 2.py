import speech_recognition as sr
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from gtts import gTTS
from deep_translator import GoogleTranslator
import os

def get_wav_audio(mp4_file, wav_file):
    """Extrae el audio de un video mp4 y lo guarda como archivo wav."""
    try:
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(wav_file, codec='pcm_s16le')
    except Exception as e:
        print(f"Error extrayendo el audio: {e}")
    finally:
        if 'ac' in locals():
            ac.close()
        if 'vc' in locals():
            vc.close()

def audio_to_text(audio_file):
    """Convierte un archivo de audio a texto en español usando el reconocimiento de voz de Google."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language='es-ES')
        return text
    except sr.UnknownValueError:
        return "unknown"
    except sr.RequestError as e:
        return f"Error en la solicitud de reconocimiento: {e}"

def text_translate(text, target_lang='ru'):
    """Traduce el texto desde español al idioma objetivo (por defecto ruso)."""
    translated = GoogleTranslator(source='es', target=target_lang).translate(text)
    return translated

def text_to_speech(text, lang, output_file):
    """Convierte el texto a voz y lo guarda como archivo mp3."""
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_file)

def add_audio_to_video(mp4_file, mp3_file, output_mp4_file):
    """Agrega audio a un video y lo guarda como un nuevo archivo."""
    videoclip = VideoFileClip(mp4_file)
    audioclip = AudioFileClip(mp3_file)

    new_audioclip = CompositeAudioClip([audioclip])
    videoclip.audio = new_audioclip
    videoclip.write_videofile(output_mp4_file)

    audioclip.close()
    videoclip.close()

if __name__ == "__main__":
    video_file = "video.mp4"
    wav_file = "extracted_audio.wav"
    output_mp3 = "translated_output.mp3"
    output_video = "video_with_russian_audio.mp4"

    # Paso 1: Extraer el audio del video
    print(f"Extrayendo audio de {video_file}...")
    get_wav_audio(video_file, wav_file)

    # Paso 2: Convertir el audio a texto en español
    print("Convirtiendo audio a texto (español)...")
    spanish_text = audio_to_text(wav_file)
    print("Texto reconocido en español:", spanish_text)

    # Paso 3: Traducir el texto en español al ruso
    if spanish_text and spanish_text != "unknown":
        print("Traduciendo texto al ruso...")
        russian_text = text_translate(spanish_text, 'ru')
        print("Texto traducido al ruso:", russian_text)

        # Paso 4: Convertir el texto traducido a voz
        print("Convirtiendo el texto traducido a voz (mp3)...")
        text_to_speech(russian_text, 'ru', output_mp3)
        print(f"Audio en ruso guardado como {output_mp3}")

        # Paso 5: Agregar el audio ruso al video original
        print("Agregando audio ruso al video...")
        add_audio_to_video(video_file, output_mp3, output_video)
        print(f"Nuevo video con audio en ruso guardado como {output_video}")
    else:
        print("No se pudo reconocer el habla del audio. No se realizó la traducción ni la síntesis de voz.")

    # Opcional: Limpiar archivos temporales wav y mp3
    if os.path.exists(wav_file):
        os.remove(wav_file)
    if os.path.exists(output_mp3):
        os.remove(output_mp3)
