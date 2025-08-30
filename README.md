# Luarmor Panel

A free alternative Luarmor key system with:
- **Flask API** (Render deployment)
- **Discord Bot** (Render background worker)
- **React Dashboard** (Vercel deployment)

## Deployment Guide

### 1. Clone Repo
```bash
git clone https://github.com/<your-username>/luarmor-panel.git
cd luarmor-panel
```

### 2. Set Up Environment Variables
Copy `.env.example` → `.env` and fill in values.

### 3. Deploy API on Render
- Root directory: `/api`
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn api:app`

### 4. Deploy Discord Bot on Render
- Root directory: `/bot`
- Build command: `pip install -r requirements.txt`
- Start command: `python bot.py`

### 5. Deploy Dashboard on Vercel
- Root directory: `/dashboard`
- Framework: `Vite + React`
- Environment variable: `VITE_API_URL`

### 6. Enjoy 🚀
