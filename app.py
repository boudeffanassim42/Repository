import streamlit as st
import pandas as pd
import openpyxl

st.title("📋 نظام إدارة تنقلات الموظفين")

# القائمة الجانبية لحماية التطبيق
st.sidebar.header("🔐 حماية التطبيق")
password_input = st.sidebar.text_input("أدخل كلمة المرور:", type="password")

if password_input != "Faresski21":
    st.warning("⚠️ الرجاء إدخال كلمة المرور الصحيحة في القائمة الجانبية للوصول إلى بيانات التطبيق.")
else:
    st.success("تم تأكيد كلمة المرور بنجاح!")
    
    uploaded_file = st.file_uploader("اختر ملف الإكسل (.xlsx)", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            # فحص ورقات العمل المتاحة في الملف
            xls = pd.ExcelFile(uploaded_file, engine="openpyxl")
            sheet_names = xls.sheet_names
            
            st.info(f"📁 ورقات العمل المكتشفة في الملف: {', '.join(sheet_names)}")
            
            # قراءة الورقة الأولى
            df = pd.read_excel(uploaded_file, sheet_name=0, engine="openpyxl")
            
            if df.empty:
                st.warning("⚠️ الملف قُرئ، لكن الجدول يبدو فارغاً. تأكد أن أسماء الأعمدة تبدأ في السطر الأول.")
            else:
                st.success(f"تم قراءة الملف بنجاح! تم تحميل {len(df)} صفاً.")
                # عرض البيانات كجدول منظم
                st.dataframe(df)
                
        except Exception as e:
            st.error(f"حدث خطأ أثناء قراءة الملف: {e}")
    else:
        st.info("الرجاء رفع ملف إكسل لتبدأ البيانات بالظهور هنا.")
