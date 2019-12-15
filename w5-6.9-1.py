import requests

api_url = 'http://numbersapi.com/'

with open('dataset_263163_3.txt') as inp_data:
    for line in inp_data:
        line = line.strip()
        res = requests.get(f'{api_url}/{line}/math?json=true')
        dict = res.json()
        for key, value in dict.items():
            if key == 'found':
                if dict[key]:
                    print('Interesting')
                else:
                    print('Boring')
