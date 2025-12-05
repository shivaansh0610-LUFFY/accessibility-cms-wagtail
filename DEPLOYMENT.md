# Netlify Deployment Guide for Wagtail Accessibility CMS

This guide walks you through deploying your Wagtail accessibility audit dashboard to Netlify as a static site.

## Prerequisites

- GitHub account
- Netlify account (free tier works)
- Git installed locally

## Step 1: Prepare Your Repository

### 1.1 Initialize Git Repository (if not already done)

```bash
cd /Users/shivaansh/accessibility-cms-wagtail
git init
git add .
git commit -m "Initial commit - Wagtail accessibility CMS ready for Netlify"
```

### 1.2 Create GitHub Repository

1. Go to [GitHub](https://github.com/new)
2. Create a new repository named `accessibility-cms-wagtail`
3. **Do NOT** initialize with README, .gitignore, or license (already exists locally)
4. Click "Create repository"

### 1.3 Push to GitHub

```bash
git remote add origin https://github.com/YOUR_USERNAME/accessibility-cms-wagtail.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy to Netlify

### 2.1 Connect Repository

1. Log in to [Netlify](https://app.netlify.com/)
2. Click **"Add new site"** → **"Import an existing project"**
3. Choose **"Deploy with GitHub"**
4. Authorize Netlify to access your GitHub account
5. Select the `accessibility-cms-wagtail` repository

### 2.2 Configure Build Settings

Netlify will auto-detect the `netlify.toml` file, but verify these settings:

- **Build command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate && python manage.py build`
- **Publish directory**: `build/`
- **Python version**: `3.11` (set in netlify.toml)

### 2.3 Set Environment Variables

Click **"Add environment variables"** and add:

| Key | Value |
|-----|-------|
| `DJANGO_SETTINGS_MODULE` | `mysite.settings.production` |
| `DJANGO_SECRET_KEY` | Generate a secure random key (see below) |

**Generate a secure secret key:**
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 2.4 Deploy

1. Click **"Deploy site"**
2. Wait for the build to complete (5-10 minutes first time)
3. Your site will be live at `https://random-name-12345.netlify.app`

## Step 3: Custom Domain (Optional)

### 3.1 Add Custom Domain

1. In Netlify dashboard, go to **"Domain settings"**
2. Click **"Add custom domain"**
3. Enter your domain (e.g., `accessibility-audit.com`)
4. Follow DNS configuration instructions

### 3.2 Enable HTTPS

Netlify automatically provisions SSL certificates via Let's Encrypt. This happens automatically once DNS is configured.

## Step 4: Redeployment Workflow

Since this is a static site, you need to rebuild and redeploy for any content changes:

### 4.1 Update Content Locally

1. Run your local development server:
   ```bash
   python manage.py runserver
   ```
2. Access admin at `http://localhost:8000/admin/`
3. Add/edit audit records and pages
4. Commit changes to your database

### 4.2 Push Changes

```bash
git add .
git commit -m "Update audit data"
git push origin main
```

### 4.3 Automatic Deployment

Netlify automatically rebuilds and deploys when you push to the `main` branch.

## Step 5: Verify Deployment

1. Visit your Netlify URL
2. Check that the homepage loads
3. Verify audit data displays correctly
4. Test navigation between pages
5. Confirm static assets (CSS, images) load properly

## Troubleshooting

### Build Fails

**Check build logs** in Netlify dashboard:
- Look for Python dependency errors
- Verify all migrations are committed
- Ensure `db.sqlite3` is committed (contains your audit data)

### Static Files Not Loading

1. Check `STATIC_ROOT` in settings
2. Verify `collectstatic` runs in build command
3. Check browser console for 404 errors

### Pages Not Building

1. Ensure all Page models have `@register` and `@build` decorators
2. Check that pages are published in Wagtail admin
3. Review build logs for wagtail-bakery errors

## Important Limitations

⚠️ **Static Site Constraints:**
- No admin interface on production (manage content locally)
- No forms or dynamic features
- Database changes require rebuild
- Best for read-only content display

## Support

For issues:
- Check [Netlify docs](https://docs.netlify.com/)
- Review [wagtail-bakery docs](https://github.com/wagtail/wagtail-bakery)
- Check build logs in Netlify dashboard

## Next Steps

- Set up custom domain
- Configure build notifications
- Add deploy previews for pull requests
- Set up analytics (Netlify Analytics or Google Analytics)
