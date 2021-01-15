import requests

url = "https://youtube.com"

if requests.get(url).status_code == 200:
    print("\033[1;35mServidor Disponível.\033[m")

else:
    print('\033[1;31mSite indisponível.')