# Random User Generator

Library ini memungkinkan untuk menghasilkan maksimal 5000 data pengguna acak menggunakan RandomUser API dan menyimpannya ke dalam file txt.



## Penggunaan Class

### `DataGenerator`

Class `DataGenerator` bertanggung jawab untuk menghasilkan data pengguna menggunakan RandomUser API.

#### Metode:
- `generate_users(results)`: Metode ini menerima argumen `results` yang merupakan jumlah data pengguna yang ingin dihasilkan. Jumlah data yang diminta akan dibatasi maksimal hingga 5000. Metode ini akan mengembalikan daftar data pengguna sesuai dengan jumlah yang diminta.

### `FileWriter`

Class `FileWriter` bertanggung jawab untuk menulis data pengguna ke dalam file teks.

#### Metode:
- `save_to_txt(users)`: Metode ini menerima argumen `users`, yang merupakan daftar data pengguna yang akan disimpan. Metode ini akan menulis data pengguna ke dalam file 'results.txt' dengan format nama depan dan belakang dari setiap pengguna di baris terpisah.


## API 
Python Basic API wrapper
```http
  https://randomuser.me/api/
```

## Installation

Install my-project with npm

```bash
  pip install randusergen
```
    

## Usage

Basic Usage :

```python
from randomuser import DataGenerator, FileWriter

# Membuat objek DataGenerator
data_generator = DataGenerator()

# Menghasilkan 10 data pengguna
users = data_generator.generate_users(10)

# Membuat objek FileWriter
file_writer = FileWriter()

# Menyimpan data pengguna ke dalam file txt
file_writer.save_to_txt(users)
```

## Authors

- [@codewithwan](https://github.com/codewithwan)

