# 🔤 Name Analyzer: Interactive String Processor

Foydalanuvchi tomonidan kiritilgan ismni tahlil qiluvchi interaktiv Python dasturi. Ushbu loyiha matnli ma'lumotlar (Strings), shart operatorlari (If-Else) va Python-ning kuchli kesish (`slicing`) mexanizmini amalda ko'rsatib beradi.

---

## 📸 Loyiha ko'rinishi (Visual Terminal Mockup)

> **Dastur terminalda ishga tushganda foydalanuvchi bilan quyidagicha interaktiv muloqot qiladi:**

======================================================
NAME ANALYZER // POWERED BY orgkamolbek
Ismingizni kiriting: kamolbek

Salom, Kamolbek! Men sizning ismingizni tahlil qilaman:

Ismingizda 8 ta harf bor.

Ismingiz undosh harf bilan boshlanadi.

Ismingizning teskarisi: keblomaK

--- Tahlil tugadi, Kamolbek! ---


### ⚙️ Dastur algoritmi va mantiqi (Data Flow Architecture)

Kodingiz orqa fonda ma'lumotlarni qanday qayta ishlashi sxemasi:

[ Foydalanuvchi kiritmasi ]  (masalan: "  kamolbek ")
             │
             ▼
   [ .strip().capitalize() ] ──► Bo'shliqlarni o'chiradi va bosh harf qiladi ("Kamolbek")
             │
             ▼
   ┌─────────┴─────────┐
   ▼                   ▼                   ▼
[ len() ]         [ name[0] ]         [ name[::-1] ]
│                   │                   │
Harflar sonini      Bosh harf unli      Matnni teskari
aniqlaydi         yoki undoshligini     tartibda o'giradi
(Length: 8)         tekshiradi          (keblomaK)


---

## ⚡ Asosiy xususiyatlari (Features)

* 🧹 **Data Cleaning:** `strip()` va `capitalize()` metodlari orqali foydalanuvchi xato yoki bo'sh joylar bilan ism kiritsa ham uni tozalab, standart formatga keltirishi.
* 🔍 **Vowel/Consonant Detector:** Ismning birinchi harfini unli harflar bazasi (`vowels`) bilan solishtirib, turini aniqlashi.
* 🔄 **String Reversing:** Python-ning o'ziga xos `[::-1]` (slicing) sintaksisidan foydalanib, matnni teskari tartibga o'girishi.

---

## 🛠️ Texnologiyalar (Tech Stack)

* **Python 3.x** — O'rnatilgan standart funksiyalar (`len()`, `string methods`).

---

## 🚀 Ishga tushirish (How to Run)

Hech qanday tashqi kutubxonalar yoki `pip` paketlari talab qilinmaydi:

1. Repozitoriyni klonlang:
   ```bash
   git clone [https://github.com/orgkamolbek/name-analyzer.git](https://github.com/orgkamolbek/name-analyzer.git)
