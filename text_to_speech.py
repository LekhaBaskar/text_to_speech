import tkinter as tk
import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio_data = recognizer.listen(source)
        try:
            recognized_text = recognizer.recognize_google(audio_data)
            text_output.config(text=f"Recognized Text: {recognized_text}")
        except sr.UnknownValueError:
            text_output.config(text="Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            text_output.config(text=f"Error occurred: {e}")

root = tk.Tk()
root.title("Speech to Text Converter")
text_output = tk.Label(root, text="", font=("Arial", 14))
text_output.pack(pady=20)
convert_button = tk.Button(root, text="Start", font=("Arial", 10), command=speech_to_text)
convert_button.pack(pady=10)

root.mainloop()
