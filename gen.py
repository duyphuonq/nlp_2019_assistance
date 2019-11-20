import csv

objects = [
    "phim",
    "thời tiết",
    "face",
    "insta",
    "intellij",
    "pycharm",
    "chrome",
    "firefox",
    "steam",
    "terminal",
    "skype",
    "dropbox",
    "pinta",
    "instagram.com",
    "insta",
    "instagram",
    "facebook.com",
    "facebook",
    "face",
    "gmail",
    "mail.google.com",
    "twitter.com",
    "tweet",
    "twitter",
    "wikipedia",
    "wiki",
    "reddit.com",
    "reddit",
    "youtube.com",
    "youtube",
    "geeksforgeeks.org",
    "geeksforgeeks",
    "xvideos.com",
    "yahoo.com",
    "yahoo.com",
    "amazon.com",
    "amazon",
    "google.com",
    "google",
    "linkedin.com",
    "linkedin",
    "netflix.com",
    "netflix",
    "phimmoi.com",
    "phimmoi",
    "thời tiết",
    "phim",
    "tủ quần áo",
    "cửa"
]

if __name__ == '__main__':
    # chuong trinh se thay "." trong s thanh ung dung can mo hoac dong
    s = list(input().split())
    label = int(input())
    pos = 0
    for i in range(len(s)):
        if s[i] == ".":
            pos = i
    with open('genData.csv', mode='a', encoding="utf8", newline='\n') as write_file:
        fieldnames = ['sentence', 'label']
        csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        for obj in objects:
            lst = s.copy()
            lst[pos] = obj
            lst = ' '.join(lst)
            print(lst)
            csv_writer.writerow({'sentence': lst, 'label': label})
