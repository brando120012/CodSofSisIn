import speech_recognition as sr
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip
from gtts import gTTS
from deep_translator import GoogleTranslator
import os

def get_wav_audio(mp4_file, wav_file):
    """Extract audio from mp4 video and save as wav file."""
    try:
        vc = VideoFileClip(mp4_file)
        ac = vc.audio
        ac.write_audiofile(wav_file, codec='pcm_s16le')
    except Exception as e:
        print(f"Error extracting audio: {e}")
    finally:
        if 'ac' in locals():
            ac.close()
        if 'vc' in locals():
            vc.close()

def audio_to_text(audio_file):
    """Convert audio file to English text using Google speech recognition."""
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio, language='en-US')
        return text
    except sr.UnknownValueError:
        return "unknown"
    except sr.RequestError as e:
        return f"Recognition request error: {e}"

def text_translate(text, target_lang='es'):
    """Translate text from English to target language (default Spanish)."""
    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
    return translated

def text_to_speech(text, lang, output_file):
    """Convert text to speech and save as mp3."""
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(output_file)

def add_audio_to_video(mp4_file, mp3_file, output_mp4_file):
    """Add audio to video and save as new video file."""
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
    output_video = "video_with_spanish_audio.mp4"

    # Step 1: Extract audio from video
    print(f"Extracting audio from {video_file}...")
    get_wav_audio(video_file, wav_file)

    # Step 2: Convert audio to English text
    print("Converting audio to text...")
    english_text = audio_to_text(wav_file)
    print("Recognized English text:", english_text)

    # Step 3: Translate English text to Spanish
    if english_text and english_text != "unknown":
        print("Translating text to Spanish...")
        spanish_text = text_translate(english_text, 'es')
        print("Translated Spanish text:", spanish_text)

        # Step 4: Convert translated text to speech
        print("Converting translated text to speech (mp3)...")
        text_to_speech(spanish_text, 'es', output_mp3)
        print(f"Saved Spanish speech audio as {output_mp3}")

        # Step 5: Add Spanish audio to original video
        print("Adding Spanish audio to video...")
        add_audio_to_video(video_file, output_mp3, output_video)
        print(f"Saved new video with Spanish audio as {output_video}")
    else:
        print("Could not recognize speech from audio. No translation or speech synthesis done.")

    # Optional: Cleanup temporary wav and mp3 files
    if os.path.exists(wav_file):
        os.remove(wav_file)
    if os.path.exists(output_mp3):
        os.remove(output_mp3)


