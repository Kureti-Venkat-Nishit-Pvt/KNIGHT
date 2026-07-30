# 🖥️ KnightVM Environment Setup Guide 🔒

--- 
![Confidential](https://img.shields.io/badge/CONFIDENTIAL-FOR%20MY%20EYES%20ONLY-red?style=for-the-badge&logo=shield&logoColor=white)

> **DO NOT** share, upload, commit, or distribute this document publicly.

---
## 📋 VM Access Details

| Property | Value |
|----------|-------|
| **Username** | `knightvm` |
| **Password** | `Ven13299kat@` |

---

# 📦 Git CLI Installation

## 🌐 Official Download

**Git for Windows**

https://git-scm.com/install/windows

---

# 📥 Git Installation & Verification

```mermaid
flowchart TD

    START([🚀 Start])

    WEBSITE["🌐 Open Git Download Page"]
    DOWNLOAD["⬇️ Download<br/>Git for Windows"]
    RUN["📦 Launch Installer"]

    subgraph INSTALL["🧙 Installation Wizard"]
        NEXT1["➡️ Click Next"]
        DEFAULT["⚙️ Keep All Default Settings"]
        INSTALLBTN["💾 Click Install"]
        FINISH["✅ Click Finish"]
    end

    VERIFY["🖥️ Open Command Prompt"]

    CMD["⌨️ Run<br/>git --version"]

    OUTPUT["✅ Expected Output<br/>git version 2.51.1.windows.1"]

    DONE([🎉 Git Successfully Installed])

    START --> WEBSITE
    WEBSITE --> DOWNLOAD
    DOWNLOAD --> RUN
    RUN --> NEXT1
    NEXT1 --> DEFAULT
    DEFAULT --> INSTALLBTN
    INSTALLBTN --> FINISH
    FINISH --> VERIFY
    VERIFY --> CMD
    CMD --> OUTPUT
    OUTPUT --> DONE

    click WEBSITE "https://git-scm.com/download/win" "Open Git Download Page"
    click DOWNLOAD "https://git-scm.com/download/win" "Download Git for Windows"
```

# 🌍 Terraform CLI Installation

## Step 1 — Create Terraform Directory

Create the following directory inside the VM C Drive.

```text
C:\Terraform
```
This folder will contain the Terraform executable.

## 🌐 Official Download

Terraform Downloads

https://developer.hashicorp.com/terraform/install > Select **Windows**.

Download the **AMD64 ZIP** package.

---

## Extract Files

Extract every file from the downloaded ZIP archive into:

```text
C:\Terraform
```

The directory should now contain:

```text
C:\Terraform
    terraform.exe
```

---

## Configure PATH Environment Variable

```mermaid
graph TD
    A[Start] --> B[Edit the system environment variables]
    B --> C[Environment Variables]
    C --> D[System Variables]
    D --> E[Select Path]
    E --> F[Click Edit]
    F --> G[Click New]
    G --> H[Add C:\Terraform]
    H --> I[Click OK]
    I --> J[Click OK]
    J --> K[Restart all open Command Prompt windows]
    K --> L[PATH Configuration Complete]
```

## Verify Installation

Open **Command Prompt** and execute:

```cmd
terraform version
```

### Expected Output

```text
Terraform v1.15.8
on windows_amd64
```

---

## Terraform Installation Workflow

```mermaid
graph TD

A[Create C:\Terraform Folder]
-->B[Open Terraform Website]
-->C[Download AMD64 ZIP]
-->D[Extract Files]
-->E[Copy terraform.exe to C:\Terraform]
-->F[Open Environment Variables]
-->G[Edit System PATH]
-->H[Add C:\Terraform]
-->I[Save Changes]
-->J[Open New Command Prompt]
-->K[Run terraform version]
-->L[Verify Installation]
```

---

# ✅ Installation Checklist

| Component | Status |
|-----------|--------|
| Create `C:\Terraform` | ☐ |
| Install Git | ☐ |
| Verify Git | ☐ |
| Download Terraform | ☐ |
| Extract Terraform | ☐ |
| Configure PATH | ☐ |
| Verify Terraform | ☐ |

---

# ✅ Verification Commands

## Git

```cmd
git --version
```

Expected:

```text
git version 2.51.1.windows.1
```

---

## Terraform

```cmd
terraform version
```

Expected:

```text
Terraform v1.15.8
on windows_amd64
```

---
