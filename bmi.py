x=" - "
print(10*x + "Calculadora de IMC" + 10*x + "\n" )
P=float(input("Digite o seu peso em kilos: "))
A=int(input("Digite a sua altura em centimetros: "))/100
IMC=P/(A*A)
print( "\n" + "Seu IMC eh: %s" % IMC)

# passo 2 falar se o cara esta fudido

if IMC <= 18.5:
    print("Voce esta magro demais!")
elif IMC > 18.5 and IMC <= 24.9:
    print("Boa campeao ta topzera")
elif IMC > 24.9 and IMC <= 29.9:
    print("Na trave, voce ta gordinho")
elif IMC > 29.9 and IMC <= 34.9:
    print("Voce ta gordo, chega de mcdonalds")
elif IMC > 34.9 and IMC <= 39.9:
    print("Voce ta bolao, so saladinha agora")
elif IMC > 39.9:
    print("Vish....")
