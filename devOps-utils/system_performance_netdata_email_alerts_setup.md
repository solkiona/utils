# Netdata — Full Setup Guide for Newsjour (system metrics + email alerts)

> Complete step-by-step reference: install Netdata, expose at `/admin/metrics/` via Nginx, secure access, and configure email alerts via Gmail (msmtp).

---

## Overview

This document covers a full, reproducible setup to monitor your Newsjour server with **Netdata** (system metrics) and send **email alerts** using **Gmail (msmtp)**. It includes the reverse proxy configuration so the Netdata web UI is available at `https://www.newsjour.com/admin/metrics/` and describes how to restrict access.

This guide assumes a Debian/Ubuntu server where you already run Newsjour (Django) behind Nginx.

---

## Prerequisites

- Debian/Ubuntu root or sudo access
- Nginx installed and configured for `www.newsjour.com` (HTTPS recommended)
- A Gmail account with **2-Step Verification enabled** and an **App Password** (16 chars)
- Basic familiarity with editing files and restarting services

---

## 1. Install Netdata (official installer)

Run the official installer (recommended). Open a shell and run:

```bash
# preferred (direct execution)
sudo bash <(curl -Ss https://my-netdata.io/kickstart.sh)
```

**If your shell complains about `/dev/fd`** (e.g. `bash: /dev/fd/63: No s3uch file or directory`), use the download-then-run approach:

```bash
curl -Ss https://my-netdata.io/kickstart.sh -o kickstart.sh
chmod +x kickstart.sh
sudo ./kickstart.sh
```

## Latest Install Netdata (official website)

```bash
wget -O /tmp/netdata-kickstart.sh https://my-netdata.io/kickstart.sh
sh /tmp/netdata-kickstart.sh

```

During install you may be prompted about AppArmor for optional pieces; choose `No` if you want fewer permission issues.

### Verify Netdata

```bash
sudo systemctl status netdata
# Check the web UI (default port)
# http://YOUR_SERVER_IP:19999
```

Netdata runs as a systemd service (`netdata`) and collects system metrics in memory.

---

## 2. Basic Netdata configuration

Files you will use:

- `/etc/netdata/netdata.conf` — global Netdata config
- `/etc/netdata/health_alarm_notify.conf` — notification (email/Slack/etc.) settings
- `/etc/netdata/health.d/` — health check (alarm) definitions

To enable health alarms globally, ensure `/etc/netdata/netdata.conf` contains:

```ini
[health]
    enabled = yes
```

---

## 3. Expose Netdata at `https://www.newsjour.com/admin/metrics/` via Nginx

By default Netdata serves on port `19999`. We’ll use Nginx to proxy requests for `/admin/metrics/` to the Netdata UI.

**Edit your Newsjour Nginx site config** (example path: `/etc/nginx/sites-available/newsjour`), inside the `server { ... }` block add:

```nginx
location /admin/metrics/ {
    proxy_pass http://127.0.0.1:19999/;
    proxy_http_version 1.1;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    # Buffers for streaming charts
    proxy_buffers 16 64k;
    proxy_buffer_size 128k;

    # Disable caching
    proxy_no_cache 1;
    proxy_cache_bypass 1;
}
```

**Test & reload Nginx**:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Now you can browse `https://www.newsjour.com/admin/metrics/` and see Netdata UI. **Important:** Nginx proxying bypasses Django authentication — access to `/admin/metrics/` will not automatically require Django admin login.

---

## 4. Secure the Netdata UI (recommended)

You have two main options to restrict access:

### Option A — Nginx Basic Auth (simple & reliable)

1. Install `htpasswd` utility:

```bash
sudo apt update
sudo apt install -y apache2-utils
```

2. Create password file (example user `adminmetrics`):

```bash
sudo htpasswd -c /etc/nginx/.netdata_admin adminmetrics
# Enter a strong password when prompted
```

3. Update the location block to require auth (add these lines inside `location /admin/metrics/ { ... }`):

```nginx
    auth_basic "Restricted Access";
    auth_basic_user_file /etc/nginx/.netdata_admin;
```

4. Reload Nginx:

```bash
sudo nginx -t
sudo systemctl reload nginx
```

Now visiting `/admin/metrics/` will prompt for the HTTP basic auth credentials.

> **Note:** This is independent of Django admin login. It's simple and effective for restricting access to admins.

### Option B — Proxy via Django (superuser-only) — advanced

If you **must** require Django superuser auth (so that only Django superusers see the page), you can implement a Django view at `/admin/metrics/` that: checks `request.user.is_authenticated` and `request.user.is_superuser` and then proxies Netdata responses (server-side). This has drawbacks:

- Adds overhead on Django (proxying large chart resources)
- More complex to implement and maintain

I recommend **Option A (Nginx Basic Auth)** for simplicity and reliability on resource-constrained servers.

---

## 5. Install & configure msmtp to send emails via Gmail

Netdata uses a local `sendmail` binary (or a configured command) to send email notifications. `msmtp` is a lightweight choice.

### Install msmtp

```bash
sudo apt update
sudo apt install -y msmtp msmtp-mta ca-certificates
```

If prompted about AppArmor during install, you may answer `No` to avoid permission complications.

### Create system-wide config `/etc/msmtprc`

```bash
sudo nano /etc/msmtprc
```

Paste the configuration (replace placeholders):

```ini
# Netdata Gmail SMTP
defaults
auth           on
tls            on
tls_trust_file /etc/ssl/certs/ca-certificates.crt
logfile        /var/log/msmtp.log

account gmail
host smtp.gmail.com
port 587
from your_email@gmail.com
user your_email@gmail.com
password your_gmail_app_password

account default : gmail
```

