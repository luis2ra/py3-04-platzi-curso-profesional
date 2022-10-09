# class 20: timezones
'''
Para este proyecto, previamente debe instalarse el modulo pytz en el entorno virtual

(venv) $ pip install pytz

'''
from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogota: ", bogota_date.strftime("%d/%m/%Y %H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print("Caracas: ", caracas_date.strftime("%d/%m/%Y %H:%M:%S"))

mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(mexico_timezone)
print("Mexico City: ", mexico_date.strftime("%d/%m/%Y %H:%M:%S"))

new_zealand_timezone = pytz.timezone("NZ")
new_zealand_datetime = datetime.now(new_zealand_timezone)
print("New Zealand: ", new_zealand_datetime.strftime("%d/%m/%Y %H:%M:%S"))

new_zealand_timezone2 = pytz.timezone("NZ-CHAT")
new_zealand_datetime2 = datetime.now(new_zealand_timezone2)
print("New Zealand - CHAT: ", new_zealand_datetime2.strftime("%d/%m/%Y %H:%M:%S"))

new_zealand_timezone3 = pytz.timezone("Pacific/Auckland")
new_zealand_datetime3 = datetime.now(new_zealand_timezone3)
print("New Zealand - Auckland: ", new_zealand_datetime3.strftime("%d/%m/%Y %H:%M:%S"))

new_zealand_timezone4 = pytz.timezone("Pacific/Chatham")
new_zealand_datetime4 = datetime.now(new_zealand_timezone4)
print("New Zealand - Chatham: ", new_zealand_datetime4.strftime("%d/%m/%Y %H:%M:%S"))

# print("list: ", pytz.all_timezones)
