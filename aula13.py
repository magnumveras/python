nome = 'Magno Veras'
altura = 1.84
peso = 105
imc = peso / altura ** 2

# Magno Veras tem 1.84 de altura,
# pesa 95 quilos e seu imc é 
# 12873717231

'f-strings'
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1,
      linha_2, 
      linha_3)