Important:

- You **must** use a Gmail App Password (16-char) — create one at your Google Account -> Security -> App Passwords after enabling 2-Step Verification.

Set file permissions:

```bash
sudo chmod 600 /etc/msmtprc
```

### Test msmtp

```bash
echo "Test email from Netdata" | msmtp --file=/etc/msmtprc recipient@example.com
```

If you get the email, msmtp is working.

If you see `account default not found` when running `msmtp` without `--file`, create a per-user `~/.msmtprc` or explicitly point to `/etc/msmtprc` in commands and configs.

---

## 6. Configure Netdata to use msmtp explicitly

Edit Netdata notification config:

```bash
sudo nano /etc/netdata/health_alarm_notify.conf
```

Set these values (replace email address):

```ini
SEND_EMAIL="YES"
DEFAULT_RECIPIENT_EMAIL="admin@newsjour.com"

# Explicit msmtp command path (confirm with `which msmtp`)
EMAIL_CMD="/usr/bin/msmtp --file=/etc/msmtprc -t"
```

> On some Netdata versions the variable name may be `SENDMAIL` or `EMAIL_CMD`. If `EMAIL_CMD` is ignored, try setting `SENDMAIL` to the full command: `SENDMAIL="/usr/bin/msmtp --file=/etc/msmtprc -t"`.

Save and restart Netdata:

```bash
sudo systemctl restart netdata
```

---

## 7. Add health checks (alerts)

Create a custom health file for Newsjour (CPU, RAM, Disk, Network):

```bash
sudo nano /etc/netdata/health.d/newsjour_server.conf
```

Example content — tune thresholds for your server:

```ini
# CPU usage
template:      system.cpu
      on:     system.cpu
    lookup:   average -1m unaligned of user
    units:    %
    every:    10s
    warn:     $this > 75
    crit:     $this > 90
    info:     CPU usage too high

# Memory available (bytes)
template:      mem.available
      on:     system.ram
    lookup:   available
    units:    bytes
    every:    10s
    warn:     $this < 500MB
    crit:     $this < 200MB
    info:     Low available RAM

# Disk usage root partition
template:      disk_space
      on:     disk.space
    lookup:   used
    units:    %
    every:    1m
    warn:     $this > 80
    crit:     $this > 90
    info:     Disk usage high

# Network throughput example (eth0)
template:      net.eth0.in
      on:     net.eth0
    lookup:   kbps_recv
    units:    kbps
    every:    1m
    warn:     $this > 10000
    crit:     $this > 20000
    info:     Incoming network traffic high
```

Save the file and restart Netdata:

```bash
sudo systemctl restart netdata
```

---

## 8. Test notifications

Find and run Netdata's alarm notify script (path differs by install):

```bash
# Common path
sudo /usr/libexec/netdata/plugins.d/alarm-notify.sh test

# Or
sudo /opt/netdata/usr/libexec/netdata/plugins.d/alarm-notify.sh test
```

You should receive test warning/critical/clear emails at `DEFAULT_RECIPIENT_EMAIL` if msmtp is configured correctly.

If you see errors like `Cannot find sendmail command in the system path`, ensure `msmtp` is installed and that `EMAIL_CMD`/`SENDMAIL` in `health_alarm_notify.conf` points to the correct msmtp path (use `which msmtp` to verify).

---

## 9. Troubleshooting tips

- **No test email & errors referencing sendmail**: Install `msmtp` and/or set `EMAIL_CMD` to `/usr/bin/msmtp --file=/etc/msmtprc -t`.
- **`account default not found` from msmtp**: explicitly pass `--file=/etc/msmtprc` or create a `~/.msmtprc` for the user running msmtp.
- **Nginx proxy shows raw Netdata**: add Basic Auth to Nginx to restrict access.
- **Netdata high memory usage**: Netdata stores metrics in RAM; reduce retention in `/etc/netdata/netdata.conf` or lower collection resolution.
- **Firewall**: ensure port `19999` is not publicly exposed if you rely on Nginx proxy; prefer blocking direct external access.

---

## 10. Security & best practices

- Protect the Netdata UI with Nginx Basic Auth or serve Netdata only on localhost and proxy via Nginx.
- Use HTTPS for `www.newsjour.com` (Let's Encrypt via certbot) so `/admin/metrics/` is secured in transit.
- Limit Netdata retention on low-memory systems.
- Regularly rotate the Gmail App Password if needed and keep `/etc/msmtprc` secured: `chmod 600 /etc/msmtprc`.

---

## 11. Uninstall Netdata (if needed)

```bash
sudo /usr/sbin/netdata-uninstall.sh
# or follow the official uninstall docs if command not present
```

---

## 12. Appendix: helpful commands

```bash
# Netdata status
sudo systemctl status netdata

# Restart netdata
sudo systemctl restart netdata

# Check which msmtp
which msmtp

# Test msmtp
echo "test" | msmtp --file=/etc/msmtprc you@domain.com

# Nginx config test
sudo nginx -t
sudo systemctl reload nginx

# Netdata notification test
sudo /usr/libexec/netdata/plugins.d/alarm-notify.sh test
```

---

## References

- Netdata official installer: [https://my-netdata.io/](https://my-netdata.io/)
- Netdata health docs: [https://learn.netdata.cloud/docs/agent/health/overview](https://learn.netdata.cloud/docs/agent/health/overview)
- msmtp: [https://marlam.de/msmtp/](https://marlam.de/msmtp/)
- Gmail App Passwords: [https://support.google.com/accounts/answer/185833](https://support.google.com/accounts/answer/185833)

---

_End of document._
