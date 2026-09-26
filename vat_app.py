<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%</title>
    <style>
        body { font-family: sans-serif; padding: 20px; }
        .container { max-width: 400px; margin: auto; border: 1px solid #ccc; padding: 20px; border-radius: 5px; }
        .result { margin-top: 15px; font-weight: bold; }
    </style>
</head>
<body>

<div class="container">
    <h3>แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%</h3>
    
    <label for="price">กรอกราคาสินค้า (บาท):</label><br>
    <input type="number" id="price" value="0" oninput="calculateVat()" style="width: 100%; padding: 5px; margin-top: 5px;"><br>

    <div class="result">
        <p>• ภาษีมูลค่าเพิ่ม (VAT 7%): <span id="vatResult">0.00</span> บาท</p>
        <p>• ราคาสุทธิ: <span id="netResult">0.00</span> บาท</p>
    </div>
</div>

<script>
function calculateVat() {
    // 1. ดึงค่าราคาสินค้าจากช่อง input
    let price = parseFloat(document.getElementById('price').value) || 0;
    
    // 2. คำนวณ VAT และ ราคาสุทธิ
    let vat = price * 0.07;
    let netPrice = price + vat;
    
    // 3. แสดงผลลัพธ์โดยทศนิยม 2 ตำแหน่ง
    document.getElementById('vatResult').innerText = vat.toFixed(2);
    document.getElementById('netResult').innerText = netPrice.toFixed(2);
}
</script>

</body>
</html>
