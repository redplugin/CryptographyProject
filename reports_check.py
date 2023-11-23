# Student: Darmen Tuyakayev
# Course: Python developer 14
# Project: Cryptography

# 4. Прочитать дешифрованные файлы (вывести в консоль)
# 5. Все префиксы "вра" заменить на "дру" (не смотря на регистр)
# 6. Добавить в конец файла новую строку "Проверено!".

import os
import re

decrypted_reports_path = 'decrypted_reports'
files = os.listdir(decrypted_reports_path)  # list of filenames in decrypted_reports folder

for file in files:
    with open(f"./{decrypted_reports_path}/{file}", "r", encoding="utf-8") as f:
        content = f.read()

        print(f"Contents of {file}:")
        print(f"{content}\n")

        # Make words starting with Вра/вра start with Дру/дру
        content = re.sub(r'\bВра(\w*)', r'Дру\1', content)
        content = re.sub(r'\bвра(\w*)', r'дру\1', content)

        # Add "Checked!" at the end of each file
        content += "\n-------------------\nChecked!"

        print(f"Contents of {file} after editing:")
        print(f"{content}\n")

    with open(f"./{decrypted_reports_path}/{file}", "w", encoding="utf-8") as f:
        f.write(content)

