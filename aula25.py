"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Magno'
preco = 1000.95897643
frase1 = 'Meu nome é %s' % nome
frase2 = '%s, o preço é R$%.2f' % (nome, preco)
print(frase1)
print(frase2)
print('O hexadecimal de %d é %04x' % (15, 15))
print('O hexadecimal de %d é %08X' % (15, 15))