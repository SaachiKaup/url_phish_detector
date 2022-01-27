import requests

API_URL = "https://developers.checkphish.ai/api/neo/scan"

def get_api_data(url_from_sms):
    url_obj = "{\"""url\""": \"" + url_from_sms + "\"}"
    print(url_obj)
    return { 
        "apiKey": "wkp6z08z27wdbfqpy541ydgjnfzy8x6x5i92trrn25tz9rmkk48faomhwh1qfcx9", 
        #"urlInfo":"{\"url\": \"https://www.rx.mloescb.com/\"}"
        "urlInfo": url_obj    
        }

def post_request(api_url, api_data):
    return requests.post(api_url, api_data)

def get_json(response):
    return response.json()

def get_jobID(response_json):
    return response_json['jobID']

def remove_key(api_data, key):
    api_data.pop(key)

def add_key(api_data, key, value):
    api_data[key] = value

def check_url(url_from_sms):
    api_data = get_api_data(url_from_sms) 
    #print(initial_api_data)
    response_json = get_json(post_request(API_URL, api_data))
    print(response_json)
    remove_key(api_data, 'urlInfo')
    add_key(api_data, 'jobID', get_jobID(response_json))
    add_key(api_data, 'insights', "True")
    final_response_json = get_json(post_request(API_URL + '/status', api_data))
    #print(final_response_json)
    return final_response_json['disposition']

#print(check_url("https://post-navigator-4jngmh54d2asd2.com/login.php?czZRhSdqaxMKF8yjeo4wkBCPHn1s267urAYJfvXbE3LOtUG0plgDNi9WVmTQI5EFb10Soj8eLsvAVnptBqJNmldR4fTkH5yOxhUiaK3cQr6zYwg29WDPZXCM7uGI99009013520&lng=en"))
