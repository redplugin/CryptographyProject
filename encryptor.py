# Student: Darmen Tuyakayev
# Course: Python developer 14
# Project: Cryptography

# 7. Проверить папку 'decrypted_reports'.
# 8. Все файлы в названии которых нет буквы "c" зашифровать и сохранить в "encrypted_reports"
# 9. Проект залить в гитхаб.

import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet

# load .env constant (my own secret key) and make a fernet instance
load_dotenv()
my_secret_key = os.getenv("MY_SECRET_KEY")

fernet_key = Fernet(my_secret_key)  # fernet instance

# check if ./decrypted_reports folder exists
decrypted_reports_path = "./decrypted_reports"
if not os.path.exists(decrypted_reports_path):
    raise Exception("There is no decrypted_reports folder in root")


# create a folder for encrypted files if it's not there
encrypted_folder = "./encrypted_reports"
if not os.path.exists(encrypted_folder):
    try:
        os.makedirs(encrypted_folder)
        print(f"Folder '{encrypted_folder}' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the folder: {e}")


# list of filenames in decrypted_reports folder
files = os.listdir(decrypted_reports_path)

# open and encrypt files that don't have "c" it its name
for file in files:
    if "c" not in file:
        with open(f"./{decrypted_reports_path}/{file}", "r", encoding="utf-8") as f:
            content = f.read()

        encrypted_content = fernet_key.encrypt(content.encode("utf-8"))

        with open(f"./{encrypted_folder}/{file}", "w", encoding="utf-8") as f:

            f.write(str(encrypted_content))


# secret_key = Fernet.generate_key()
#
# fernet_key = Fernet(secret_key)
# data = b"Hello, World!"
#
# encrypted_data = fernet_key.encrypt(data)
#
# print("Encrypted data: ", encrypted_data)
#
#
# decrypted_data = fernet_key.decrypt(encrypted_data)
# print(decrypted_data)
