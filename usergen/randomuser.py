import requests
import codecs

class DataGenerator:
    def __init__(self):
        self.base_url = 'https://randomuser.me/api/'

    def generate_users(self, results=1):
        if results > 5000:
            results = 5000  # Maksimal 5000 data
        url = f'{self.base_url}?results={results}'
        response = requests.get(url)
        data = response.json()
        return data.get('results', [])

class FileWriter:
    def save_to_txt(self, users):
        with codecs.open('results.txt', 'w', 'utf-8') as file:
            for user in users:
                full_name = f"{user['name']['first']} {user['name']['last']}\n"
                file.write(full_name)
        print("Data pengguna telah disimpan di results.txt")
