import sqlite3
import datetime
import schedule
import time
import google.generativeai as genai
from twilio.rest import Client

# AI-Powered Health Agent - Competition Template
# This file contains 8 TODOs corresponding to 8 functions in the provided implementation.
# Participants need to copy the correct code blocks from the jumbled implementation
# and complete each TODO.

# =============================================================================
# CONFIGURATION
# =============================================================================
# Direct API key assignment (replace with actual values or load from env)
api_key = "your_actual_gemini_api_key_here"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

TWILIO_ACCOUNT_SID = "your_twilio_sid_here"
TWILIO_AUTH_TOKEN = "your_twilio_token_here"
TWILIO_PHONE_NUMBER = "your_twilio_number_here"
YOUR_PHONE_NUMBER = "your_personal_number_here"

# =============================================================================
# TODO 1: DATABASE INITIALIZATION
# =============================================================================
# Find the init_db() function in jumbled implementation.
# This function should:
# - Connect to SQLite database `health_data.db`
# - Create table `health_logs` with columns:
#   date, meals, water, sleep, suggestions
# - Commit and close connection


# =============================================================================
# TODO 2: SAVE LOG
# =============================================================================
# Find the save_log() function in jumbled implementation.
# This function should:
# - Insert one record into `health_logs`
# - Save meals, water, sleep, and suggestions for today's date
# - Commit and close connection


# =============================================================================
# TODO 3: HEALTH ADVICE
# =============================================================================
# Find the health_advice() function in jumbled implementation.
# This function should:
# - Create a Gemini prompt using meals, water, and sleep data
# - Generate short actionable AI advice
# - Return the model’s response as text


# =============================================================================
# TODO 4: SEND SMS
# =============================================================================
# Find the send_sms() function in jumbled implementation.
# This function should:
# - Use Twilio Client with SID and Token
# - Send message to YOUR_PHONE_NUMBER
# - Print success/failure logs
# - Return True if successful, False otherwise


# =============================================================================
# TODO 5: GENERATE WEEKLY SMS
# =============================================================================
# Find the generate_weekly_sms() function in jumbled implementation.
# This function should:
# - Fetch last 7 records from DB
# - Summarize them in short lines (Day 1: meals..., water, sleep)
# - Ask Gemini to create motivational message <160 chars
# - Return formatted SMS message


# =============================================================================
# TODO 6: DAILY HEALTH CHECK
# =============================================================================
# Find the daily_health_check() function in jumbled implementation.
# This function should:
# - Prompt user for meals, water, sleep inputs
# - Call health_advice() for suggestions
# - Save log into DB
# - Print AI suggestions and success message


# =============================================================================
# TODO 7: WEEKLY SUMMARY (Console)
# =============================================================================
# Find the weekly_summary() function in jumbled implementation.
# This function should:
# - Fetch last 7 records
# - Ask Gemini to summarize weekly health patterns
# - Print the AI-generated weekly summary


# =============================================================================
# TODO 8: WEEKLY SMS NOTIFICATION
# =============================================================================
# Find the send_weekly_sms_notification() function in jumbled implementation.
# This function should:
# - Call generate_weekly_sms()
# - Send it via send_sms()
# - Print confirmation logs


# =============================================================================
# MAIN EXECUTION
# =============================================================================
# After implementing all TODOs:
# - Call init_db()
# - Schedule daily check at 23:33
# - Schedule weekly summary + SMS on Thursday
# - Run scheduler loop

if __name__ == "__main__":
    init_db()

    schedule.every().day.at("23:33").do(daily_health_check)
    schedule.every().thursday.at("23:34").do(weekly_summary)
    schedule.every().thursday.at("23:35").do(send_weekly_sms_notification)

    print("Health AI Agent is running... (Press Ctrl+C to stop)")
    print("Will send autonomous SMS every Thursday")

    while True:
        schedule.run_pending()
        time.sleep(60)


# =============================================================================
# COMPETITION INSTRUCTIONS
# =============================================================================
"""
AGENT BUILDING COMPETITION CHALLENGE:

Your task is to implement the missing functionality in this health AI agent
by using the code blocks provided in the jumbled implementation.

WHAT YOU NEED TO DO:
1. Study the function signatures and TODO comments above
2. Look at the jumbled implementation for actual code
3. Copy and adapt the relevant code blocks to complete each function
4. Ensure the system works end-to-end with Gemini + Twilio + SQLite

EVALUATION CRITERIA:
- Functionality: Does the health agent track daily logs?
- AI Integration: Does it generate meaningful suggestions?
- SMS System: Does it send weekly motivational messages?
- Code Quality: Is the code clean and modular?
- User Experience: Is it interactive and easy to follow?

BONUS POINTS:
- Add error handling for missing inputs
- Enhance SMS message personalization
- Add visualization of weekly trends
- Export logs to CSV or PDF
- Add reminder notifications

RESOURCES PROVIDED:
- jumbled.py: Contains all the implementation code blocks
- .env.example / config section: For API keys
- README.md: Setup and usage instructions
- requirements.txt: Required Python packages

SUBMISSION:
Submit your completed agent.py file that implements all the required functionality
using the code blocks from jumbled implementation.

Good luck! 🚀
"""
