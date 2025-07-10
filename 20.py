def intercalar_listas(lista1, lista2):
  lista_intercalada = []
  for i in range(len(lista1)):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
  return lista_intercalada

lista_numeros = [1, 2, 3]
lista_letras = ["a", "b", "c"]
resultado = intercalar_listas(lista_numeros, lista_letras)
print(resultado)