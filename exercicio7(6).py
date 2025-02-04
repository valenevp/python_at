def converter_para_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

horas = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))
segundos = int(input("Digite os segundos: "))

total_segundos = converter_para_segundos(horas, minutos, segundos)
print(f"O tempo total em segundos é: {total_segundos}")
