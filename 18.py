def senha_segura(senha):
  tem_maiuscula = False
  tem_minuscula = False
  tem_numero = False

  if len(senha) < 8:
    return False

  for char in senha:
    if char.isupper():
      tem_maiuscula = True
    elif char.islower():
      tem_minuscula = True
    elif char.isdigit():
      tem_numero = True
      
  return tem_maiuscula and tem_minuscula and tem_numero

print(senha_segura("Senha123"))
