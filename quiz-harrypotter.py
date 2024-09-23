user=input("Olá, qual o seu nome?")
print(f"Seja bem vindo(a), {user}!!")

iniciar=input("Está pronto para saber se você conhece bastante sobre a saga do Harry Potter? Sim ou Não?")
if iniciar != "Sim":
    quit()

score=0

print("Vamos iniciar!!")

#pergunta 1
print("Qual o sobrenome da familia que tem marca própria sendo identificada pelos cabelos ruivos?")
result1=input("Resposta:")

if result1=="Weasley":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreto!")

#pergunta 2
print("Qual nome da autora da saga Harry Potter? \n(A)J. K. Rowling \n(B)David Yates \n(C)Katherine Waterston")
result2=input("Respota:")

if result2=="A":
    print("Certa resposta!")
    score=score+1
else:
    ("Incorreta!")

#pergunta 3
print("Quanto custa para estudar em Hogwarts? \n(A)US$ 43.450 \n(B)US$ 600.450 \n(C)Nenhum custo")
result3=input("Respota:")

if result3=="C":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreta!")

#pergunta 4
print("Qual o nome da famosa cobra (Horcrux) de Voldemort?")
result4=input("Resposta:")

if result4=="Nagini":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreta!")


#pergunta 5
print("Quantas cabeças o cão gigante tem que aparece em Harry Potter e a Pedra Filosofal? \nA) 2 Cabeças \n(B)3 Cabeças \n(C)4 Cabeças")
result5=input("Resposta")

if result5=="B":
    print("Certa resposta!")
    score-score+1

else:
    print("Incorreta")

#pergunta 6
print("Qual feitiço era usado para abrir itens como janelas, portas, trancas em Harry Potter?")
result6=input("Resposta:")

if result6=="Alorramora":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreta!")

#pergunta 7
print("Qual feitiço matou a Bellatriz em Harry Potter? \n(A)Reducto \n(B)Avada Kedavra \n(C)Expelliarmus")
result7=input("Respota:")

if result7=="A":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreta")

#pergunta 8
print("Com quantos anos o bruxo recebe a carta para entrar em Hogwarts?")
result8=input("Resposta:")

if result8=="11":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreta!")
#pergunta 9
print("Qual nome da Atriz que interpreta a Hermione? \n(A)Ema Wattson \n(B)Elena Bohan Cáter \n(C)Emma Watson")
result9=input("Resposta:")

if result9=="C":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreta!")

#pergunta 10
print("Qual é a estação que fica a plataforma 9 três quartos? \n(A)Estação de londres \n(B) Estação de kings cross")
result10=input("Resposta:")

if result10=="B":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreta!")

#pergunta 11
print("Qual a cor do vestido de baile da Hermione no livro?")
result11=input("Resposta:")

if result11=="azul":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreta!")

#pergunta 12
print("Qual é o núcleo da varinho de Lúcios Malfoi? \n(A)Cauda de unicónio \n(B)Coração de dragão \n(C)Pena de fênix")
result12=input("Resposta:")

if result12=="B":
    print("Certa resposta!")
    score=score+1
else:
    print("Incorreta!")
















print(f"O Quiz chegou ao final, sua Pontuação foi: {score}/12")