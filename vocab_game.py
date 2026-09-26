import time
import streamlit as st

st.title("🏆 เกมเติมคำศัพท์รับรางวัล")

# #1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

# ตัวแปรควบคุมเวลาหรือสถานะเริ่มใหม่
def reset_game():
    st.session_state.ans1_val = ""  # เคลียร์ค่าคำตอบข้อ 1
    st.session_state.ans2_val = ""  # เคลียร์ค่าคำตอบข้อ 2
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog

# #---------------------------------------
# #2. ฟังก์ชัน MessageBox (Dialog)
@st.dialog("สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2):
    st.balloons()
    score = 0
    
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    
    # ตรวจข้อ 1
    if u_ans1 == "apple":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ผิด! คำตอบคือ '{u_ans1}'")
        
    # ตรวจข้อ 2
    if u_ans2 == "fish":  # แก้ไข Syntax จากภาพเดิม
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ผิด! คำตอบคือ '{u_ans2}'")
        
    st.info(f"🏅 คะแนนรวมของคุณ: {score} คะแนน")
    
    if score == 2:
        st.success("🎉 You win!")
    else:
        st.error("😢 You lose!")

# #---------------------------------------
# #1. ปุ่มเริ่มเล่นเกม
st.button("🔄 เริ่มเล่นใหม่", on_click=reset_game)

# #2. แถบแสดงเวลาและการนับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(30 - (time.time() - st.session_state.start))
    
    if time_left <= 0:
        st.error("⏰ หมดเวลาแล้ว!")
        st.session_state.is_ended = True
        st.rerun()
    else:
        st.info(f"⏳ เหลือเวลาอีก: {time_left} วินาที")
        st.rerun()

st.divider()

# #3. ช่องรับคำตอบ (ไม่พร้อมกัน ไม่ส่งผลกับข้อความเดาเพื่อส่งต่อโค้ด)
ans1 = st.text_input(
    "ข้อ 1: An a_ _ _e a day keeps the doctor away. 🍎",
    value=st.session_state.ans1_val
)

ans2 = st.text_input(
    "ข้อ 2: Cats love to eat f_ _h. 🐟",
    value=st.session_state.ans2_val
)  # แก้ไขเครื่องหมายปีกกาเป็นวงเล็บปิด

# อัปเดตค่าล่าสุดเข้าสู่ระบบค้างไว้
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2

# #4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📤 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

time.sleep(1)
st.rerun()

# #5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(st.session_state.ans1_val, st.session_state.ans2_val)

st.divider()
st.write("นันทิพัฒน์ ไพเชฐศักดิ์ เลขที่2 ม4/15")
