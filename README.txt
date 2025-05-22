
# Trợ lý AI Y học sử dụng GPT-4

## 📦 Nội dung gói
- Assistant_Gpt4_Medical.py — mã nguồn Streamlit
- .streamlit/secrets.toml — cấu hình API Key
- README.txt — hướng dẫn cài đặt và chạy

## 🧰 Yêu cầu môi trường
- Python 3.8+ đã được cài
- Các thư viện:
    pip install streamlit openai PyPDF2

## 🚀 Cách chạy ứng dụng

1. Tạo thư mục, ví dụ:
    C:\Users\User\Documents\Assistant_Gpt4_Medical\

2. Giải nén gói ZIP vào đó

3. Chạy dòng lệnh:
    cd C:\Users\User\Documents\Assistant_Gpt4_Medical
    streamlit run Assistant_Gpt4_Medical.py

4. Truy cập trình duyệt tại địa chỉ:
    http://localhost:8501

## 🔐 Cấu hình API Key

1. Mở file `.streamlit/secrets.toml`
2. Dán API key OpenAI vào dòng:
    OPENAI_API_KEY = "sk-..."

Chúc bạn thành công!
