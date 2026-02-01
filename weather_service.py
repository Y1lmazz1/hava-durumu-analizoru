import requests

def get_weather_data(lat, lon):
    """Koordinatları kullanarak anlık hava durumunu getirir."""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["current_weather"]
    return None