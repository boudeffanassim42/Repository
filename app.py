import streamlit as st
import pandas as pd
import openpyxl

# عنوان التطبيق
st.title("📋 نظام إدارة تنقلات الموظفين")
st.write("قم برفع ملف الإكسل الخاص بالبيانات للبدء:")

# أداة رفع ملفات الإكسل
uploaded_file = st.file_uploader("اختر ملف الإكسل (.xlsx)", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # قراءة ملف الإكسل بشكل آمن تماماً وبدون أخطاء تشفير
        df = pd.read_excel(uploaded_file, engine="openpyxl")
        
        st.success("تم قراءة الملف بنجاح!")
        
        # عرض البيانات كجدول منظم
        st.dataframe(df)
        
    except Exception as e:
        st.error(f"حدث خطأ أثناء قراءة الملف: {e}")
else:
    st.info("الرجاء رفع ملف إكسل لتبدأ البيانات بالظهور هنا.")
