# Импортируем SMTP протокол для отправки сообщений, необходим для поключения к почте
import smtplib
# Класс из модуля, для работы с сообщениями
from email.message import EmailMessage


# Список нужных адресов
imails_list = ['...', '...']


for adres in imails_list:                       # Описываем цикл для каждого адреса
    email = EmailMessage()                      # Присваиваем переменной класс
    email['from'] = '...'                       # Пишем от кого будет сообщение имя и фамилия
    email['to'] = adres                         
    email['subject'] = '...'                    # Тема сообщения

    # Загружаем файл с сообщением 
    letter = open('letter.txt')
    email.set_content(letter.read())

    # Подключаемся к акаунту gmail
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('логин', 'пароль')             # Логинимся
        # Указываем то, что будем отправлять
        smtp.send_message(email)
        # Вывести запись, что все хорошо
        print('all done')
