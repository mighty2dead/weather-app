import requests as req

api_key = '92cf615e430ba8e76af22343866cce91'


city = input("Enter a city name: ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
response = req.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp}')
    print(f'Description: {desc}')
else:
    print('There was a problem when we attempted to fetch the data from the API.')