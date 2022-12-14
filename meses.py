meses = ['JAN' ,' FEV' ,'MAR','ABR','MAI','JUN','JUL','AGO','SET','OCT','NOV','DEZ']
vendas_1sem = [25000, 2900 , 22200 , 17750 , 15870 , 19960]
vendas_2sem = [ 9850 , 20120 , 17540 , 15555 , 49051 , 19650]
vendas_ano = vendas_1sem+vendas_2sem
maior = max(vendas_ano)
menor = min(vendas_ano)
mes = vendas_ano.index(maior)
print("Melhor mês foi {} com R$ {}".format(meses[mes],maior))
print ("Pior mês foi {} com R$ {}".format(meses[mes],menor))