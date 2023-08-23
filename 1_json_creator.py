import requests
from bs4 import BeautifulSoup
import constants

# importing constants
main_slug = constants.MAIN_SLUG
page_slug = constants.PAGE_SLUG
page = constants.PAGE
category = constants.CATEGORY
img_size = constants.IMG_SIZE
file_name = constants.FILE_NAME


def get_response(category, page):
    # function to get the response from the server

    url = main_slug + category + page_slug + str(page)
    response = requests.get(url)

    if response.status_code == 200:
        print("Website response is correct.")
    elif response.status_code == 404:
        print("The requested page was not found (404).")
    elif response.status_code == 403:
        print("Access to the requested page is forbidden (403).")
    elif response.status_code == 500:
        print("The server encountered an internal error (500).")
    else:
        print(
            f"There was a problem with the website response. Status code: {response.status_code}")

    return response


response = get_response(category, page)
soup = BeautifulSoup(response.content, "html.parser")


def remove_everything_before_string(soup, target_string):
    # function to remove everything before a string

    lines = str(soup).split(target_string, 1)
    if len(lines) > 1:
        content_after_target = lines[1]
        updated_content = target_string + content_after_target
    else:
        updated_content = str(soup)
    updated_soup = BeautifulSoup(updated_content, 'html.parser')

    return updated_soup


def remove_everything_after_string(soup, target_string):
    # function to remove everything after a string

    lines = str(soup).split('\n')
    keep_flag = True
    modified_content = []
    for line in lines:
        if target_string in line:
            keep_flag = False
        if keep_flag:
            modified_content.append(line)
    updated_content = '\n'.join(modified_content)
    updated_soup = BeautifulSoup(updated_content, 'html.parser')

    return updated_soup


def remove_lines_containing_strings(input_string, strings_to_remove):
    # function to remove lines containing certain strings from a list

    lines = input_string.split('\n')
    modified_content = []
    for line in lines:
        if not any(remove_str in line for remove_str in strings_to_remove):
            modified_content.append(line)
    updated_content = '\n'.join(modified_content)

    return updated_content


# using the preeviously made functions to get the correct string format for json from the soup element
updated_soup_1 = remove_everything_before_string(soup, "images = [")
updated_soup_2 = remove_everything_after_string(updated_soup_1, "];\n")
updated_soup_3 = remove_everything_after_string(updated_soup_2, "<div ")

string_to_write = str(updated_soup_3)
string_to_write = string_to_write[:-1]
beginning_string = "import json \n\n"
ending_string = "\n\nwith open(\"image_data.json\", \"w\") as json_file: \n\t json.dump(images, json_file, indent=4)"
string_to_write = beginning_string + string_to_write + ending_string

# removing the unwanted key-value pairs from the json string
strings_to_remove = ['title', 'height', 'width', 'url', 'potw:']
final_string = remove_lines_containing_strings(
    string_to_write, strings_to_remove)


def perform_find_replace(input_string):
    # function to fina and replace certain strings to get the correct json format

    find_replace_dict = {
        "id": "'id'",
        "src": "'src'",
        "thumb300y": img_size
    }

    try:
        content = input_string

        for find_str, replace_str in find_replace_dict.items():
            content = content.replace(find_str, replace_str)

        print("Find and replace operations completed successfully.")
        return content

    except Exception as e:
        print("An error occurred:", str(e))
        return None


json_string = perform_find_replace(final_string)
# print(json_string)

# create/rewrite the python file
try:
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(json_string)
    print(f"File '{file_name}' written successfully.")
except Exception as e:
    print("An error occurred:", str(e))
