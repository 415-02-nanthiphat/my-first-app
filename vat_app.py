<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%</title>
    <style>
        body { 
            font-family: sans-serif; 
            padding: 20px; 
            background-color: #f9f9f9;
        }
        .container { 
            max-width: 400px; 
            margin: auto; 
            border: 1px solid #ccc; 
            padding: 20px; 
            border-radius: 5px; 
            background-color: #fff;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .result { 
            margin-top: 15px; 
            font-weight: bold; 
        }
        input[type="number"] {
            width: 100%; 
            padding: 8px; 
            margin-top: 5px; 
            margin-bottom: 10px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h3>แอปพลิเคชันคำนวณราคาสินค้ารวม VAT 7%</h3>
        
        <label for="price">กรอกราคาสินค้า (บาท):</label><br>
        <input type="number" id="price" value="0" min="0" step="any" oninput="calculateVat()"><br>
        
        <div class="result">
            <p>ภาษีมูลค่าเพิ่ม (VAT 7%): <span id="vatResult">0.00</span> บาท</p>
            <p>ราคาสุทธิ: <span id="netResult">0.00</span> บาท</p>
        </div>
    </div>

    <script>
        function calculateVat() {
            // ดึงค่าราคาสินค้าจากช่อง input
            let price = parseFloat(document.getElementById("price").value);
            
            // ตรวจสอบว่ามีค่าและเป็นตัวเลขหรือไม่ ถ้าไม่มีให้เท่ากับ 0
            if (isNaN(price) || price < 0) {
                price = 0;
            }
            
            // คำนวณ VAT 7% และราคารวมสุทธิ
            let vat = price * 0.07;
            let netTotal = price + vat;
            
            // แสดงผลลัพธ์โดยปัดเศษทศนิยม 2 ตำแหน่ง
            document.getElementById("vatResult").innerText = vat.toFixed(2);
            document.getElementById("netResult").innerText = netTotal.toFixed(2);
        }
    </script>

</body>
</html>
