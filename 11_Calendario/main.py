import calendar
from datetime import date, datetime

yy = 2012  # Year
mm = 3    # Month

# Display The Calendar
def Calendar(year, month):
    print(calendar.month(year, month))

Calendar(yy, mm)

data_atual = date.today()
print(data_atual)


now = datetime.now()
print(now)

# Obter o ano
year = now.year
print(year)

# Obter o mês
month = now.month
print(month)


Calendar(year, month)