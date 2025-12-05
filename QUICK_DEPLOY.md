# 🚀 Quick Deploy to Render

Your Wagtail CMS is **ready for Render deployment with full admin access!**

## ✅ What's Configured

- ✅ `render.yaml` - Infrastructure as code
- ✅ `build.sh` - Automated deployment script
- ✅ PostgreSQL database configuration
- ✅ Production settings optimized
- ✅ Static files with WhiteNoise

---

## 🎯 Deploy in 3 Steps

### 1️⃣ Push to GitHub

```bash
cd /Users/shivaansh/accessibility-cms-wagtail
git add .
git commit -m "Ready for Render deployment"
git push origin main
```

### 2️⃣ Deploy on Render

1. Go to https://dashboard.render.com/
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Render auto-detects `render.yaml` ✨
5. Add environment variables:
   - `SECRET_KEY`: Generate with `python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
   - `DATABASE_URL`: Link PostgreSQL database
6. Click **"Create Web Service"**

### 3️⃣ Create Admin Account

After deployment:
1. Click **"Shell"** in Render dashboard
2. Run: `python manage.py createsuperuser`
3. Enter username, email, password

**Admin URL**: `https://your-app.onrender.com/admin/` 🎉

---

## 📚 Full Documentation

See [RENDER_DEPLOY.md](file:///Users/shivaansh/accessibility-cms-wagtail/RENDER_DEPLOY.md) for complete step-by-step guide.

---

## 🆚 Netlify vs Render

| Feature | Netlify | Render |
|---------|---------|--------|
| Admin Interface | ❌ No | ✅ Yes |
| Database | ❌ Local only | ✅ PostgreSQL |
| Content Updates | Rebuild required | Instant via admin |
| Type | Static files | Full Django app |

---

**Ready to deploy!** You'll have full admin access online. 🚀
