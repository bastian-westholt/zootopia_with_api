import src.animals_web_generator as gen
from src.data_fetcher import fetch_data

def main():
    """Main function to orchestrate the HTML generation process."""
    animal = input('Enter an animal or an animal-race: ').lower()
    animals_data = fetch_data(animal)
    animals_data_str = gen.get_data(animals_data, animal)
    gen.replace_html_content('templates/animals_template.html', f'output/{animal}.html', animals_data_str)
    print('''
######## - WEBSITE WAS SUCCESSFULLY GENERATED TO "animal.html" - ########''')


if __name__ == '__main__':
    main()