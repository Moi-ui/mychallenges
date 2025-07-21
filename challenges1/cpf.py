cpf = input("Insira um CPF: ")
cpf = [int(digito) for digito in cpf]
print(cpf)

soma = 0
for i in range(9):
    soma += cpf[i] * (10 - i)
    
# Primeiro dígito verificador.
d10 = (soma*10)%11
soma2 = 0
for i in range(10):
    soma2 += cpf[i] * (11 - i)
d11 = (soma2 * 10) % 11

# Segundo dígito verificador.
if d11 == 10:
    d11 = 0

# Verificação
if cpf[9] == d10 and cpf[10] == d11:
    print("CPF válido")
else:
    print("CPF inválido")