# esa-hubble-dataset-creator
A collection of consecutively run python scripts to download images taken by the Hubble's Telescope

This repository contains Python scripts to scrape and download images from the [ESA Hubble website](https://esahubble.org/). The scripts utilize web scraping techniques to gather image data, generate JSON files, and download the corresponding images. The downloaded images are organized into categories and saved in separate directories.

## Prerequisites
Before running the scripts, ensure you have the following dependencies installed:

- Python (3.x)
- requests library
- BeautifulSoup library

You can install the required packages using the following command:
`pip install requests BeautifulSoup4`

## Scripts
### 1_json_creator.py
This script scrapes image data from the ESA Hubble website. It retrieves images based on a specified category and page number, processes the data, and generates a JSON file named `image_data.json`.

### 2_json_saver.py
This script generates a JSON file containing image information. You can customize the list of images with their IDs and URLs. This script can be used to create the initial JSON dataset before scraping from the website.

### 3_image_downloader.py
This script uses the JSON file generated by the previous scripts to download images from the ESA Hubble website. The images are saved in separate directories based on the specified category.

## Usage
1. Run the `1_json_creator.py` script to scrape image data from the ESA Hubble website. You can customize the category and page number in the script. This file will generate the next file to be executed.
2. This file saved the json data in into a file called `image_data.json`. Alternatively, if you want to use a pre-defined set of images, you can modify the `2_json_saver.py` script to include your desired image data and run it to generate the JSON file.
3. Run the `3_image_downloader.py` script to download images based on the JSON data. Images will be saved in separate directories named after the specified category.

## Runner Files
- `run_scripts.bat`: A batch file to automate the execution of the Python scripts. Modify the batch file to include the appropriate Python interpreter and script filenames.
- `run_scripts.txt`: In case the `run_scripts.bat` doesn't get executed, copy the text from this file and paste it in the terminal or command window in the same directory as your scripts and run.

## License
This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).

The images are taken from ESA Hubble official website. They are licensed under the [Free Creative Commons Images](https://esahubble.org/public/copyright/).

## Acknowledgments
The scripts in this repository were developed for educational purposes and utilize web scraping techniques. Use them responsibly and in accordance with the terms of use of the ESA Hubble website.
