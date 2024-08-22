def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if not recipient.endswith(".com") and not recipient.endswith(".ru") and not recipient.endswith(".net"):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if not sender.endswith(".com") and not sender.endswith(".ru") and not sender.endswith(".net"):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if '@' not in sender or recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    elif sender != "university.help@gmail.com" or sender == ('.net' or '.ru' or '.com'):
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Привет', 'assah.ru', sender='boobs@ah.ru')
