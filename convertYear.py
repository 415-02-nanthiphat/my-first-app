import streamlit as st

st.title("แอปพลิเคชันแปลง พ.ศ. เป็น ค.ศ.")

# ใช้ st.number_input แทน text_input และกำหนดชื่อตัวแปรให้ตรงกัน
bh_year = st.number_input("กรอกปี พ.ศ.", value=2569, step=1)

# คำนวณปี ค.ศ. โดยนำ bh_year มาลบด้วย 543
ce_year = bh_year - 543

# แสดงผลลัพธ์โดยใช้ f-string และใส่ปีกกาให้ถูกต้อง
st.header(f"ปี ค.ศ. คือ : {ce_year}")
