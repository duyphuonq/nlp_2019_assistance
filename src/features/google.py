import os


def google(text):
    os.system('python -m webbrowser -t "https://www.google.com/search?q=' + text + '"')
