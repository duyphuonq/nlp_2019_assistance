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
    "xvideos",
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

sentences = [
    ["tôi muốn tắt . ngay", 0],
    ["đóng . ngay lập tức", 3],
    ["tôi muốn tắt . ngay", 0],
    ["tôi rất muốn mở . ngay bây giờ", 0],
    ["làm ơn bật . cho tôi", 0],
    ["mở .", 0],
    ["đóng .", 3],
    ["mày đóng . đi", 3],
    ["bạn hãy mở . cho tôi", 0],
    ["mở . đi", 0],
    ["mở . lên đi", 0],
    ["tắt . lại nhé", 3],
    ["bật . lên", 0],
    ["ngắt . ngay", 3],
    ["hãy khởi động .", 0],
    ["khởi động .", 0],
    ["tôi muốn xem .",0],
    ["tắt . đi nhé", 3],
    ["tôi muốn . được bật lên", 0],
    ["tôi muốn . được đóng", 3],
    ["đừng để tôi thấy . nữa", 3],
    ["tôi không muốn thấy . nữa",3],
    [". ơi mở ra", 0],
    [". ơi đóng lại", 3],
    ["cho tôi dùng .", 0],
    [". chạy đi", 0],
    ["tôi muốn bạn chạy .", 0],
    ["tôi muốn . dừng lại", 3],
    ["không muốn thấy . nữa",3],
    ["tôi chán . rồi", 3],
    ["tôi chán .", 3],
    ["tôi thích dùng . ngay bây giờ", 0],
    [". dừng ngay",3],
    [". bật lên",0],
    ["tôi không dùng . nữa", 3],
    ["đóng . lại ngay nhé",3],
    ["tôi muốn . chạy",0],
    ["giúp tôi mở .", 0],
    ["giúp tôi tắt .", 3],
    ["bật . nào", 0],
    ["lướt . nào", 0],
    [". ở đâu rồi mở lên", 0]
]

if __name__ == '__main__':
    # chuong trinh se thay "." trong s thanh ung dung can mo hoac dong

    with open('genData.csv', mode='a', encoding="utf8", newline='\n') as write_file:
        fieldnames = ['sentence', 'label']
        csv_writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for str, label in sentences:
            s = str.split()
            pos = -1
            for i in range(len(s)):
                if s[i] == ".":
                    pos = i
            if pos == -1:
                continue
            for obj in objects:
                lst = s.copy()
                lst[pos] = obj
                lst = ' '.join(lst)
                print(lst)
                csv_writer.writerow({'sentence': lst, 'label': label})
