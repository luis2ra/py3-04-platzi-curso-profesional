# class 19: date management
'''
Si quieren aplicar Python para análisis de datos, es fundamental que 
se domine el manejo de fechas.

La librería "datetime" tiene dos funciones muy utilizadas para estos casos:

1- timedelta: retorna un delta de tiempo, es de ayuda en situaciones donde
necesitamos restar o sumar tiempos (ejemplo: 1 día a cada fecha o 20 minutos cada fecha hora)

2- strptime: recibe un str y retorna un objeto datetime, esto se usa para 
validar formatos de fecha capturando un ValueError cuando se trabaja con archivos y 
queremos validar formatos de fechas con simple lambda podemos aplicar formato a 
todo el dataset y capturas los errores antes de operar con ellos o guardar en la db.
'''
import datetime


delta_hr = datetime.timedelta(hours=3)
print("delta in hours: ", delta_hr)

delta_min = datetime.timedelta(minutes=20)
print("delta in minutes: ", delta_min)

delta_sec = datetime.timedelta(seconds=30)
print("delta in seconds: ", delta_sec)

# si no se cumple con el formato lanzara un ValueError
date_time = datetime.datetime.strptime('2022-10-09 00:40:00' , '%Y-%m-%d %H:%M:%S')
date_time_other = datetime.datetime.strptime('2022-12-12', "%Y-%m-%d")
result = date_time + delta_min
print("time initial: ", date_time)
print("time modified: ", result)
print("other test: ", date_time_other)
