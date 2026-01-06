# daily_bot.py
import requests
import json

def post_daily_reminder():
    webhook_url = "SEU_SLACK_WEBHOOK"
    message = {
        "text": "🚀 Daily Standup 9h30!\n\n1. O que fiz ontem?\n2. O que vou fazer hoje?\n3. Bloqueios?",
        "channel": "#dailies"
    }
    requests.post(webhook_url, json=message)

if __name__ == "__main__":
    post_daily_reminder()