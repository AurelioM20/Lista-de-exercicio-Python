produtos = [
    {"codigo": "A1", "nome": "Notebook", "preco": 4500.00},
    {"codigo": "B2", "nome": "Mouse Sem Fio", "preco": 120.50},
    {"codigo": "C3", "nome": "Teclado Mecânico", "preco": 350.00}
]

def extrair_nomes(lista_de_objetos):
  return [objeto["nome"] for objeto in lista_de_objetos]

nomes_dos_produtos = extrair_nomes(produtos)
print(f"A lista de nomes extraída é: {nomes_dos_produtos}")