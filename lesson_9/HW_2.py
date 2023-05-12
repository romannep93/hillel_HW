import json

with open('manager_sales.json', 'r') as f:
    data = json.load(f)

managers_sales = []
for item in data:
    manager = item['manager']['first_name'] + ' ' + item['manager']['last_name']
    sales = sum([car['price'] for car in item['cars']])
    managers_sales.append({'manager': manager, 'sales': sales})

top_manager = max(managers_sales, key=lambda x: x['sales'])
print(f'The most successful manager: {top_manager["manager"]}. Total amount of sales: {top_manager["sales"]}')
