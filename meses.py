meses = ['JAN','FEVEREIRO','MAR','ABR','MAI','JUN','JUL','AGO','SET','OCT','NOV','DEZ']
vendas_1sem = [25000, 2900 , 22200 , 17750 , 15870 , 19960]
vendas_2sem = [ 9850 , 20120 , 17540 , 15555 , 49051 , 19650]
vendas_ano = vendas_1sem+vendas_2sem
maior = max(vendas_ano)
menor = min(vendas_ano)
mesm = vendas_ano.index(maior)
mesp = vendas_ano.index(menor)
fat_total = sum(vendas_ano)
p = maior * 100 /fat_total

print("Melhor mês foi {} com R$ {}".format(meses[mesm],maior))
print("Pior mês foi {} com R$ {}".format(meses[mesp],menor))
print(f"Faturamento anual : R$ {fat_total}")
print(f"{maior} é {p:.2f}% de {fat_total}")
print(print(p)
      
      
      for in range(3):
        maior = max(vendas_ano)
        top3.append(maior)
        vendas_anos.remove(maior)
      print(
