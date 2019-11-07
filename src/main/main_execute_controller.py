# -*- coding: utf-8 -*
from trainer import trained_model, read_data
from src.utils.data_utils import data_in_file
from src.utils.get_app_name import open_app, close_app
from src.constants import ROOT_DIR, path_new_data, CHAT_ACTION, CLOSE_ACTION, OPEN_ACTION, SEARCH_ACTION, NORMAL_APP, WEB_APP
from src.features import chatbot, execute_programs, google, url

my_model = trained_model()


def execute(sentence):
    file_path = data_in_file(sentence)
    data_to_find = read_data(ROOT_DIR + path_new_data + file_path, label_fn=None)
    pred = my_model.predict(data_to_find)
    print(pred)
    result = pred[0]
    if result == CHAT_ACTION:
        print("chat action")
        return chatbot.chat(sentence)
    elif result == SEARCH_ACTION:
        print("search action")
        google.google(sentence)
        return "Tôi đã tìm kiếm kết quả này cho bạn nè!"
    elif result == OPEN_ACTION:
        print("open app action")
        app_type, name = open_app(sentence)
        if app_type == NORMAL_APP:
            execute_programs.open_program(name)
        else:
            print("address")
            url.open_address(name)
        return "Tôi đã mở {} cho bạn nè!".format(name)
    elif result == CLOSE_ACTION:
        print("close app action")
        name = close_app(sentence)
        execute_programs.close_program(name)
        return "Tôi đã đóng {} cho bạn nè!".format(name)
    return ""


# print(execute("tôi muốn dùng facebook"))
# print(execute("terminat đâu rồi"))
# print(execute("tôi không muốn dùng termina"))
# print(execute("chrome ơi mở ra"))
# print(execute("tôi không muốn thấy firefox nữa"))
# print(execute("hôm nay trời đẹp nhỉ"))
# print(execute("giá cặp sách"))
