import smtplib
from email.mime.text import MIMEText
from email.header import Header


class MailSender(object):
    """
    Email notification class. You can use it in your code. When a long-time mission completes,
    the class will send a notification to you.
    Using:
    sender = MailSender(sender, subject, message, mail_host=xxx, mail_user=xxx, mail_pass=xxx)
    <your codes>
    sender.send_mail(successful_message)
    """
    def __init__(self, sender, subject, message, *args, **kwargs):
        """
        Initialize the mail server. You must provide the information of your mail server.
        :param subject: String. The subject of your mail.
        :param message: String. The message body of your mail.
        :param args:
        :param kwargs: Support these three parameters:
        - mail_host: your mail host server.
        - mail_user: your username of the mail host server.
        - mail_pass: your password of your mail host server. On some servers it may be an authentication code.
        """
        self.mail_host = kwargs['mail_host']
        self.mail_user = kwargs['mail_user']
        self.mail_pass = kwargs['mail_pass']
        self.sender = sender
        self.receivers = [sender]

        self.message = MIMEText(message, 'plain', 'utf-8')
        self.message['From'] = Header(sender, 'utf-8')
        self.message['To'] = Header(sender, 'utf-8')
        self.message['Subject'] = Header(subject, 'utf-8')

    def send_mail(self, return_msg):
        """
        Send the email to yourself.
        :param return_msg: If the mail is sent successfully, return a notification message.
        :return:
        """
        try:
            smtpobj = smtplib.SMTP()
            smtpobj.connect(self.mail_host, 25)
            smtpobj.login(self.mail_user, self.mail_pass)
            smtpobj.sendmail(self.sender, self.receivers, self.message.as_string())
            print(return_msg)
        except smtplib.SMTPException:
            print("Failed to send mail.")
