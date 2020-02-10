# Bài tập lớn môn Xử Lý Ngôn Ngữ Tự Nhiên 
# Chủ đề: Virtual Assistant
<hr>

## Hướng dẫn cài đặt
Nếu là linux:  
```
chmod +x init_linux.sh
./init_linux.sh
```  
Sau đó:
```
pip3 install -r requirements.txt
```  

## Yêu cầu: python3.6
## Test
Tại thư mục gốc project
```bash
python3 src/main.py
```
## Cập nhật thứ 5 ngày 7/11/2019:
tại branch test: 

- Thêm chức năng text to speech (Giọng nói chị G

- Môi trường Linux, chưa cập nhật cho windows

- Module pip cài thêm: 

  + gtts ```bash pip3 install gTTS```
- Hệ thống cài thêm:
  + mpeg ```sudo apt install mpeg``` : Dùng để mở file mp3 
  
## Cập nhật chủ nhật ngày 10/11/2019:

tại branch master:
- Mọi chức năng gần như đã hoàn thành và tích hợp 
- Thêm âm thanh báo hiệu lúc bắt đầu ghi âm và kết thúc ghi âm
- Thêm hoạt ảnh con bò ngộ nghĩnh
- module cài thêm:
  + xcowsay ```sudo apt install xcowsay```
- Lưu ý mới chỉ hoạt động trên Linux, chưa bổ sung cho windows 
  
