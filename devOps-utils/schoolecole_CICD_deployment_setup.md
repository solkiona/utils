# 🚀 Schoolecole — Full GitHub CI/CD Deployment Setup (Server + GitHub Actions)

This document details the full process used to successfully automate deployment for the **Schoolecole Django project**, from GitHub to the production server via SSH and systemd service restarts.

---

## 🧩 Overview

The deployment pipeline:
1. A **push to the master branch** on GitHub triggers a GitHub Action.
2. The **GitHub Action connects to the production server via SSH** using a secure deploy key.
3. The server:
   - Pulls the latest code.
   - Runs migrations and collects static files.
   - Restarts `uwsgi` and `nginx` automatically (with no password prompts).

---

## 🧰 Prerequisites

Ensure your production server has:
- Ubuntu/Debian-based Linux
- Python 3 and `venv` configured
- Django project setup and working manually
- Git installed and linked to the same repo
- `uwsgi` and `nginx` already configured and running

---

## 🛠️ Step 1 — Generate a Deploy Key Pair

On your **server**, generate a dedicated SSH key pair for GitHub deployments:

```bash
mkdir -p ~/.ssh
ssh-keygen -t ed25519 -f ~/.ssh/github-deploy -C "github-deploy-key"
```

This creates two files:

| File | Purpose | Safe to Share? |
|------|----------|----------------|
| `~/.ssh/github-deploy` | Private key (used by your server to connect to GitHub) | ❌ No |
| `~/.ssh/github-deploy.pub` | Public key (added to GitHub repository) | ✅ Yes |

---

## 🔐 Step 2 — Add the Public Key to GitHub

1. Copy the contents of your public key:

   ```bash
   cat ~/.ssh/github-deploy.pub
   ```

2. Go to your GitHub repository:
   - **Settings → Deploy keys → Add deploy key**
   - Paste the public key
   - Check ✅ **Allow write access**

---

## 🧭 Step 3 — Configure SSH on the Server

Open or create your SSH config file:

```bash
nano ~/.ssh/config
```

Add this block:

```bash
Host github-schoolecole
    HostName github.com
    User git
    IdentityFile ~/.ssh/github-deploy
    IdentitiesOnly yes
```

### 🔍 Explanation

- `Host github-schoolecole`: an alias for convenience (used later in Git commands).
- `IdentityFile ~/.ssh/github-deploy`: points to your **private key**.
- `IdentitiesOnly yes`: ensures SSH uses only this key.

Now test your connection:

```bash
ssh -T github-schoolecole
```

Expected output:
```
Hi Uobis! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 🧱 Step 4 — Link Git Repository on the Server

In your project directory (e.g., `/home/www/schoolecole`):

```bash
git remote set-url origin git@github-schoolecole:Uobis/schoolecole.git
```

Check:
```bash
git remote -v
```

Output:
```
origin  git@github-schoolecole:Uobis/schoolecole.git (fetch)
origin  git@github-schoolecole:Uobis/schoolecole.git (push)
```

---

## ⚙️ Step 5 — Allow `sudo systemctl` Without Password

Edit sudoers:

```bash
sudo visudo
```

Add:

```bash
uobis ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart uwsgi.service
uobis ALL=(ALL) NOPASSWD: /usr/bin/systemctl restart nginx.service
uobis ALL=(ALL) NOPASSWD: /usr/bin/supervisorctl restart *
```

✅ Important: Using `.service` (e.g., `uwsgi.service`) **prevents password prompts**.

---

## ⚡ Step 6 — Create GitHub Workflow File

In your project root, create:

```
.github/workflows/deploy.yml
```

Add the following:

```yaml
name: Deploy Schoolecole

on:
  push:
    branches:
      - master

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Deploy to Server
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.SERVER_IP }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SERVER_SSH_KEY }}
          script: |
            echo "Starting deployment..."
            cd /home/www/schoolecole
            git fetch origin master
            git reset --hard origin/master
            echo "Code updated."

            echo "Applying migrations..."
            source venv/bin/activate
            python manage.py migrate --noinput
            python manage.py collectstatic --noinput

            echo "Restarting services..."
            sudo /usr/bin/systemctl restart uwsgi.service
            sudo /usr/bin/systemctl restart nginx.service

            echo "Deployment completed successfully!"
```

---

## 🧾 Step 7 — Add GitHub Secrets

In your GitHub repository:

**Settings → Secrets → Actions** → Add new repository secrets:

| Secret | Description |
|--------|-------------|
| `SERVER_IP` | Your server IP |
| `SERVER_USER` | SSH username (e.g., `uobis`) |
| `SERVER_SSH_KEY` | Contents of your private key (`~/.ssh/github-deploy`) |

To get the private key:
```bash
cat ~/.ssh/github-deploy
```

---

## 🧰 Step 8 — File Permissions

```bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/github-deploy
chmod 600 ~/.ssh/authorized_keys
```

---

## ✅ Step 9 — Test the Deployment

1. Push to the `master` branch.
2. Check GitHub → **Actions** tab.
3. You should see:
   ```
   Deployment completed successfully!
   ```

Verify services:

```bash
sudo systemctl status uwsgi.service
sudo systemctl status nginx.service
```

---

## 🧩 Troubleshooting

| Issue | Fix |
|-------|-----|
| `sudo: a password is required` | Ensure NOPASSWD lines include full `.service` names |
| `Permission denied (publickey)` | Verify your `~/.ssh/config` points to the correct private key |
| `GitHub Action fails at restart` | Check sudoers configuration |
| `Repository not found` | Make sure deploy key has write access |

---

## 🧭 Checklist

- [x] Deployment completes successfully  
- [x] No password prompts during systemctl restart  
- [x] uwsgi and nginx restart automatically  
- [x] Migrations apply successfully  
- [x] Static files collected successfully  

---

## 🎯 Summary

✅ Secure SSH key authentication  
✅ GitHub deploy key integration  
✅ Passwordless service restarts  
✅ Automated Django migrations + static collection  
✅ Full CI/CD pipeline via GitHub Actions  

---

**Author:** Uobis (Adule Solomon Onwukwe)  
**Project:** Schoolecole  
**Stack:** GitHub Actions • Debian • Django • uwsgi • nginx
