import sqlite3
import datetime
import schedule
import time
import google.generativeai as genai
from twilio.rest import Client

# AI-Powered Health Agent - Jumbled Implementation
# This file contains all function implementations but in jumbled order.
# Use this to complete agent.py by copying the correct blocks.

# Direct API key assignment
api_key = "your_actual_gemini_api_key_here"
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

TWILIO_ACCOUNT_SID = "your_twilio_sid_here"
TWILIO_AUTH_TOKEN = "your_twilio_token_here"
TWILIO_PHONE_NUMBER = "your_twilio_number_here"
YOUR_PHONE_NUMBER = "your_personal_number_here"

# =============================================================================
# CODE BLOCK A: WEEKLY SUMMARY (Console)
# =============================================================================
def weekly_summary():
    conn = sqlite3.connect("health_data.db")
    cur = conn.cursor()
    cur.execute("SELECT meals, water, sleep, suggestions FROM health_logs ORDER BY date DESC LIMIT 7")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        print("No data yet.")
        return

    past_week = "\n".join([f"Meals: {r[0]}, Water: {r[1]}, Sleep: {r[2]}, Advice: {r[3]}" for r in rows])
    prompt = f"""
    You are a health AI agent.
    Here are 7 days of user health logs:
    {past_week}

    Summarize trends, improvements, and give overall health advice.
    """
    response = model.generate_content(prompt)
    print("\nWeekly Health Summary:\n", response.text)

# =============================================================================
# CODE BLOCK B: DATABASE INITIALIZATION
# =============================================================================
def init_db():
    conn = sqlite3.connect("health_data.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS health_logs (
            date TEXT,
            meals TEXT,
            water TEXT,
            sleep TEXT,
            suggestions TEXT
        )
    """)
    conn.commit()
    conn.close()

# =============================================================================
# CODE BLOCK C: SEND SMS
# =============================================================================
def send_sms(message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
        print(f"SMS sent successfully! Message ID: {message.sid}")
        return True
    except Exception as e:
        print(f"SMS failed: {e}")
        return False

# =============================================================================
# CODE BLOCK D: HEALTH ADVICE
# =============================================================================
def health_advice(meals, water, sleep):
    prompt = f"""
    You are a personal wellness AI agent.
    Analyze this daily health info and give short, actionable advice.
    Meals: {meals}
    Water Intake: {water}
    Sleep: {sleep}
    Output:
    """
    response = model.generate_content(prompt)
    return response.text

# =============================================================================
# CODE BLOCK E: DAILY HEALTH CHECK
# =============================================================================
def daily_health_check():
    print("\n=== AI Health Agent ===")
    meals = input("What did you eat today? ")
    water = input("How many glasses of water did you drink? ")
    sleep = input("How many hours of sleep did you get? ")

    suggestions = health_advice(meals, water, sleep)
    print("\nAI Suggestions:\n", suggestions)

    save_log(meals, water, sleep, suggestions)
    print("Data saved for today.")

# =============================================================================
# CODE BLOCK F: SAVE LOG
# =============================================================================
def save_log(meals, water, sleep, suggestions):
    conn = sqlite3.connect("health_data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO health_logs VALUES (?, ?, ?, ?, ?)",
                (str(datetime.date.today()), meals, water, sleep, suggestions))
    conn.commit()
    conn.close()

# =============================================================================
# CODE BLOCK G: GENERATE WEEKLY SMS
# =============================================================================
def generate_weekly_sms():
    conn = sqlite3.connect("health_data.db")
    cur = conn.cursor()
    cur.execute("SELECT meals, water, sleep, suggestions FROM health_logs ORDER BY date DESC LIMIT 7")
    rows = cur.fetchall()
    conn.close()

    if not rows:
        return "Health Agent: No data logged this week. Start tracking your health!"

    past_week = "\n".join([f"Day {i+1}: {r[0][:20]}..., {r[1]} water, {r[2]} sleep" 
                          for i, r in enumerate(reversed(rows))])
    
    prompt = f"""
    You are an autonomous health AI agent sending a weekly summary via SMS.
    
    Week's data:
    {past_week}

    Create a SHORT, motivational message (under 160 characters) that includes:
    1. Key insight about the week
    2. One specific improvement suggestion
    3. Encouraging tone
    
    Format: Like a helpful friend texting you.
    """
    response = model.generate_content(prompt)
    
    message = f"Your Health Agent:\n\n{response.text}\n\nStay healthy!"
    return message

# =============================================================================
# CODE BLOCK H: WEEKLY SMS NOTIFICATION
# =============================================================================
def send_weekly_sms_notification():
    print("\nGenerating autonomous weekly health SMS...")
    
    message = generate_weekly_sms()
    print(f"Message: {message}")
    
    if send_sms(message):
        print("Autonomous SMS notification sent!")
    else:
        print("Failed to send SMS notification")
