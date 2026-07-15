# KNIGHT **Checkov** Demo — Step-by-Step Guide (For Your Reference)

> **Use this file as your personal cheat sheet.** Read it once before the demo, then follow each step while you present.

---

## Do I Need an AWS Account?

**No. You do NOT need an AWS account or AWS credentials to run this demo.**

Here is why:

- Checkov is a **Static Application Security Testing (SAST)** tool.
- SAST means it reads your Terraform **code files only** — it does not connect to AWS.
- Everything runs inside the **GitHub Actions runner** (a free virtual machine GitHub gives you).
- No real servers, buckets, or networks are created.
- The demo is **100% free** and **100% safe** — nothing goes live in the cloud.

You only need:
1. A **GitHub account** (free tier is fine)
2. This project folder on your laptop
3. About **15–20 minutes** for the full demo

---

## Before You Start — Quick Checklist

Make sure these files exist in your project folder:

| File | What it is |
|------|------------|
| `providers.tf` | AWS provider settings (used only for code analysis, not live deployment) |
| `main.tf` | Terraform code with **intentional** security mistakes |
| `.github/workflows/standard-deploy.yml` | Normal pipeline — checks syntax only |
| `.github/workflows/checkov-scan.yml` | Security pipeline — runs Checkov scan |
| `README.md` | Project overview for your manager |
| `STEPS.md` | This guide (for you only) |

Open **VS Code** or **Cursor** and have this file open on a second screen or printed out.

---

## Step 1: Git and GitHub Setup

Do this **once**, before your manager joins the call.

### 1.1 — Open a terminal in your project folder

