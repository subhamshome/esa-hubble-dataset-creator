import os
import requests
import json

# Load the JSON data from the file
with open("image_data.json", "r") as json_file:
    images = json.load(json_file)

# Create a directory to save the images
category = 'solarsystem'  # All available categories:
# 'viewall', 'anniversary', 'csomology', 'exoplanets', 'galaxies', 'illustrations', 'jwst',
# 'mission', 'misc', 'nebulae', 'blackholes', 'solarsystem', 'spacecraft', 'starclusters', 'stars'
os.makedirs(category, exist_ok=True)

# Download and save the images
for image in images:
    img_id = image["id"]
    img_url = image["src"]

    img_response = requests.get(img_url)
    if img_response.status_code == 200:
        with open(f"{category}/{img_id}.jpg", "wb") as f:
            f.write(img_response.content)
            print(f"Downloaded {img_id}.jpg")
    else:
        print(
            f"Failed to download {img_id}.jpg. Error Code: {img_response.status_code}")

print("Image download completed.")
