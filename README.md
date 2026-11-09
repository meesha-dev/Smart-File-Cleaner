# Smart-File-Cleaner
# 🧹 Smart File Cleaner

A lightweight, interactive Python utility built to automate the tedious process of cleaning and standardizing messy CSV and Excel datasets. Designed to save time for data preparation tasks and freelance workflows.

---

## 🚀 Features

* **Multi-Format Support:** Seamlessly handles both `.csv` and Excel (`.xlsx`, `.xls`) files.
* **Interactive CLI:** A user-friendly command-line interface that lets you toggle specific cleaning operations on the fly.
* **Data Standardization:**
  * Automatically strips extra whitespace from text columns.
  * Standardizes column headers (converts to lowercase, trims spaces, replaces spaces with underscores).
  * Handles missing numerical data safely by filling gaps.
  * Detects and removes duplicate rows to ensure data integrity.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Core Library:** Pandas (Data manipulation and input/output handling)

---

## 📈 Project Evolution (Changelog)

* **Version 0.5 (Current):** Added an automated audit summary report displaying row counts, duplicate metrics, and cleaning confirmation.
* **Version 0.4:** Added interactive CLI menu and dynamic toggle options for custom data cleaning.
* **Version 0.3:** Added support for Excel file formats alongside CSV.
* **Version 0.2:** Implemented core data cleaning logic (whitespace trimming, header normalization, duplicate removal).
* **Version 0.1:** Initial script setup and file loading architecture.

## 💻 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR-USERNAME/Smart-File-Cleaner.git](https://github.com/YOUR-USERNAME/Smart-File-Cleaner.git)
