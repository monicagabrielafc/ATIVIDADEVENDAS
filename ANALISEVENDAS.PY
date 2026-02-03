import pandas as pd

dados = pd.read_excel("vendas.xlsx", engine="openpyxl")


dados = dados.fillna(0)

dados['valordavenda'] = dados['quantidade'] * dados['preco_unitario']

print (dados)

def nivelvenda(venda):
    if venda > 500:
        return "Alto"
    elif venda >= 100 and venda <= 500:
        return "Médio"
    elif venda < 100 and venda > 1 :
        return "Baixo"
    else:
        return "venda inválida"
    

dados["niveldavenda"] = dados["valordavenda"].apply(nivelvenda)

dados["imposto"] = 0.1

dados.loc[(dados["valordavenda"] > 300, "imposto")] = 0.15

dados ["impostopago"] = dados ["valordavenda"]* dados ["imposto"]

dados['valorliquido'] = dados['valordavenda'] - dados["impostopago"]

print (dados.to_string())
