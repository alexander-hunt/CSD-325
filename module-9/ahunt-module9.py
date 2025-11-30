import requests
import json

def tutorial():
    response = requests.get("http://api.open-notify.org/astros")
    print(response.status_code)
    #print(response.json())
    text = json.dumps(response.json(), sort_keys=True, indent=4)
    print(text)

def step6(is_formatted: bool):
    response = requests.get("http://anapioficeandfire.com/api/houses/1")
    print(response.status_code)
    if not is_formatted:
        print(response.json())
    if is_formatted:
        text = json.dumps(response.json(), sort_keys=True, indent=4)
        print(text)

if __name__ == "__main__":
    #tutorial()
    print("Step 6 without formatting:")
    step6(False)
    print()
    print("Step 6 with formatting:")
    step6(True)