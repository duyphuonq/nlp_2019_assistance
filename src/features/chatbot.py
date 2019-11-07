# -*- coding: utf-8 -*
from googletrans import Translator
import requests


def api_google(langfrom, langto, text):
    translator = Translator()
    return translator.translate(text, src=langfrom, dest=langto).text


def api_chatbot(question):
    response = requests.post('https://pandorabots.com/pandora/talk?botid=cd44746d1e3755a1', data=[('input', question)])
    return response.text


def chat(vi_question):
    eng_question = api_google('vi', 'en', vi_question)
    eng_answer = api_chatbot(eng_question).splitlines()[10][19:-7]
    vi_answer = api_google('en', 'vi', eng_answer)
    print(vi_answer)
    return vi_answer


# question = "tôi đang rất buồn"
# print(chat(question))
