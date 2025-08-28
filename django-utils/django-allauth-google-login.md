# 🔐 Django Allauth Google Login Setup (MVT, TailwindCSS Styled)

A step-by-step guide for integrating and customizing Google login in a Django MVT app using Django-Allauth and Tailwind CSS.

---

## 📦 Prerequisites

- Django installed
- `django-allauth` installed
- Tailwind CSS set up for your project

```bash
pip install django-allauth
```

---

## ⚙️ 1. Add Required Settings

In `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
```

---

## 🌐 2. Set Up URLs

In `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    ...
    path('accounts/', include('allauth.urls')),
]
```

---

## 🗃️ 3. Run Migrations

```bash
python manage.py migrate
```

---

## 🔑 4. Set Up Google OAuth Credentials

1. Go to https://console.cloud.google.com
2. Create a project
3. Go to **APIs & Services → Credentials**
4. Create OAuth 2.0 Client ID
   - Application type: Web
   - Authorized JavaScript origins: `http://localhost:8000`
   - Authorized redirect URIs: `http://localhost:8000/accounts/google/login/callback/`

Copy:
- **Client ID**
- **Client Secret**

---

## 🔄 5. Create SocialApp in Django Admin

1. Visit `/admin/socialaccount/socialapp/add/`
2. Provider: `Google`
3. Name: `Newsjour`
4. Client ID: (paste from Google)
5. Secret Key: (paste from Google)
6. Add your current Site (e.g., `example.com` or `localhost:8000`)

---

## 🖼️ 6. Customize the Google Login Button

Use Tailwind + Google SVG:

```django
<a href="{% provider_login_url 'google' %}"
   class="inline-flex items-center px-5 py-2.5 bg-white text-gray-800 dark:bg-gray-900 dark:text-white rounded-lg shadow hover:shadow-md transition gap-3 border border-gray-300 dark:border-gray-700">
  <svg class="w-5 h-5" ...>...</svg> <!-- Google Icon -->
  Sign in with Google
</a>
```

---

## ⚠️ 7. Handle OAuth Errors

### Override Template: `authentication_error.html`

Path: `templates/socialaccount/authentication_error.html`

```html
{% extends "base.html" %}
{% block content %}
<div class="min-h-screen flex items-center justify-center bg-gray-100 dark:bg-gray-900 text-gray-900 dark:text-white">
  <div class="bg-white dark:bg-gray-800 p-8 rounded-xl shadow-md max-w-md w-full">
    <h2 class="text-xl font-bold text-center mb-4">Login Failed</h2>
    <p class="text-sm text-center mb-6">
      Something went wrong while signing in with Google. Try again or use another method.
    </p>
    <a href="{% url 'account_login' %}" class="bg-blue-600 text-white px-4 py-2 rounded-lg text-center block hover:bg-blue-700 transition">
      Try Again
    </a>
  </div>
</div>
{% endblock %}
```

✅ Also override `login_cancelled.html` similarly if needed.

---

## 🧼 8. Common Errors and Fixes

| Error | Fix |
|-------|-----|
| `SocialApp.DoesNotExist` | Ensure you’ve added a SocialApp in Django Admin and attached the current Site |
| `NoReverseMatch: 'socialaccount_login'` | Don’t use nonexistent route names — use `{% provider_login_url 'google' %}` |
| `SessionInterrupted` / `UpdateError` | Run `python manage.py clearsessions` or switch to cookie-based sessions |
| Ugly login error page | Create `authentication_error.html` in `templates/socialaccount/` |
| Template not picked up | Ensure `TEMPLATES['DIRS']` in `settings.py` includes your `templates/` directory |

---

## 💡 Bonus Tips

- You can override allauth templates: `account/login.html`, `signup.html`, etc.
- Use `ACCOUNT_SIGNUP_FIELDS` and `ACCOUNT_LOGIN_METHODS` instead of deprecated `ACCOUNT_USERNAME_REQUIRED` and `ACCOUNT_AUTHENTICATION_METHOD`.

---

## ✅ Done!

You're now ready to use Google login in your Django app with clean design, dark mode, and a fully integrated auth flow. 🎉
