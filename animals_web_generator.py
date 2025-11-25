"""Module for loading animal data and generating HTML output."""

import requests
import json
import os

HEADERS = {
    'X-Api-Key': 'RBOdUrcCXeFrF/AO12uvQA==YcxtK55xKHfbOX6J'
}

def load_data(url):
    """Requests animal json from animal-api.

    Args:
        url: URL for HTTP GET-Method

    Returns:
        Parsed JSON data
    """
    animals_res = requests.get(url, headers=HEADERS).json()
    return animals_res


def serialize_animal(animal):
    """Serialize a single animal object to HTML.

    Args:
        animal: Dictionary containing animal data

    Returns:
        HTML string representation of the animal
    """
    output = ''
    output += f'<li class="cards__item">\n'
    output += f'  <div class="card__title">Name: {animal["name"]}</div>\n'
    output += f'  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}</br>\n'
    output += f'      <strong>Location:</strong> {animal["locations"][0]}</br>\n'
    if "type" in animal["characteristics"]:
        output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}\n'
    output += f'  </p>\n'
    output += f'  </div>\n'
    output += f'</li>\n'
    output += '\n'
    return output


def get_data(animals_data):
    """Convert all animals data to HTML string.

    Args:
        animals_data: List of animal dictionaries

    Returns:
        Combined HTML string for all animals
    """
    output = ''
    for animal in animals_data:
        output += serialize_animal(animal)
    return output


def replace_html_content(template_path, output_path, animals_data_str):
    """Replace placeholder in HTML template with animal data.

    Args:
        template_path: Path to the HTML template file
        output_path: Path for the output HTML file
        animals_data_str: HTML string containing animal data
    """
    with open(template_path, "r") as reader:
        html_content = reader.readlines()

    new_html_content = []
    for line in html_content:
        if '__REPLACE_ANIMALS_INFO__' in line:
            line = line.strip().replace('__REPLACE_ANIMALS_INFO__',
                                        animals_data_str)
        new_html_content.append(line)

    with open(output_path, "w") as writer:
        writer.writelines(new_html_content)


def main():
    """Main function to orchestrate the HTML generation process."""
    animal = input('Enter an animal or an animal-race: ').lower()
    url = f'https://api.api-ninjas.com/v1/animals?name={animal}'
    animals_data = load_data(url)
    animals_data_str = get_data(animals_data)
    replace_html_content('animals_template.html', 'animals.html', animals_data_str)
    print('''
######## - WEBSITE WAS SUCCESSFULLY GENERATED TO "animal.html" - ########''')


if __name__ == '__main__':
    main()