import moeda

preço= float(input("Digite o preço: R$ "))

print (f"A metade de R$ {preço} é {moeda.metade(preço)}")
print (f"O dobro do R$ {preço} é {moeda.dobro(preço)}")
print (f"Aumentando 10%, temos R$ {preço} é {moeda.aumentar(preço,10)}")
print (f"O dobro de R$ {preço} é {moeda.dobro(preço)}")