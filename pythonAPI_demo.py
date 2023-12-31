import os
import requests


def pick_img(image):
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'images': [image]
    }
    request_url = "http://127.0.0.1:8001/detect"
    response = requests.post(request_url, headers=headers, json=data)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


if __name__ == '__main__':
    image_path = r"./data"
    for img in os.listdir(image_path):
        new_path = os.path.join(image_path, img)
        data = pick_img(new_path)
        print(data)
