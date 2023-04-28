v1 = float(input('Please enter V1 volume of water: '))
t1 = float(input('Please enter T1 water temperature: '))
v2 = float(input('Please enter V2 volume of water: '))
t2 = float(input('Please enter T2 water temperature: '))
mixture = (v1*t1 + v2*t2) / (v1 + v2)
if v1 <= 0:
    print('Check "V1 volume of water" input field')
elif t1 < 0:
    print('Check "T1 water temperature" input field')
elif v2 <= 0:
    print('Check "V2 volume of water" input field')
elif t2 < 0:
    print('Check "T2 water temperature" input field')
else:
    print(round(mixture, 2), 'temperature')
    print(round(v1+v2, 2), 'volume of water')
