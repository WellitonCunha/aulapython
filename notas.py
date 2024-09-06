quantidadeNotas = int(input("Informe a quantidade de notas a ser calculadas: "))

x=1
soma = 0
while(x<= quantidadeNotas):
    nota = float(input(f"Informe a {x} nota: "))
    x += 1
    soma += nota

media = soma / quantidadeNotas

if (media >= 7):
    print(f"Aprovado média igual {media:.2f}")
else:
    print(f"Reprovado média igual {media:.2f}")