from django.shortcuts import render
import requests


API_KEY = '14eb0a9b999f7cf5e177761ed68b0a0d'

def home(request):
    city = 'Bangalore'

    if request.method == 'POST':
        city = request.POST.get('city')

        if not city:
            city = 'Bangalore'

    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    data = None
    error = None

    try:
        response = requests.get(url=URL)
        print(response)
        print("Status Code:", response.status_code)
        print("\nHeaders:")
        print(response.headers)

        print("\nText:")
        print(response.text)

        print("\nContent (bytes):")
        print(response.content)

        print("\nJSON:")
        print(response.json())

        if response.status_code == 200:
            data = response.json()
            print(type(data),type(response))
            print(response)
        else:
            error =  'City not found'
    except:
        error = 'Something went wrong!!!'
        
        
    context = {
        'data':data,
        'error':error,
    }

    return render(request, 'home.html', context)