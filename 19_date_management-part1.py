# class 19: date management
import datetime


my_datetime = datetime.datetime.now()

print(f'Now (local): {my_datetime}')
print(f'Now (UTC): {datetime.datetime.utcnow()}')

my_day = datetime.date.today()

print(f'Year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')

# Formato de fechas
my_str1 = my_datetime.strftime('%d/%m/%Y')
print(f'Formato LATAM: {my_str1}')

my_str2 = my_datetime.strftime('%m/%d/%Y')
print(f'Formato USA: {my_str2}')

my_str3 = my_datetime.strftime(f'Estamos en el año %Y')
print(f'Formato random: {my_str3}')
