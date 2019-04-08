# Mail Notification

![python-version](https://img.shields.io/pypi/pyversions/Django.svg) ![module-version](https://img.shields.io/badge/version-1.0-brightgreen.svg)

This simple python script is used to notify you that your task has completed.

You should prepare an e-mail account and setup it with SMTP/POP3/IMAP authentication code.

Using:

This script can be imported into the project of yourself. After your code completes running, this module will send a mail to you.

It is adapted to a long loop in Python.

```python
from Notification import MailSender

sender = MailSender(sender, subject, message, mail_host=mail_host, mail_user=mail_user, mail_pass=mail_pass)
# your code here
sender.send_mail(success_message)

```
