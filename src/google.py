def google(text):
    import os
    os.system('python -m webbrowser -t "https://www.google.com/search?q=' + text + '"')

google('thời tiết')