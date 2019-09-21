import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="MailNotification",
    version="1.0.1",
    author="RyuAsuka",
    author_email="paulexe@163.com",
    description="A mail notification module",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/RyuAsuka/mail_notification',
    packages=setuptools.find_packages(),
    classifier=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)
