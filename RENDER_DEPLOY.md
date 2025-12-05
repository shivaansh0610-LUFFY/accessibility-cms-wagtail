# 🚀 Render Deployment Guide - Wagtail Accessibility CMS

Complete guide to deploy your Wagtail CMS on Render with full admin access.

## Prerequisites

- GitHub account
- Render account (free tier) - Sign up at https://render.com/
- Git installed locally

---

## Step 1: Push to GitHub

### 1.1 Commit All Changes

```bash
cd /Users/shivaansh/accessibility-cms-wagtail
git add .
git commit -m "Configure for Render deployment with PostgreSQL"
git push origin main
```

If you haven't set up Git yet:
```bash
git init
git add .
git commit -m "Initial commit - Render deployment ready"
git remote add origin https://github.com/YOUR_USERNAME/accessibility-cms-wagtail.git
git branch -M main
git push -u origin main
```

---

## Step 2: Deploy on Render

### 2.1 Create New Web Service

1. Log in to https://dashboard.render.com/
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account (if not already connected)
4. Select the `accessibility-cms-wagtail` repository
5. Click **"Connect"**

### 2.2 Configure Web Service

Render will auto-detect your `render.yaml` configuration, but verify these settings:

| Setting | Value |
|---------|-------|
| **Name** | `accessibility-cms-wagtail` (or your choice) |
| **Runtime** | Python 3 |
| **Build Command** | `./build.sh` |
| **Start Command** | `gunicorn mysite.wsgi:application` |
| **Plan** | Free |

### 2.3 Add Environment Variables

Click **"Advanced"** → **"Add Environment Variable"** and add:

| Key | Value | Notes |
|-----|-------|-------|
| `PYTHON_VERSION` | `3.11.0` | Python version |
| `DJANGO_SETTINGS_MODULE` | `mysite.settings.production` | Use production settings |
| `SECRET_KEY` | *Generate below* | Django secret key |
| `ALLOWED_HOSTS` | `.onrender.com` | Your Render domain |

**Generate SECRET_KEY:**
```bash
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 2.4 Create PostgreSQL Database

1. In Render dashboard, click **"New +"** → **"PostgreSQL"**
2. Configure:
   - **Name**: `accessibility-cms-db`
   - **Database**: `accessibility_cms`
   - **User**: `accessibility_user`
   - **Plan**: Free
3. Click **"Create Database"**
4. Wait for database to provision (~2 minutes)

### 2.5 Link Database to Web Service

1. Go back to your Web Service settings
2. Scroll to **"Environment Variables"**
3. Click **"Add Environment Variable"**
4. Add:
   - **Key**: `DATABASE_URL`
   - **Value**: Click "Select from database" → Choose `accessibility-cms-db`
   - This auto-populates the PostgreSQL connection URL

### 2.6 Deploy

1. Click **"Create Web Service"**
2. Render will automatically:
   - Clone your repository
   - Run `build.sh` (install deps, migrate, collect static)
   - Start gunicorn server
3. Wait 5-10 minutes for first deployment

---

## Step 3: Create Superuser (Admin Account)

After deployment completes:

### 3.1 Open Render Shell

1. In your Web Service dashboard, click **"Shell"** tab
2. Click **"Launch Shell"**
3. Run:
   ```bash
   python manage.py createsuperuser
   ```
4. Enter:
   - **Username**: (your choice, e.g., `admin`)
   - **Email**: your email
   - **Password**: strong password (enter twice)

---

## Step 4: Access Your Site

### 4.1 Public Site

Your site is live at: `https://your-app-name.onrender.com`

### 4.2 Admin Interface 🎉

Access the admin at: `https://your-app-name.onrender.com/admin/`

Login with the superuser credentials you just created!

---

## Step 5: Update Wagtail Base URL

1. In Render dashboard, add environment variable:
   - **Key**: `WAGTAILADMIN_BASE_URL`
   - **Value**: `https://your-app-name.onrender.com` (your actual URL)
