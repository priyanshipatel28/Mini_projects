#the json fiel is in dictionary not list so, i can't use choice as random!!!
# import requests
# import json
# import random
# url = "https://qapi.vercel.app/api/random"
# r = requests.get(url)
# qu = r.json()
# quote = random.choice(qu)

# print(quote)


import requests
import json

url = "https://qapi.vercel.app/api/random"

try:
    r = requests.get(url)
    r.raise_for_status()  # Raises an HTTPError if the request was unsuccessful
    qu = r.json()

    # Extract quote and author safely
    quote = qu.get("quote", "No quote found.")
    author = qu.get("author", "Unknown Author")

    # Print the formatted output
    print("\nRandom Quote")
    print(f"\"{quote}\"")
    print(f"- {author}\n")

except requests.exceptions.RequestException as e:
    print("\nError: Unable to fetch quote!")
    print(f"Reason: {e}\n")

except json.JSONDecodeError:
    print("\nError: Failed to decode API response. The data format might have changed.\n")

