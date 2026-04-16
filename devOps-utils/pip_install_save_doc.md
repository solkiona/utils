# Automatic Python Dependency Tracking with pip-install-save

This document explains how to automatically track Python dependencies in your project and update `requirements.txt` whenever you install new packages using a custom bash function.

---

## 1. Overview

When using `pip install`, new dependencies are not automatically added to `requirements.txt`. Forgetting to update this file can cause inconsistencies, especially in deployments or collaborative projects.

The `pip-install-save` function:

1. Installs the requested package(s) in the **current virtual environment**.
2. Appends **new packages** to `requirements.txt`.
3. Avoids duplicating existing packages.
4. Keeps `requirements.txt` up-to-date automatically.

---

## 2. Setup Instructions

### Step 1: Open your `~/.bashrc`

```bash
nano ~/.bashrc
```

### Step 2: Add the `pip-install-save` function

```bash
# Wrapper for pip install that appends new packages to requirements.txt
pip-install-save() {
    # Install packages
    pip install "$@"

    # Ensure requirements.txt exists
    if [ ! -f "requirements.txt" ]; then
        pip freeze > requirements.txt
        echo "requirements.txt created with installed packages."
        return
    fi

    # Freeze current environment to a temporary file
    pip freeze > /tmp/current_requirements.txt

    # Append only new packages that aren't already in requirements.txt
    grep -Fxv -f requirements.txt /tmp/current_requirements.txt >> requirements.txt

    # Cleanup
    rm /tmp/current_requirements.txt

    echo "requirements.txt updated with new packages."
}
```

### Step 3: Reload your bash configuration

```bash
source ~/.bashrc
```

### Step 4: Activate your virtual environment

```bash
source /path/to/venv/bin/activate
```

### Step 5: Use the function to install packages

Instead of:

```bash
pip install package_name
```

Use:

```bash
pip-install-save requests
pip-install-save django pillow
```

- Only new packages are appended to `requirements.txt`.
- Existing packages are **not duplicated**.
- Works in the **current directory** (where `requirements.txt` is located).

---

## 3. How It Works

1. The function freezes your current environment (`pip freeze`) to a temporary file.
2. Compares it with your existing `requirements.txt`.
3. Appends only packages **not yet listed**.
4. Ensures `requirements.txt` stays clean and updated automatically.

---

## 4. Example Usage

Initial `requirements.txt`:

```
Django==4.2.5
requests==2.31.0
```

Run:

```bash
pip-install-save pillow
```

Resulting `requirements.txt`:

```
Django==4.2.5
requests==2.31.0
Pillow==10.0.0
```

- `Pillow` was added automatically.
- `Django` and `requests` were not duplicated.

---

## 5. Testing

Install a small test package to ensure it works:

```bash
pip-install-save colorama
```

Check `requirements.txt` to confirm it was appended correctly.

Test package:

```bash
python -c "import colorama; print(colorama.Fore.GREEN + 'Test successful!' + colorama.Style.RESET_ALL)"
```

---

## 6. Benefits

- Keeps `requirements.txt` **always up-to-date**.
- Reduces errors in deployments or CI/CD pipelines.
- Works seamlessly with virtual environments.
- Avoids duplicates and keeps the file clean.

---

## 7. Notes

- Ensure you are in the **project root directory** when using the function.
- Make sure your **virtual environment is active**.
- For very large environments, appending is faster than rewriting the entire