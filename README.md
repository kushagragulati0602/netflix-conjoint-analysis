# Netflix Conjoint Analysis (Python Edition)

This is a **Python Streamlit** application for analyzing Netflix conjoint analysis data. It replaces the previous React implementation with a pure Python solution for easier data science integration.

## Prerequisites

- **Python 3.8+** installed on your system.

## Setup Instructions

1.  **Open a terminal** in this folder.
2.  **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv .venv
    # Windows:
    .venv\Scripts\activate
    # Mac/Linux:
    source .venv/bin/activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install streamlit pandas plotly numpy
    ```
4.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

## Project Structure

- `app.py`: Main Streamlit application file (UI & Routing).
- `utils.py`: Helper functions for data generation and market share calculation.
- `_archive/`: Contains the archived legacy React code.
