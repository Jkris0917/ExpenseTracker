# 💴 Expense Tracker CLI

A command-line expense tracking tool built with Python.
Designed to help users log, view, search, and manage daily expenses,
with data persisted to a local JSON file.

## Features

- Add expenses with category, amount, date, and notes
- Edit or delete existing expenses by ID
- Search expenses by category or keyword
- Data saved automatically to `expense.json`
- Japanese text supported (UTF-8 encoding)

## Tech stack

- Python 3.12
- `json` · `datetime` · `os` (standard library only)

## How to run

```bash
git clone https://github.com/jkris0917/expense-tracker
cd ExpenseTracker
python main.py
```

## What I learned

- Modular code structure (separating logic from UI)
- JSON file I/O with UTF-8 encoding for Japanese text support  
- Error handling with specific exception types
- Dictionary mutation patterns and avoiding stale data bugs

---

# 💴 経費トラッカー CLI

Pythonで作ったコマンドライン経費管理ツールです。
日々の支出をカテゴリ・金額・メモで記録し、JSONファイルに保存します。

## 機能

- カテゴリ・金額・日付・メモで支出を追加
- IDで支出を編集・削除
- キーワードで支出を検索
- データは自動的に `expense.json` に保存

## 実行方法

```bash
python main.py
```