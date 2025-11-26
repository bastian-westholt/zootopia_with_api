"""Module for loading animal data and generating HTML output."""

import os
from dotenv import load_dotenv
import data_fetcher


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
    output += f'    <p class="card__text">\n'
    output += f'        <strong>Diet:</strong> {animal["characteristics"]["diet"]}</br>\n'
    output += f'        <strong>Location:</strong> {animal["locations"][0]}</br>\n'
    if "type" in animal["characteristics"]:
        output += f'        <strong>Type:</strong> {animal["characteristics"]["type"]}\n'
    output += f'    </p>\n'
    output += f'  </div>\n'
    output += f'</li>\n'
    output += '\n'
    return output


def get_data(animals_data, animal_input):
    """Convert all animals data to HTML string.

    Args:
        animals_data: List of animal dictionaries

    Returns:
        Combined HTML string for all animals
    """
    output = ''
    if not animals_data:
        output += f"<h2 class='cards__item' style='text-align: center'>The animal \"{animal_input}\" doesn't exist.</h2>"
    else:
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