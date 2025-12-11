"""
Toolhouse Holiday Email Agent
Sends holiday greetings to customers from CSV using Toolhouse
"""

import csv
import time
import requests

# Your deployed agent URL
AGENT_URL = "https://agents.toolhouse.ai/d931e375-1c13-4693-8bd4-7de807a2e278"


def load_customers_from_csv(file_path: str) -> list:
    customers = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            customers.append({
                "name": row.get("name", "Valued Customer"),
                "email": row.get("email")
            })
    return customers


def send_holiday_email(customer_name: str, customer_email: str) -> bool:
    """Send holiday email via Toolhouse agent"""
    
    payload = {
        "vars": {
            "customer_name": customer_name,
            "customer_email": customer_email
        }
    }
    
    response = requests.post(AGENT_URL, json=payload)
    return response.status_code == 200


def main():
    print("🎄 Toolhouse Holiday Email Agent 🎄")
    print("=" * 50)
    
    customers = load_customers_from_csv("customers.csv")
    print(f"📋 Loaded {len(customers)} customers\n")
    
    successful = 0
    failed = 0
    
    for i, customer in enumerate(customers, 1):
        name = customer["name"]
        email = customer["email"]
        
        print(f"📧 [{i}/{len(customers)}] Sending to {name} ({email})...")
        
        if send_holiday_email(name, email):
            print(f"   ✅ Sent!")
            successful += 1
        else:
            print(f"   ❌ Failed")
            failed += 1
        
        time.sleep(1)  # Small delay between emails
    
    print("\n" + "=" * 50)
    print(f"🎉 Done! Sent: {successful} | Failed: {failed}")


if __name__ == "__main__":
    main()