import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
import threading
import customtkinter
import time

rec = sr.Recognizer()

def falar():
    engine = pyttsx3.init()
    engine.say('''Olá, me chamo Júlia''')
    engine.runAndWait()

# Criação da janela principal
janela = tk.Tk()

# Define as dimensões da janela
largura = 1366
altura = 768
janela.geometry(f"{largura}x{altura}")
janela.title('SESC IPARANA')

# Carregamento e exibição da imagem em tela cheia
imagem_principal = Image.open("magens\iparan.png")
imagem_principal = imagem_principal.resize((largura, altura))
imagem_principal_tk = ImageTk.PhotoImage(imagem_principal)

label_imagem_principal = tk.Label(janela, image=imagem_principal_tk)
label_imagem_principal.pack()


def criar_janela_secundaria():
    janela_secundaria = tk.Toplevel()
    janela_secundaria.title('Janela Secundária')
    largura = 1366
    altura = 768
    janela_secundaria.geometry(f"{largura}x{altura}")
    janela_secundaria.title('SESC IPARANA2')
    # IMAGEM DE FRAME
    img1 = ImageTk.PhotoImage(file='magens\eservapagin.png')
    l1 = customtkinter.CTkLabel(master=janela_secundaria, image=img1)
    l1.pack()
    nomeentrada = customtkinter.CTkEntry(master=janela_secundaria, width=100, height=200, placeholder_text="Digite seu nome:")
    nomeentrada.place(x=100, y=60)
    cpf = customtkinter.CTkEntry(master=janela_secundaria, width=100, placeholder_text="Digite seu cpf:")
    cpf.place(x=200, y=60)
    def capturaraudio(entry):
        engine = pyttsx3.init()
        engine.say('''Diga seu nome:''')
        engine.runAndWait()
        with sr.Microphone() as source:
            rec.adjust_for_ambient_noise(source)
            audio = rec.listen(source)
            try:
                transnome = rec.recognize_google(audio, language='pt-BR')
                entry.insert(tk.END, transnome)
            except sr.UnknownValueError:
                print("Não foi possível reconhecer o áudio.")
            except sr.RequestError as e:
                print(f"Erro ao chamar o serviço de reconhecimento de fala: {e}")
            else:
                print('erro')
    def capturaraudio2(entry2):
        engine = pyttsx3.init()
        engine.say('''Diga seu cpf:''')
        engine.runAndWait()
        with sr.Microphone() as source:
            rec.adjust_for_ambient_noise(source)
            audio2=rec.listen(source)
            try:
                transcpf=rec.recognize_google(audio2,language='pt-BR')
                entry2.insert(tk.END,transcpf)
            except sr.UnknownValueError:
                print('Não consegui escutar nada')
            except sr.RequestError:
                print('Erro ao chamar a ia')


                


            



                
    def iniciar_reconhecimento(entry1,cpf):
        entry1.focus_set()  # Definir o foco na primeira entrada para capturar o áudio diretamente
        capturaraudio(entry1)  # Chamar a função de captura de áudio para a primeira entrada
        cpf.focus_set()
        capturaraudio2(cpf)
    janela_secundaria.after(100, lambda: iniciar_reconhecimento(nomeentrada,cpf))
        




def escutar_comando():
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        while True:
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            if 'reserva' in texto.lower():
                falaa = pyttsx3.init()
                falaa.say('Que bom tê-lo conosco, vamos fazer a sua reserva!')
                falaa.runAndWait()
                criar_janela_secundaria()
            elif 'repetir' in texto.lower():
                falaa = pyttsx3.init()
                falaa.say('''[1] Se você deseja fazer uma reserva
                [2] Se você deseja fazer um check-in
                [3] Serviços de comorbidade
                [4] Informações Locais e atrações turísticas''')
                falaa.runAndWait()
            

# Inicialização do mecanismo de fala
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Iniciar a fala após a janela estar aberta
janela.after(1000, falar)

# Iniciar a escuta contínua em um thread separado
thread = threading.Thread(target=escutar_comando)
thread.daemon = True
thread.start()

# Execução da janela principal
janela.mainloop()
