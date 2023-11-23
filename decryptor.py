# Student: Darmen Tuyakayev
# Course: Python developer 14
# Project: Cryptography

# 1. Проверить наличие отчета внутри папки 'spy_reports' для каждого дня октября.
# 2. Если отчета не существует, вывести в консоль что его нет.
# 3. Если отчет есть, нужно дешифровать и сохранить в другом месте (decrypted_reports/) для дальнейшей работы.
# (ключи для дешифрования нужно записать в .env файл)

import os
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# load .env constant (secret key provided by project files)
load_dotenv()
secret_key = os.getenv("SECRET_KEY")

# make a fernet instance
fernet_key = Fernet(secret_key)

# create a folder for decrypted files if it's not there
decrypted_folder = "./decrypted_reports"
if not os.path.exists(decrypted_folder):
    try:
        os.makedirs(decrypted_folder)
        print(f"Folder '{decrypted_folder}' created successfully.")
    except Exception as e:
        print(f"Error occurred while creating the folder: {e}")


# create dictionary with all the datetimes with reports
spy_reports_path = 'spy_reports'
files = os.listdir(spy_reports_path)  # list of filenames in spy_reports folder

dates_with_report = dict()
for file in files:
    # Extract date part from the file name
    date_part = file.split('_')[0:3]  # Extract DD, MM, YYYY as a list

    # Join the date parts to form the date string
    date_string = '_'.join(date_part)

    # Convert the date string to a datetime object
    file_date = datetime.strptime(date_string, '%d_%m_%Y')
    dates_with_report[file_date] = file


# Set the first day of October, the last day of October and current day as datetime instances
current_year = datetime.now().year
first_day_october = datetime(current_year, 10, 1)
last_day_october = datetime(current_year, 10, 31)
current_day = first_day_october

# Iterate through every day of October
while current_day <= last_day_october:
    if current_day not in dates_with_report.keys():
        print(current_day.strftime("%d %b %Y") + " There is no report for this date, skipping...")
        current_day += timedelta(days=1)
        continue
    else:
        with open(f"./{spy_reports_path}/{dates_with_report[current_day]}", "rb") as f:
            encrypted_content = f.read()
            decrypted_content = fernet_key.decrypt(encrypted_content)
            utf8 = decrypted_content.decode()

        with open(f"{decrypted_folder}/{dates_with_report[current_day]}", "w", encoding="utf-8") as fw:
            fw.write(utf8)
        print(current_day.strftime("%d %b %Y") + " The report is decrypted and saved to",
              decrypted_folder + "/" + dates_with_report[current_day])

    current_day += timedelta(days=1)


