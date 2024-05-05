import sys
import requests

def fetch_proxies(country_code, output_files=None):
    url = f"https://api.proxyscrape.com/v3/free-proxy-list/get?request=displayproxies&country={country_code}&proxy_format=protocolipport&format=text"
    response = requests.get(url)

    if response.status_code == 200:
        proxy_list = response.text.split('\n')
        if output_files:
            for output_file in output_files:
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
    output_files = []
    if len(sys.argv) > 1:
        i = 0
        while i < len(sys.argv[1:]):
            arg = sys.argv[1:][i]
            if arg.startswith("--country="):
                country_code = arg.split("=")[1]
            elif arg == "-o":
                i += 1
                if i < len(sys.argv[1:]):
                    output_files.append(sys.argv[1:][i])
            i += 1
    
    if country_code:
        fetch_proxies(country_code, output_files)
    else:
        print("Please provide a country code.")
