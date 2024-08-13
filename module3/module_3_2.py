def send_email(message: str, recipient: str, *, sender='university.help@gmail.com') -> str:
    """Returns a notification about the sending status of a message

    Args:
        message: message to send
        recipient: receives a letter
        sender: sends a letter

    Returns:
        notification

    """
    flag_email = ['.com', '.ru', '.net']
    check_email_correct_recipient = False
    check_email_correct_sender = False
    check_email_correct_all = True
    check_at_sign = False

    for i in flag_email:
        if recipient.endswith(i):
            check_email_correct_recipient = True
        if sender.endswith(i):
            check_email_correct_sender = True
    if not (check_email_correct_recipient and check_email_correct_sender):
        check_email_correct_all = False

    if "@" in sender and "@" in recipient:
        check_at_sign = True

    if not (check_email_correct_all and check_at_sign):
        notification = f'Невозможно отправить письмо с адреса "{sender}" на адрес "{recipient}"'
    elif recipient == sender:
        notification = 'Нельзя отправить письмо самому себе!'
    elif sender == 'university.help@gmail.com':
        notification = f'Письмо успешно отправлено с адреса "{sender}" на адрес "{recipient}".'
    else:
        notification = f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса "{sender}" на адрес "{recipient}"'
    return notification


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(
    send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
