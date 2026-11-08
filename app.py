import streamlit as st
import pandas as pd

# ÅÚÏÇÏÇÊ ÕİÍÉ ÇáÊØÈíŞ (áßí ÊÙåÑ ÈÔßá ÇÍÊÑÇİí Úáì ÇáåÇÊİ æÇáßãÈíæÊÑ)
st.set_page_config(
    page_title="äÙÇã ÍÑßÉ ÇáãæÙİíä",
    page_icon="??",
    layout="centered"
)

# ÚäæÇä ÇáÊØÈíŞ ÇáÑÆíÓí
st.title("?? ÇáäÙÇã ÇáÂáí áÅÏÇÑÉ ÍÑßÉ ÇáãæÙİíä")
st.markdown("---")
st.write("ãÑÍÈÇğ Èß! åĞå æÇÌåÉ ÇáÊÍßã ÇáãÑßÒíÉ áÊÔÛíá ÍÑßÉ ÇáãæÙİíä¡ ÇÓÊÎÑÇÌ ÇáÅÍÕÇÆíÇÊ¡ æÊÕÏíÑ ÇáÊŞÇÑíÑ ÈÓåæáÉ ÊÇãÉ ãä ÇáåÇÊİ Ãæ ÇáßãÈíæÊÑ.")

# ŞÓã ÇáÃÒÑÇÑ æÇáÊÍßã ÇáÑÆíÓí
st.subheader("?? áæÍÉ ÇáÊÍßã ÇáÊÔÛíáíÉ")

col1, col2 = st.columns(2)

with col1:
    if st.button("?? ÊÔÛíá ÇáÍÑßÉ æÇáÊŞÇÑíÑ", use_container_width=True):
        with st.spinner("ÌÇÑí ãÚÇáÌÉ ÇáÈíÇäÇÊ æÊæÒíÚ ÇáÍÑßÇÊ... ÈÑÌÇÁ ÇáÇäÊÙÇÑ"):
            # ãÍÇßÇÉ ÚãáíÉ ãÚÇáÌÉ ÇáäÙÇã (íãßääÇ áÇÍŞÇğ ÑÈØåÇ ÈÏæÇá ÇáÈÇííËæä ÇáÍŞíŞíÉ)
            # time.sleep(2) 
            st.success("Êã ÊÔÛíá ÇáäÙÇã æÊæáíÏ ÇáÊŞÇÑíÑ ÈäÌÇÍ!")
            st.balloons()

with col2:
    if st.button("?? ÚÑÖ ÇáÅÍÕÇÆíÇÊ", use_container_width=True):
        st.info("ÓíÊã ÚÑÖ ÌÏÇæá ÇáÅÍÕÇÆíÇÊ åäÇ.")

st.markdown("---")

# ŞÓã ÚÑÖ ÇáÈíÇäÇÊ (ßãËÇá ÊæÖíÍí ááÌÏÇæá ÇáÊİÇÚáíÉ)
st.subheader("?? ãáÎÕ ÍÇáÉ ÇáÊæÒíÚ ÇáÍÇáíÉ")

# ÈíÇäÇÊ ÊÌÑíÈíÉ (íãßä ÇÓÊÈÏÇáåÇ Èãáİ ÅßÓá ÇáÎÇÕ Èß áÇÍŞÇğ)
data = {
    "ÇáãÄÓÓÉ / ÇáãÑßÒ": ["ãÄÓÓÉ ŞäØÇÓ", "ãÄÓÓÉ ÇÈä ÌÈíÑ", "ãÄÓÓÉ ÈæÍÌÉ", "ãÄÓÓÉ ÈæÑÎæã"],
    "ÇáÔÇÛÑ ÇáÓÇÈŞ": [12, 8, 15, 6],
    "ÇáãÚíøäæä ÇáÌÏÏ": [4, 3, 5, 2],
    "ÇáÍÇáÉ": ["ãßÊãá", "ŞíÏ ÇáãÚÇáÌÉ", "ãßÊãá", "ãßÊãá"]
}

df = pd.DataFrame(data)

# ÚÑÖ ÇáÌÏæá ÈÔßá ÊİÇÚáí íÏÚã ÇáÊãÑíÑ Úáì ÇáåÇÊİ
st.dataframe(df, use_container_width=True)

# ÒÑ ÊÍãíá ÇáÊŞÇÑíÑ
st.markdown("### ?? ÊÍãíá ÇáÊŞÇÑíÑ ÇáäåÇÆíÉ")
st.download_button(
    label="ÊÍãíá ÊŞÑíÑ ÇáãÄÓÓÇÊ (Excel)",
    data="dummy_data", # ÓíÊã ÑÈØå Èãáİ ÇáÊŞÇÑíÑ ÇáÍŞíŞí áÇÍŞÇğ
    file_name="ÇáÊŞÇÑíÑ_ÇáäåÇÆíÉ_ááÍÑßÉ.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetspreadsheetml.sheet",
    use_container_width=True
)