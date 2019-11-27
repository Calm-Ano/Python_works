import requests

url = "https://i-amabile.com/concert/tduorch81"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}

for i in range( int(input("how many connect")) ):
    print_message = requests.get(url, headers)
    print (print_message)
