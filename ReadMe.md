# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   https://github.com/RamMarthi9/ExpenseTrackingSystem
   cd expense-management-system
   ```
2. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
3. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
4. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
## 📸 Application Screenshots

### ➕ Add / Update Expenses
![Add Update Screen](docs/screenshots/add_update.png)

---

### 📊 Analytics by Category
![Category Analytics](docs/screenshots/analytics_by_category.png)

---

### 📈 Monthly Expense Analytics
![Monthly Analytics](docs/screenshots/monthly_analytics.png)
