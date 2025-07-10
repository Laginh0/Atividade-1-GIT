def contar_vogais(palavra):
  vogais = "aeiou"
  contador = 0
  for letra in palavra.lower():
    if letra in vogais:
      contador += 1
  return contador

print(contar_vogais("python"))
