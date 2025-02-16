# Setting Up Tailwind CSS and Auto Browser Reload in Django

This guide provides a step-by-step approach to setting up **Tailwind CSS** in a Django project along with **django-browser-reload** to enable automatic browser reloading when making changes to styles.

---

## **Step 1: Install Tailwind CSS for Django**
Run the following command to install Tailwind CSS support:
```bash
pip install django-tailwind
```

---

## **Step 2: Add Tailwind to Installed Apps**
Open `settings.py` and add `tailwind` to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # Other apps
    "tailwind",
]
```

---

## **Step 3: Initialize Tailwind App**
Run the following command to create a Tailwind app:
```bash
python3 manage.py tailwind init
```
This will create a new Django app named **theme** which will store Tailwind configurations, by hitting `enter` key on the keyboard leaving it empty.

***Open `settings.py` and add `theme` to `INSTALLED_APPS`:***
```python
INSTALLED_APPS = [
    # Other apps
    "tailwind",
    "theme",  # This is the default name for the Tailwind app
]
```

---

## **Step 4: Set Tailwind App in Django Settings**
In `settings.py`, add the following line:
```python
TAILWIND_APP_NAME = "theme"
```

---

## **Step 5: Install Tailwind Dependencies**
Run the following command to install Tailwind's required dependencies:
```bash
python3 manage.py tailwind install
```

---

## **Step 6: Start Tailwind Watcher**
To automatically compile Tailwind styles as you make changes, run:
```bash
python3 manage.py tailwind start
```

This will watch for changes and update the styles in real time.

---

## **Step 7: Link Tailwind CSS in Django Templates**
In your base template (`base.html`), add the compiled Tailwind CSS:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/dist/styles.css' %}">
```

---

## **Step 8: Install django-browser-reload for Auto Refresh**
To enable automatic browser refreshing, install:
```bash
pip install django-browser-reload
```

Then, add it to `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    # Other apps
    "django_browser_reload",
]
```

And add the middleware:
```python
MIDDLEWARE = [
    # Other middleware
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
```

---

## **Step 9: Add Browser Reload URL**
In your main `urls.py`, include:
```python
from django.urls import path, include

urlpatterns = [
    # Other URLs
    path("__reload__/", include("django_browser_reload.urls")),
]
```

---

## **Step 10: Include Reload Script in Templates**
In your `base.html`, inside the `<body>` tag, add:
```html
{% load django_browser_reload %}
{% django_browser_reload_script %}
```

---

## **Step 11: Run Django and Tailwind Together**
In one terminal tab, run:
```bash
python3 manage.py runserver
```

In another terminal tab, run:
```bash
python3 manage.py tailwind start
```

Now, when you modify styles, Tailwind will recompile the CSS, and the browser will **automatically refresh**.

---

## **Step 12: Build Tailwind for Production**
Once you're satisfied with your styles and ready for deployment, run:
```bash
python3 manage.py tailwind build
```
This generates an optimized CSS file for production.

---

## **Conclusion**
🎉 Your Django project is now set up with **Tailwind CSS** for styling and **django-browser-reload** for automatic browser refreshing! Happy coding! 🚀

