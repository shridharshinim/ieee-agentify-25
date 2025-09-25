# 🏥 Health Agent

A Python health tracking application that logs daily health data (meals, water, sleep) and provides AI-powered recommendations. Includes automated SMS notifications for weekly health summaries.

## 📦 Dependencies

```
google-generativeai
twilio
schedule
```

## 🚀 Installation & Setup

1. **Install dependencies:**
   ```bash
   pip install google-generativeai twilio schedule
   ```

2. **Configure API keys in `health_agent.py`:**
   - Replace `"your_actual_gemini_api_key_here"` with your Gemini API key
   - Replace Twilio credentials with your actual values

3. **Get API Keys:**
   - **Gemini API**: Visit [Google AI Studio](https://aistudio.google.com/) → Get API Key
   - **Twilio SMS**: Visit [Twilio Console](https://console.twilio.com/) → Get credentials

## 🔑 API Setup Guide

### Gemini AI API
- **What it does**: Powers the AI health recommendations and analysis
- **Setup**:
  1. Go to [Google AI Studio](https://aistudio.google.com/)
  2. Sign in with Google account
  3. Click "Get API Key" → "Create API Key"
  4. Copy the key and replace `api_key = "your_actual_gemini_api_key_here"`
- **Cost**: Free tier available with usage limits

### Twilio SMS API
- **What it does**: Sends automated SMS notifications with weekly health summaries
- **Setup**:
  1. Create account at [Twilio](https://console.twilio.com/)
  2. Get Account SID, Auth Token from dashboard
  3. Get a Twilio phone number (free trial gives you one)
  4. Replace these values in the code:
     ```python
     TWILIO_ACCOUNT_SID = "your_account_sid"
     TWILIO_AUTH_TOKEN = "your_auth_token"  
     TWILIO_PHONE_NUMBER = "+1234567890"  # Your Twilio number
     YOUR_PHONE_NUMBER = "+1987654321"    # Your personal number
     ```
- **Cost**: Free trial credits, then pay-per-message

## ▶️ How to Run

```bash
python health_agent.py
```

The app will:
- Run continuously with scheduled health check-ins
- Daily prompt at 23:04 for health data
- Weekly SMS summary every Thursday
- Store data in SQLite database (`health_data.db`)

## 🔧 What it does

- **Daily Tracking**: Log meals, water intake, and sleep
- **AI Analysis**: Get personalized health advice using Gemini AI
- **SMS Alerts**: Automated weekly health summaries via Twilio
- **Data Storage**: Persistent SQLite database for health history

## ⚠️ Note

Replace all placeholder API keys in the code before running. This is for informational purposes only - consult healthcare professionals for medical advice.