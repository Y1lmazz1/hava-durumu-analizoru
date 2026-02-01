import requests

def get_coordinates(city_name):
    """Şehir ismini koordinata (lat, lon) çevirir."""
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1&language=tr&format=json"
    
    response = requests.get(url)
    data = response.json()
    
    if "results" in data:
        result = data["results"][0]
        return {
            "lat": result["latitude"],
            "lon": result["longitude"],
            "name": result["name"],
            "country": result.get("country", "Bilinmiyor")
        }
    else:
        return None

