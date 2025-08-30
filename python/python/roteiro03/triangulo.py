lado1 = int(input("digite o primeiro lado do triangulo "))
lado2 = int(input("digite o segundo lado do triangulo "))
lado3 = int(input("digite o terrceiro lado do triangulo "))

if lado1 == lado2 and lado2 == lado3:
    print('triangulo equilatero')

if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('triangulo isoceles')
else:
    print('triangulo escaleno')
