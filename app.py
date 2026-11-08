import streamlit as st
import pandas as pd
import openpyxl

# إعداد صفحة التطبيق
st.title("📋 نظام إدارة تنقلات الموظفين")

# طلب كلمة المرور في الباب (Sidebar أو في الواجهة الرئيسية)
st.sidebar.header("🔐 حماية التطبيق")
password_input = st.sidebar.text_input("أدخل كلمة المرور:", type="password")

# التحقق من كلمة المرور
if password_input != "Faresski21":
    st.warning("⚠️ الرجاء إدخال كلمة المرور الصحيحة في القائمة الجانبية (أو أعلى الصفحة) للوصول إلى بيانات التطبيق.")
    st.info("كلمة المرور الخاصة بك هي: Faresski21")
else:
    # إذا كانت كلمة المرور صحيحة، يفتح النظام بالكامل
    st.success("تم تأكيد كلمة المرور بنجاح! يمكنك الآن إدارة الملفات.")
    
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
