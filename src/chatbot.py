def api_google(langfrom, langto, text):
    from googletrans import Translator
    translator = Translator()
    return translator.translate(text, src=langfrom, dest=langto).text

def api_chatbot(question):
    import requests
    response = requests.post('https://pandorabots.com/pandora/talk?botid=cd44746d1e3755a1', data=[('input', question), ('botcust2', 'eca814928ea9d039')])
    return response.text

def chat(vi_question):
    eng_question = api_google('vi', 'en', vi_question)
    eng_answer = api_chatbot(eng_question).splitlines()[10][19:-7]
    vi_answer = api_google('en', 'vi', eng_answer)
    return vi_answer

question = input()
print(chat(question))
