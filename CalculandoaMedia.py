numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def calcular_media(lista):
  if not lista:
    return 0
  
  soma_dos_valores = sum(lista)
  
  quantidade_de_valores = len(lista)
  
  return soma_dos_valores / quantidade_de_valores

media = calcular_media(numeros)
print(f"A média dos valores na lista é: {media}")