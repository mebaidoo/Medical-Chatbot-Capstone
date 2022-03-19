import requests

def Terms(term):
    api_address = 'https://www.dictionaryapi.com/api/v3/references/medical/json/'
    key = 'key=493ac855-7f9b-4e02-bd03-7564a897bdd0'
    url = api_address + term + '?' + key
    print(url)
    json_data = requests.get(url).json()
    format_add = json_data[1]['shortdef'][0]
    print(format_add)
    return format_add
