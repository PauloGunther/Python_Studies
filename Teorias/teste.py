import requests

try:
    acesso = requests.get('http://www.pudim.com.br/')
except:
    print('\033[1;31mO site pudim não está acessivel no momento.\033[m')
else:
    print('\033[1;32mContectado ao site pudim com sucesso!\033[m')
