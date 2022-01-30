from django.core.mail import send_mail

def send(user_mail):
    send_mail(
        'Вы подписались на рассылку от Галереи',
        'Спасибо, что вы подписались на рассылку! Вы будете получать анонсы предстоящих событий и информацию о новых работах художников.',
        'kiselev@nataliustimenko.ru',
        [user_mail],
        fail_silently=False,
    )