import requests
import json

API_KEY = os.environ.get('CLOCKIFY_API_KEY')

def main():
    data = {'x-api-key': API_KEY}
    r = requests.get('https://api.clockify.me/api/v1/user', headers=data)
    print(r.content)

if __name__ == "__main__":
    main()
