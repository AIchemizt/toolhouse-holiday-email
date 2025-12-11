# 🎄 Toolhouse Holiday Email Agent

Send personalized holiday greeting emails to customers using **Toolhouse** and **SendGrid**.

Built for the [Toolhouse Discord Bounty](https://discord.toolhouse.ai) - December 2025

## ✨ Features

- ✅ **CSV Integration** - Reads customer emails from CSV file
- ✅ **Toolhouse Agent** - Uses Toolhouse Agent Runs API with variables
- ✅ **SendGrid Email** - Sends via Toolhouse MCP + SendGrid
- ✅ **Scheduled Sending** - Auto-sends on December 25 at 9 AM

## 🏗️ How It Works
```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  customers.csv  │────▶│   Toolhouse     │────▶│    SendGrid     │
│  (your CRM)     │     │   Agent API     │     │   (emails)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        │                       ▼                       │
        │               AI generates                    │
        │            holiday greeting                   │
        │                                               ▼
        └──────────────────────────────────────▶  📧 Emails Sent!
```

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/AIchemizt/toolhouse-holiday-email
cd toolhouse-holiday-email
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your customers

Edit `customers.csv`:
```csv
name,email
John Smith,john@example.com
Sarah Johnson,sarah@example.com
```

### 4. Run it!
```bash
python main.py
```

## 🔧 Configuration

### Using the Toolhouse CLI

You can also run and deploy the agent directly:
```bash
# Install CLI
npm i -g @toolhouseai/cli

# Login
th login

# Test the agent
th run holiday.yaml

# Deploy
th deploy holiday.yaml
```

### Agent Variables

The agent uses these variables (passed via API or set in schedule):

| Variable | Description | Default |
|----------|-------------|---------|
| `customer_name` | Recipient's name | Valued Customer |
| `customer_email` | Recipient's email | test@example.com |

## 📧 Sample Output
```
🎄 Toolhouse Holiday Email Agent 🎄
==================================================
📋 Loaded 3 customers from CSV

📧 [1/3] Sending to Abhishek (myac017@gmail.com)...
   ✅ Sent!

📧 [2/3] Sending to John Smith (john@example.com)...
   ✅ Sent!

📧 [3/3] Sending to Sarah Johnson (sarah@example.com)...
   ✅ Sent!

==================================================
🎉 Done! Sent: 3 | Failed: 0
```

## 📅 Scheduled Sending

The agent is scheduled to auto-run on **December 25 at 9:00 AM** using Toolhouse Schedules.

Cron expression: `0 9 25 12 *`

You can also set up your own schedule:

### Option 1: Toolhouse Schedules (Recommended)
- Go to [Toolhouse Schedules](https://app.toolhouse.ai)
- Create new schedule with cadence `0 9 25 12 *`

### Option 2: Cron Job
```bash
0 9 25 12 * cd /path/to/project && python main.py
```

### Option 3: GitHub Actions
```yaml
on:
  schedule:
    - cron: '0 9 25 12 *'
```

## 🛠️ Tech Stack

- **[Toolhouse](https://toolhouse.ai)** - Agent Runs API + CLI
- **[SendGrid](https://sendgrid.com)** - Email delivery (via Toolhouse MCP)
- **Python 3.8+**

## 📁 Project Structure
```
toolhouse-holiday-email/
├── holiday.yaml      # Toolhouse agent config
├── main.py           # Python script for CSV processing
├── customers.csv     # Customer email list
├── requirements.txt  # Python dependencies
└── README.md
```

## 🎯 Bounty Requirements

| Requirement | Status |
|-------------|--------|
| Holiday email written & formatted | ✅ |
| CSV/CRM integration | ✅ |
| Toolhouse + email platform (SendGrid) | ✅ |
| Auto-send on pre-set date | ✅ |

## 🔗 Links

- **Agent URL**: https://agents.toolhouse.ai/d931e375-1c13-4693-8bd4-7de807a2e278
- **Toolhouse**: https://toolhouse.ai
- **Discord**: https://discord.toolhouse.ai

---

Built with ❤️ for the Toolhouse community 🎄