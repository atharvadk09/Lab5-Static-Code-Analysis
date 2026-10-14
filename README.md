# Lab 5: Static Code Analysis — Digital Wallet & Payment Tracker

## Overview
This project demonstrates static code analysis using Pylint, Bandit, and Flake8 on a Python-based digital wallet application.

## Features
- Add money to a wallet
- Validate PINs before merchant payments
- Enforce a daily payment limit
- Display recent transactions
- Calculate cashback
- Verify a payment gateway secret

## Tools Used
- Python
- Pylint — code quality analysis
- Bandit — security analysis
- Flake8 — style and formatting analysis

## Files
- `digital_wallet.py` — cleaned application code
- `issues.md` — identified issues and proposed fixes
- `reflection.md` — reflection questions and answers
- `pylint_report.txt` — Pylint results
- `bandit_report.txt` — Bandit results
- `flake8_report.txt` — Flake8 results


## Final Analysis Results
- Pylint: 10.00/10
- Bandit: No issues identified
- Flake8: No output (no reported violations)

## Run the Program
```bash
python digital_wallet.py
```

## Run Static Analysis
```bash
python -m pylint digital_wallet.py
python -m bandit -r digital_wallet.py
python -m flake8 digital_wallet.py
```