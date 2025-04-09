# CV Generator 網頁履歷產生器 📝

> 使用 Django + pdfkit 所開發的履歷產生工具，支援 CKEditor 富文本、多欄位輸入、即時 PDF 預覽，可一鍵產出專業履歷 PDF，適合用於外商求職申請。

## 🚀 Features
- 多欄位動態編輯（Summary、Skills、Projects、Awards 等）
- CKEditor 富文本支援
- 圖片上傳與排版（支援左、置中）
- 即時產生 PDF 預覽
- 支援本機圖片轉換與字型設定

## 🛠 技術
- Python 3 / Django 5
- CKEditor 4
- pdfkit（wkhtmltopdf）

## 網頁展示
![image](https://github.com/user-attachments/assets/163c0ad2-942d-445f-8d9c-72fb85705f2f)

## 效果展示
![image](https://github.com/user-attachments/assets/bc4d76ae-c8cd-4193-844d-76257e8a34e6)



## 🔧 本機啟動
```bash
pip install -r requirements.txt
python manage.py runserver
