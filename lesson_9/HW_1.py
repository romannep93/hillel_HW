import json


with open('group_people.json', 'r') as file:
    data = json.load(file)


max_female_count = 0
max_female_group_id = None


for group in data:
    group_id = group['id_group']
    female_count = 0

    for person in group['people']:
        if person['gender'] == 'Female' and int(person['year']) > 1977:
            female_count += 1

    if female_count > max_female_count:
        max_female_count = female_count
        max_female_group_id = group_id

print('ID of the group with the largest number of women born after 1977:', max_female_group_id)
print('Number of women born after 1977 in this group:', max_female_count)
