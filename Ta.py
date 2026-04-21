import streamlit as st
import pandas as pd
from PIL import Image
import io

# --- إعدادات الصفحة ---
st.set_page_config(page_title="الشامل للتحليل الذكي", layout="wide", page_icon="🎯")

# --- واجهة الموقع ---
st.markdown("<h1 style='text-align: center;'>🔍 المنصة الشاملة لتحليل النصوص والصور والملفات</h1>", unsafe_allow_html=True)
st.divider()

# --- القائمة الجانبية للتنقل ---
with st.sidebar:
    st.title("🛠️ لوحة التحكم")
    option = st.radio("اختر نوع التحليل:", ["📄 تحليل الملفات (Data)", "🖼️ تحليل الصور (Images)", "📝 تحليل النصوص (Text)"])
    st.info("قم باختيار القسم ثم ارفع الملف المطلوب.")

# --- 1. قسم تحليل الملفات (CSV/Excel) ---
if option == "📄 تحليل الملفات (Data)":
    st.header("📊 تحليل جداول البيانات")
    file = st.file_uploader("ارفع ملف CSV أو Excel", type=['csv', 'xlsx'])
    
    if file:
        df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
        st.success("تم رفع الملف بنجاح!")
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.write("### ملخص سريع")
            st.write(f"**عدد الأسطر:** {df.shape[0]}")
            st.write(f"**عدد الأعمدة:** {df.shape[1]}")
        with col2:
            st.write("### معاينة البيانات")
            st.dataframe(df.head(10))

# --- 2. قسم تحليل الصور ---
elif option == "🖼️ تحليل الصور (Images)":
    st.header("📷 معالجة وتحليل الصور")
    img_file = st.file_uploader("ارفع صورة (JPG, PNG, JPEG)", type=['jpg', 'png', 'jpeg'])
    
    if img_file:
        image = Image.open(img_file)
        st.image(image, caption="الصورة المرفوعة", use_container_width=True)
        
        # معلومات تقنية عن الصورة
        st.write("### ℹ️ تفاصيل الصورة")
        col1, col2, col3 = st.columns(3)
        col1.write(f"**الصيغة:** {image.format}")
        col2.write(f"**الحجم:** {image.size}")
        col3.write(f"**النمط اللوني:** {image.mode}")
        
        if st.button("تحويل الصورة إلى أبيض وأسود"):
            bw_img = image.convert("L")
            st.image(bw_img, caption="الصورة بعد التحويل")

# --- 3. قسم تحليل النصوص ---
elif option == "📝 تحليل النصوص (Text)":
    st.header("📝 تحليل النصوص والمحتوى")
    user_text = st.text_area("أدخل النص هنا للتحليل:", placeholder="اكتب أو الصق النص هنا...")
    
    if user_text:
        st.subheader("📊 نتائج تحليل النص")
        words = user_text.split()
        
        c1, c2, c3 = st.columns(3)
        c1.metric("عدد الكلمات", len(words))
        c2.metric("عدد الحروف", len(user_text))
        c3.metric("عدد الأسطر", user_text.count('\n') + 1)
        
        if st.button("استخراج الكلمات الفريدة"):
            unique_words = set(words)
            st.write(f"الكلمات الفريدة: {list(unique_words)[:20]}...")

# --- التذييل ---
st.divider()
st.caption("<center>نظام التحليل المتكامل | 2026</center>", unsafe_allow_html=True)
    
