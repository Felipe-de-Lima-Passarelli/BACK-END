texto = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "GRATIS",
         "ESTUDAR", "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO")

for p in texto:
    print(f"\nA palavra é {p}, suas vogais são: ", end = "")
    for letra in p:
        if letra in "AEIOU":
            print(f"{letra} ", end = "")
