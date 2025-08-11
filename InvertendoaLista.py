numeros = [987654-321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def inverter_lista(lista):
  return lista[::-1]

lista_invertida = inverter_lista(numeros)

print(f"Lista original: {numeros}")
print(f"Lista invertida: {lista_invertida}")