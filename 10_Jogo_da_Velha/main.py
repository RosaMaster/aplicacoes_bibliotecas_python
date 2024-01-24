import tkinter
from tkinter import *
from tkinter import ttk

# cores

co0 = "#FFFFFF"  # branca / white
co1 = "#333333"  # preta pesado / dark black
co2 = "#fcc058"  # laranja / orange
co3 = "#38576b"  # valor / value
co4 = "#3297a8"   # azul / blue
co5 = "#fff873"   # amarela / yellow
co6 = "#fcc058"  # laranja / orange
co7 = "#e85151"   # vermelha / red
co8 = co4   # + verde
co10 ="#fcfbf7"
fundo = "#3b3b3b" # preta / black

# criando janela principal
janela = Tk()
janela.title('Jogo da Velha')
janela.geometry('260x370')
janela.configure(background=fundo)

# Dividindo a janela em 2 frames ----------------------------------------------
# criando frames
frame_cima = Frame(janela, bg=co1, width=240, height=100, relief='raise')
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, bg=fundo, width=240, height=300, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

# Configurando o frame de cima -------------------------------------------------
app_x = Label(frame_cima, text='X', relief='flat', anchor='center', bg=co1, fg=co7, font='Ivy 40 bold', height=1)
app_x.place(x=25, y=10)

app_x = Label(frame_cima, text='Jogador 1', relief='flat', anchor='center', bg=co1, fg=co0, font='Ivy 7 bold', height=1)
app_x.place(x=17, y=70)

app_x_pontos = Label(frame_cima, text='0', relief='flat', anchor='center', bg=co1, fg=co8, font='Ivy 30 bold', height=1)
app_x_pontos.place(x=80, y=20)

# Separador
app_separador = Label(frame_cima, text=':', relief='flat', anchor='center', bg=co1, fg=co0, font='Ivy 30 bold', height=1)
app_x_pontos.place(x=110, y=20)

app_x = Label(frame_cima, text='O', relief='flat', anchor='center', bg=co1, fg=co4, font='Ivy 40 bold', height=1)
app_x.place(x=165, y=10)

app_x = Label(frame_cima, text='Jogador 2', relief='flat', anchor='center', bg=co1, fg=co0, font='Ivy 7 bold', height=1)
app_x.place(x=165, y=70)

app_x_pontos = Label(frame_cima, text='0', relief='flat', anchor='center', bg=co1, fg=co8, font='Ivy 30 bold', height=1)
app_x_pontos.place(x=130, y=20)

janela.mainloop()