In VS Code / Cursor: press `` Ctrl + ` `` to open the terminal.
Make sure you are inside the `KNIGHT` folder.

### 1.2 — Initialize Git

```bash
git init
```

This turns your folder into a Git repository so you can track changes.

### 1.3 — Stage all files

```bash
git add .
```

The dot (`.`) means "add everything in this folder."

### 1.4 — Create your first commit

```bash
git commit -m "Initial commit: KNIGHT Checkov security demo"
```

A commit is like a saved snapshot of your code.

### 1.5 — Create a new repo on GitHub

1. Go to [https://github.com/new](https://github.com/new)
2. Repository name: `KNIGHT`
3. Keep it **Public** or **Private** — either works
4. **Do NOT** tick "Add a README" (you already have one)
5. Click **Create repository**

### 1.6 — Link your local folder to GitHub

Copy the URL GitHub shows you, then run

```bash
git remote add origin https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT.git
```

### 1.7 — Push to the `checkov` branch

```bash
git branch -M checkov
git push -u origin checkov
```

If GitHub asks you to log in, use your GitHub username and a **Personal Access Token** (not your password).

> **Tip:** After this push, GitHub Actions will start running automatically. Wait about 1–2 minutes before opening the Actions tab.

---

## Step 2: How to Show the "Insecure" Demo

This is the main part of your presentation. Share your screen on the **GitHub website**.

### 2.1 — Open your repo on GitHub

Go to: `https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT`

### 2.2 — Click the **Actions** tab

You will see two workflow runs (they start automatically after your push):

| Workflow Name | Expected Result |
|---------------|-----------------|
| **Standard Pipeline (No Security Scan)** | ✅ Green checkmark — PASSED |
| **Security Pipeline (With Checkov)** | ❌ Red X — FAILED |

### 2.3 — Show the passing workflow first

1. Click on **Standard Pipeline (No Security Scan)**
2. Click on the **lint-and-validate** job
3. Expand the steps — show `terraform fmt`, `terraform init`, `terraform validate` all passed

**What to say:**
> "This is our current pipeline. It checks that the Terraform code is written correctly — no syntax errors, valid structure. It passed. From a developer's view, this code looks ready to deploy."

### 2.4 — Show the failing Checkov workflow

1. Go back to the Actions tab
2. Click on **Security Pipeline (With Checkov)**
3. Click on the **security-gate** job
4. Scroll down to the **Run Checkov** step — expand it
5. You will see a list of **FAILED** checks with policy IDs like `CKV_AWS_79`, `CKV_AWS_24`, `CKV_AWS_19`

**What to say:**
> "But when we add Checkov — a security scanner — the same code fails. Checkov found 3 real security problems that our standard pipeline completely missed."

### 2.5 — Walk through the 3 failures

Open `main.tf` in your editor side-by-side (or show it on GitHub under the **Code** tab):

| # | Checkov ID | Problem | Line in main.tf |
|---|------------|---------|-----------------|
| 1 | CKV_AWS_79 | EC2 disk is not encrypted | `encrypted = false` |
| 2 | CKV_AWS_24 | SSH port 22 open to the whole internet | `cidr_blocks = ["0.0.0.0/0"]` |
| 3 | CKV_AWS_19 | S3 bucket has no encryption | No encryption block on the bucket |

**What to say for each:**
- **Encryption off:** "If someone gets access to this disk, they can read all data in plain text."
- **SSH open to world:** "Anyone on the internet can try to brute-force login to this server."
- **S3 not encrypted:** "Files stored here are not protected at rest — a compliance violation."

---

## Step 3: Manager Presentation Script

Read this naturally — you do not need to memorize every word. Use it as your talking points.

---

**Opening (30 seconds):**

> "Hi Kolappan, today I want to show you something called **shift-left security** — catching security problems in our code *before* they ever reach AWS. I built a small demo project called **KNIGHT** to prove this works."

---

**The Problem (1 minute):**

> "Right now, most teams only run `terraform validate` in CI. That checks if the code is *syntactically correct* — like spell-check for infrastructure code. But it does not check if the code is *secure*.

> In our demo, we wrote Terraform that creates an EC2 server with an unencrypted disk, opens SSH to the entire internet, and creates an S3 bucket with no encryption. Our standard pipeline gave it a green checkmark. That code could have gone to production."

---

**The Solution — Checkov (1 minute):**

> "Checkov is a free, open-source tool from Bridgecrew (now part of Palo Alto Networks). It scans Terraform, CloudFormation, Kubernetes, and other IaC files against hundreds of security policies — CIS benchmarks, SOC2, PCI-DSS, and more.

> We added one step to our GitHub Actions pipeline. Same code, same repo — but now Checkov blocks the merge if security rules are broken. This is called **shifting left**: we fix security issues at the code stage, not after a breach or audit failure."

---
s
**Business Value (1 minute):**

> "Why does this matter for us?
>
> 1. **Cost** — Fixing a security bug in code takes minutes. Fixing it after deployment takes hours or days, and may require downtime.
> 2. **Compliance** — Many of our clients require CIS or SOC2 controls. Checkov checks those automatically on every pull request.
> 3. **No AWS needed for testing** — Checkov reads the code statically. We can run this in CI for free, with zero cloud cost.
> 4. **Developer-friendly** — Developers see the exact line and policy that failed, right in the GitHub Actions log. No security team bottleneck."

---

**Live Demo Transition:**

> "Let me show you this live. I pushed our intentionally insecure code to GitHub a few minutes ago. Watch what happens in the Actions tab..."

*(Now do Step 2 above — show the green standard pipeline, then the red Checkov pipeline.)*

---

**Closing the "Insecure" section:**

> "So we just proved that 'green pipeline' does not mean 'secure code.' Now let me show you how fast we can fix it."

---

## Step 4: How to Show the "Fix"

This is the satisfying ending — both pipelines turn green.

### 4.1 — Open `main.tf` in your editor

Replace the entire contents of `main.tf` with the secured version from `README.md` (bottom section), or make these 3 changes:

**Change 1 — Encrypt the EC2 disk:**
```hcl
root_block_device {
  encrypted = true    # was: false
}
```

**Change 2 — Restrict SSH to private network only:**
```hcl
cidr_blocks = ["10.0.0.0/8"]    # was: ["0.0.0.0/0"]
```

**Change 3 — Add S3 encryption block (add this after the bucket resource):**
```hcl
resource "aws_s3_bucket_server_side_encryption_configuration" "insecure_bucket" {
  bucket = aws_s3_bucket.insecure_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
```

### 4.2 — Commit and push the fix

In your terminal:

```bash
git add main.tf
git commit -m "Fix: remediate 3 Checkov security findings"
git push
```

### 4.3 — Watch both pipelines on GitHub Actions

1. Go back to the **Actions** tab on GitHub
2. You will see two new workflow runs starting
3. Wait 1–2 minutes

| Workflow | Expected Result |
|----------|-----------------|
| **Standard Pipeline (No Security Scan)** | ✅ PASSED |
| **Security Pipeline (With Checkov)** | ✅ PASSED (this time!) |

### 4.4 — Show the Checkov log is clean

1. Click **Security Pipeline (With Checkov)**
2. Expand the **Run Checkov** step
3. Show that there are **0 failed checks**

**What to say:**

> "Three lines of code changed. Zero AWS resources deployed. Both pipelines green. That is shift-left security — we caught and fixed real vulnerabilities in under 5 minutes, for free, before anything touched the cloud."

---

## Troubleshooting — Common Issues

| Problem | Fix |
|---------|-----|
| `git push` asks for password | Use a GitHub Personal Access Token instead of your password. Go to GitHub → Settings → Developer settings → Personal access tokens. |
| Actions tab is empty | Make sure you pushed to the `main` branch and the workflow files are in `.github/workflows/`. |
| Both workflows fail | Run `terraform fmt` locally to fix formatting, then commit and push again. |
| Checkov fails with unexpected errors | Make sure you ran `git add .` and committed ALL files including `.github/workflows/`. |
| Folder still shows old name `HAVOT-2` | The folder was renamed to `KNIGHT`. Re-open the project from the new path. |

---

## Demo Timing Guide

| Section | Time |
|---------|------|
| Step 1 — Git setup (do before call) | 5 min |
| Step 2 — Show insecure demo | 5 min |
| Step 3 — Manager script | 5 min |
| Step 4 — Show the fix | 5 min |
| **Total presentation time** | **~15–20 min** |

---

## One-Line Summary (If Your Manager Asks "So What?")

> "We added one free tool to our pipeline that catches security mistakes in Terraform before they cost us money, time, or a compliance audit failure."

Good luck with your demo! 🛡️
