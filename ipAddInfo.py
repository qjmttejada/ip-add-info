import requests

#get user input 
def get_ip():
    response = input("Enter IP Address: ")
    return response

#API to get the info of the computer's IP Address
def get_info():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "postal_code": response.get("postal"),
        "isp": response.get("org")
    }
    return location_data

print(get_info())