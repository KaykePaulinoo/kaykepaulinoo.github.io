senha_correta ="python"
limite_tentativa = 3

tentativas = 0
acesso_pemitido = False

print('insira a senha')
print(f'voce tem {limite_tentativa} para acerta senha')

while tentativas < limite_tentativa:
    senha_digitada = input(f'tentativa {tentativas + 1 }: digite a senha:')
    tentativas +=1

    if senha_digitada == senha_correta:
        print('senha correta! Acesso permitido')
        acesso_pemitido = True
        break
    else:
        tentativas_restantes = limite_tentativa - tentativas
    if tentativas_restantes > 0 :
            print(f'senha incorreta. Você ainda tem {tentativas_restantes}tentativa(s)')
    if not acesso_pemitido:
     print('voce exedeu o limite de tentativas')
