# Django Project Vercel Deployment Guide

This document outlines the steps taken to configure the Django project for deployment on Vercel.

## Configuration Summary

### 1. Settings Configuration (`myapp1/settings.py`)
The settings file already contained excellent Vercel-ready configurations:

- **Environment-based configuration**: Uses environment variables for `SECRET_KEY`, `DEBUG`, and `DATABASE_URL`
- **Vercel-specific ALLOWED_HOSTS**: Automatically includes `.vercel.app` and `*` domains
- **Whitenoise middleware**: Added for efficient static file serving
- **CSRF trusted origins**: Configured for Vercel domains
- **Proxy settings**: `SECURE_PROXY_SSL_HEADER` and `USE_X_FORWARDED_HOST` enabled
- **Database flexibility**: Supports both SQLite (development) and PostgreSQL (Vercel Postgres)
- **Static files optimization**: Uses `whitenoise.storage.CompressedStaticFilesStorage`
- **Proper directory configuration**: `STATIC_ROOT`, `STATICFILES_DIRS`, `MEDIA_ROOT` set correctly

### 2. Vercel Configuration (`vercel.json`)
Updated to properly handle Django requests:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "15mb",
        "runtime": "python3.12"
      }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/media/(.*)",
      "dest": "/media/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/api/index.py"
    }
  ],
  "env": {
    "DJANGO_SETTINGS_MODULE": "myapp1.settings",
    "PYTHONPATH": "."
  }
}
```

### 3. Entry Point (`api/index.py`)
Already correctly configured for Django:
- Sets `DJANGO_SETTINGS_MODULE` to `myapp1.settings`
- Implements automatic static file collection on startup
- Exposes the WSGI application as both `application` and `app` (for Vercel compatibility)

### 4. Dependencies (`requirements.txt`)
Includes all necessary packages:
- `Django` - Core framework
- `whitenoise` - Static file serving (essential for Vercel)
- `psycopg[binary]` - PostgreSQL adapter (for Vercel Postgres)
- `Pillow` - Image handling (for user uploads)

### 5. Vercel Ignore (`.vercelignore`)
Created to prevent uploading unnecessary files:
- Excludes development files, caches, logs, IDE files, etc.
- Reduces deployment size and improves build times

## Verification

✅ **Static Files Collection**: Successfully tested with `python manage.py collectstatic --dry-run --noinput`
✅ **Django Import**: Confirmed Django can be imported with the correct settings module
✅ **Configuration Validation**: All settings load properly

## Deployment Instructions

1. **Push to GitHub**: Ensure your code is in a GitHub repository
2. **Import to Vercel**: 
   - Go to vercel.com
   - Click "New Project"
   - Import your GitHub repository
   - Vercel should automatically detect the Python/Django project
3. **Environment Variables**: Set in Vercel Dashboard:
   - `DJANGO_SECRET_KEY`: Your Django secret key
   - `DJANGO_DEBUG`: Set to "False" for production
   - `DATABASE_URL`: PostgreSQL connection string (if using Vercel Postgres)
   - Any other app-specific environment variables

## Important Notes

### Media Files Handling
⚠️ **Warning**: Vercel has a read-only filesystem. User-uploaded files (like student profile images) will not persist between deployments or scale across serverless functions.

For production use with persistent file uploads, consider:
- Using cloud storage (AWS S3, Google Cloud Storage, Cloudinary)
- Implementing external storage backends in Django
- Or accepting that uploads are temporary (suitable for demo applications)

### Database
- For development: SQLite works fine
- For production: Use Vercel Postgres or another external database service
- The settings.py already handles automatic switching based on `DATABASE_URL`

### Static Files
- Whitenoise will serve compressed static files efficiently
- Static files are collected during the Vercel build process
- No additional configuration needed for CSS, JS, images

## Troubleshooting

1. **Build fails**: Check Vercel build logs for Python/pip errors
2. **Static files not loading**: Verify `STATIC_URL` and whitenoise middleware
3. **Database connection errors**: Check `DATABASE_URL` environment variable
4. **500 errors**: Check Vercel function logs for Django tracebacks

## Files Modified/Added

- `vercel.json` - Updated for proper Django routing
- `.vercelignore` - Created to optimize deployment
- `VERCEL_DEPLOYMENT.md` - This documentation file

The project is now ready for deployment on Vercel!