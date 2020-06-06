# ========TRATAMENTO DE ERROS=======
#Ira impede que apareça mensagem de erro!

try:  # peço para tentar executar o codigo
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except:  # se der problema ira acontecer o seguinte:
    print('Infelizmente tivemos um problema. =(')

else:  # e se deu certo o pograma fará: (OPCIONAL)
    print(f'O resultado é {r:.1f}')

finally:  # irá acontecer indepente se deu erro ou nao (OPCIONAL)
    print('Volte sempre!')


# PODE-SE MOSTRAR O TIPO DE ERRO DEFININDO O EXCEPATION
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b

except Exception as erro:  # erro é uma variavel definida pro erro
    print(f'O problema encontrado foi {erro.__cause__}')
    print(f'O problema encontrado foi {erro.__class__}')
    print(f'O problema encontrado foi {erro.__context__}')
    print(f'O problema encontrado foi {erro.__traceback__}')
except (ValueError, TypeError):  # pode-se personalisar a mensagem para cada tipo de erro
    print('Tivemos um problema com os tipos de dados digitados')
except ZeroDivisionError:  # pode-se ter diversas trativas de erro
    print('O valor nao pode ser divisivel por 0')

else:  # (OPCIONAL)
    print(f'O resultado é {r:.1f}')
finally:  # (OPCIONAL)
    print('Volte sempre!')
