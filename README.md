# 📧 Email Classification for Support Team

This project classifies incoming support emails into predefined categories (e.g., Billing, Technical Support) while masking personal information like names, emails, and card numbers.

### ✅ Features
- Mask PII (personal information (PII) )using Regex
- Classify emails using Naive Bayes + TF-IDF
- Gradio frontend for Hugging Face Spaces

### Feature extract for text
- Full Name
- Email Address
- Phone number 
- Date of birth 
- Aadhar card number 
- Credit/ Debit Card Number
- CVV number
- Card expiry number 

### 🛠 Project Structure
- `app.py`: Gradio app
- `train_model.py`: Train & save classifier model
- `models.py`: Model saving, loading, predicting
- `utils.py`: PII masking
- `data/data.csv`: Training data
- `model/`: Saved classifier and vectorizer

### 🚀 How to Run Locally

#### create virtual envirment

- python -m venv .venv

##### activete virtual envirment
- .venv\Scripts\activate

### then run this command step by step
- pip install -r requirements.txt
### before run train_model.py create  a folder model then run
- python train_model.py
### then run this
- python app.py

### app link

https://huggingface.co/spaces/saisatyabrat/email-pii-classifier

you can cheack here 👆
