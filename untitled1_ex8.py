d = float(input("Uma distância em metros: "))
print("A medida de {} corresponde a \n{}Km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm" .format(d, (d/1000), (d/100), (d/10), (d*10), (d*100), (d*1000)))