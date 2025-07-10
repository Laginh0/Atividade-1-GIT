def palindromo(palavra):
  palavra_limpa = palavra.lower().replace(" ", "")
  return palavra_limpa == palavra_limpa[::-1]

print(palindromo("arara"))
