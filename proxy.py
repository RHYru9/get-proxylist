import sys
import requests

def fetch_proxies(country_code, output_file=None):
    url = f"https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&country={country_code}&proxy_format=protocolipport&format=text"
    response = requests.get(url)

    if response.status_code == 200:
        proxy_list = response.text.split('\n')
        if output_file:
            with open(output_file, 'w') as f:
                for proxy in proxy_list:
                    f.write(proxy + '\n')
            print(f"Proxies saved to {output_file}")
        else:
            for proxy in proxy_list:
                print(proxy)
    else:
        print("Failed to fetch proxies. Status code:", response.status_code)

if __name__ == "__main__":
    country_code = None
    output_file = None
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg.startswith("--country="):
                country_code = arg.split("=")[1]
            elif arg.startswith("-o="):
                output_file = arg.split("=")[1]
    
    if country_code:
        fetch_proxies(country_code, output_file)
    else:
        print("Please provide a country code.")
