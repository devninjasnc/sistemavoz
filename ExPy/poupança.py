import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
import threading
import customtkinter

rec = sr.Recognizer()
engine = pyttsx3.init()

def capturar_audio(entry):
    with sr.Microphone() as source:
        print("Diga algo...")
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        try:
            texto = rec.recognize_google(audio, language='pt-BR')
            entry.insert(tk.END, texto)  # Inserir o texto reconhecido na entrada
        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
        except sr.RequestError as e:
            print(f"Erro ao chamar o serviço de reconhecimento de fala; {e}")

def iniciar_reconhecimento(entry1, entry2):
    entry1.focus_set()  # Definir o foco na primeira entrada para capturar o áudio diretamente
    capturar_audio(entry1)  # Chamar a função de captura de áudio para a primeira entrada
    entry2.focus_set()  # Definir o foco na segunda entrada
    capturar_audio(entry2)  # Chamar a função de captura de áudio para a segunda entrada

janela = tk.Tk()
# Código para configurar a janela principal...

# Criar as duas entradas do customtkinter
entrada_custom1 = customtkinter.CTkEntry(master=janela, width=100)
entrada_custom1.pack()

entrada_custom2 = customtkinter.CTkEntry(master=janela, width=100)
entrada_custom2.pack()

# Chamar a função de captura de áudio assim que a janela for aberta
janela.after(100, lambda: iniciar_reconhecimento(entrada_custom1, entrada_custom2))

janela.mainloop()
