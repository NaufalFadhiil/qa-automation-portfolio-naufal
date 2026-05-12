# QA Automation Portfolio - Naufal Fadhiil 

<p align="center">
  <img src="https://img.shields.io/badge/QA-Automation-green" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Cypress-E2E-17202C?style=flat&logo=cypress&logoColor=white" />
  <img src="https://img.shields.io/badge/Selenium-WebDriver-43B02A?style=flat&logo=selenium&logoColor=white" />
  <img src="https://img.shields.io/badge/API-Testing-orange" />
</p>

Repository ini berisi kumpulan project Quality Assurance Automation yang saya kerjakan sebagai bagian dari pengembangan keterampilan QA Engineer, khususnya pada bidang Web Automation Testing dan API Automation Testing.

Project di dalam repository ini mencakup:

* **Web UI Automation Testing**
* **API Automation Testing**
* **Page Object Model (POM)**
* **Fixtures & Test Data Management**
* **Intercept & API Validation**
* **Positive & Negative Test Case Automation**

## 🛠 Tech Stack

### Automation Tools
* Cypress
* Selenium WebDriver

### Programming Language
* JavaScript
* Python

## Other Tools
* VS Code
* PyCharm
* ChromeDriver
* Git & GitHub

## 1. OrangeHRM Automation Testing ![Status](https://img.shields.io/badge/Completed-success)
Automation testing project menggunakan **Cypress** pada website **OrangeHRM Demo** dengan implementasi **Page Object Model (POM), fixtures, reusable methods, serta API intercept validation.**

Automation project ini mencakup beberapa testing-fitur utama seperti: </br>
**1.) Login Feature Automation </br>
2.) Forgot Password Automation </br>
3.) Directory Section Feature Automation**

### Test Coverage
#### 1.) Login Feature:
- Login dengan kredensial valid
- Login dengan password salah
- Login dengan username salah
- Login tanpa username
- Login tanpa password
- Login tanpa input
- Validasi password hidden
- Forgot password navigation

#### 2.) Forgot Password Feature:
- Navigate forgot password page
- Submit valid username
- Submit invalid username
- Submit empty username
- Cancel forgot password process

#### 3.) Directory Feature:
- Navigate to Directory page
- Search valid employee
- Search invalid employee
- Reset employee search
- API response validation

### 4.) Implementation:
- Cypress Automation Testing
- Positive & Negative Test Case
- Cypress Intercept
- Page Object Model (POM)
- Fixtures & Test Data Management
- API Validation
- Reusable Methods
- Clean Automation Structure

---

## 5. Platzi API Automation Testing ![Status](https://img.shields.io/badge/Completed-success)
API Automation Testing menggunakan Cypress pada Platzi Fake API.

### Endpoint
* Categories API

### Test Coverage

* GET all categories
* GET category by ID
* GET invalid category
* POST create category
* PUT update category
* PUT invalid category
* DELETE category

### Implementation

* API Request Testing
* Response Validation
* Status Code Assertion
* CRUD API Automation

---

## 6. Selenium Basic Automation ![Status](https://img.shields.io/badge/Learning-informational)
Latihan dasar automation testing menggunakan Selenium WebDriver dan Python.

### Learning Topics

* Element interaction
* Navigation handling
* Alert handling
* Basic automation scenario

---

# ▶️ How to Run Cypress Project

## 1. Install dependencies

```bash
npm install
```

## 2. Open Cypress

```bash
npx cypress open
```

## 3. Run specific test

```bash
npx cypress run
```

---

# ▶️ How to Run Selenium Project

## 1. Install Selenium

```bash
pip install selenium
```

## 2. Run automation script

```bash
python belajarselenium.py
```

Note:
Pastikan ChromeDriver sudah sesuai dengan versi browser Google Chrome.

---

### 📌 Development Notes:
Repository ini merupakan bagian dari perjalanan pembelajaran saya sebagai QA Automation Engineer.
Melalui project-project ini saya mempelajari:
* Automation testing menggunakan Cypress & Selenium WebDriver
* API Automation Testing
* Page Object Model (POM)
* Fixtures & reusable automation structure
* Intercept dan API validation
* Penyusunan automation framework yang lebih rapi dan scalable

Ke depannya repository ini akan terus dikembangkan dengan:
* Playwright Automation
* CI/CD Integration
* Reporting Dashboard
* Custom Commands
* Environment Configuration
* Advanced API Testing
* Cross Browser Testing

---

# 🔗 Repository Highlights
* Web UI Automation
* API Automation
* Cypress Intercept
* Page Object Model
* Fixtures Management
* Selenium Basic Automation
* Positive & Negative Testing

---

✍️ Author: Naufal Fadhiil
🎓 Informatics Engineering Student - Widyatama University
📅 Last Updated: May 2026
