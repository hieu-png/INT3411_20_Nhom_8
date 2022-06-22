# Sản phẩm
Bài tập lớn nhóm 8 môn học xử lý tiếng nói

Ứng dụng trợ lý ảo với các chức năng hỗ trợ người dùng bằng giọng nói sử dụng Tkinter và OpenCV

# Cách cài đặt
1. Cài đặt các thư viện:

    _pip install -r requirements.txt_ 


    Vào https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio. Chọn và tải phiên bản đúng với phiên bản python đang chạy (python --version) và chạy 
    
    _pip install [đường dẫn đến file]_

    Ví dụ python 3.10

    _pip install lib/PyAudio-0.2.11-cp310-cp310-win_amd64.whl__

    
2. Chạy ứng dụng

    _python GUIASSISTANT.py_
# Phương pháp

- Sử dụng các hàm của thư viện speech_recognition

- Đối tượng recognizer của thư viện sẽ được khởi tạo. Nó được dùng để chương trình có thể nhận biết được khi nào thì giọng nói của người dùng sẽ được đưa vào xử lý qua thông số năng lượng của âm thanh. Âm thanh được đưa liên tục cho recognizer qua đối tượng Microphone của trương trình

Recognizer chia luồng âm thanh thành nhiều frame và cho vào một buffer để xử lý từng frame một. Bẳng việc sử dụng hàm rms của module audioop của Python năng lượng của từng frame sẽ được lấy. 
Khi mức năng lượng đó quá một ngưỡng nào đó thì cả luồng âm thanh sẽ được nhận. Ở đây nhóm đã đế khi năng lượng của âm thanh quá 4000 thì chương trình nhận giọng nói.

Sau thu âm giọng nói xong file âm thanh được gửi cho api của google để xử lý và nhóm sẽ lấy kết quả nhận được đó để tạo ra các chức năng của phần mềm. Sample rate của sẽ được đảm bảo hơn 8 kHz và kích thước hơn 16kb bởi chương trình trước khi gửi.

- Mô hình mà google đã sử dụng là: 

![github_preview/Show.png](github_preview/Show.PNG)

Với P(A|W) là mô hình âm thanh theo Hidden Markov Model

P(W) là mô hình ngôn ngữ theo Markov Chain

Mô hình đầu ra sẽ sử dụng thêm mô hình âm học GMM hay Gaussian mixture model

![github_preview/GMM.png](github_preview/GMM.PNG)


- Các thuật toán mà google dùng để nhận dạng giọng nói là:

PLP features

![github_preview/PLP.png](github_preview/PLP.png)

Viterbi search

![github_preview/Viterbi.png](github_preview/Viterbi.png)



Deep Neural Networks

discriminative training

WFST (weighted finite-state transducers) framework

![github_preview/WFST.png](github_preview/WFST.png)

- Tập dữ liệu training của model mà google đã sử dụng bao gồm lời nói với phiên âm kéo dài tới tận 87.000 giờ được lấy từ log của tính năng Voice Search. Tập dữ liệu có frame-rate là 100hz.

Nguồn: https://storage.googleapis.com/pub-tools-public-publication-data/pdf/41133.pdf

# Các chức năng:

- Trò chuyện cơ bản

![github_preview/img_3.png](github_preview/img_3.png)

![github_preview/img_2.png](github_preview/img_2.png)

![github_preview/img_1.png](github_preview/img_1.png)


- Tìm kiếm bằng webScraping

![github_preview/img_4.png](github_preview/img_4.png)

![github_preview/img_9.png](github_preview/img_9.png)

- Chỉ đường bằng google map

![img.png](github_preview/img10.png)

![img_1.png](github_preview/img_11.png)


- Tìm kiếm trên youtube

![img_3.png](github_preview/img_13.png)

![img_2.png](github_preview/img_12.png)

- Xem thời tiết

![github_preview/img_5.png](github_preview/img_5.png)

- Máy tính 

![github_preview/img_6.png](github_preview/img_6.png)

![github_preview/img_7.png](github_preview/img_7.png)

- Truyện cười

![github_preview/img_8.png](github_preview/img_8.png)

Bản đồ https://youtu.be/XOoF3z5vrkI

Chỉ đường trên bản đồ https://youtu.be/WDBXBkExfKo

Tìm kiếm google đơn giản https://youtu.be/ZlmLjy8hNfY



# Thành viên
Nguyễn Trung Hiếu 19021271

Mai Công Danh 19021233

Nguyễn Thế Hoàng 19021283

Lê Bá Gia Huy 19021305

# Phân chia công việc
3 backend - 1 frontend

Frontend: Nguyễn Thế Hoàng

Backend: 

- Nguyễn Trung Hiếu

- Lê Bá Gia Huy

- Mai Công Danh
