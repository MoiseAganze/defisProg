from moviepy.editor import VideoFileClip,AudioFileClip
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator

def extract_audio_from_video(video_path, audio_output_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_output_path)



def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        
        try:
            text = recognizer.recognize_google(audio_data, language="fr-FR") 
            return text
        except sr.UnknownValueError:
            return "La reconnaissance vocale n'a pas pu comprendre l'audio."
        except sr.RequestError:
            return "Le service de reconnaissance vocale a échoué."



def traduct_text(text,lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=lang)
    return translated_text


def text_to_audio(text, output_file,lang):
    tts = gTTS(text=text, lang=lang) 
    tts.save(output_file)
    print(f"Audio enregistré en tant que {output_file}")


def combine_video_with_audio(video_path, audio_path, output_video_path):
    video = VideoFileClip(video_path)
    new_audio = AudioFileClip(audio_path)
    final_video = video.set_audio(new_audio)
    final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")


extract_audio_from_video("ma_video.mp4", "mon_audio.wav")
texte = convert_audio_to_text("mon_audio.wav")
print(texte)
transtext=traduct_text(texte,'en').text
print(transtext)
text_to_audio(transtext, "sortie_audio.mp3",'en')
combine_video_with_audio("ma_video.mp4","sortie_audio.mp3","sortie_video.mp4")