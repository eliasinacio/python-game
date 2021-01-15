import datetime

ano_atual = datetime.date.today().year
print(ano_atual)

def voto(ano_pessoa):
    idade = ano_atual - ano_pessoa
    
    if idade < 16:
        return "negado"
    elif 16 <= idade < 18:
        return "facultativo"
    elif idade >= 18:
        return "obrigatorio"

ano = int(input("Qual o ano que voce nasceu? \n>>"))
print("Seu voto e " + voto(ano))
