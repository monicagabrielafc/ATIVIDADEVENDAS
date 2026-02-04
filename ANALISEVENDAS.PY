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

print (dados)

dados["faixaetaria"] = "Jovem"

dados.loc[(dados["idade"] >= 50, "faixaetaria")] = "Sênior"
dados.loc[(dados["idade"] <=30) & (dados["idade"] <= 49), "faixaetaria"] = "Adulto"
print (dados)


#Total de Vendas Brutas
totalvendasbrutas = dados["valordavenda"].sum()
#Total de Impostos
totalimpostos = dados["impostopago"].sum()
# Total de Vendas Líquidas
totalvendasliquidas = dados["valorliquido"].sum()
# Número total de vendas
numerototalvendas = len(dados)
# Número de vendedores únicos
vendedoresunicos = dados["vendedor"].nunique()
#Número de clientes únicos
clientesunicos = dados["cliente"].nunique()
# Média do valor da venda (bruto)
mediavalorvenda = dados["valordavenda"].mean()
#Ticket médio líquido
ticketmedioliquido = dados["valorliquido"].mean()

print(" MÉTRICAS DE VENDAS")
print(f"Total de Vendas Brutas: R$ {totalvendasbrutas:.2f}")
print(f"Total de Vendas Líquidas: R$ {totalvendasliquidas:.2f}")
print(f"Total Imposto Pago: R$ {totalimpostos:.2f}")
print(f"Número Total das Vendas: R$ {numerototalvendas:2f}")
print(f"Número de Vendedores Únicos: {vendedoresunicos:.2f}")
print(f"Clientes únicos: {clientesunicos}")
print(f"Média do valor da venda: R$ {mediavalorvenda:.2f}")
print(f"Ticket médio líquido: R$ {ticketmedioliquido:.2f}")


agrupamento_vendedor = dados.groupby("vendedor").agg(
    faturamento_bruto = ("valordavenda", "sum"),
    faturamento_liquido = ("valorliquido", "sum"),
    total_imposto = ("impostopago", "sum"),
    numero_vendas = ("valordavenda", "count")  
)


print(dados.sample(10))
print(agrupamento_vendedor.sort_values("valordavenda",ascending=False))