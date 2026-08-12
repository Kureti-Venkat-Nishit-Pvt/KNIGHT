# 🔐 tfsec Installation Guide

![Security](https://img.shields.io/badge/Security-tfsec_|_Terraform_Security-2E7D32?style=for-the-badge)

tfsec is an open-source static analysis security scanner for **Terraform**. It analyzes Terraform configurations to identify security vulnerabilities, insecure defaults, and compliance violations before infrastructure is deployed.

Within the **KNIGHT Framework**, tfsec performs Terraform-focused security scanning immediately after validation to identify infrastructure security risks early in the Local Terraform Quality Gate.

---

# 📑 Table of Contents

[![📦 Overview](https://img.shields.io/badge/📦_Overview-Tool_Introduction-1565C0?style=for-the-badge)](#-overview)
[![🛠️ Prerequisites](https://img.shields.io/badge/🛠️_Prerequisites-System_Requirements-1565C0?style=for-the-badge)](#️-prerequisites)

[![📂 Local_Demo](https://img.shields.io/badge/📂_Local_Demo-Project_Setup-2E7D32?style=for-the-badge)](#-local-demo-project-setup)
[![📄 Demo_Files](https://img.shields.io/badge/📄_Demo_Files-Required_Files-2E7D32?style=for-the-badge)](#-demo-files-required)

[![⬇️ Download](https://img.shields.io/badge/⬇️_Download-tfsec-6A1B9A?style=for-the-badge)](#-download-information)
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
| **What is it?** | tfsec is a static security scanner designed specifically for Terraform configurations. |
| **What is it used for?** | It scans Terraform code for security vulnerabilities and Infrastructure as Code misconfigurations. |
| **When do we use it?** | After Terraform validation and before deployment. |
| **Why are we implementing it?** | To identify Terraform security vulnerabilities early and demonstrate Infrastructure as Code security scanning within the KNIGHT Framework. |

---

# 🛠️ Prerequisites

Before installing **tfsec**, ensure the following requirements are available.

![Operating System](https://img.shields.io/badge/Operating_System-Windows_10_|_Windows_11-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Terminal](https://img.shields.io/badge/Terminal-Command_Prompt_(CMD)_|_Required-1565C0?style=for-the-badge)

![Network](https://img.shields.io/badge/Network-Internet_Connection_|_Required-EF6C00?style=for-the-badge)

![Permissions](https://img.shields.io/badge/Permissions-Administrator_Access_|_Recommended-B71C1C?style=for-the-badge)

---

# 📂 Local Demo Project Setup

The following project structure will be used throughout the tfsec demonstration.

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

C --> C1["tfsec_report.txt"]

D --> D1["03-tfsec_Installation_Guide.md"]

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
| `tfsec_report.txt` | ⭐ | tfsec scan report |
| `README.md` | ✅ | Project documentation |

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

C --> C1["📋 tfsec_report.txt"]

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

![Executable](https://img.shields.io/badge/Executable-tfsec.exe-B71C1C?style=for-the-badge)
![Verification](https://img.shields.io/badge/Verification-tfsec_--version-623CE4?style=for-the-badge)

---

# 🌍 Official Resources

[![📘 Documentation](https://img.shields.io/badge/📘_Documentation-tfsec-2E7D32?style=for-the-badge)](https://aquasecurity.github.io/tfsec/)
[![💻 GitHub](https://img.shields.io/badge/💻_GitHub-aquasecurity/tfsec-181717?style=for-the-badge&logo=github)](https://github.com/aquasecurity/tfsec)
[![⬇️ Releases](https://img.shields.io/badge/⬇️_Download-tfsec_Releases-623CE4?style=for-the-badge)](https://github.com/aquasecurity/tfsec/releases)

---

# 🔐 tfsec Installation

Before using **tfsec**, download the Windows binary, configure the executable, and verify the installation.

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
    --> C["https://github.com/aquasecurity/tfsec/releases"]

    --> D["Download Windows AMD64 Binary"]

    --> E["Extract ZIP Archive"]

    E
    --> F

    subgraph F["📂 Copy tfsec Binary"]
        direction LR

        subgraph F1["Rename"]
            direction LR
            F11["tfsec.exe"]
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
            H21["tfsec --version"]
        end

        H1 --> H2

    end

    H21
    --> I([tfsec Installed Successfully])

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

# 📝 Step 1 – Download tfsec

Download the latest **Windows AMD64** binary from the official GitHub Releases page.

[![tfsec Releases](https://img.shields.io/badge/⬇️_Download-tfsec_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/aquasecurity/tfsec/releases)

## 📦 Download Details

![Platform](https://img.shields.io/badge/🪟_Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Architecture](https://img.shields.io/badge/💻_Architecture-AMD64-1565C0?style=for-the-badge)

![File Type](https://img.shields.io/badge/📦_File_Type-ZIP_Archive-EF6C00?style=for-the-badge)

![Binary](https://img.shields.io/badge/⚙️_Binary-tfsec.exe-623CE4?style=for-the-badge)

---

# 📝 Step 2 – Extract the Archive

Extract the downloaded ZIP archive to a temporary folder.

---

# 📝 Step 3 – Copy the Binary

Copy **tfsec.exe** to:

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

# 📝 Step 5 – Verify the Installation

Open a **new Command Prompt (CMD)**.

Run the following command:

```cmd
tfsec --version
```

---

# 📷 Expected Verification Output

```text
tfsec v1.xx.x
```

---

# 🎯 Verification Checklist

- [ ] Downloaded the Windows AMD64 binary.
- [ ] Extracted the ZIP archive.
- [ ] Copied `tfsec.exe` to `C:\KNIGHT\Tools`.
- [ ] Added `C:\KNIGHT\Tools` to the PATH environment variable.
- [ ] Restarted **Command Prompt (CMD)**.
- [ ] Executed `tfsec --version`.
- [ ] tfsec version displayed successfully.
- [ ] Ready for Terraform security scanning.

---

# 💡 Installation Tips

- Always download the latest stable Windows AMD64 release.
- Keep all KNIGHT CLI tools in **`C:\KNIGHT\Tools`**.
- Restart **Command Prompt (CMD)** after updating the PATH.
- Verify the installation before scanning Terraform code.
- Use the same installation directory for all KNIGHT security tools.

---

# 💻 Commands & Variations

The following commands are commonly used while working with **tfsec**.

| Purpose | Command |
|----------|---------|
| Display Version | `tfsec --version` |
| Scan Current Directory | `tfsec .` |
| Scan Terraform Folder | `tfsec terraform` |
| Scan Single Terraform File | `tfsec main.tf` |
| Generate JSON Report | `tfsec . --format json` |
| Generate SARIF Report | `tfsec . --format sarif` |
| Exclude Specific Checks | `tfsec . --exclude <CHECK_ID>` |
| Show Help | `tfsec --help` |

---

# 📷 Sample Output

## ✅ Successful Scan

```text
======================================================
tfsec v1.xx.x

Result #1 HIGH

Resource
aws_security_group.demo

Description
Security group allows ingress from 0.0.0.0/0

Impact
Your infrastructure may be exposed publicly.

Resolution
Restrict the CIDR block.

------------------------------------------------------

Result #2 MEDIUM

Resource
aws_s3_bucket.demo

Description
Bucket versioning disabled.

------------------------------------------------------

2 potential problems detected.
```

---

## 📊 Scan Summary

![Critical](https://img.shields.io/badge/Critical-0-success?style=for-the-badge)

![High](https://img.shields.io/badge/High-1-red?style=for-the-badge)

![Medium](https://img.shields.io/badge/Medium-1-orange?style=for-the-badge)

![Low](https://img.shields.io/badge/Low-0-lightgrey?style=for-the-badge)

---

# 🧪 Demo Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🔍 Verify Installation"]
        B1["tfsec --version"]
    end

    B1 --> C1

    subgraph C["📂 Scan Current Project"]
        C1["tfsec ."]
    end

    C1 --> D1

    subgraph D["📁 Scan Terraform Folder"]
        D1["tfsec terraform"]
    end

    D1 --> E1

    subgraph E["📄 Scan Single Terraform File"]
        E1["tfsec main.tf"]
    end

    E1 --> F1

    subgraph F["📊 Generate JSON Report"]
        F1["tfsec . --format json"]
    end

    F1 --> G1

    subgraph G["📝 Generate SARIF Report"]
        G1["tfsec . --format sarif"]
    end

    G1 --> H([Demo Completed])

    %% Styles

    classDef command fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    class B1,C1,D1,E1,F1,G1 command;

    class H success;
```

---

# 🎯 Expected Result

After completing the demonstration:

- ✅ tfsec launches successfully.
- ✅ Terraform files are scanned without errors.
- ✅ Security findings are displayed.
- ✅ High, Medium and Low severity issues are identified.
- ✅ Reports can be generated in multiple formats.
- ✅ Ready for integration into the **KNIGHT Local Terraform Quality Gate**.

---

# 📋 Verification Checklist

- [ ] `tfsec --version` executed successfully.
- [ ] Current project scanned successfully.
- [ ] Terraform folder scanned successfully.
- [ ] Single Terraform file scanned successfully.
- [ ] JSON report generated successfully.
- [ ] SARIF report generated successfully.
- [ ] Ready for the KNIGHT tfsec demonstration.

---

# 💡 Demo Tips

- Start by verifying the installed version using `tfsec --version`.
- Demonstrate scanning the current Terraform project.
- Explain the severity levels (**Critical**, **High**, **Medium**, and **Low**).
- Highlight one detected issue and discuss its security impact.
- Generate a JSON report to demonstrate automation.
- Generate a SARIF report to explain integration with GitHub Advanced Security.
- Explain where tfsec fits within the **KNIGHT Local Terraform Quality Gate**.

---

# ⚠️ Troubleshooting

The following are common issues encountered during the installation and usage of **tfsec**.

| Error | Possible Cause | Resolution |
|--------|----------------|------------|
| `'tfsec' is not recognized as an internal or external command` | `tfsec.exe` is not in the PATH or Command Prompt was not restarted | Verify `tfsec.exe` exists in `C:\KNIGHT\Tools`, ensure the directory is added to the PATH, and restart Command Prompt. |
| `Failed to load Terraform configuration` | Invalid Terraform configuration | Execute `terraform init` and `terraform validate` before running tfsec. |
| `No Terraform files found` | Incorrect working directory | Navigate to the directory containing the `.tf` files before executing tfsec. |
| `Access is denied` | Insufficient permissions | Run **Command Prompt (CMD)** as Administrator and retry. |
| `Unsupported Terraform version` | Older Terraform syntax or unsupported configuration | Upgrade Terraform or modify the configuration to a supported version. |

---

# 💡 Common Resolution Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🔍 Verify tfsec Installation"]
        B1["tfsec --version"]
    end

    B1 --> C1

    subgraph C["📂 Verify Current Directory"]
        C1["dir"]
    end

    C1 --> D1

    subgraph D["⚙️ Initialize Terraform"]
        D1["terraform init"]
    end

    D1 --> E1

    subgraph E["✅ Validate Terraform"]
        E1["terraform validate"]
    end

    E1 --> F1

    subgraph F["🔄 Re-run tfsec Scan"]
        F1["tfsec ."]
    end

    F1 --> G([Resolution Completed])

    %% ===================================
    %% Styles
    %% ===================================

    classDef command fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    class B1,C1,D1,E1,F1 command;

    class G success;
```

---

# 📋 Installation Checklist

- [ ] Downloaded the Windows AMD64 binary.
- [ ] Extracted the ZIP archive.
- [ ] Renamed the executable to **tfsec.exe**.
- [ ] Copied **tfsec.exe** to `C:\KNIGHT\Tools`.
- [ ] Added `C:\KNIGHT\Tools` to the Windows PATH.
- [ ] Restarted **Command Prompt (CMD)**.
- [ ] Verified the installation using `tfsec --version`.
- [ ] Successfully scanned a Terraform project.
- [ ] Generated a security scan report.
- [ ] Ready for the **KNIGHT Local Terraform Quality Gate**.

---

# 📚 References

[![📘 Documentation](https://img.shields.io/badge/📘_Documentation-tfsec-2E7D32?style=for-the-badge)](https://aquasecurity.github.io/tfsec/)
[![💻 GitHub Repository](https://img.shields.io/badge/💻_GitHub-aquasecurity/tfsec-181717?style=for-the-badge&logo=github)](https://github.com/aquasecurity/tfsec)
[![⬇️ Releases](https://img.shields.io/badge/⬇️_Download-tfsec_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/aquasecurity/tfsec/releases)
[![🐳 Aqua Security](https://img.shields.io/badge/🛡️_Vendor-Aqua_Security-00ACC1?style=for-the-badge)](https://www.aquasec.com/)
[![📖 Terraform Documentation](https://img.shields.io/badge/📖_Terraform-Official_Documentation-623CE4?style=for-the-badge&logo=terraform&logoColor=white)](https://developer.hashicorp.com/terraform/docs)

---


# 🔄 tfsec in the KNIGHT Local Quality Gate

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
| **Tool Category** | Terraform Security Scanner |
| **Primary Purpose** | Detect Infrastructure as Code (IaC) security vulnerabilities |
| **Input** | Terraform configuration files (`*.tf`) |
| **Output** | Security findings with severity levels |
| **Integration Point** | KNIGHT Local Terraform Quality Gate |
| **Verification Command** | `tfsec --version` |
| **Primary Scan Command** | `tfsec .` |

---
