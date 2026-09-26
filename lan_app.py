def main():
    # 1. กำหนดรายการสินค้าและราคาจากใบงาน
    menu = {
        1: {"name": "เซ็ตปกติ", "price": 199},
        2: {"name": "เซ็ตกลาง", "price": 299},
        3: {"name": "เซ็ตใหญ่", "price": 359},
        4: {"name": "เซ็ตกินเอาตาย", "price": 1059}
    }

    print("==========================================")
    print("      ระบบคำนวณราคา ร้าน หลงล่า เยเกอร์      ")
    print("==========================================")
    for key, item in menu.items():
        print(f"[{key}] {item['name']:<15} ราคา {item['price']:,} บาท")
    print("------------------------------------------")

    total_qty = 0
    subtotal = 0
    order_details = []

    # 2. รับค่าจำนวนที่สั่งซื้อในแต่ละรายการ
    for key, item in menu.items():
        while True:
            try:
                qty_input = input(f"ระบุจำนวนที่สั่งซื้อ {item['name']} (กด Enter หากไม่ได้สั่ง): ")
                qty = int(qty_input) if qty_input.strip() != "" else 0
                if qty < 0:
                    print("กรุณาระบุจำนวนเป็นตัวเลขที่ไม่ติดลบ")
                    continue
                break
            except ValueError:
                print("กรุณากรอกตัวเลขที่ถูกต้อง")

        if qty > 0:
            item_total = qty * item["price"]
            total_qty += qty
            subtotal += item_total
            order_details.append(f"- {item['name']} x {qty} = {item_total:,} บาท")

    # 3. ตรวจสอบเงื่อนไขส่วนลด (กินครบ 5 เซ็ตขึ้นไป ลด 15%)
    discount_rate = 0.15 if total_qty >= 5 else 0.0
    discount_amount = subtotal * discount_rate
    net_total = subtotal - discount_amount

    # 4. แสดงผลสรุปรายการและใบเสร็จ
    print("\n==========================================")
    print("               สรุปรายการสั่งซื้อ            ")
    print("==========================================")
    if order_details:
        for line in order_details:
            print(line)
    else:
        print("ไม่มีรายการสั่งซื้อ")

    print("------------------------------------------")
    print(f"จำนวนรวมทั้งหมด    : {total_qty} เซ็ต")
    print(f"ราคารวมก่อนส่วนลด  : {subtotal:,.2f} บาท")

    if total_qty >= 5:
        print(f"ส่วนลดพิเศษ (15%)  : -{discount_amount:,.2f} บาท")
    else:
        print(f"ส่วนลด             : 0.00 บาท (สั่งไม่ครบ 5 เซ็ต)")

    print("------------------------------------------")
    print(f"ยอดเงินสุทธิที่ต้องชำระ : {net_total:,.2f} บาท")
    print("==========================================")

if __name__ == "__main__":
    main()
