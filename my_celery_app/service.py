from django.core.mail import send_mail


def send(user_email):
    send_mail('Вы подписаны на рассылку',
              'Это спам',
              '11masek33@gmail.com',
              [user_email],
              fail_silently=False
              )
