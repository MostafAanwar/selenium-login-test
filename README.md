# Selenium Login Test Project

This is a basic QA automation project that tests the login functionality of a demo website using Selenium WebDriver, Pytest, and Python.

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/selenium-login-test.git
   cd selenium-login-test
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the tests**
   ```bash
   pytest
   ```

## 📁 Project Structure

```
selenium-login-test/
├── tests/               # Contains all test cases
├── pages/               # Page Object Models
├── utils/               # WebDriver setup utility
├── .gitignore           # Ignored files for git
├── requirements.txt     # Required Python packages
└── README.md            # Project overview
```

## ✅ Test Scenarios

- **test_valid_login:** Logs in with correct credentials and verifies success message.
- **test_invalid_login:** Attempts login with invalid credentials and checks the error message.

## 🔗 Test Website

Tests use [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)

## 🧪 Tools Used

- Python
- Selenium
- Pytest

---

Happy Testing! 🧪
