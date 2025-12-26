# 🤖 AutoApply AI

A personal project exploring job application automation using **Python**, **Selenium**, and **basic AI concepts**.

The goal of this project is to better understand how web automation, text similarity, and AI-assisted content generation can work together in a real-world scenario.

---

## 💡 Project Overview

**AutoApply AI** is an experimental automation script that simulates parts of the job application process.

Instead of blindly submitting applications, the project focuses on:
1.  **Analyzing** job descriptions directly from job boards.
2.  **Comparing** them with a resume using **Vector Mathematics** (TF-IDF).
3.  **Generating** a simple, customized cover letter based on the match score.
4.  **Storing** the results in a local database to track opportunities.

> *Note: This project was built as a learning exercise and is not intended to be used at scale for spamming.*

---

## 🚀 What It Does

- **Web Automation**: Uses **Selenium** (Edge WebDriver) to navigate job pages, scroll, and extract real content while simulating human behavior to avoid bot detection.
- **Smart Matching Logic**: Computes a similarity score (0-100%) between a resume and a job description using `scikit-learn` (**TF-IDF & Cosine Similarity**). *No random numbers involved.*
- **Cover Letter Generation**: Automatically drafts a tailored cover letter content based on the relevance score.
- **Local Persistence**: Keeps track of analyzed jobs using an **SQLite** database to prevent duplicate analysis.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Automation**: Selenium
- **Data Science / NLP**: Scikit-Learn, NumPy
- **Database**: SQLite, SQLAlchemy

---

## ⚙️ How to Run

Follow these steps to set up and run the project locally:


Create a virtual environment:
> python -m venv venv

Activate: 
> .\venv\Scripts\activate

Install dependencies:
> pip install -r requirements.txt

Run the script:
> python main.py

---

## 📊 How to View Results

Once the script finishes running, a database file will be created at `data/jobs.db`.

You can view the results (jobs found, match scores, generated letters) using:
- Any **SQLite Viewer** (like DB Browser for SQLite).
- By inspecting the **logs** in the terminal during execution.

---

**Created by Rayan Saadani Hassani**