import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate


class Sender:
    def __init__(self, config, file_path: str):
        self.config = config
        self.file_path = file_path

    # с почтой не работал, взял пример. Пытался добавить множественную рассылку, но не дал из-за подозрения на спам
    # ну и файлы приходят странного формата, не смог справиться с этим
    def send_counterparties_data(self):

        from_mail = self.config['login']  # Почта отправителя
        from_passwd = self.config['password']  # пароль от почты отправителя
        server_adr = self.config['server_name']  # адрес почтового сервера
        to_mail = self.config['to']  # адрес получателя

        msg = self.form_letter(from_mail, to_mail)

        smtp = smtplib.SMTP(server_adr, 25)  # Создаем объект для отправки сообщения
        smtp.starttls()  # Открываем соединение
        smtp.ehlo()
        smtp.login(from_mail, from_passwd)  # Логинимся в свой ящик
        smtp.sendmail(from_mail, to_mail, msg.as_string())  # Отправляем сообщения
        smtp.quit()  # Закрываем соединение

    def form_letter(self, from_mail, to_mail):
        file_name, _ = os.path.basename(self.file_path).split('.')
        date = ' '.join(os.path.basename(self.file_path).split(' ')[:2])
        msg = MIMEMultipart()  # Создаем сообщение
        msg["From"] = from_mail  # Добавляем адрес отправителя
        msg['To'] = ', '.join(to_mail)  # Добавляем адрес получателя
        msg["Subject"] = Header(f"Сбор данных контрагентов за {date}", 'utf-8')  # Пишем тему сообщения
        msg["Date"] = formatdate(localtime=True)  # Дата сообщения
        msg.attach(MIMEText("Добрый день! Направляю полученные данные компаний-контрагентов", 'html', 'utf-8'))  # Добавляем форматированный текст сообщения

        with open(self.file_path, "rb") as attachment:
            part = MIMEBase("application", "vnd.ms-excel")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_name}",
        )

        # Внесение вложения в сообщение и конвертация сообщения в строку
        msg.attach(part)

        return msg
