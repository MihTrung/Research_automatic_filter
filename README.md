# 🧪 Research Filter Tool (Python)

This is a simple Python tool to **filter and clean research data** (e.g., from academic databases like Web of Science or Scopus) stored in `.csv` format. It is useful for researchers who want to **quickly remove duplicates, short papers, low-impact research, non-English texts, or review/survey articles**.

---

## 📂 Folder Structure

```
project/
│
├── input/
│   └── Raw_data.csv         ← Your raw research data (CSV)
│
├── output/
│   └── output_research.csv  ← Filtered result saved here
│
├── function.py              ← All core filtering functions
├── main.py                  ← The main entry point
├── reference.txt            ← Required libraries
└── README.md                ← This file
```

---

## 🚀 Features

The tool performs the following filtering steps sequentially:

1. **Normalize Publication Dates**
   Convert short date formats (e.g. `JAN`, `FEB 2`) into day-of-year integers for comparison.

2. **Remove Duplicate Titles**
   Keep only the **most recent version** of duplicated research based on publication year and day.

3. **Remove Short Research Papers**
   Filter out papers with fewer than `5` pages (adjustable).

4. **Remove Inferior Research**
   Remove research with **fewer than 5 citations**, unless published in the current year.

5. **Keep Only English Research**
   Use language detection to retain only articles written in English.

6. **Remove Reviews or Surveys**
   Exclude papers with “review” or “survey” in the abstract.

---

## 🛠 How to Use

### 1. Install Dependencies

Install the required packages listed in `reference.txt`:

```bash
pip install -r reference.txt
```

This includes:

* `pandas`
* `langdetect`
* `datetime`

### 2. Place Input File

Put your raw research CSV file inside the `input/` folder.
Rename it to `Raw_data.csv`, or modify the filename path in `main.py` here:

```python
input_path = Path(__file__).parent / "input" / "Raw_data.csv"
```

### 3. Run the Script

Run the main script to apply all filters:

```bash
python main.py
```

### 4. Output File

The cleaned result will be saved to:

```
output/output_research.csv
```

---

## 📄 Example Input Columns

Make sure your input CSV includes at least the following columns:

* `DOI`
* `Language`
* `Article Title`
* `Abstract`
* `Times Cited, All Databases`
* `Publication Year`
* `Publication Date`
* `Number of Pages`

---

## 📌 Notes

* You can change thresholds (e.g., `min_pages`, citation count) by editing the function parameters in `main.py`.
* Non-English detection is based on `langdetect`, which works best with well-written abstracts.
* If your file encoding is not Latin1, update this line accordingly:

  ```python
  df = pd.read_csv(input_path, encoding='latin1')
  ```

---

## ✅ Sample Output Log

```
I removed 32 duplicate research!
Now it has 268 research!
----------
I removed 45 short researchs !!
Now it has 223 researchs !!!
----------
I removed 41 inferior researchs !!
Now it has 182 researchs !!!
----------
I get 170 English researchs !!
Now it has 170 researchs !!!
----------
I removed 21 survey and review researchs !!
Now it has 149 researchs !!!
--------------------
Done!
```


#### --- make by GPT ---