num = int(input("Digite um numero natural inteiro: "))
primo = True
if num <=1:
    primo = False
else:
    for n in range (2, num):
        if num % n == 0:
            primo = False
if  primo:
    print(f"O numero {num} é primo")
else:
    print(f"O numero {num} não é primo")


