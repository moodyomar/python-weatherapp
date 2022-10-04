import requests

def get_relevant_bg():
    bgs = {
        "overcast clouds":"static/images/clouds.jpeg",
        "clear sky":"static/images/clear.jpeg",
        "snow":"static/images/snow.jpeg",
        "heavy intensity rain":"static/images/heavyrain.jpeg",
        "moderate rain":"static/images/rain.jpeg",
        "light intensity shower rain":"static/images/rain.jpeg",
        "broken clouds":"static/images/brokenclouds.jpeg",
        "scattered clouds":"static/images/scatteredclouds.jpeg",
        "few clouds":"static/images/fewclouds.jpeg",
        "light rain":"static/images/lightrain.jpeg",
        "light intensity drizzle":"static/images/lightrain.jpeg",
        "haze":"static/images/haze.jpeg",
        "fog":"static/images/fog.jpeg",
    }
    return bgs

api = {
    "key": "f738629a362bfb615e811eeeda4f40a1",
    "baseurl": "https://api.openweathermap.org/data/2.5/",
    "city":"phuket"
    }

def get_daily_data():
    data = f"{api['baseurl']}/weather?q={api['city']}&units=metric&APPID={api['key']}"    
    response = requests.get(data)
    return response.json()
        

def get_weekly_data():
    city = get_daily_data()
    days = f"{api['baseurl']}onecall?lat={city['coord']['lat']}&lon={city['coord']['lon']}&units=metric&appid={api['key']}"
    response = requests.get(days)
    return response.json()['daily']

def is_url_up(url):
    try:
        r = requests.head(url)
    except Exception:
        return False
    return r.status_code == 200