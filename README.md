# CV Generator 網頁履歷產生器 📝

> 使用 Django + pdfkit 所開發的履歷產生工具，支援 CKEditor 富文本、多欄位輸入、即時 PDF 預覽，可一鍵產出專業履歷 PDF，適合用於外商求職申請。

## 🚀 Features
- 多欄位動態編輯（Summary、Skills、Projects、Awards 等）
- CKEditor 富文本支援
- 圖片上傳與排版（支援左、右、置中）
- 即時產生 PDF 預覽
- 支援本機圖片轉換與字型設定

## 🛠 技術棧
- Python 3 / Django 5
- CKEditor 4
- pdfkit（wkhtmltopdf）

## 📸 截圖展示
![editor screenshot](screenshots/editor.png)
![pdf preview](screenshots/preview.png)


## 🔧 本機啟動
```bash
pip install -r requirements.txt
python manage.py runserver
