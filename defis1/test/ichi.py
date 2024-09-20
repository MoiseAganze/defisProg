from moviepy.editor import VideoFileClip
import speech_recognition as sr


def extract_audio_from_video(video_path, audio_output_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(audio_output_path)

# Exemple d'utilisation
extract_audio_from_video("ma_video.mp4", "mon_audio.wav")


def convert_audio_to_text(audio_path):
    recognizer = sr.Recognizer()
    
    # Ouvrir le fichier audio
    with sr.AudioFile(audio_path) as source:
        audio_data = recognizer.record(source)
        
        # Transcrire l'audio en texte (utilise ici Google Speech Recognition)
        try:
            text = recognizer.recognize_google(audio_data, language="fr-FR")  # ou "en-US" pour l'anglais
            return text
        except sr.UnknownValueError:
            return "La reconnaissance vocale n'a pas pu comprendre l'audio."
        except sr.RequestError:
            return "Le service de reconnaissance vocale a échoué."

# Exemple d'utilisation
texte = convert_audio_to_text("mon_audio.wav")
print(texte)

from gtts import gTTS

def text_to_audio(text, output_file):
    # Convertir le texte en audio
    tts = gTTS(text=text, lang='fr')  # Utilise 'fr' pour le français ou 'en' pour l'anglais
    tts.save(output_file)
    print(f"Audio enregistré en tant que {output_file}")


text_to_audio(texte, "sortie_audio.mp3")

