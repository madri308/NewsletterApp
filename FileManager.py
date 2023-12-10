import webbrowser
import os
import json
import re

CSS_FILENAME_PATTERN = re.compile(r'<link\s+rel="stylesheet"\s+type="text/css"\s+href="([^"]+)"\s*/>(?![\s\S]*<!--\s*<link)', re.IGNORECASE)
RECIPIENTS_DATA_JSON_FILENAME = "recipients_data.json"

def open_html_in_browser(html_content):
    # Save HTML content to a file
    with open("temp.html", "w") as html_file:
        html_file.write(html_content)

    # Open the file in the default web browser
    webbrowser.open('file://' + os.path.realpath("temp.html"))

def get_html_data(file_path):
    # Read the content of the selected file
    with open(file_path, "r", encoding="utf-8") as file:
        return (file.read(), file.name.split("/")[-1:][0], file_path)

def get_css_content(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read().replace("\n", "\n\t")
        
def integrate_css(html_content, html_file_path):
        match = CSS_FILENAME_PATTERN.search(html_content)
        while match:
            css_path = os.path.normpath(os.path.join(os.path.dirname(html_file_path), match.group(1)))
            html_content = html_content.replace(
                match.group(0), 
                ('<!-- Style %s -->\n<style>\n%s\n</style>'%(
                    match.group(1), 
                    get_css_content(css_path)
                ))
            )
            match = CSS_FILENAME_PATTERN.search(html_content)
        return html_content

def load_data():
    try:
        with open(RECIPIENTS_DATA_JSON_FILENAME, "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None
    
def save_data(data):
    with open(RECIPIENTS_DATA_JSON_FILENAME, "w") as file:
        json.dump(data, file, indent=2)