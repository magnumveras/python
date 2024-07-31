primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    # print('{primeiro_valor=} é maior do que {1}'.format(primeiro_valor, segundo_valor))
    print(f'{primeiro_valor=} é maior '
          f'do que {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    # print('{1} é maior do que {0}'.format(primeiro_valor, segundo_valor))
    print(f'{segundo_valor=} é maior '
          f'do que {primeiro_valor=}')
else:
    print('Valores são iguais!')