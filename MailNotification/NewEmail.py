class Email(object):
    """
    The class of an e-mail.

    Attributes:
        sender (str): The sender of this mail. It should belong to the user of
            mail server.
        receivers (List[str]): The receivers of this mail.
        subject (str): The subject of this mail. Default is "No subject"
        content (str): The content of this mail. Default is empty string.
    """
    def __init__(self, sender=None, receivers=None, subject='No subject', content=''):
        """
        The definition of an email.

        Args:
            sender (str): The sender of this mail. It should belong to the user of
                mail server.
            receivers (List[str]): The receivers of this mail.
            subject (str): The subject of this mail. Default is "No subject"
            content (str): The content of this mail. Default is empty string.
        """
        self.sender = sender
        self.receivers = receivers
        self.subject = subject
        self.content = content
