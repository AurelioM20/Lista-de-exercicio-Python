numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def contar_ocorrencias(lista, valor):
  return lista.count(valor)

valor_a_contar_1 = 9
ocorrencias_1 = contar_ocorrencias(numeros, valor_a_contar_1)
print(f"O valor {valor_a_contar_1} aparece {ocorrencias_1} vezes na lista.")

valor_a_contar_2 = 13
ocorrencias_2 = contar_ocorrencias(numeros, valor_a_contar_2)
print(f"O valor {valor_a_contar_2} aparece {ocorrencias_2} vezes na lista.")

valor_a_contar_3 = 500
ocorrencias_3 = contar_ocorrencias(numeros, valor_a_contar_3)
print(f"O valor {valor_a_contar_3} aparece {ocorrencias_3} vezes na lista.")