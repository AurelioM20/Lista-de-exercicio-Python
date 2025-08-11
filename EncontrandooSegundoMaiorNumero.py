numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def encontrar_segundo_maior(lista):
  numeros_unicos = set(lista)

  lista_de_unicos = list(numeros_unicos)

  lista_ordenada = sorted(lista_de_unicos)

  if len(lista_ordenada) < 2:
    return "A lista não possui um segundo maior número."
  
  return lista_ordenada[-2]

segundo_maior = encontrar_segundo_maior(numeros)
print(f"O segundo maior número na lista é: {segundo_maior}")
