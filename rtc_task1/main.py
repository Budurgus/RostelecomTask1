import os
import json
import pandas as pd
from datetime import datetime
from typing import List
from parser import Parse
from email_sender import Sender

def main():


    with open('data/listINN.txt') as file:
        file_info = file.read()

        # Получаем список ИНН
        list_inn: List["str"] = file_info.split("\n")
        counterparties_info = pd.DataFrame()

        # Формируем таблицу
        for inn in list_inn[:]:
            row: dict = Parse(f"https://saby.ru/profile/{inn}").data_collector()
            counterparties_info = pd.concat([counterparties_info, pd.DataFrame([row])], ignore_index=True)

        # Сохраняем таблицу
        file_path = f'C:/Users/{os.getlogin()}/Documents/{datetime.now().strftime("%Y-%m-%d %H-%M-%S")} Данные контрагентов.xlsx'
        counterparties_info.to_excel(file_path)

    with open('data/config.json', 'r', encoding='utf-8') as file:
        config = json.load(file)

        if (config["login"] != ""):
            email_sender = Sender(config, file_path)
            email_sender.send_counterparties_data()
        else:
            print("Проверьте файл config")

if __name__ == "__main__":
    main()