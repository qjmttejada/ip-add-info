import requests
    
#API to get the info of the computer's IP Address
def get_info(ip_address):
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "country_code": response.get("country_code"),
        "postal_code": response.get("postal"),
        "isp": response.get("org"),
        "asn": response.get("asn")
    }
    return location_data

#Main functon
while True:
    response = input("Enter IP Address: ")
    if response == "quit" or response == "q":
        break
    info = get_info(response)
    print(info)