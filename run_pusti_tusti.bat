@echo off

call venv\Scripts\activate

start cmd /k "uvicorn backend.main:app --reload"

timeout /t 5 >nul

start cmd /k "python -m streamlit run frontend/app.py"

timeout /t 5 >nul

start http://localhost:8501