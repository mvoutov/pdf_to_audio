from gtts import gTTS
import PyPDF2

def pdf_to_audio_gTTS(pdf_path, audio_path):
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            full_text = ""

            for page in pdf_reader.pages:
                full_text += page.extract_text() + " "

        tts = gTTS(text=full_text, lang='en')
        tts.save(audio_path)
    except Exception as e:
        print("An error occurred:", e)

# Usage example
pdf_to_audio_gTTS('aspray_kelly_ensmenger-inventing_the_computer.pdf', 'aspray_kelly_ensmenger-inventing_the_computer.mp3')

