# 🛠️ KNIGHT Tools Installation Guide

This guide provides the complete installation workflow for all tools required to set up the **KNIGHT Local Terraform Quality Gate** on a Windows machine.

---

# 📑 Table of Contents

[![📦 Overview](https://img.shields.io/badge/📦_Overview-Guide_Introduction-1565C0?style=for-the-badge)](#-overview)
[![🛠️ Prerequisites](https://img.shields.io/badge/🛠️_Prerequisites-System_Requirements-1565C0?style=for-the-badge)](#️-prerequisites)

[![📂 Demo_Project](https://img.shields.io/badge/📂_Demo_Project-Local_Setup-2E7D32?style=for-the-badge)](#-demo-project-setup)
[![📋 Installation_Order](https://img.shields.io/badge/📋_Installation-Order-2E7D32?style=for-the-badge)](#-installation-order)

[![⚙️ Installation](https://img.shields.io/badge/⚙️_Tool-Installation_Workflows-6A1B9A?style=for-the-badge)](#️-tool-installation-workflows)

[![🪟 Windows_PATH](https://img.shields.io/badge/🪟_Configure-Windows_PATH-EF6C00?style=for-the-badge)](#-configure-the-windows-path)

[![💻 Verification](https://img.shields.io/badge/💻_Verification-Commands-B71C1C?style=for-the-badge)](#-verification-commands)

[![📷 Expected_Output](https://img.shields.io/badge/📷_Expected-Output-B71C1C?style=for-the-badge)](#-expected-output)

[![🚀 Quality_Gate](https://img.shields.io/badge/🚀_KNIGHT-Quality_Gate-00838F?style=for-the-badge)](#-knight-local-terraform-quality-gate)

[![📚 Resources](https://img.shields.io/badge/📚_Official-Resources-2E7D32?style=for-the-badge)](#-official-resources)

---

# 📦 Overview

The **KNIGHT Local Terraform Quality Gate** combines multiple open-source tools to validate, secure, lint, document, and enforce policy for Terraform Infrastructure as Code before deployment.

Instead of installing each tool independently, this guide provides a single workflow that installs every required tool for local development and demonstrations.

After completing this guide, your workstation will be capable of:

- ✅ Formatting Terraform code
- ✅ Initializing Terraform projects
- ✅ Validating Terraform configurations
- ✅ Performing Terraform lint analysis
- ✅ Running Infrastructure as Code security scans
- ✅ Enforcing Policy-as-Code
- ✅ Generating Terraform documentation automatically

---

# 🛠️ Prerequisites

Before starting the installation, ensure the following software and requirements are available.

![Operating_System](https://img.shields.io/badge/Operating_System-Windows_10_|_Windows_11-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Terminal](https://img.shields.io/badge/Terminal-Command_Prompt_(CMD)-1565C0?style=for-the-badge)

![Internet](https://img.shields.io/badge/Internet-Connection_Required-EF6C00?style=for-the-badge)

![Administrator](https://img.shields.io/badge/Permissions-Administrator_Recommended-B71C1C?style=for-the-badge)

---

# 📂 Demo Project Setup

The following project structure will be used throughout this guide.

```mermaid
flowchart TB

A["📁 Terraform_Demo"]

A --> B["📂 terraform"]

A --> C["📂 policy"]

A --> D["📂 reports"]

A --> E["📄 README.md"]

B --> B1["main.tf"]
B --> B2["provider.tf"]
B --> B3["variables.tf"]
B --> B4["outputs.tf"]

C --> C1["policy.rego"]
C --> C2["input.json"]

D --> D1["reports"]

classDef root fill:#4A148C,stroke:#6A1B9A,stroke-width:4px,color:#ffffff,font-weight:bold;

classDef folder fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef terraform fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#ffffff,font-weight:bold;

classDef policy fill:#EF6C00,stroke:#E65100,stroke-width:2px,color:#ffffff,font-weight:bold;

classDef report fill:#00838F,stroke:#006064,stroke-width:2px,color:#ffffff,font-weight:bold;

classDef readme fill:#6A1B9A,stroke:#4A148C,stroke-width:2px,color:#ffffff,font-weight:bold;

class A root;

class B,C,D folder;

class B1,B2,B3,B4 terraform;

class C1,C2 policy;

class D1 report;

class E readme;
```

---

# 📋 Installation Order

The following installation order is recommended for the **KNIGHT Local Terraform Quality Gate**.

```mermaid
flowchart LR

A["⚙️ Terraform"]

-->

B["🐍 Python"]

-->

C["📦 pip"]

-->

D["⚖️ OPA"]

-->

E["🔍 Checkov"]

-->

F["🔐 tfsec"]

-->

G["🛡️ Terrascan"]

-->

H["📝 TFLint"]

-->

I["📖 terraform-docs"]

classDef terraform fill:#623CE4,stroke:#4A148C,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef dependency fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef security fill:#00838F,stroke:#006064,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef documentation fill:#EF6C00,stroke:#E65100,stroke-width:3px,color:#ffffff,font-weight:bold;

class A terraform;

class B,C dependency;

class D,E,F,G,H security;

class I documentation;
```

---

# ⚙️ Tool Installation Workflows

The following sections contain the installation workflows for each tool required by the **KNIGHT Local Terraform Quality Gate**.

Each workflow follows a consistent approach:

- Download the latest release.
- Extract the package.
- Copy the executable to **`C:\KNIGHT\Tools`** (where applicable).
- Configure the Windows **PATH**.
- Verify the installation.
- Confirm the tool is ready for use.

---

# ⚙️ Terraform Installation Workflow

```mermaid
flowchart TD

    A([Start])

    --> B

    subgraph B["📂 Create Installation Folder"]
        direction LR

        subgraph B1["Run"]
            direction LR
            B11["mkdir C:\Terraform"]
        end

    end

    B11
    --> C["https://developer.hashicorp.com/terraform/install"]

    --> D["Download Windows AMD64 ZIP"]

    --> E["Extract ZIP Archive"]

    E
    --> F

    subgraph F["📂 Copy Terraform Binary"]
        direction LR

        subgraph F1["Copy"]
            direction LR
            F11["terraform.exe"]
        end

        subgraph F2["Path"]
            direction LR
            F21["C:\Terraform"]
        end

        F1 --> F2

    end

    F21
    --> G

    subgraph G["⚙️ Configure PATH"]
        direction LR

        G1["Environment Variables"]

        --> G2["System PATH"]

        --> G3["Add C:\Terraform"]

    end

    G3
    --> H

    subgraph H["💻 Command Prompt"]
        direction LR

        subgraph H1["Run"]
            direction LR
            H11["terraform version"]
        end

    end

    H11
    --> I([Terraform Installed])

classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#fff;
classDef url fill:#6A1B9A,stroke:#8E24AA,stroke-width:3px,color:#fff;
classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#fff;
classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#fff;

class B11,F11,F21,G3,H11 cmd;
class C,D url;
class G1,G2 process;
class I success;
```

---

# 🐍 Python Installation Workflow

```mermaid
flowchart TD

    A([Start])

    --> B

    subgraph B["📥 Download Python"]

        B1["Open"]
        --> B2["https://www.python.org/downloads/windows/"]
        --> B3["Download Windows Installer (64-bit)"]

    end

    B
    --> C

    subgraph C["🖥️ Install Python"]

        C1["Run Installer"]
        --> C2["Enable 'Add Python to PATH'"]
        --> C3["Click Install Now"]
        --> C4["Complete Installation"]

    end

    C
    --> D

    subgraph D["💻 Command Prompt"]

        subgraph D1["Open"]
            D11["New Command Prompt"]
        end

        subgraph D2["Run"]
            D21["python --version"]
        end

        subgraph D3["Run"]
            D31["pip --version"]
        end

        D1 --> D2 --> D3

    end

    D
    --> E([Python Installed Successfully])

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

    class B2,B3 url;

    class D21,D31 cmd;

    class B1,C1,C2,C3,C4,D11 process;

    class E success;
```

---

# ⚖️ OPA Installation Workflow

```mermaid
flowchart TD

    A([Start])

    --> B

    subgraph B["📂 Create Installation Folder"]

        subgraph B1["Run"]
            B11["mkdir C:\KNIGHT\Tools"]
        end

    end

    B
    --> C["https://github.com/open-policy-agent/opa/releases"]
    --> D["Download Windows AMD64 Binary"]
    --> E["Extract ZIP Archive"]

    E
    --> F

    subgraph F["📂 Copy OPA Binary"]

        subgraph F1["Rename"]
            F11["opa.exe"]
        end

        subgraph F2["Copy"]
            F21["C:\KNIGHT\Tools"]
        end

        F1 --> F2

    end

    F
    --> G

    subgraph G["⚙️ Configure PATH Environment Variable"]

        G1["Edit the system environment variables"]
        --> G2["Environment Variables"]
        --> G3["System Variables"]
        --> G4["Select Path"]
        --> G5["Click Edit"]
        --> G6["Click New"]

        G6
        --> G7

        subgraph G7["Add PATH"]
            G71["C:\KNIGHT\Tools"]
        end

        G7
        --> G8["Click OK"]
        --> G9["Click OK"]
        --> G10["Restart all open CMD / PowerShell windows"]

    end

    G
    --> H

    subgraph H["💻 Command Prompt"]

        subgraph H1["Open"]
            H11["New Command Prompt"]
        end

        subgraph H2["Run"]
            H21["opa version"]
        end

        H1 --> H2

    end

    H
    --> I([OPA Installed Successfully])

    %% ===================================
    %% Styles
    %% ===================================

    classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef url fill:#6A1B9A,stroke:#8E24AA,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef path fill:#EF6C00,stroke:#E65100,stroke-width:3px,color:#ffffff,font-weight:bold;

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

# 🔍 Checkov Installation Workflow

```mermaid
flowchart TD

    A([Start])

    --> B

    subgraph B["🛡️ Install Checkov"]

        subgraph B1["Run"]
            B11["pip install checkov"]
        end

    end

    B
    --> C

    subgraph C["💻 Command Prompt"]

        subgraph C1["Open"]
            C11["New Command Prompt"]
        end

        subgraph C2["Run"]
            C21["checkov --version"]
        end

        C1 --> C2

    end

    C
    --> D([Checkov Installed Successfully])

    %% ===================================
    %% Styles
    %% ===================================

    classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    %% ===================================
    %% Apply Styles
    %% ===================================

    class B11,C21 cmd;

    class C11 process;

    class D success;
```

---

# 🔐 tfsec Installation Workflow

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

    subgraph G["⚙️ Configure PATH"]
        direction LR

        G1["Environment Variables"]

        --> G2["System PATH"]

        --> G3["Add C:\KNIGHT\Tools"]

    end

    G3
    --> H

    subgraph H["💻 Command Prompt"]
        direction LR

        subgraph H1["Run"]
            direction LR
            H11["tfsec --version"]
        end

    end

    H11
    --> I([tfsec Installed])

classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#fff;
classDef url fill:#6A1B9A,stroke:#8E24AA,stroke-width:3px,color:#fff;
classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#fff;
classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#fff;

class B11,F11,F21,G3,H11 cmd;
class C,D url;
class G1,G2 process;
class I success;
```

---

# 🛡️ Terrascan Installation Workflow

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

    subgraph G["⚙️ Configure PATH"]
        direction LR

        G1["Environment Variables"]

        --> G2["System PATH"]

        --> G3["Add C:\KNIGHT\Tools"]

    end

    G3
    --> H

    subgraph H["💻 Command Prompt"]
        direction LR

        subgraph H1["Run"]
            direction LR
            H11["terrascan version"]
        end

    end

    H11
    --> I

    subgraph I["📥 Initialize Policies"]
        direction LR

        subgraph I1["Run"]
            direction LR
            I11["terrascan init"]
        end

    end

    I11
    --> J([Terrascan Installed])

classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#fff;
classDef url fill:#6A1B9A,stroke:#8E24AA,stroke-width:3px,color:#fff;
classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#fff;
classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#fff;

class B11,F11,F21,G3,H11,I11 cmd;
class C,D url;
class G1,G2 process;
class J success;
```

---

# 📝 TFLint Installation Workflow

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
    --> C["https://github.com/terraform-linters/tflint/releases"]

    --> D["Download Windows AMD64 Binary"]

    --> E["Extract ZIP Archive"]

    E
    --> F

    subgraph F["📂 Copy TFLint Binary"]
        direction LR

        subgraph F1["Rename"]
            direction LR
            F11["tflint.exe"]
        end

        subgraph F2["Copy"]
            direction LR
            F21["C:\KNIGHT\Tools"]
        end

        F1 --> F2

    end

    F21
    --> G

    subgraph G["⚙️ Configure PATH"]
        direction LR

        G1["Environment Variables"]

        --> G2["System PATH"]

        --> G3["Add C:\KNIGHT\Tools"]

    end

    G3
    --> H

    subgraph H["💻 Command Prompt"]
        direction LR

        subgraph H1["Run"]
            direction LR
            H11["tflint --version"]
        end

    end

    H11
    --> I

    subgraph I["🔌 Initialize Plugins"]
        direction LR

        subgraph I1["Run"]
            direction LR
            I11["tflint --init"]
        end

    end

    I11
    --> J([TFLint Installed])

classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#fff;
classDef url fill:#6A1B9A,stroke:#8E24AA,stroke-width:3px,color:#fff;
classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#fff;
classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#fff;

class B11,F11,F21,G3,H11,I11 cmd;
class C,D url;
class G1,G2 process;
class J success;
```

---

# 📖 terraform-docs Installation Workflow

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
    --> C["https://github.com/terraform-docs/terraform-docs/releases"]

    --> D["Download Windows AMD64 Binary"]

    --> E["Extract ZIP Archive"]

    E
    --> F

    subgraph F["📂 Copy terraform-docs Binary"]
        direction LR

        subgraph F1["Rename"]
            direction LR
            F11["terraform-docs.exe"]
        end

        subgraph F2["Copy"]
            direction LR
            F21["C:\KNIGHT\Tools"]
        end

        F1 --> F2

    end

    F21
    --> G

    subgraph G["⚙️ Configure PATH"]
        direction LR

        G1["Environment Variables"]

        --> G2["System PATH"]

        --> G3["Add C:\KNIGHT\Tools"]

    end

    G3
    --> H

    subgraph H["💻 Command Prompt"]
        direction LR

        subgraph H1["Run"]
            direction LR
            H11["terraform-docs --version"]
        end

    end

    H11
    --> I

    subgraph I["📖 Generate Documentation"]
        direction LR

        subgraph I1["Run"]
            direction LR
            I11["terraform-docs markdown table ."]
        end

    end

    I11
    --> J([terraform-docs Installed])

classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#fff;
classDef url fill:#6A1B9A,stroke:#8E24AA,stroke-width:3px,color:#fff;
classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#fff;
classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#fff;

class B11,F11,F21,G3,H11,I11 cmd;
class C,D url;
class G1,G2 process;
class J success;
```

---

# 🪟 Configure the Windows PATH

After installing all required tools, add the following directories to the Windows **PATH Environment Variable**.

```text
C:\Terraform

C:\KNIGHT\Tools

C:\Users\<Your_User_Name>\AppData\Local\Programs\Python\Python313

C:\Users\<Your_User_Name>\AppData\Local\Programs\Python\Python313\Scripts
```

> **Note**
>
> Replace **`<Your_User_Name>`** with your Windows user profile name.
>
> Replace **`Python313`** with your installed Python version if different.

---

# 📋 Windows PATH Configuration Workflow

```mermaid
flowchart LR

A([Start])

-->

B["🪟 Open Windows Search"]

-->

C["⚙️ Edit the System Environment Variables"]

-->

D["📋 Environment Variables"]

-->

E["📂 System Variables"]

-->

F["📝 Select Path"]

-->

G["➕ Click Edit"]

-->

H["➕ Click New"]

-->

I["📂 Add Required Paths"]

-->

J["💾 Click OK"]

-->

K["🔄 Restart Command Prompt"]

-->

L([PATH Configured])

classDef system fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef path fill:#EF6C00,stroke:#E65100,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

class B,C,D,E,F,G,H,J,K system;

class I path;

class L success;
```

---

# 📂 Required PATH Entries

| Tool | PATH |
|------|------|
| Terraform | `C:\Terraform` |
| OPA | `C:\KNIGHT\Tools` |
| tfsec | `C:\KNIGHT\Tools` |
| Terrascan | `C:\KNIGHT\Tools` |
| TFLint | `C:\KNIGHT\Tools` |
| terraform-docs | `C:\KNIGHT\Tools` |
| Python | `C:\Users\<Your_User_Name>\AppData\Local\Programs\Python\Python313` |
| pip | `C:\Users\<Your_User_Name>\AppData\Local\Programs\Python\Python313\Scripts` |

> 💡 **Recommendation**
>
> Store all executable tools inside **`C:\KNIGHT\Tools`** to simplify maintenance and PATH configuration.

---

# 💻 Verification Commands

Run the following commands one by one in **Command Prompt (CMD)** to verify that all tools have been installed successfully.

```cmd
terraform version

python --version

pip --version

opa version

checkov --version

tfsec --version

terrascan version

tflint --version

terraform-docs --version
```

---

# 📷 Expected Output

```text
Terraform v1.xx.x

Python 3.xx.x

pip xx.x.x

Version: x.x.x
Build Commit: xxxxxxxxxxxxxxxxx

Checkov xx.x.x

==================================================

tfsec v1.xx.x

Version: v1.xx.x

TFLint version 0.xx.x

terraform-docs version v0.xx.x
```

---

# 📋 Verification Checklist

- [ ] Terraform installed successfully.
- [ ] Python installed successfully.
- [ ] pip installed successfully.
- [ ] OPA installed successfully.
- [ ] Checkov installed successfully.
- [ ] tfsec installed successfully.
- [ ] Terrascan installed successfully.
- [ ] TFLint installed successfully.
- [ ] terraform-docs installed successfully.
- [ ] Windows PATH configured successfully.
- [ ] Command Prompt restarted.
- [ ] All verification commands executed successfully.
- [ ] KNIGHT Local Terraform Quality Gate is ready.

---

# 🎯 Installation Summary

| Category | Status |
|----------|:------:|
| Terraform CLI | ✅ Installed |
| Python Runtime | ✅ Installed |
| Policy as Code (OPA) | ✅ Installed |
| Security Scanner (Checkov) | ✅ Installed |
| Security Scanner (tfsec) | ✅ Installed |
| Compliance Scanner (Terrascan) | ✅ Installed |
| Terraform Linter (TFLint) | ✅ Installed |
| Documentation Generator (terraform-docs) | ✅ Installed |


---

# 🚀 KNIGHT Local Terraform Quality Gate

After installing all required tools, the recommended local execution order is shown below.

```mermaid
flowchart LR

A["📝 terraform fmt"]

-->

B["⚙️ terraform init"]

-->

C["✅ terraform validate"]

-->

D["📝 TFLint"]

-->

E["🔍 Checkov"]

-->

F["🔐 tfsec"]

-->

G["🛡️ Terrascan"]

-->

H["⚖️ OPA"]

-->

I["📖 terraform-docs"]

-->

J["🚀 Ready for Deployment"]

%% ===================================
%% Styles
%% ===================================

classDef terraform fill:#623CE4,stroke:#4A148C,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef quality fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef security fill:#00838F,stroke:#006064,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef policy fill:#6A1B9A,stroke:#4A148C,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef docs fill:#EF6C00,stroke:#E65100,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

class A,B,C terraform;

class D quality;

class E,F,G security;

class H policy;

class I docs;

class J success;
```

---

# 📊 KNIGHT Tool Comparison Matrix

| Tool | Category | Purpose | Primary Command |
|------|----------|---------|-----------------|
| **Terraform** | Infrastructure as Code | Builds and manages infrastructure | `terraform apply` |
| **OPA** | Policy as Code | Enforces custom organizational policies | `opa eval` |
| **Checkov** | Security Scanner | Detects Infrastructure as Code security issues | `checkov -d .` |
| **tfsec** | Security Scanner | Identifies Terraform security vulnerabilities | `tfsec .` |
| **Terrascan** | Governance & Compliance | Validates security and compliance policies | `terrascan scan` |
| **TFLint** | Code Quality | Detects Terraform configuration issues | `tflint` |
| **terraform-docs** | Documentation | Generates Terraform module documentation | `terraform-docs markdown table .` |

---

# 📚 Official Resources

| Tool | Documentation | GitHub | Releases |
|------|---------------|---------|----------|
| **Terraform** | https://developer.hashicorp.com/terraform/docs | https://github.com/hashicorp/terraform | https://developer.hashicorp.com/terraform/install |
| **OPA** | https://www.openpolicyagent.org/docs | https://github.com/open-policy-agent/opa | https://github.com/open-policy-agent/opa/releases |
| **Checkov** | https://www.checkov.io | https://github.com/bridgecrewio/checkov | https://github.com/bridgecrewio/checkov/releases |
| **tfsec** | https://aquasecurity.github.io/tfsec | https://github.com/aquasecurity/tfsec | https://github.com/aquasecurity/tfsec/releases |
| **Terrascan** | https://runterrascan.io | https://github.com/tenable/terrascan | https://github.com/tenable/terrascan/releases |
| **TFLint** | https://github.com/terraform-linters/tflint | https://github.com/terraform-linters/tflint | https://github.com/terraform-linters/tflint/releases |
| **terraform-docs** | https://terraform-docs.io | https://github.com/terraform-docs/terraform-docs | https://github.com/terraform-docs/terraform-docs/releases |

---

# 📋 Final Verification Checklist

- [ ] Terraform CLI installed successfully.
- [ ] Python installed successfully.
- [ ] pip installed successfully.
- [ ] OPA installed successfully.
- [ ] Checkov installed successfully.
- [ ] tfsec installed successfully.
- [ ] Terrascan installed successfully.
- [ ] TFLint installed successfully.
- [ ] terraform-docs installed successfully.
- [ ] Windows PATH configured successfully.
- [ ] All verification commands executed successfully.
- [ ] KNIGHT Local Terraform Quality Gate completed successfully.

---

# 🏆 KNIGHT Environment Ready

🎉 Congratulations 🎉

You have successfully configured the complete **KNIGHT Local Terraform Quality Gate**.

Your local development environment now includes:

- ✅ Terraform CLI
- ✅ OPA
- ✅ Checkov
- ✅ tfsec
- ✅ Terrascan
- ✅ TFLint
- ✅ terraform-docs

This toolchain enables you to:

- 📝 Format Terraform code.
- ⚙️ Initialize Terraform projects.
- ✅ Validate Terraform configurations.
- 📝 Improve Terraform code quality.
- 🛡️ Perform Infrastructure as Code security scanning.
- ⚖️ Enforce organizational policies.
- 📖 Automatically generate Terraform documentation.
- 🚀 Build deployment-ready Infrastructure as Code.

---

# 🎯 Complete Local Validation Workflow

```mermaid
flowchart LR

A["👨‍💻 Write Terraform Code"]

-->

B["📝 terraform fmt"]

-->

C["⚙️ terraform init"]

-->

D["✅ terraform validate"]

-->

E["📝 TFLint"]

-->

F["🔍 Checkov"]

-->

G["🔐 tfsec"]

-->

H["🛡️ Terrascan"]

-->

I["⚖️ OPA"]

-->

J["📖 terraform-docs"]

-->

K["🚀 Deploy Infrastructure"]

classDef developer fill:#3949AB,stroke:#1A237E,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef terraform fill:#623CE4,stroke:#4A148C,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef quality fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef security fill:#00838F,stroke:#006064,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef policy fill:#6A1B9A,stroke:#4A148C,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef docs fill:#EF6C00,stroke:#E65100,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef deploy fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

class A developer;
class B,C,D terraform;
class E quality;
class F,G,H security;
class I policy;
class J docs;
class K deploy;
```

---

# 🙌 Thank You

Thank you for using the **KNIGHT Tools Installation Guide**.

This guide provides a unified installation workflow for the tools used throughout the **KNIGHT** project. Once your environment is configured, you're ready to explore the remaining KNIGHT documentation, execute the Local Terraform Quality Gate, and build secure, well-documented Infrastructure as Code.

**Happy Learning and Happy Automating! 🚀**
---