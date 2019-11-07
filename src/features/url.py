import os


def open_address(url):
    os.system('python -m webbrowser -t "https://' + url + '"')
