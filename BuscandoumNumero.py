numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def buscar_numero(lista, numero_alvo):
  return numero_alvo in lista

numero_a_buscar_1 = 42
encontrado_1 = buscar_numero(numeros, numero_a_buscar_1)
print(f"O número {numero_a_buscar_1} foi encontrado na lista? {encontrado_1}")

numero_a_buscar_2 = 100
encontrado_2 = buscar_numero(numeros, numero_a_buscar_2)
print(f"O número {numero_a_buscar_2} foi encontrado na lista? {encontrado_2}")
