import smtplib
from email.mime.text import MIMEText
from email.header import Header
from NewEmail import Email


class MailSender(object):
    """
    Email notification class. You can use it in your code. When a long-time mission completes,
    this module will send a notification to you.

    Usage:
        email = Email(sender, receivers, subject, content)
        sender = MailSender(server_address, username, password)
        (your code here)
        sender.send_mail(email, success_msg, failure_msg)
    """
    def __init__(self, mail_server_address=None, mail_username=None, mail_password=None):
        """
        Initialize the mail server. You must provide the information of your mail server.

        Args:
            mail_server_address (str): The host address of your mail server.
            mail_username (str): Your username.
            mail_password (str): Your password.
        """
        self.mail_server_address = mail_server_address
        self.mail_username = mail_username
        self.mail_password = mail_password

    def send_mail(self, email, success_msg, failure_msg, debug=False):
        """
        Login to mail server and send mail to receivers.

        Args:
            email (Email): The email to be sent.
            success_msg (str): If the email is sent successfully, return the message.
            failure_msg (str): If the email failed to send, return the error message.
            debug (bool): Enables the debug functions.

        Returns:
            str: The success or failure messages.
        Raises:
            smtplib.SMTPException: SMTP Exception
        """
        mail_body = MIMEText(email.content, 'plain', 'utf-8')
        mail_body['From'] = Header(email.sender, 'utf-8')
        if len(email.receivers) == 1:
            mail_body['To'] = Header(email.receivers[0], 'utf-8')
        elif len(email.receivers) > 1:
            mail_body['To'] = Header(','.join(email.receivers), 'utf-8')
        mail_body['Subject'] = Header(email.subject, 'utf-8')
        try:
            smtp_obj = smtplib.SMTP()
            smtp_obj.connect(self.mail_server_address, 25)
            smtp_obj.login(self.mail_username, self.mail_password)
            smtp_obj.sendmail(email.sender, email.receivers, mail_body.as_string())
            return success_msg
        except smtplib.SMTPException as e:
            if debug:
                print(e)
            return failure_msg

