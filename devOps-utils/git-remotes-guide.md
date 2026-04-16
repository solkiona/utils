# Git Remotes Setup for Personal & Company Accounts

## Markdown Reference Guide

This guide helps you push your project to Vercel using your personal GitHub, while keeping your company GitHub added as a backup remote.

## 1. Initialize Git (if not already)

```bash
git init
```

## 2. Add Your Personal GitHub as the Primary Remote

This is the remote Vercel will connect to for now.

```bash
git remote add origin https://github.com/solkiona/AchramApp.git
git branch -M main
git push -u origin main
```

## 3. Add Your Company GitHub Repo as a Backup Remote

Replace the URL with your company repo URL:

```bash
git remote add uobis https://github.com/UobisTech/AchramApp.git
```

## 4. Push to Either Remote

### Push to Personal GitHub

```bash
git push origin main
```

### Push to Company GitHub

```bash
git push uobis main
```

## 5. Check Your Remotes Anytime

```bash
git remote -v
```

You should see:

```
origin   https://github.com/solkiona/AchramApp.git
uobis    https://github.com/UobisTech/AchramApp.git
```

## 6. Workflow Recommendation

1. Push to `origin` (personal) for testing on Vercel.
2. After confirming everything works, push the same commits to `uobis` (company).

This keeps your workflow clean and safe.

## 7. Change Default Remote (Optional)

If later you want the company repo to be the default:

```bash
git remote remove origin
git remote rename uobis origin
```