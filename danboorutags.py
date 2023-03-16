import subprocess
import requests
import json
import sys


def clear_screen():
    try:
        subprocess.run('clear', shell=True, check=True, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError:
        subprocess.run('cls', shell=True, check=True, stderr=subprocess.DEVNULL)
    except:
        pass


def main():
    image_id = '6110318'
    base_url = 'https://danbooru.donmai.us/posts'

    clear_screen()

    response = requests.get(f'{base_url}/{image_id}.json')

    if image_id == '':
        sys.exit('[ABORTED]: The Image ID cannot be empty!')

    if not response.status_code == 200:
        sys.exit(f'[ERROR]: {response.status_code}')
    
    data = json.loads(response.text)

    character = data['tag_string_character']
    origin = data['tag_string_copyright']
    tags = data['tag_string_general']
    prompt = f'{character} {origin} {tags}'

    print(f'Character: {character}')
    print(f'Origin: {origin}')
    print(f'Tags: {tags.replace(" ", ", ")}')
    print(f'\nPrompt: {prompt.replace(" ", ", ")}')

  
if __name__ == '__main__':
    main()
