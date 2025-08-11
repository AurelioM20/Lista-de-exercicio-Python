numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def remover_duplicatas(lista):
  conjunto_sem_duplicatas = set(lista)
  
  lista_final = list(conjunto_sem_duplicatas)
  
  return lista_final

lista_sem_duplicatas = remover_duplicatas(numeros)

print(f"Lista original: {numeros}")
print(f"Lista sem duplicatas (a ordem pode variar): {lista_sem_duplicatas}")