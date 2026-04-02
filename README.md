# 🚀 Instagram Comment-to-DM Automation

<div align="center">

![Instagram Automation](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=next.js&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)

**Automate your Instagram engagement like a pro! 💬✨**

Turn comments into conversations instantly with smart keyword-triggered DMs.

[🎯 Features](#-features) • [🛠️ Setup](#️-quick-setup) • [🚀 Deploy](#-deployment) • [📸 Demo](#-demo)

</div>

---

## 🎯 Features

✨ **Smart Automation**
- 🔍 Keyword detection in comments
- 💌 Instant DM responses
- 💬 Public comment replies
- 🎬 Per-reel customization

🎨 **Beautiful Dashboard**
- 📊 Real-time stats
- 🖼️ Visual reel grid
- ⚡ One-click configuration
- 🌈 Stunning glassmorphism UI

🔒 **Secure & Reliable**
- 🔐 Webhook verification
- 🛡️ Environment-based secrets
- 📝 JSON-based storage (no DB needed!)
- ☁️ Production-ready deployment

---

## 🛠️ Quick Setup

### 📋 Prerequisites

- Instagram Business Account
- Meta Developer App
- Python 3.8+
- Node.js 18+

### 🔑 Get Your Credentials

1. **VERIFY_TOKEN**: Any random string (e.g., `my_secret_token_123`)
2. **INSTAGRAM_ACCESS_TOKEN**: 
   - Go to [Meta App Dashboard](https://developers.facebook.com/apps/)
   - Generate token (starts with `IGAA`)
   - Permissions needed: `instagram_business_basic`, `instagram_business_manage_messages`, `instagram_business_manage_comments`
3. **IG_BUSINESS_ACCOUNT_ID**: 
   - Found in Meta Business Suite → Instagram Settings
   - Long number like `17841433084275074`

---

## 💻 Local Development

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
cp .env.example .env
# Edit .env with your credentials
uvicorn main:app --reload
```

🎉 Backend running at `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
cp .env.local.example .env.local
# Set NEXT_PUBLIC_API_URL=http://localhost:8000
npm run dev
```

🎉 Frontend running at `http://localhost:3000`

---

## 🚀 Deployment

### 🚂 Railway (Backend)

1. Push code to GitHub
2. Create new project on [Railway](https://railway.app)
3. Connect your repo
4. Set root directory: `backend`
5. Add environment variables:
   ```
   VERIFY_TOKEN=your_token
   INSTAGRAM_ACCESS_TOKEN=your_ig_token
   IG_BUSINESS_ACCOUNT_ID=your_account_id
   ```
6. Deploy! 🎊

### ▲ Vercel (Frontend)

1. Create new project on [Vercel](https://vercel.com)
2. Import your GitHub repo
3. Set root directory: `frontend`
4. Add environment variable:
   ```
   NEXT_PUBLIC_API_URL=https://your-railway-url.railway.app
   ```
5. Deploy! 🎊

### 🔗 Configure Webhook

1. Go to Meta App Dashboard → Webhooks
2. Callback URL: `https://your-railway-url.railway.app/webhook`
3. Verify Token: Your `VERIFY_TOKEN`
4. Subscribe to `comments` field
5. Save! ✅

---

## 📸 Demo

### Dashboard View
Beautiful, responsive dashboard to manage all your reels in one place.

### How It Works

1. 👤 User comments on your reel with trigger keyword (e.g., "info")
2. ⚡ Webhook instantly notifies your server
3. 💌 System sends personalized DM
4. 💬 Posts public reply on comment
5. 🎉 User gets instant response!

---

## 🎨 Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 **FastAPI** | Lightning-fast Python backend |
| ⚛️ **Next.js 14** | Modern React framework |
| 📘 **TypeScript** | Type-safe frontend |
| 🎨 **Tailwind CSS** | Beautiful, responsive UI |
| 📦 **JSON Storage** | Simple, no-database solution |
| 🚂 **Railway** | Backend hosting |
| ▲ **Vercel** | Frontend hosting |

---

## 📖 Usage Guide

### Step 1: Open Dashboard
Navigate to your deployed frontend URL

### Step 2: View Your Reels
All your Instagram reels appear in a beautiful grid

### Step 3: Configure Automation
Click any reel to set:
- 🔑 **Trigger Keyword**: Word that activates automation
- 💌 **DM Message**: Private message sent to user
- 💬 **Comment Reply**: Public response on their comment
- ✅ **Active/Inactive**: Toggle automation on/off

### Step 4: Save & Test
Comment on your reel with the trigger keyword and watch the magic happen! ✨

---

## 🔧 Configuration

### Default Settings
All reels start with default configuration:
```json
{
  "trigger_keyword": "info",
  "dm_message": "Thanks for your interest! Check your DMs.",
  "comment_reply": "Sent you a DM!",
  "active": true
}
```

Customize each reel individually through the dashboard!

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests

---

## 📄 License

MIT License - feel free to use this project for personal or commercial purposes!

---

## 💖 Credits

Built with ❤️ by **Tejas.algo**

---

<div align="center">

**⭐ Star this repo if you found it helpful!**

Made with 🔥 and ☕

</div>
