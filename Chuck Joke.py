import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        joke = data.get("value")
        if joke:
            print("Chuck Norris Joke:")
            print(joke)
        else:
            print("Could not find a joke in the response.")
    else:
        print(f"Failed to get joke. Status code: {response.status_code}")

if __name__ == "__main__":
    get_chuck_norris_joke()
