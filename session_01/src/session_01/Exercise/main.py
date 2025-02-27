import requests

def fetch_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print("Data fetched successfully:")
        print(data)
    else:
        print("Failed to fetch data")

if __name__ == "__main__":
    fetch_data()