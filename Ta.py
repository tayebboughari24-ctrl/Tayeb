import streamlit as st
import pandas as pd
import plotly.express as px
import time

# --- إعدادات الصفحة الاحترافية ---
st.set_page_config(
    page_title="Pro Analyzer | B.TAYEB",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- تنسيق مخصص باستخدام CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border_radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    </style>
    """, unsafe_allow_html=True)

# --- وظيفة معالجة البيانات (Caching لتحسين السرعة) ---
@st.cache_data
def load_data(file):
    time.sleep(1) # محاكاة معالجة بسيطة
    df = pd.read_csv(file)
    return df

# --- القائمة الجانبية (Sidebar) ---
with st.sidebar:
    st.title("🛠️ لوحة التحكم")
    uploaded_file = st.file_uploader("ارفع ملف البيانات (CSV)", type=["csv"])
    st.divider()
    st.info("هذا التطبيق مطور لتقديم تحليلات ذكية وسريعة.")

# --- الواجهة الرئيسية ---
st.title("📊 المحلل الذكي - Pro Analyzer")
st.caption("أداة احترافية لتحويل البيانات الخام إلى رؤى بصرية")

if uploaded_file is not None:
    # تحميل البيانات
    with st.spinner('جاري تحليل البيانات بدقة...'):
        df = load_data(uploaded_file)
    
    # صف المؤشرات العلوية (KPIs)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("إجمالي السجلات", len(df))
    with col2:
        st.metric("عدد الأعمدة", len(df.columns))
    with col3:
        st.metric("القيم المفقودة", df.isnull().sum().sum())
    with col4:
        st.metric("نوع الملف", "CSV")

    st.divider()

    # تبويبات لتنظيم المحتوى
    tab1, tab2, tab3 = st.tabs(["📑 استعراض البيانات", "📈 التحليل البصري", "🤖 إحصائيات متقدمة"])

    with tab1:
        st.subheader("معاينة البيانات المرفوعة")
        st.dataframe(df.head(10), use_container_width=True)
        
        # زر لتحميل البيانات المنظفة
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("تحميل البيانات كـ CSV", data=csv, file_name='cleaned_data.csv', mime='text/csv')

    with tab2:
        st.subheader("الرسوم البيانية التفاعلية")
        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
        
        if numeric_cols:
            col_x = st.selectbox("اختر محور (X)", df.columns)
            col_y = st.selectbox("اختر محور (Y)", numeric_cols)
            
            chart_type = st.radio("نوع الرسم البياني", ["خطوط", "أعمدة", "نقاط بعثرة"], horizontal=True)
            
            if chart_type == "خطوط":
                fig = px.line(df, x=col_x, y=col_y, template="plotly_white", color_discrete_sequence=['#007BFF'])
            elif chart_type == "أعمدة":
                fig = px.bar(df, x=col_x, y=col_y, template="plotly_white")
            else:
                fig = px.scatter(df, x=col_x, y=col_y, template="plotly_white")
            
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("لا توجد أعمدة رقمية كافية لإنشاء رسوم بيانية.")

    with tab3:
        st.subheader("تحليل إحصائي سريع")
        st.write(df.describe())

else:
    # واجهة ترحيبية عند عدم وجود ملف
    st.image("https://img.freepik.com/free-vector/data-extraction-concept-illustration_114360-4766.jpg", width=400)
    st.write("👈 يرجى رفع ملف من القائمة الجانبية للبدء.")

# --- التذييل (Footer) ---
st.divider()
st.markdown("<center>صنع بكل إتقان بواسطة B.TAYEB | 2026</center>", unsafe_allow_html=True)
