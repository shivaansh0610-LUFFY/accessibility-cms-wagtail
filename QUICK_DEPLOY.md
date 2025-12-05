# 🚀 Quick Deploy Guide - Netlify

Your Wagtail accessibility CMS is **ready for Netlify deployment!**

## ✅ What's Been Configured

- ✅ `netlify.toml` with automated build pipeline
- ✅ Production settings with whitenoise compression
- ✅ `requirements.txt` updated with deployment dependencies
- ✅ Static build tested successfully (4.8 MB)
- ✅ Build output: `build/` directory ready to deploy

## 🎯 Deploy in 3 Steps

### 1️⃣ Push to GitHub

```bash
cd /Users/shivaansh/accessibility-cms-wagtail
git init
git add .
git commit -m "Ready for Netlify deployment"
git remote add origin https://github.com/YOUR_USERNAME/accessibility-cms-wagtail.git
git branch -M main
git push -u origin main
```

### 2️⃣ Connect to Netlify

1. Go to https://app.netlify.com/
2. Click **"Add new site"** → **"Import an existing project"**
3. Choose **GitHub** and select your repository
4. Netlify auto-detects `netlify.toml` ✨

### 3️⃣ Set Environment Variable

Add in Netlify dashboard:
- **Key**: `DJANGO_SECRET_KEY`
- **Value**: Generate with:
  ```bash
  python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
  ```

Click **"Deploy site"** and you're live! 🎉

---

## 📁 Build Output

```
build/
├── index.html (6.8 KB) - Your homepage
└── static/ (4.8 MB) - All CSS, JS, images
```

---

## ⚠️ Important: Static Site Limitations

- **No admin on Netlify** - Manage content locally
- **Rebuild required** - Push to GitHub triggers redeploy
- **Read-only content** - Perfect for displaying audit data

---

## 📚 Full Documentation

- **[DEPLOYMENT.md](file:///Users/shivaansh/accessibility-cms-wagtail/DEPLOYMENT.md)** - Complete deployment guide
- **[walkthrough.md](file:///Users/shivaansh/.gemini/antigravity/brain/18e39507-f85d-4638-b7b9-b1fe2bc5dede/walkthrough.md)** - All changes made

---

## 🧪 Test Locally

```bash
# Build static site
python3 manage.py build

# Preview with simple server
cd build
python3 -m http.server 8080
# Visit http://localhost:8080
```

---

**Ready to deploy!** Follow the 3 steps above to go live on Netlify's global CDN. 🌍