2. This ensures email notifications and previews work correctly

---

## Custom Domain (Optional)

### Add Your Domain

1. In Web Service settings, go to **"Settings"** → **"Custom Domain"**
2. Click **"Add Custom Domain"**
3. Enter your domain (e.g., `accessibility-audit.com`)
4. Follow DNS configuration instructions
5. Update `ALLOWED_HOSTS` environment variable:
   ```
   .onrender.com,accessibility-audit.com,www.accessibility-audit.com
   ```

Render automatically provisions SSL certificates via Let's Encrypt.

---

## Redeployment Workflow

### Automatic Deployments

Render auto-deploys when you push to `main` branch:

```bash
# Make changes locally
git add .
git commit -m "Update content or code"
git push origin main
# Render automatically rebuilds and deploys
```

### Manual Deploy

In Render dashboard:
1. Go to your Web Service
2. Click **"Manual Deploy"** → **"Deploy latest commit"**

---

## Database Management

### View Database

1. Go to your PostgreSQL database in Render dashboard
2. Click **"Connect"** → **"External Connection"**
3. Use provided credentials with tools like pgAdmin or DBeaver

### Backup Database

Render Free tier includes:
- Daily automatic backups (retained for 7 days)
- Manual backups via dashboard

### Run Migrations

After model changes:
```bash
# In Render Shell
python manage.py makemigrations
python manage.py migrate
```

Or add to `build.sh` for automatic migrations on deploy.

---

## Troubleshooting

### Build Fails

**Check build logs** in Render dashboard:
- Look for Python dependency errors
- Verify `build.sh` has execute permissions
- Check PostgreSQL connection

### Static Files Not Loading

1. Verify `collectstatic` runs in `build.sh`
2. Check whitenoise is in `MIDDLEWARE`
3. Look for 404 errors in browser console

### Database Connection Errors

1. Verify `DATABASE_URL` environment variable is set
2. Check PostgreSQL database is running
3. Ensure `dj-database-url` is in `requirements.txt`

### Admin Not Accessible

1. Verify superuser was created
2. Check URL is correct: `/admin/` (with trailing slash)
3. Ensure migrations ran successfully

---

## Important Notes

### Free Tier Limitations

- **Spin down after 15 min inactivity** (first request takes ~30s to wake)
- **750 hours/month** (enough for one service)
- **PostgreSQL**: 90-day expiration (export data before)

### Upgrade for Production

For production sites, consider:
- **Starter Plan** ($7/month) - No spin down, better performance
- **PostgreSQL Standard** ($7/month) - No expiration, daily backups

---

## Configuration Summary

| Component | Value |
|-----------|-------|
| **Platform** | Render |
| **Runtime** | Python 3.11 |
| **Database** | PostgreSQL (free tier) |
| **Web Server** | Gunicorn |
| **Static Files** | WhiteNoise |
| **SSL** | Automatic (Let's Encrypt) |
| **Deployments** | Automatic from GitHub |

---

## Next Steps

- ✅ Access admin interface online
- ✅ Add audit records via admin
- ✅ Customize site content
- ✅ Set up custom domain (optional)
- ✅ Configure email settings for notifications
- ✅ Add team members to Wagtail admin

---

## Support Resources

- 📖 [Render Docs](https://render.com/docs)
- 📖 [Wagtail Docs](https://docs.wagtail.org/)
- 🔧 [render.yaml](file:///Users/shivaansh/accessibility-cms-wagtail/render.yaml)
- 🔧 [build.sh](file:///Users/shivaansh/accessibility-cms-wagtail/build.sh)

---

## Success! 🎉

Your Wagtail CMS is now live on Render with:
- ✅ Full admin interface access online
- ✅ PostgreSQL database
- ✅ Automatic deployments from GitHub
- ✅ Free SSL certificates
- ✅ Professional hosting infrastructure

**Admin URL**: `https://your-app-name.onrender.com/admin/`

Enjoy managing your accessibility audit dashboard! 🚀
