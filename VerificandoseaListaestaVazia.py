def verificar_lista_vazia(lista):
  return not lista

lista_cheia = [1, 2, 3]
resultado_cheia = verificar_lista_vazia(lista_cheia)
print(f"A lista {lista_cheia} está vazia? {resultado_cheia}")

lista_vazia = []
resultado_vazia = verificar_lista_vazia(lista_vazia)
print(f"A lista {lista_vazia} está vazia? {resultado_vazia}")