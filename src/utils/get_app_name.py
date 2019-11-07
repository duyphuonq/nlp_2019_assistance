# -*- coding: utf-8 -*
computerApp = [
    "intellij",
    "pycharm",
    "chrome",
    "firefox",
    "steam",
    "terminal",
    "skype",
    "dropbox",
    "pinta"
]

famousWebsite = {
    "instagram.com": ["instagram.com", "insta", "instagram"],
    "facebook.com": ["facebook.com", "facebook", "face"],
    "mail.google.com": ["gmail", "mail.google.com"],
    "twitter.com": ["twitter.com", "tweet", "twitter"],
    "wikipedia.com": ["wikipedia", "wiki"],
    "reddit.com": ["reddit.com", "reddit"],
    "youtube.com": ["youtube.com", "youtube"],
    "github.com": ["github.com", "github", "git"],
    "geeksforgeeks.org": ["geeksforgeeks.org", "geeksforgeeks"],

    "xvideos.com": ["xvideos.com", "xvideos"],
    "pornhub.com": ["pornhub.com", "pornhub"],
    "xnxx.com": ["xnxx.com", "xnxx"],
    "xhamster.com": ["xhamster.com", "xhamster"],

    "yahoo.com": ["yahoo.com", "yahoo.com"],
    "amazon.com": ["amazon.com", "amazon"],
    "google.com": ["google.com", "google"],
    "linkedin.com": ["linkedin.com", "linkedin"],
    "netflix.com": ["netflix.com", "netflix"],
    "phimmoi.com": ["phimmoi.com", "phimmoi"]
}


from src.constants import NORMAL_APP, WEB_APP


def open_app(command):
    newCommand = command.lower()
    newCommand = newCommand.split()
    isApp = True
    result = "-1"
    diff = 0
    for word in newCommand:
        for item in computerApp:
            currentDiff = abs(len(item) - len(word))
            for i in range(0, min(len(item), len(word))):
                if item[i] != word[i]:
                    currentDiff += 1
            if result == "-1" or currentDiff < diff:
                result = item
                diff = currentDiff

    for word in newCommand:
        for itemDict in famousWebsite:
            for item in famousWebsite[itemDict]:
                currentDiff = abs(len(item) - len(word))
                for i in range(0, min(len(item), len(word))):
                    if item[i] != word[i]:
                        currentDiff += 1
                if result == "-1" or currentDiff < diff:
                    result = itemDict
                    diff = currentDiff
                    isApp = False
    if isApp:
        return [NORMAL_APP, result]
    else:
        return [WEB_APP, "www." + result]


def close_app(command):
    newCommand = command.lower()
    newCommand = newCommand.split()
    result = "-1"
    diff = 0
    for word in newCommand:
        for item in computerApp:
            currentDiff = abs(len(item) - len(word))
            for i in range(0, min(len(item), len(word))):
                if item[i] != word[i]:
                    currentDiff += 1
            if result == "-1" or currentDiff < diff:
                result = item
                diff = currentDiff
    return result


if __name__ == '__main__':
    print(open_app('tôi muốn vào chrom quá'))
