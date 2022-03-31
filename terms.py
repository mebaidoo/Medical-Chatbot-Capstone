import requests
import json


#This function is used to make requests to the Merriam-Webster medical dictionary API which provides definitions to medical terms
def Terms(term):
    api_address = 'https://www.dictionaryapi.com/api/v3/references/medical/json/'
    key = 'key=493ac855-7f9b-4e02-bd03-7564a897bdd0'
    url = api_address + term + '?' + key
    json_data = requests.get(url).json()
    #Convert the json data into a python dictionary
    data = json.dumps(json_data)
    data = json.loads(data)
    #Access the short definitions part of each medical term
    format_add = data[0]["shortdef"][0]
    return format_add
