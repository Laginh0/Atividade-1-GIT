def analisa_lista(numeros):
  if not numeros:
    return (None, None, 0)
  
  maior = max(numeros)
  menor = min(numeros)
  media = sum(numeros) / len(numeros)
  
  return maior, menor, media

minha_lista = [10, 20, 5, 15]
resultado = analisa_lista(minha_lista)
print(resultado)