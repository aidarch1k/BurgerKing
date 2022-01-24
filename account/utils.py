from django.core.mail import send_mail


def send_welcome_email(email):
    message = f'Dear {email}, thank you for registration on our website BurgerKing!'
    send_mail(
        'Weclome to BurgerKing!',
        message,
        'burgerkingadmin@burger.net',
        [email],
        fail_silently=False

    )