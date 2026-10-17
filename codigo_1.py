## INPUT
nome: str = input("Adicione seu nome: ")
idade: int = int(input("Adicione sua idade: "))
r_casado: str = input("Atualmente está casado? ").lower()
pretensao: float = float(input("Qual sua pretensao salarial? "))

if(r_casado == "sim"):
    casado = True
else:
    casado = False

## OUTPUT
print("RELATORIO")
print("O Sr(a) ", nome)
print("idade ", idade)

print(casado)

if(casado):
   print("estado civil CASADO")
else:
   print("estado civil SOLTEIRO")

print("tem pretensão salarial de ", pretensao)