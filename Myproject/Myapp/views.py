import requests
from django.http import JsonResponse
from django.shortcuts import render

def get_weather(request):
    location = request.GET.get('location')  # Get the location from the request parameters
    
    # Make the API request
    if ',' in location:
        # If it's a coordinate, directly use it in the API request
        coordinates = location.split(',')
        url = f'http://api.weatherapi.com/v1/current.json?key=9987e23118a54507b64131642230810&q={coordinates[0]},{coordinates[1]}&aqi=no'
    else:
        # If it's a location name, use it in the API request
        url = f'http://api.weatherapi.com/v1/current.json?key=9987e23118a54507b64131642230810&q={location}&aqi=no'
    response = requests.get(url)

    # Process the API response
    if response.status_code == 200:
        weather_data = response.json()
        # Extract the specific weather information you need from weather_data

        # For example, extracting temperature and conditions:
        temperature = weather_data['current']['temp_c']
        conditions = weather_data['current']['condition']['text']
        # location=location['name']
        wind=weather_data['current']['wind_kph']
        humidity=weather_data['current']['humidity']
        precip_in=weather_data['current']['precip_in']
        # Prepare the response data
        data = {
            'temperature': temperature,
            'conditions': conditions,  
            'location':location,
            'wind':wind,
            'humidity':humidity,
            'precip_in':precip_in
        }
        return JsonResponse(data)
    else:
        # Handle API request errors
        return JsonResponse({'error': 'Unable to fetch weather data'}, status=500)
    
def weather_page(request):
    return render(request, 'home.html')  # Render the weather.html template
