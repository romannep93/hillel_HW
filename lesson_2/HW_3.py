value = ['UAH', 'USD', 'EUR']
currency_value = str(input('Choose your currency (UAH, USD, EUR): ')).upper().replace(' ', '')
exchange_value = str(input('Select exchange currency(UAH, USD, EUR): ')).upper().replace(' ', '')
exchange_amount = float(input('Enter the exchange amount: '))
if currency_value not in value:
    print('Check "currency value" input field')
elif exchange_value not in value:
    print('Check "exchange value" input field')
elif exchange_amount <= 0:
    print('Check "exchange amount" input field')
elif currency_value == 'UAH' and exchange_value == 'UAH':
    print(exchange_amount)
elif currency_value == 'USD' and exchange_value == 'USD':
    print(exchange_amount)
elif currency_value == 'EUR' and exchange_value == 'EUR':
    print(exchange_amount)
elif currency_value == 'UAH' and exchange_value == 'USD':
    print(round(exchange_amount / 36.57, 2))
elif currency_value == 'UAH' and exchange_value == 'EUR':
    print(round(exchange_amount / 40.42, 2))
elif currency_value == 'USD' and exchange_value == 'UAH':
    print(round(exchange_amount * 36.57, 2))
elif currency_value == 'USD' and exchange_value == 'EUR':
    print(round(exchange_amount / 1.11, 2))
elif currency_value == 'EUR' and exchange_value == 'UAH':
    print(round(exchange_amount * 40.42, 2))
elif currency_value == 'EUR' and exchange_value == 'USD':
    print(round(exchange_amount * 1.11, 2))
