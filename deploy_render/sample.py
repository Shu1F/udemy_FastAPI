import requests
import json


def main():
    url = "https://udemy-fastapi-1hav.onrender.com/"
    data = {"x": 12, "y": 3.0}
    res = requests.post(url, json.dumps(data))
    print(res.json())


if __name__ == "__main__":
    main()
