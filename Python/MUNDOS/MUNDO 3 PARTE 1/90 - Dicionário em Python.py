aluno = {
    "Nome" : str(input("Digite seu nome: ")),
    "Média" : float(input("Digite sua média: ")),
    "Situação" : ""
}

if aluno["Média"] >= 7:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"

print(f"Nome é igual a {aluno["Nome"]}")
print(f"Média é igual a {aluno["Média"]}")
print(f"Situação é igual a: {aluno["Situação"]}")
