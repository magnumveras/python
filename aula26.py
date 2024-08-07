"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X Hexadecimal 
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
= - força o sinal a aparecer antes dos zeros
Sinal - + ou - 
Ex.: 0>-100,.1f
Conversion flags - !r !s !a __repr__
"""

variavel = 'ABC'

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:$^10}.')
print(f'{variavel:0^10}.')
print(f'{1000.1238128312873718:.2f}')
print(f'{-1000.1238128312873718:+.2f}') #Mostra o sinal de positivo quando for positivo
print(f'{+1000.1238128312873718:+.2f}') #Nesse caso é positivo então vai aparecer o sinal 
print(f'{1000.1238128312873718:,.3f}')
print(f'{1000.1238128312873718:0<10.2f}') #Completa com 10 zeros a direita
print(f'{1000.1238128312873718:0>10.2f}') #Completa com 10 zeros a esquerda
print(f'{1000.1238128312873718:0>+10.2f}') #Completa com 10 zeros a esquerda
print(f'{1000.1238128312873718:0=+10.2f}') #Completa com 10 zeros a esquerda e coloca o sinal de positivo no inicio 
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}')