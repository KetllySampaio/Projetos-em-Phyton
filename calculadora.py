# importando tkinter
from tkinter import*
from tkinter import ttk

#cores

cor1="#383838" # preta
cor2="#ffffff" #branca
cor3="#575e91" #azul
cor4="#a8a2a5" #cinza
cor5="#eb7f1a" #laranja

janela =Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

#display

frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela,width=235, height=268)
frame_corpo.grid(row=1, column=0)

#variavel todos valores
todos_valores=''


#CRIANDO LABEL
valor_texto=StringVar()



#criando FUNÇÕES
def entrar_valores(event):
    
    global todos_valores


    todos_valores=todos_valores+str(event)

    
    
    #PASSANDOVALOR PARA TELA
    valor_texto.set(todos_valores)


#Função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))



#Função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores =""
    valor_texto.set("")






app_label=Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)



#criando botoes


bot_1=Button(frame_corpo, command=limpar_tela,text="C", width=12, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_1.place(x=0,y=0) #largura do botão x comprimento y largura
bot_2=Button(frame_corpo,command=lambda:entrar_valores('%'),text="%", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_2.place(x=118,y=0)
bot_3=Button(frame_corpo, command=lambda:entrar_valores('/'),text="/", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_3.place(x=177,y=0)


bot_4=Button(frame_corpo, command=lambda:entrar_valores('7'),text="7", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_4.place(x=0,y=52)
bot_5=Button(frame_corpo, command=lambda:entrar_valores('8'),text="8", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_5.place(x=59,y=52)
bot_6=Button(frame_corpo, command=lambda:entrar_valores('9'),text="9", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_6.place(x=118,y=52)
bot_7=Button(frame_corpo, command=lambda:entrar_valores('*'),text="*", width=5, height=2, bg=cor5,fg=cor2, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_7.place(x=177,y=52)


bot_8=Button(frame_corpo,command=lambda:entrar_valores('4'), text="4", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_8.place(x=0,y=104)
bot_9=Button(frame_corpo, command=lambda:entrar_valores('5'),text="5", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_9.place(x=59,y=104)
bot_10=Button(frame_corpo,command=lambda:entrar_valores('6'), text="6", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_10.place(x=118,y=104)
bot_11=Button(frame_corpo,command=lambda:entrar_valores('-'), text="-", width=5, height=2, bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_11.place(x=177,y=104)


bot_12=Button(frame_corpo,command=lambda:entrar_valores('1'), text="1", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_12.place(x=0,y=156)
bot_13=Button(frame_corpo,command=lambda:entrar_valores('2'), text="2", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_13.place(x=59,y=156)
bot_14=Button(frame_corpo,command=lambda:entrar_valores('3'), text="3", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_14.place(x=118,y=156)
bot_15=Button(frame_corpo,command=lambda:entrar_valores('+'), text="+", width=5, height=2, bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_15.place(x=177,y=156)


bot_16=Button(frame_corpo,command=lambda:entrar_valores('0'), text="0", width=12, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_16.place(x=0,y=208) #largura do botão x comprimento y largura
bot_17=Button(frame_corpo,command=lambda:entrar_valores('.'), text=".", width=5, height=2, bg=cor4,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_17.place(x=118,y=208)
bot_18=Button(frame_corpo,command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE)
bot_18.place(x=177,y=208)


janela.mainloop()
