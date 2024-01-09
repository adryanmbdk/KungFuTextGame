##MIGUEL ESTEVE AQUI
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import font, messagebox
import math, random, time
from Player import Player

## variaveis
player = Player(grana=0, energiaMax=20, poder=2, forca=1, agilidade=1)
energia = player.energiaMax
recuperacao_em_andamento = False
recuperacao = 1
recuperacaoAux = recuperacao

## funções
def atualizar(energia, energiaMax, forca, agilidade, grana):
    player.poder = player.forca + player.agilidade
    poder = round((player.forca + player.agilidade),2)
    label_energia.config(text="Energia: " + str(energia) + "/" + str(energiaMax))
    label_grana.config(text="Grana: " + str(grana))
    label_poder.config(text="Poder: " + str(poder))
    label_forca.config(text="Força: " + str(forca))
    label_agilidade.config(text="Agilidade: " + str(agilidade))

def flexao():
    global energia, recuperacao_em_andamento, recuperacao
    condicao = energia - 10
    if condicao >= 0:
        energia -= 10
        ## player.forca = round((player.forca + player.forca * 0.0325),2)  ## calculo de quanto de força que ganha a cada flexao
        aumentarForca(1)
        atualizar(energia, player.energiaMax, player.forca, player.agilidade, player.grana)
        if not recuperacao_em_andamento:
            recuperarEnergia()

def agachamento():
    global energia, recuperacao_em_andamento, recuperacao
    condicao = energia - 10
    if condicao >= 0:
        energia -= 10
        aumentarAgilidade(1)
        atualizar(energia, player.energiaMax, player.forca, player.agilidade, player.grana)
        if not recuperacao_em_andamento:
            recuperarEnergia()

def recuperarEnergia():
    global energia, recuperacao_em_andamento, recuperacao
    if energia < player.energiaMax:
        recuperacao_em_andamento = True
        if energia + recuperacao > player.energiaMax:
            energia = player.energiaMax
        else:
            energia += recuperacao
        atualizar(energia, player.energiaMax, player.forca, player.agilidade, player.grana)
        janela.after(1000, recuperarEnergia)    
    else:
        recuperacao_em_andamento = False
        
def perderEnergia(num):
    global energia
    if (energia - num) < 0:
        energia = 0
    else:
        energia = energia - num
    if (recuperacao_em_andamento == False):
        recuperarEnergia()

def aumentarForca(num):
    if (player.forca + 1) % 5 == 0 and player.forca != 1:
        player.forca += num
        player.energiaMax += 1
    else:
        player.forca += num
    
def aumentarAgilidade(num):
    global recuperacao
    if (player.agilidade + 1) % 25 == 0 and player.agilidade != 1:
        player.agilidade += num
        recuperacao += 1
    else:
        player.agilidade += num

def baterCarteira():
    chance = random.randint(1, 100)
    condicao = energia - 10
    if chance > 80 and condicao >= 0:
        messagebox.showinfo("Alguém te viu!", "Você foi quase foi pego batendo carteira!\n \t-10 de ENERGIA")
        perderEnergia(10)
    elif chance <= 80 and condicao >= 0:
        chance2 = random.randint(1, 100)
        if chance2 < 80:
            grana = random.randint(10,20)
        else:
            grana = random.randint(35,50)
        player.grana += grana
        messagebox.showinfo("Ladrãozinho!", "Você conseguiu roubar uma carteira e ganhou "+ str(grana)+ " reais!\n \t-10 de ENERGIA")
        perderEnergia(10)
    atualizar(energia, player.energiaMax, player.forca, player.agilidade, player.grana)

## configurando app
app = tk.Tk()
app.title("Fung Ku")
app.geometry("400x330")
app.configure(bg="#39393b")
app.resizable(False,False)

nb = ttk.Notebook(app)
nb.place(x=0,y=0,width=400,height=330)

janela=Frame(nb)
grana=Frame(nb)

nb.add(janela, text="Inicio")
nb.add(grana, text="Grana")

fonte_negrito = font.Font(family="Arial", size=12, weight="bold")
fonte_label = font.Font(family="Arial", size=4, weight="bold")
#################################################################
##configurando stats
stats = Frame()
stats.pack(side="right")
stats.pack_propagate(FALSE)
stats.configure(bg="#39393b", width=100, height=330)

label_energia = tk.Label(stats, text="Energia: " + str(energia) + "/" + str(player.energiaMax), font="fonte_negrito", bg="#39393b", fg="yellow")
label_grana = tk.Label(stats, text="Grana: " + str(player.grana), font="fonte_negrito", bg="#39393b", fg="lime")
label_poder = tk.Label(stats, text="Poder: " + str(player.poder), font="fonte_negrito", bg="#39393b", fg="red")
label_forca = tk.Label(stats, text="Força: " + str(player.forca), font="fonte_negrito", bg="#39393b", fg="orange")
label_agilidade = tk.Label(stats, text="Agilidade: " + str(player.agilidade), font="fonte_negrito", bg="#39393b", fg="cyan")
label_energia.grid(row=0, padx=15, pady=10)
label_grana.grid(row=1, padx=15, pady=10)
label_poder.grid(row=2, padx=15, pady=10)
label_forca.grid(row=3, padx=15, pady=10)
label_agilidade.grid(row=4, padx=15, pady=10)

################################################################
##configurando a janela
janela.configure(bg="#39393b", width=300, height=330)

botaoFlexao = tk.Button(janela, text="Flexão", command=flexao, width=12, height=2, font="fonte_negrito")
lb_flexao = tk.Label(janela, text="-10 Energia\n +1 Força", bg="#39393b", fg="white",font="fonte_label")
botaoAgachamento = tk.Button(janela, text="Agachamento", command=agachamento, width=12, height=2, font="fonte_negrito")
lb_agachamento = tk.Label(janela, text="-10 Energia\n +1 Agilidade", bg="#39393b", fg="white",font="fonte_label")

botaoFlexao.grid(row=0, column=0, padx=10, pady=10)
botaoAgachamento.grid(row=1, column=0, padx=10, pady=10)
lb_flexao.grid(row=0, column=1, padx=0, pady=10)
lb_agachamento.grid(row=1, column=1, padx=0, pady=10)

################################################################
##configurando a grana
grana.configure(bg="#39393b")

botaoBaterCarteira = tk.Button(grana, text="Bater Carteira", command=baterCarteira, width=12, height=2, font="fonte_negrito")
lb_baterCarteira = tk.Label(grana, text="-10 Energia\n 10-50 Grana", bg="#39393b", fg="white",font="fonte_label")

botaoBaterCarteira.grid(row=0, column=0, padx=10, pady=10)
lb_baterCarteira.grid(row=0, column=1, padx=0, pady=10)

# Iniciar o loop principal da janela
janela.mainloop()

