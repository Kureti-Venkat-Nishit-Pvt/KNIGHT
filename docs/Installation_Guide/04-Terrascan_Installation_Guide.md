# 🛡️ Terrascan Installation Guide

![Security](https://img.shields.io/badge/Security-Terrascan_|_Infrastructure_Security-2E7D32?style=for-the-badge)

Terrascan is an open-source **Infrastructure as Code (IaC) Security and Compliance Scanner** developed by Tenable. It scans Terraform, Kubernetes, CloudFormation, ARM Templates, Kustomize and other Infrastructure as Code frameworks against security, governance, and compliance policies.

Within the **KNIGHT Framework**, Terrascan performs policy-based Infrastructure as Code analysis after Terraform validation, helping identify security vulnerabilities, compliance violations, and governance issues before infrastructure deployment.

---

# 📑 Table of Contents

[![📦 Overview](https://img.shields.io/badge/📦_Overview-Tool_Introduction-1565C0?style=for-the-badge)](#-overview)
[![🛠️ Prerequisites](https://img.shields.io/badge/🛠️_Prerequisites-System_Requirements-1565C0?style=for-the-badge)](#️-prerequisites)

[![📂 Local_Demo](https://img.shields.io/badge/📂_Local_Demo-Project_Setup-2E7D32?style=for-the-badge)](#-local-demo-project-setup)
[![📄 Demo_Files](https://img.shields.io/badge/📄_Demo_Files-Required_Files-2E7D32?style=for-the-badge)](#-demo-files-required)

[![🌐 Download](https://img.shields.io/badge/🌐_Download-Information-6A1B9A?style=for-the-badge)](#-download-information)
[![📋 Installation](https://img.shields.io/badge/📋_Installation-Workflow-6A1B9A?style=for-the-badge)](#-installation-workflow)
[![📝 Installation](https://img.shields.io/badge/📝_Installation-Step--by--Step-6A1B9A?style=for-the-badge)](#-installation-steps)

[![💻 Commands](https://img.shields.io/badge/💻_Commands-Variations-B71C1C?style=for-the-badge)](#-commands--variations)
[![📷 Sample_Output](https://img.shields.io/badge/📷_Sample-Output-B71C1C?style=for-the-badge)](#-sample-output)
[![🧪 Demo](https://img.shields.io/badge/🧪_Demo-Commands-B71C1C?style=for-the-badge)](#-demo-commands)
[![🎯 Expected](https://img.shields.io/badge/🎯_Expected-Result-B71C1C?style=for-the-badge)](#-expected-result)

[![⚠️ Troubleshooting](https://img.shields.io/badge/⚠️_Troubleshooting-Common_Issues-EF6C00?style=for-the-badge)](#️-troubleshooting)
[![☑️ Checklist](https://img.shields.io/badge/☑️_Installation-Checklist-EF6C00?style=for-the-badge)](#-installation-checklist)

---

# 📊 Overview

| Question | Answer |
|----------|--------|
| **What is it?** | Terrascan is an open-source Infrastructure as Code (IaC) security and compliance scanner. |
| **What is it used for?** | It scans Infrastructure as Code files against built-in security, governance, and compliance policies. |
| **When do we use it?** | After Terraform validation and before infrastructure deployment. |
| **Why are we implementing it?** | To identify security vulnerabilities, governance violations, and compliance issues within the KNIGHT Local Terraform Quality Gate. |

---

# 🛠️ Prerequisites

Before installing **Terrascan**, ensure the following requirements are available.

![Operating_System](https://img.shields.io/badge/Operating_System-Windows_10_|_Windows_11-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Terminal](https://img.shields.io/badge/Terminal-Command_Prompt_(CMD)_|_Required-1565C0?style=for-the-badge)

![Infrastructure](https://img.shields.io/badge/Software-Terraform_|_Installed-623CE4?style=for-the-badge&logo=terraform&logoColor=white)

![Network](https://img.shields.io/badge/Network-Internet_Connection_|_Required-EF6C00?style=for-the-badge)

![Permissions](https://img.shields.io/badge/Permissions-Administrator_Access_|_Recommended-B71C1C?style=for-the-badge)

---

# 📂 Local Demo Project Setup

The following project structure will be used throughout the Terrascan demonstration.

```mermaid
flowchart TB

A["📁 Terraform_Demo"]

A --> B["📂 terraform"]
A --> C["📂 reports"]
A --> D["📂 docs"]

B --> B1["main.tf"]
B --> B2["provider.tf"]
B --> B3["variables.tf"]
B --> B4["outputs.tf"]

C --> C1["terrascan_report.json"]

D --> D1["04-Terrascan_Installation_Guide.md"]

classDef root fill:#4A148C,stroke:#6A1B9A,stroke-width:4px,color:#ffffff,font-weight:bold;
classDef folder fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;
classDef file fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#ffffff,font-weight:bold;

class A root;
class B,C,D folder;
class B1,B2,B3,B4,C1,D1 file;
```

---

# 📄 Demo Files Required

| File | Required | Purpose |
|------|:--------:|---------|
| `main.tf` | ✅ | Terraform configuration to scan |
| `provider.tf` | ✅ | Terraform provider configuration |
| `variables.tf` | ✅ | Terraform variables |
| `outputs.tf` | ✅ | Terraform outputs |
| `terrascan_report.json` | ⭐ | Generated Terrascan report |
| `README.md` | ✅ | Demo documentation |

---

# 📁 Demo File Structure

```mermaid
flowchart TB

A["📁 Terraform_Demo"]

A --> B["📂 terraform"]
A --> C["📂 reports"]
A --> D["📄 README.md"]

B --> B1["📜 main.tf"]
B --> B2["⚙️ provider.tf"]
B --> B3["📝 variables.tf"]
B --> B4["📤 outputs.tf"]

C --> C1["📋 terrascan_report.json"]

classDef root fill:#4A148C,stroke:#6A1B9A,stroke-width:4px,color:#ffffff,font-weight:bold;
classDef folder fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;
classDef terraform fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#ffffff,font-weight:bold;
classDef report fill:#EF6C00,stroke:#E65100,stroke-width:2px,color:#ffffff,font-weight:bold;
classDef readme fill:#00838F,stroke:#006064,stroke-width:2px,color:#ffffff,font-weight:bold;

class A root;
class B,C folder;
class B1,B2,B3,B4 terraform;
class C1 report;
class D readme;
```

---

# 🌐 Download Information

![Category](https://img.shields.io/badge/Category-Security-2E7D32?style=for-the-badge)

![Installation](https://img.shields.io/badge/Installation-Windows_Binary-623CE4?style=for-the-badge)

![Executable](https://img.shields.io/badge/Executable-terrascan.exe-B71C1C?style=for-the-badge)

![Verification](https://img.shields.io/badge/Verification-terrascan_version-623CE4?style=for-the-badge)

---

# 🌍 Official Resources

[![📘 Documentation](https://img.shields.io/badge/📘_Documentation-Terrascan-2E7D32?style=for-the-badge)](https://runterrascan.io/)

[![💻 GitHub Repository](https://img.shields.io/badge/💻_GitHub-tenable/terrascan-181717?style=for-the-badge&logo=github)](https://github.com/tenable/terrascan)

[![⬇️ Releases](https://img.shields.io/badge/⬇️_Download-Terrascan_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/tenable/terrascan/releases)

---

# 🛡️ Terrascan Installation

Before using **Terrascan**, download the Windows binary, configure the executable, and verify the installation.

---

# 📋 Installation Workflow

```mermaid
flowchart TD

    A([Start])

    --> B

    subgraph B["📂 Create Installation Folder"]
        direction LR

        subgraph B1["Run"]
            direction LR
            B11["mkdir C:\KNIGHT\Tools"]
        end

    end

    B11
    --> C["https://github.com/tenable/terrascan/releases"]

    --> D["Download Windows AMD64 Binary"]

    --> E["Extract ZIP Archive"]

    E
    --> F

    subgraph F["📂 Copy Terrascan Binary"]
        direction LR

        subgraph F1["Rename"]
            direction LR
            F11["terrascan.exe"]
        end

        subgraph F2["Copy"]
            direction LR
            F21["C:\KNIGHT\Tools"]
        end

        F1 --> F2

    end

    F21
    --> G

    subgraph G["⚙️ Configure PATH Environment Variable"]
        direction LR

        G1["Edit the system environment variables"]
        --> G2["Environment Variables"]
        --> G3["System Variables"]
        --> G4["Select Path"]
        --> G5["Click Edit"]
        --> G6["Click New"]

        G6
        --> G7

        subgraph G7["Add PATH"]
            direction LR
            G71["C:\KNIGHT\Tools"]
        end

        G7
        --> G8["Click OK"]
        --> G9["Click OK"]
        --> G10["Restart all open Command Prompt windows"]

    end

    G10
    --> H

    subgraph H["💻 Command Prompt"]
        direction LR

        subgraph H1["Open"]
            direction LR
            H11["New Command Prompt"]
        end

        subgraph H2["Run"]
            direction LR
            H21["terrascan version"]
        end

        H1 --> H2

    end

    H21
    --> I([Terrascan Installed Successfully])

    %% ===================================
    %% Styles
    %% ===================================

    classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;
    classDef url fill:#6A1B9A,stroke:#8E24AA,stroke-width:3px,color:#ffffff,font-weight:bold;
    classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;
    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    %% ===================================
    %% Apply Styles
    %% ===================================

    class B11,F11,F21,G71,H21 cmd;

    class C,D url;

    class G1,G2,G3,G4,G5,G6,G8,G9,G10,H11 process;

    class I success;
```
---

# 📝 Step 1 – Download Terrascan

Download the latest **Windows AMD64** release from the official GitHub Releases page.

[![Terrascan Releases](https://img.shields.io/badge/⬇️_Download-Terrascan_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/tenable/terrascan/releases)

## 📦 Download Details

![Platform](https://img.shields.io/badge/🪟_Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Architecture](https://img.shields.io/badge/💻_Architecture-AMD64-1565C0?style=for-the-badge)

![File Type](https://img.shields.io/badge/📦_File_Type-ZIP_Archive-EF6C00?style=for-the-badge)

![Binary](https://img.shields.io/badge/⚙️_Binary-terrascan.exe-623CE4?style=for-the-badge)

> **Note:** Download the latest stable Windows AMD64 release.

---

# 📝 Step 2 – Extract the ZIP Archive

Extract the downloaded ZIP archive to a temporary location.

---

# 📝 Step 3 – Copy the Binary

Copy **`terrascan.exe`** to the following directory:

```text
C:\KNIGHT\Tools
```

---

# 📝 Step 4 – Configure the PATH Environment Variable

Add the following directory to the Windows **PATH** environment variable.

```text
C:\KNIGHT\Tools
```

> **⚠️ Important:** Restart **Command Prompt (CMD)** after updating the PATH environment variable.

---

# 📝 Step 5 – Restart the Command Prompt

After updating the **Windows PATH Environment Variable**, any currently open **Command Prompt (CMD)** windows must be restarted.

## 📌 Restart Command Prompt

1. Close all open **Command Prompt (CMD)** windows.
2. Open a **new Command Prompt (CMD)** window.

> **⚠️ Important:** Existing Command Prompt windows will **not** detect the updated **PATH** automatically.

---

# 📝 Step 6 – Verify the Installation

Open a **new Command Prompt (CMD)**.

Run the following command:

```cmd
terrascan version
```

---

# 📷 Expected Verification Output

```text
Version: v1.xx.x
```

---

# 📋 Verification Checklist

| Check | Expected Result |
|--------|-----------------|
| `terrascan.exe` copied successfully | ✅ |
| PATH configured correctly | ✅ |
| Command Prompt restarted | ✅ |
| `terrascan version` executes successfully | ✅ |
| Terrascan version displayed | ✅ |

---

# 💡 Installation Tips

- Download the latest stable **Windows AMD64** release.
- Store all KNIGHT CLI tools under **`C:\KNIGHT\Tools`**.
- Restart **Command Prompt (CMD)** after updating the PATH.
- Verify the installation before scanning Terraform code.
- Keep Terrascan updated by downloading the latest release from GitHub.

---
---

# 💻 Commands & Variations

The following commands are commonly used while working with **Terrascan**.

| Purpose | Command |
|----------|---------|
| Display Version | `terrascan version` |
| Initialize Policy Database | `terrascan init` |
| Scan Current Directory | `terrascan scan` |
| Scan Terraform Folder | `terrascan scan -d terraform` |
| Scan Single Terraform File | `terrascan scan -f main.tf` |
| Generate JSON Report | `terrascan scan -o json` |
| Generate YAML Report | `terrascan scan -o yaml` |
| Show Help | `terrascan help` |

---

# 📷 Sample Output

## ✅ Successful Scan

```text
2026-08-06T18:40:12.123Z  info  loading policies...
2026-08-06T18:40:13.231Z  info  scanning Terraform files...

Violation Details

Name        : AWS S3 Bucket Encryption
Category    : Security
Severity    : High
Resource    : aws_s3_bucket.demo

Description :
S3 bucket encryption is not enabled.

-----------------------------------------------------

Scan Summary

Violated Policies : 1

Passed Policies   : 24

Skipped Policies  : 0
```

---

## 📊 Scan Summary

![High](https://img.shields.io/badge/High-1-red?style=for-the-badge)

![Passed](https://img.shields.io/badge/Passed-24-success?style=for-the-badge)

![Skipped](https://img.shields.io/badge/Skipped-0-lightgrey?style=for-the-badge)

---

# 🧪 Demo Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🔍 Verify Installation"]
        B1["terrascan version"]
    end

    B1
    --> C1

    subgraph C["📥 Initialize Policies"]
        C1["terrascan init"]
    end

    C1
    --> D1

    subgraph D["📂 Scan Current Project"]
        D1["terrascan scan"]
    end

    D1
    --> E1

    subgraph E["📁 Scan Terraform Folder"]
        E1["terrascan scan -d terraform"]
    end

    E1
    --> F1

    subgraph F["📄 Scan Single Terraform File"]
        F1["terrascan scan -f main.tf"]
    end

    F1
    --> G1

    subgraph G["📊 Generate JSON Report"]
        G1["terrascan scan -o json"]
    end

    G1
    --> H([Demo Completed])

    %% ===================================
    %% Styles
    %% ===================================

    classDef command fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    class B1,C1,D1,E1,F1,G1 command;

    class H success;
```

---

# 🎯 Expected Result

After completing the demonstration:

- ✅ Terrascan launches successfully.
- ✅ Policy database initializes successfully.
- ✅ Terraform files are scanned without errors.
- ✅ Security and compliance violations are displayed.
- ✅ Reports can be generated in multiple output formats.
- ✅ Ready for integration into the **KNIGHT Local Terraform Quality Gate**.

---

# 📋 Verification Checklist

- [ ] `terrascan version` executed successfully.
- [ ] `terrascan init` completed successfully.
- [ ] Current project scanned successfully.
- [ ] Terraform folder scanned successfully.
- [ ] Single Terraform file scanned successfully.
- [ ] JSON report generated successfully.
- [ ] Ready for the KNIGHT Terrascan demonstration.

---

# 💡 Demo Tips

- Begin by verifying the installation using `terrascan version`.
- Run `terrascan init` before performing the first scan.
- Demonstrate scanning the current Terraform project.
- Explain the difference between **security**, **compliance**, and **governance** policies.
- Highlight one policy violation and discuss its impact.
- Generate a JSON report to demonstrate integration with automation pipelines.
- Explain how Terrascan complements **Checkov** and **tfsec** within the KNIGHT Local Terraform Quality Gate.

---

---

# ⚠️ Troubleshooting

The following are common issues encountered during the installation and usage of **Terrascan**.

| Error | Possible Cause | Resolution |
|--------|----------------|------------|
| `'terrascan' is not recognized as an internal or external command` | `terrascan.exe` is not available in the Windows PATH | Verify that `terrascan.exe` exists in `C:\KNIGHT\Tools`, add the directory to the PATH, and restart Command Prompt. |
| `Error loading policies` | Policy bundle has not been initialized | Execute `terrascan init` before running your first scan. |
| `No Terraform files found` | Incorrect working directory | Navigate to the folder containing the Terraform (`*.tf`) files. |
| `Failed to parse Terraform configuration` | Invalid Terraform syntax | Run `terraform init` and `terraform validate` before scanning. |
| `Access is denied` | Insufficient permissions | Open **Command Prompt (CMD)** as Administrator and retry. |

---

# 💡 Common Resolution Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🔍 Verify Terrascan Installation"]

        subgraph B2["Run"]
            B1["terrascan version"]
        end

    end

    B1
    --> C1

    subgraph C["📥 Initialize Policies"]

        subgraph C2["Run"]
            C1["terrascan init"]
        end

    end

    C1
    --> D1

    subgraph D["📂 Verify Current Directory"]

        subgraph D2["Run"]
            D1["dir"]
        end

    end

    D1
    --> E1

    subgraph E["⚙️ Initialize Terraform"]

        subgraph E2["Run"]
            E1["terraform init"]
        end

    end

    E1
    --> F1

    subgraph F["✅ Validate Terraform"]

        subgraph F2["Run"]
            F1["terraform validate"]
        end

    end

    F1
    --> G1

    subgraph G["🛡️ Re-run Terrascan Scan"]

        subgraph G2["Run"]
            G1["terrascan scan"]
        end

    end

    G1
    --> H([Resolution Completed])

    %% ===================================
    %% Styles
    %% ===================================

    classDef command fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    class B1,C1,D1,E1,F1,G1 command;

    class H success;
```

---

# 📋 Installation Checklist

- [ ] Downloaded the Windows AMD64 binary.
- [ ] Extracted the ZIP archive.
- [ ] Renamed the executable to **terrascan.exe**.
- [ ] Copied **terrascan.exe** to `C:\KNIGHT\Tools`.
- [ ] Added `C:\KNIGHT\Tools` to the Windows **PATH**.
- [ ] Restarted **Command Prompt (CMD)**.
- [ ] Verified the installation using `terrascan version`.
- [ ] Initialized the policy database using `terrascan init`.
- [ ] Successfully scanned a Terraform project.
- [ ] Ready for the **KNIGHT Local Terraform Quality Gate**.

---

---

# 📚 References

[![📘 Documentation](https://img.shields.io/badge/📘_Documentation-Terrascan-2E7D32?style=for-the-badge)](https://runterrascan.io/)

[![💻 GitHub Repository](https://img.shields.io/badge/💻_GitHub-tenable/terrascan-181717?style=for-the-badge&logo=github)](https://github.com/tenable/terrascan)

[![⬇️ Releases](https://img.shields.io/badge/⬇️_Download-Terrascan_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/tenable/terrascan/releases)

[![🏢 Vendor](https://img.shields.io/badge/🏢_Vendor-Tenable-0096D6?style=for-the-badge)](https://www.tenable.com/)

[![📖 Terraform Documentation](https://img.shields.io/badge/📖_Terraform-Official_Documentation-623CE4?style=for-the-badge&logo=terraform&logoColor=white)](https://developer.hashicorp.com/terraform/docs)

---

# 🔄 Terrascan in the KNIGHT Local Quality Gate

```mermaid
flowchart LR

A["📝 terraform fmt"]

-->

B["⚙️ terraform init"]

-->

C["✅ terraform validate"]

-->

D["🛡️ TFLint"]

-->

E["🔍 Checkov"]

-->

F["🔐 tfsec"]

-->

G["🛡️ Terrascan"]

-->

H["📖 terraform-docs"]

-->

I["🚀 Ready for Deployment"]

%% ===================================
%% Styles
%% ===================================

classDef terraform fill:#623CE4,stroke:#4A148C,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef security fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef docs fill:#00838F,stroke:#006064,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

%% ===================================
%% Apply Styles
%% ===================================

class A,B,C terraform;

class D,E,F,G security;

class H docs;

class I success;
```

---

# 📌 Key Takeaways

| Topic | Summary |
|--------|---------|
| **Tool Category** | Infrastructure as Code Security & Compliance Scanner |
| **Primary Purpose** | Detect security, governance, and compliance violations |
| **Supported Platforms** | Terraform, Kubernetes, ARM, CloudFormation, Kustomize and more |
| **Input** | Infrastructure as Code configuration files |
| **Output** | Security and compliance policy violations |
| **Integration Point** | KNIGHT Local Terraform Quality Gate |
| **Verification Command** | `terrascan version` |
| **Primary Scan Command** | `terrascan scan` |

---

