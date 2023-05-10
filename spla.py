import requests

api_key = "N7OWNHWblNfll0UKvQrkkB4qty4l2U_xE_miY4SZcBY"
url = f"https://api.unsplash.com/photos/random?client_id={api_key}"
response = requests.get(url)
print(response.status_code)
