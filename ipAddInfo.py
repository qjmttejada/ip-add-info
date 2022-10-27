import requests
import ipaddress
    
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

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        return True
    except ValueError:
        return False

#Main functon
while True:
    response = input("Enter IP Address: ")
    validate = validate_ip_address(response)
    if response == "quit" or response == "q":
        break
    if validate == True:
        info = get_info(response)
        print(info)
    else:
        print("invalid input")
