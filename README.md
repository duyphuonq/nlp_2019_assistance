# nlp_2019_assistance
<hr>

## Hướng dẫn cài đặt
Nếu là linux:  
```
chmod +x init_linux.sh
./init_linux.sh
```  
  
Sau đó:
```
pip3 install requirements.txt
```  

## Yêu cầu: python3.6

# Xong, bên dưới là giới thiệu

## Các thư viện cần cài đặt:
<h3>Numpy, Pandas, Matplotlib, Sklearn, Speech Recognition, Py Audio</h3>

## Cài đặt 
Sử dụng [pip](https://pip.pypa.io/en/stable/) để cài đặt.

```bash
pip install numpy pandas matplotlib sklearn SpeechRecognition 
```
hoặc pip3 nếu có cả 2 phiên bản python trong máy tính.

Riêng với pyaudio

<b>Windows</b>
```bash
pip install pyaudio
```
<b>Linux</b>
```bash
sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && sudo pip install pyaudio
```
Nếu không cài được pyaudio thì làm theo hướng dẫn trên google để cài đặt
## Test
Tại thư mục gốc project
```bash
python3 src/main.py
```
## Cập nhật thứ 5 ngày 7/11/2019:
tại branch test: 

-thêm chức năng text to speech

-môi trường Linux, chưa cập nhật cho windows

-mudule cài thêm: 

  + gtts ```bash pip3 install gTTS```
  + mpeg ```sudo apt install mpeg``` : Dùng để mở file mp3 
  
