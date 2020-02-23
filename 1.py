import json

with open(r'C:\Users\dmfil\PycharmProjects\projects\info.json', 'r') as f:
    data = json.load(f)
    people = []
    max_amount = 0
    for item in data:
        if item.get('amount') > max_amount:
            max_amount = item.get('amount')
        elif item.get('amount') >= 1000:
            people.append(item.get('name'))
    print(max_amount)
    print(people)

with open(r'C:\Users\dmfil\PycharmProjects\projects\info1.json', 'w') as f:
    json.dump(people, f, indent=4)