money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение

while money_capital - spend > 0:
    money_capital = money_capital + (salary - spend)
    spend += spend * increase
    month += 1
"""
money_total = money_capital + salary
def live_(x, y, month):
    while x - y > 0:
        x -= y
        y += y * increase
        x += salary
        month += 1
    return(month)
"""
print(month)
