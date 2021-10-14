days = int(input())
months = 0
years = days / 365

if (years != 0):
    years_rest = days - (int(years) * 365)
    months = years_rest / 30
    if (months != 0):
        days = years_rest - (int(months) * 30)
    else:
        days = years_rest
else:
    months = days / 30
    if (months != 0):
        days = days - (int(months) * 30)
    else:
        days = years / 30 

print(f"{str(int(years))} ano(s)\n{str(int(months))} mes(es)\n{str(int(days))} dia(s)")