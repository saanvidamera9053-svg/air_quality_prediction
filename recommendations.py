def get_aqi_recommendations(aqi):
    if aqi <= 50:
        return "Air quality is good 😊"
    elif aqi <= 100:
        return "Moderate air quality 😐"
    elif aqi <= 150:
        return "Unhealthy for sensitive groups 😷"
    elif aqi <= 200:
        return "Unhealthy 🚫"
    else:
        return "Very unhealthy ☠️ Stay indoors!"