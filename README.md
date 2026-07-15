# 🧠 NeuroVision AI - Brain Tumor Detection System

An AI-powered web application that detects brain tumors from MRI images using a Convolutional Neural Network (CNN). The system allows users to register, log in, upload MRI scans, receive tumor predictions with confidence scores, and securely manage access through authentication.

---

## 📌 Features

### 🔐 Authentication
- User Registration
- User Login (JWT Authentication)
- Forgot Password (Without OTP)
- Secure Password Hashing (bcrypt)
- Logout

### 🧠 Brain Tumor Prediction
- Upload Brain MRI Image
- CNN Model Prediction
- Confidence Score
- Supports 4 Classes:
  - Glioma
  - Meningioma
  - Pituitary
  - No Tumor
- Prediction Result Display
- Stores Prediction History in MongoDB

### 🎨 User Interface
- Professional Medical Theme
- Responsive Design
- Dashboard
- Image Preview
- Loading Spinner
- Bootstrap 5 UI
- Vanilla JavaScript

### ☁️ Deployment
- Azure App Service
- MongoDB
- TensorFlow/Keras Model

---

# 🛠️ Tech Stack

## Frontend
- HTML5
- CSS3
- Bootstrap 5
- JavaScript

## Backend
- Flask
- Flask-JWT-Extended
- Flask-CORS

## Deep Learning
- TensorFlow
- Keras
- OpenCV
- NumPy

## Database
- MongoDB

## Deployment
- Microsoft Azure

---

# 📂 Project Structure

```text
BrainTumorClassification/

│
├── app.py
├── config.py
├── requirements.txt
├── .env
│
├── database/
│      mongodb.py
│
├── middleware/
│      jwt_auth.py
│
├── models/
│      brain_tumor.keras
│
├── routes/
│      auth_routes.py
│      dashboard_routes.py
│      prediction_routes.py
│
├── services/
│      auth_service.py
│      dashboard_service.py
│      prediction_service.py
│
├── utils/
│      image_utils.py
│
├── uploads/
│
├── templates/
│      login.html
│      register.html
│      forgot_password.html
│      dashboard.html
│      prediction.html
│
├── static/
│      css/
│      js/
│      images/
│
└── training/
       train_model.py
```

---

# 🧠 CNN Model Architecture

```
Input Image (224 × 224 × 3)

↓

Conv2D

↓

AveragePooling2D

↓

Flatten

↓

Dense

↓

Softmax Output Layer

↓

Prediction
```

---

# 🩺 Brain Tumor Classes

| Class | Description |
|--------|-------------|
| Glioma | Brain Tumor |
| Meningioma | Brain Tumor |
| Pituitary | Brain Tumor |
| No Tumor | Healthy Brain |

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/NeuroVision-AI.git
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret

MONGO_URI=mongodb://localhost:27017

DATABASE_NAME=BrainTumorDB
```

---

## Run Application

```bash
python app.py
```

Application will run on

```
http://127.0.0.1:5000
```

---

# 🔑 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/register` | Register User |
| POST | `/api/login` | Login User |
| PUT | `/api/forgot-password` | Reset Password |

---

## Dashboard

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/dashboard` | Dashboard Data |

---

## Prediction

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/predict` | Predict Brain Tumor |

---

# 🖼️ Application Flow

```
Register

↓

Login

↓

Dashboard

↓

Upload MRI

↓

CNN Prediction

↓

Display Result

↓

Save Prediction
```

---

# 📈 Model Output Example

```
Prediction

Glioma

Confidence

98.74%
```

---

# 📊 Dataset

The CNN model is trained on a Brain MRI dataset containing four classes:

- Glioma
- Meningioma
- Pituitary
- No Tumor

Images are resized to **224 × 224** before training.

---

# 🔒 Security Features

- JWT Authentication
- Password Hashing (bcrypt)
- Protected APIs
- Session Management

---

# 📌 Future Improvements

- Prediction History
- User Profile
- Email Notifications
- Admin Dashboard
- Model Retraining
- Docker Support
- Azure Blob Storage
- Role-Based Authentication

---

# 👩‍💻 Author

**Rashi Jariwala**

**AI & Full Stack Developer**

---
