import streamlit as st

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="หลงล่า เยเกอร์", page_icon="🍲", layout="centered")

# ส่วนหัวของแอปพลิเคชัน
st.title("🍲 ร้าน หลงล่า เยเกอร์")
st.subheader("ระบบคำนวณราคาและส่วนลดประจำร้าน")
st.write("---")

# 1. กำหนดรายการสินค้าและราคาจากใบงาน
menu = {
    "เซ็ตปกติ": 199,
    "เซ็ตกลาง": 299,
    "เซ็ตใหญ่": 359,
    "เซ็ตกินเอาตาย": 1059
}

st.header("🛒 เลือกรายการอาหาร")

# 2. สร้างช่องให้ผู้ใช้ปรับเลือกจำนวนสินค้า
order = {}
total_qty = 0

col1, col2 = st.columns(2)

for i, (item_name, price) in enumerate(menu.items()):
    # สลับแสดงรายการ 2 คอลัมน์ให้ดูสวยงาม
    with col1 if i % 2 == 0 else col2:
        qty = st.number_input(
            label=f"{item_name} ({price:,} บาท)",
            min_value=0,
            value=0,
            step=1,
            key=item_name
        )
        order[item_name] = qty
        total_qty += qty

st.write("---")

# 3. คำนวณราคาและส่วนลด
subtotal = sum(menu[item] * qty for item, qty in order.items())

# เงื่อนไขส่วนลด: กินครบ 5 เซ็ตขึ้นไป ลด 15%
if total_qty >= 5:
    discount_rate = 0.15
    discount_amount = subtotal * discount_rate
else:
    discount_rate = 0.0
    discount_amount = 0.0

net_total = subtotal - discount_amount

# 4. แสดงผลสรุปรายการและคำนวณราคา
st.header("🧾 สรุปรายการสั่งซื้อ")

if total_qty > 0:
    for item_name, qty in order.items():
        if qty > 0:
            item_total = menu[item_name] * qty
            st.write(f"- **{item_name}** x {qty} = {item_total:,} บาท")
    
    st.markdown("---")
    
    # แสดงตัวเลขสรุปด้วย Metric
    c1, c2, c3 = st.columns(3)
    c1.metric("จำนวนรวม", f"{total_qty} เซ็ต")
    c2.metric("ราคารวม", f"{subtotal:,.2f} ฿")
    c3.metric("ส่วนลด (15%)", f"-{discount_amount:,.2f} ฿" if discount_rate > 0 else "0.00 ฿")

    if total_qty >= 5:
        st.success("🎉 คุณได้รับส่วนลดพิเศษ 15% เนื่องจากสั่งซื้อครบ 5 เซ็ตขึ้นไป!")
    else:
        st.info(f"💡 สั่งเพิ่มอีก {5 - total_qty} เซ็ต เพื่อรับส่วนลดพิเศษ 15%")

    st.markdown(f"### **ยอดเงินสุทธิที่ต้องชำระ: :red[{net_total:,.2f}] บาท**")

else:
    st.info("กรุณาเลือกจำนวนเซ็ตอาหารด้านบนเพื่อคำนวณราคา")
