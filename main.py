nota1 = float(input("Informe a 1º nota: "))
nota2 = float(input("Informe a 2º nota: "))
nota3 = float(input("Informe a 3º nota: "))
nota4 = float(input("Informe a 4º nota: "))

media = (nota1+nota2+nota3+nota4)/4

if (media >= 7):
    print(f"aprovado média igual {media:.2f}")
else:
    print(f"reprovado média igual {media:.2f}")