from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="oskolkov_web")
location = geolocator.reverse("61.29, 47.20")
print(location.address)