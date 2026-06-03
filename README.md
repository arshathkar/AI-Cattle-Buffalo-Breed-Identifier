# 🐄 BovID

### AI-Powered Cattle & Buffalo Breed Identification System

BovID is a deep learning-powered web application that identifies Indian cattle and buffalo breeds from images using Computer Vision and Transfer Learning. The system provides breed classification, confidence scoring, breed information, and non-bovine image rejection through an efficient AI pipeline.

---

## 📌 Overview

Accurate breed identification is essential for livestock management, breeding programs, productivity analysis, and breed conservation. Traditional methods rely on manual inspection and domain expertise, making the process time-consuming and inconsistent.

BovID automates breed identification using deep learning, enabling fast and reliable predictions from a single image.

---

## 🚀 Features

- Image-based cattle and buffalo breed identification
- Deep learning-powered classification
- Non-bovine image rejection
- Automatic image quality validation
- Confidence-based predictions
- Breed information retrieval
- Cross-breed information generation
- Lightweight and scalable architecture

---

## 🧠 AI & Machine Learning

### Model Architecture

- MobileNetV2 (Transfer Learning)
- Convolutional Neural Network (CNN)
- Fine-tuned on livestock breed datasets

### Training Strategy

#### Phase 1: Feature Extraction

- Pre-trained MobileNetV2 backbone
- Base layers frozen
- Custom classification layers trained

**Purpose:**
- Preserve ImageNet features
- Faster convergence
- Reduced overfitting

#### Phase 2: Fine-Tuning

- Upper layers unfrozen
- Low learning rate training
- Breed-specific adaptation

**Purpose:**
- Learn horn structures
- Learn hump patterns
- Learn coat textures
- Improve breed-level classification accuracy

---

## 📊 Data Augmentation

To improve model generalization and reduce overfitting, the following augmentation techniques were applied:

- Rotation
- Translation
- Zoom
- Shear
- Horizontal Flip
- Brightness Adjustment

---

## 🔍 Prediction Workflow

```text
Image Upload
      │
      ▼
Image Validation
      │
      ▼
Image Preprocessing
      │
      ▼
Bovine Verification
      │
      ▼
Breed Classification
      │
      ▼
Confidence Scoring
      │
      ▼
Breed Information Lookup
      │
      ▼
Final Prediction
```

---

## 🛠 Technology Stack

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Flask
- Python

### AI / Machine Learning
- TensorFlow
- Keras
- MobileNetV2

### Image Processing
- Pillow (PIL)
- NumPy

---

## 📂 Project Structure

```text
BovID
│
├── app.py
├── train_model.py
├── augment_other.py
├── regen_class_indices.py
│
├── models/
├── labels/
│
├── requirements.txt
├── runtime.txt
├── README.md
└── index.html
```

---

## ⚙ Installation

### Clone the Repository

```bash
git clone https://github.com/<username>/BovID.git
cd BovID
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶ Running the Application

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## 📈 Applications

- Livestock Management
- Breed Verification
- Veterinary Assistance
- Agricultural Research
- Breed Conservation Programs
- Educational Demonstrations

---

## 🌱 Future Enhancements

- Multi-view Breed Recognition
- Mobile Application Deployment
- Offline Inference Support
- RFID Integration
- Livestock Tracking
- Health & Disease Detection
- Milk Yield Prediction
- Real-time Video Classification
- Multi-language Support

---

## 🎯 Performance Highlights

- Lightweight MobileNetV2 Architecture
- Fast Inference
- Transfer Learning-Based Training
- Optimized for Resource-Constrained Environments
- Scalable Deployment Architecture

---

## 📜 License

This project is intended for educational, research, and demonstration purposes.

---

## 👨‍💻 Maintainer

**Harieaswar**

AI • Computer Vision • Machine Learning