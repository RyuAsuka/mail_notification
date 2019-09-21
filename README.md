# Mail Notification

![python-version](https://img.shields.io/pypi/pyversions/Django.svg) ![module-version](https://img.shields.io/badge/version-1.0.1-green.svg) ![license](https://img.shields.io/github/license/RyuAsuka/mail_notification)

This simple python script is used to notify you that your task has completed.

You should prepare an e-mail account and setup it with SMTP/POP3/IMAP authentication code.

Usage:

This script can be imported into the project of yourself. After your code completes running, this module will send a mail to you.

It is adapted to a long loop in Python.

```python
from MailNotification.NewEmail import Email
from MailNotification.Notification import MailSender


# Build an email
mail = Email(sender, receiver, subject, content)
# Define a mail sender
sender = MailSender(mail_server_address="your e-mail smtp server", mail_username="your username", mail_password="your password")
# your code here
sender.send_mail(mail, success_message, fail_message)

```

If the code runs successfully, you (or other receivers) will receive the mail.
