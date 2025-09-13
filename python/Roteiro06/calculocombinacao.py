from calculofatorial import calcular_fatorial
def calculacombinacao(n,k):
    if k > n:
        return "ERRO: N deve ser maior ou igual a K"
    fatorial_n = calcular_fatorial(n)
    fatorial_k = calcular_fatorial(k)
    fatorial_n_menos_k = calcular_fatorial(n - k)
    return fatorial_n / (fatorial_k * fatorial_n_menos_k)
n_teste = 10
k_teste = 3 
print(f"A combinação de {n_teste} mais a {k_teste} é {calculacombinacao(n_teste, k_teste)}")