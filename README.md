# PANDUAN MENJALANKAN PROGRAM
## Analisis Sentimen Twitter/X - Random Forest

**Nama:** ILHAM BUSTOMI  
**NIM:** 231011401918  
**Kelas:** 05TPLP034

---

## 📦 INSTALASI LIBRARY

### Install Semua Library Yang Dibutuhkan:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn ntscraper playwright
python -m playwright install chromium
```

**Note:** Jika tidak ingin install Playwright (ukuran besar), skip dan program akan pakai dataset manual.

---

## 🚀 CARA MENJALANKAN

### **Opsi 1: Via Terminal/Command Prompt** (Recommended)

1. **Buka Terminal/CMD**

2. **Navigate ke folder:**
   ```bash
   cd "C:\Users\ibust\Downloads\UAS KB"
   ```

3. **Jalankan Script:**
   ```bash
   python RANDOM_FOREST.py
   ```

4. **Selesai!** 
   - Program akan otomatis crawling atau pakai dataset manual
   - Hasil akurasi akan ditampilkan di terminal

---

### **Opsi 2: Via Google Colab**

1. **Upload Files ke Colab:**
   - `UAS_Analisis_Sentimen_Random_Forest.ipynb`
   - `dataset_sentimen_indonesia.csv`

2. **Install Library (di cell pertama):**
   ```python
   !pip install ntscraper
   ```

3. **Run All Cells:**
   - Runtime → Run All (atau Ctrl+F9)

---

### **Opsi 3: Via Jupyter Notebook (Local)**

1. **Buka Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Buka file:**
   - Klik `UAS_Analisis_Sentimen_Random_Forest.ipynb`

3. **Run All:**
   - Cell → Run All

---

## 📊 OUTPUT YANG DIHASILKAN

### **Di Terminal:**
```
============================================================
   ANALISIS SENTIMEN TWITTER - RANDOM FOREST
============================================================

[OPSI 1] Mencoba crawling via BROWSER AUTOMATION...
    >>> [SUKSES] Dapat 315 tweet
    >>> [SAVED] crawled_browser_20260107_102345.csv

✓ Menggunakan MURNI hasil crawling untuk analisis.

[HASIL] Akurasi Model: 83.33%
```

### **File yang Mungkin Dibuat:**
- `crawled_browser_YYYYMMDD_HHMMSS.csv` (jika crawling berhasil)
- `crawled_nitter_YYYYMMDD_HHMMSS.csv` (jika pakai Nitter)

---

## ⚙️ TIPS UNTUK UAS

### **Sehari Sebelum UAS:**
- ✅ Test jalankan dengan: `python RANDOM_FOREST.py`
- ✅ Pastikan muncul akurasi (79-85%)
- ✅ Jangan jalankan berkali-kali (simpan IP bersih)

### **Saat Presentasi:**
1. Jalankan **SEKALI**: `python RANDOM_FOREST.py`
2. Tunggu hasil (30-60 detik)
3. Show akurasi ke dosen
4. Jika berhasil crawl → bonus WOW factor!
5. Jika pakai dataset manual → tetap bagus (412 data)

---

## 🔧 TROUBLESHOOTING CEPAT

### ❌ Error: ModuleNotFoundError
**Solusi:** `pip install [nama-library]`

### ❌ Crawling Gagal (429 / Rate Limit)
**Solusi:** Biarkan program pakai dataset manual (412 data sudah cukup)

### ❌ Browser Tidak Muncul
**Normal!** Browser jalan di background (headless mode)

---

## ✅ KESIMPULAN

Program ini **selalu berhasil** karena punya fallback 4-layer:
1. Browser Automation (best)
2. Auth Token  
3. Nitter
4. Dataset Manual (garanteed 412 data)

**Tinggal jalankan dan tunggu hasilnya!**
