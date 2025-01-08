import requests
import json
import os

def getItemInfo(url): # Function to get item info from CSFloat API
    url = "https://api.csfloat.com/?url=" + url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://csfloat.com/",
        "Origin": "https://csfloat.com",
        "DNT": "1",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "saeme-site",
        "Sec-GPC": "1",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()['iteminfo']
    else:
        return None
    
def downloadMetadata(data_dict, filename):
    """
    Saves a dictionary as JSON and downloads an image from its URL.

    Args:
        data_dict (dict): The dictionary to save as JSON.
        filename (str): The filename (without extension) for both JSON and image.
    """

    # Create directory if it doesn't exist
    skin_data_dir = 'skinData'
    os.makedirs(skin_data_dir, exist_ok=True)  # exist_ok avoids permission errors

    # Save JSON file
    json_file_path = os.path.join(skin_data_dir, filename + '.json')
    with open(json_file_path, 'w+') as json_file:
        json.dump(data_dict, json_file)

    # Download image (if URL exists)
    image_url = data_dict.get('imageurl')
    if image_url:
        image_path = os.path.join(skin_data_dir, filename + '.png')
        img_data = requests.get(image_url).content
        with open(image_path, 'wb') as image_file:
            image_file.write(img_data)


# Example usage:
url = "steam://rungame/730/76561202255233023/+csgo_econ_action_preview%20M4863400006831077058A37123283156D7522146505598479261"
item_info = getItemInfo(url)
downloadMetadata(item_info, "1")
print(item_info.get('imageurl'))
print(type(item_info))
print(item_info)