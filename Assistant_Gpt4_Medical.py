
# Mẫu trợ lý AI cá nhân hóa sử dụng API GPT-4
# Ứng dụng: trợ lý khoa học y học – hỏi đáp học thuật và phân tích bài báo PDF

try:
    import openai
except ModuleNotFoundError:
    raise ModuleNotFoundError("Chưa cài đặt thư viện 'openai'. Vui lòng chạy: pip install openai")

try:
    import streamlit as st
except ModuleNotFoundError:
    raise ModuleNotFoundError("Chưa cài đặt thư viện 'streamlit'. Vui lòng chạy: pip install streamlit")

try:
    import PyPDF2
except ModuleNotFoundError:
    raise ModuleNotFoundError("Chưa cài đặt thư viện 'PyPDF2'. Vui lòng chạy: pip install PyPDF2")

import tempfile

# ===== Cấu hình =====
openai.api_key = st.secrets["OPENAI_API_KEY"]  # Đặt API key trong file .streamlit/secrets.toml

# ===== Giao diện =====
st.set_page_config(page_title="Trợ lý AI Y học", layout="wide")
st.title("🧠 Trợ lý AI hỗ trợ Nghiên cứu Y học")

# ===== Vai trò hệ thống =====
def system_prompt():
    return (
        "Bạn là một trợ lý AI chuyên ngành Giải phẫu học và Chẩn đoán hình ảnh."
        " Trả lời chính xác, ngắn gọn, có dẫn nguồn học thuật nếu có."
    )

# ===== Tùy chọn: Nhập tay hoặc Tải file PDF =====
tab1, tab2 = st.tabs(["📄 Nhập câu hỏi", "📘 Phân tích bài báo PDF"])

# === Tab 1: Nhập câu hỏi ===
with tab1:
    user_input = st.text_area("Nhập câu hỏi nghiên cứu hoặc nội dung cần tư vấn:", height=150)
    if st.button("Phân tích với GPT-4") and user_input:
        with st.spinner("Đang truy vấn GPT-4..."):
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": system_prompt()},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.4,
                    max_tokens=1500
                )
                output = response["choices"][0]["message"]["content"]
                st.success("Phân tích hoàn tất")
                st.markdown("### 🧾 Kết quả phân tích")
                st.markdown(output)
            except Exception as e:
                st.error(f"Lỗi truy vấn: {e}")

# === Tab 2: Phân tích bài báo PDF ===
with tab2:
    uploaded_file = st.file_uploader("Tải lên bài báo y học (PDF)", type=["pdf"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_file_path = tmp_file.name

        with open(tmp_file_path, "rb") as f:
            pdf_reader = PyPDF2.PdfReader(f)
            full_text = ""
            for page in pdf_reader.pages:
                if page.extract_text():
                    full_text += page.extract_text() + "\n"

        st.markdown("### 📖 Nội dung bài báo (rút gọn)")
        st.text(full_text[:2000] if full_text else "Không trích xuất được nội dung từ PDF.")

        if full_text and st.button("Tóm tắt và phân tích bài báo"):
            with st.spinner("Đang phân tích với GPT-4..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": system_prompt()},
                            {"role": "user", "content": f"Hãy tóm tắt và phân tích bài báo y học sau:\n{full_text}"}
                        ],
                        temperature=0.3,
                        max_tokens=1800
                    )
                    output = response["choices"][0]["message"]["content"]
                    st.success("Tóm tắt hoàn tất")
                    st.markdown("### 📑 Phân tích bài báo")
                    st.markdown(output)
                except Exception as e:
                    st.error(f"Lỗi khi xử lý bài báo: {e}")

# ===== Gợi ý câu hỏi mẫu =====
st.sidebar.markdown("### 📌 Gợi ý câu hỏi")
st.sidebar.write("- So sánh giải phẫu động mạch não giữa các lát cắt MRI axial và coronal")
st.sidebar.write("- Đặc điểm hình ảnh tổn thương thùy trán trên CT")
st.sidebar.write("- Các dấu hiệu MRI gợi ý u màng não")
