segundos_entrada=int(input("Por favor, entre com o número de segundos que deseja converter:"))
dias=segundos_entrada//86400
segundosrestantes=segundos_entrada%86400
horas=segundosrestantes//3600
segundosrestantes2=segundosrestantes%3600
minutos=segundosrestantes2//60
segundos=segundosrestantes2%60


print(dias, "dias, " ,horas, "horas ", minutos, "minutos e", segundos, "segundos" )