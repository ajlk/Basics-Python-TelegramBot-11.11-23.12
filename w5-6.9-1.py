import requests

api_url = 'http://numbersapi.com/'

with open('dataset_263163_3.txt') as inp_data:
    for line in inp_data:
        line = line.strip()
        res = (requests.get(f'{api_url}/{line}/math?json=true')).json()
        for key, value in res.items():
            if key == 'found':
                if res[key]:
                    print('Interesting')
                else:
                    print('Boring')
