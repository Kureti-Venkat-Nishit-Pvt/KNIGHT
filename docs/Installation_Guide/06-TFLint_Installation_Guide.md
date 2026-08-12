# 🛡️ TFLint Installation Guide

![Quality](https://img.shields.io/badge/Quality-TFLint_|_Terraform_Linter-2E7D32?style=for-the-badge)

TFLint is an open-source **Terraform Linter** that analyzes Terraform configurations to detect syntax issues, deprecated arguments, provider-specific best practice violations, unused declarations, and potential configuration mistakes before infrastructure deployment.

Within the **KNIGHT Framework**, TFLint performs Terraform code quality analysis immediately after **terraform validate**, helping developers identify coding issues and provider-specific recommendations before security scanning begins.

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
| **What is it?** | TFLint is an open-source linter designed specifically for Terraform configurations. |
| **What is it used for?** | It analyzes Terraform code for syntax issues, deprecated arguments, provider best practices, and configuration quality. |
| **When do we use it?** | After `terraform validate` and before security scanning. |
| **Why are we implementing it?** | To improve Terraform code quality, detect provider-specific issues early, and enforce Infrastructure as Code best practices within the KNIGHT Local Terraform Quality Gate. |

---

# 🛠️ Prerequisites

Before installing **TFLint**, ensure the following requirements are available.

![Operating_System](https://img.shields.io/badge/Operating_System-Windows_10_|_Windows_11-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Terminal](https://img.shields.io/badge/Terminal-Command_Prompt_(CMD)_|_Required-1565C0?style=for-the-badge)

![Infrastructure](https://img.shields.io/badge/Software-Terraform_|_Installed-623CE4?style=for-the-badge&logo=terraform&logoColor=white)

![Network](https://img.shields.io/badge/Network-Internet_Connection_|_Required-EF6C00?style=for-the-badge)

![Permissions](https://img.shields.io/badge/Permissions-Administrator_Access_|_Recommended-B71C1C?style=for-the-badge)

---

# 📂 Local Demo Project Setup

The following project structure will be used throughout the TFLint demonstration.

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

C --> C1["tflint_report.json"]

D --> D1["05-TFLint_Installation_Guide.md"]

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
| `main.tf` | ✅ | Terraform configuration to lint |
| `provider.tf` | ✅ | Terraform provider configuration |
| `variables.tf` | ✅ | Terraform variables |
| `outputs.tf` | ✅ | Terraform outputs |
| `.tflint.hcl` | ⭐ | TFLint configuration |
| `tflint_report.json` | ⭐ | Generated lint report |
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
B --> B5["⚙️ .tflint.hcl"]

C --> C1["📋 tflint_report.json"]

classDef root fill:#4A148C,stroke:#6A1B9A,stroke-width:4px,color:#ffffff,font-weight:bold;
classDef folder fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;
classDef terraform fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#ffffff,font-weight:bold;
classDef config fill:#EF6C00,stroke:#E65100,stroke-width:2px,color:#ffffff,font-weight:bold;
classDef report fill:#00838F,stroke:#006064,stroke-width:2px,color:#ffffff,font-weight:bold;
classDef readme fill:#6A1B9A,stroke:#4A148C,stroke-width:2px,color:#ffffff,font-weight:bold;

class A root;
class B,C folder;
class B1,B2,B3,B4 terraform;
class B5 config;
class C1 report;
class D readme;
```

---

# 🌐 Download Information

![Category](https://img.shields.io/badge/Category-Code_Quality-2E7D32?style=for-the-badge)

![Installation](https://img.shields.io/badge/Installation-Windows_Binary-623CE4?style=for-the-badge)

![Executable](https://img.shields.io/badge/Executable-tflint.exe-B71C1C?style=for-the-badge)

![Verification](https://img.shields.io/badge/Verification-tflint_--version-623CE4?style=for-the-badge)

---

# 🌍 Official Resources

[![📘 Documentation](https://img.shields.io/badge/📘_Documentation-TFLint-2E7D32?style=for-the-badge)](https://github.com/terraform-linters/tflint)

[![💻 GitHub Repository](https://img.shields.io/badge/💻_GitHub-terraform--linters/tflint-181717?style=for-the-badge&logo=github)](https://github.com/terraform-linters/tflint)

[![⬇️ Releases](https://img.shields.io/badge/⬇️_Download-TFLint_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/terraform-linters/tflint/releases)

[![📖 Terraform Documentation](https://img.shields.io/badge/📖_Terraform-Official_Documentation-623CE4?style=for-the-badge&logo=terraform&logoColor=white)](https://developer.hashicorp.com/terraform/docs)

---

---

# 🛡️ TFLint Installation

Before using **TFLint**, download the Windows binary, configure the executable, initialize the plugins, and verify the installation.

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
            H21["tflint --version"]
        end

        H1 --> H2

    end

    H21
    --> I

    subgraph I["🔌 Initialize Plugins"]
        direction LR

        subgraph I1["Run"]
            direction LR
            I11["tflint --init"]
        end

    end

    I11
    --> J([TFLint Installed Successfully])

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

    class B11,F11,F21,G71,H21,I11 cmd;

    class C,D url;

    class G1,G2,G3,G4,G5,G6,G8,G9,G10,H11 process;

    class J success;
```

---

# 📝 Step 1 – Download TFLint

Download the latest **Windows AMD64** release from the official GitHub Releases page.

[![TFLint Releases](https://img.shields.io/badge/⬇️_Download-TFLint_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/terraform-linters/tflint/releases)

## 📦 Download Details

![Platform](https://img.shields.io/badge/🪟_Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Architecture](https://img.shields.io/badge/💻_Architecture-AMD64-1565C0?style=for-the-badge)

![File Type](https://img.shields.io/badge/📦_File_Type-ZIP_Archive-EF6C00?style=for-the-badge)

![Binary](https://img.shields.io/badge/⚙️_Binary-tflint.exe-623CE4?style=for-the-badge)

---

# 📝 Step 2 – Extract the ZIP Archive

Extract the downloaded ZIP archive to a temporary location.

---

# 📝 Step 3 – Copy the Binary

Copy **`tflint.exe`** to:

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

After updating the Windows **PATH Environment Variable**, close all open **Command Prompt (CMD)** windows.

Open a **new Command Prompt (CMD)** window before verifying the installation.

---

# 📝 Step 6 – Verify the Installation

Run the following command:

```cmd
tflint --version
```

---

# 📷 Expected Verification Output

```text
TFLint version 0.xx.x
```

---

# 📝 Step 7 – Initialize TFLint Plugins

Run the following command:

```cmd
tflint --init
```

This downloads and installs the required provider plugins defined in the **`.tflint.hcl`** configuration file.

---

# 📷 Expected Plugin Initialization Output

```text
Installing "terraform" plugin...

Plugin installed successfully.

All plugins are ready.
```

---

# 📋 Verification Checklist

- [ ] Downloaded the Windows AMD64 binary.
- [ ] Extracted the ZIP archive.
- [ ] Renamed the executable to **tflint.exe**.
- [ ] Copied **tflint.exe** to `C:\KNIGHT\Tools`.
- [ ] Added `C:\KNIGHT\Tools` to the Windows PATH.
- [ ] Restarted **Command Prompt (CMD)**.
- [ ] Verified the installation using `tflint --version`.
- [ ] Initialized the plugins using `tflint --init`.
- [ ] Ready for Terraform code quality analysis.

---

# 💡 Installation Tips

- Download the latest stable **Windows AMD64** release.
- Store all KNIGHT CLI tools under **`C:\KNIGHT\Tools`**.
- Restart **Command Prompt (CMD)** after updating the PATH.
- Always execute **`tflint --init`** before running TFLint in a new project.
- Keep your provider plugins up to date by rerunning **`tflint --init`** whenever the configuration changes.

---

---

# 💻 Commands & Variations

The following commands are commonly used while working with **TFLint**.

| Purpose | Command |
|----------|---------|
| Display Version | `tflint --version` |
| Initialize Plugins | `tflint --init` |
| Lint Current Directory | `tflint` |
| Lint Specific Terraform Folder | `tflint terraform` |
| Generate JSON Report | `tflint --format json` |
| Enable Recursive Scan | `tflint --recursive` |
| Show Help | `tflint --help` |

---

# 📷 Sample Output

## ✅ Successful Scan

```text
$ tflint

3 issue(s) found:

Warning: terraform_required_version

  on versions.tf line 1:

Terraform version constraint is missing.

------------------------------------------------------

Warning: terraform_required_providers

  on provider.tf line 2:

Provider version constraint is missing.

------------------------------------------------------

Notice: aws_instance_invalid_type

  on main.tf line 10:

Instance type should follow provider recommendations.

------------------------------------------------------

3 issue(s) detected.
```

---

## 📊 Scan Summary

![Errors](https://img.shields.io/badge/Errors-0-success?style=for-the-badge)

![Warnings](https://img.shields.io/badge/Warnings-2-orange?style=for-the-badge)

![Notices](https://img.shields.io/badge/Notices-1-blue?style=for-the-badge)

---

# 🧪 Demo Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🔍 Verify Installation"]

        subgraph B2["Run"]
            direction LR
            B1["tflint --version"]
        end

    end

    B1
    --> C1

    subgraph C["🔌 Initialize Plugins"]

        subgraph C2["Run"]
            direction LR
            C1["tflint --init"]
        end

    end

    C1
    --> D1

    subgraph D["📂 Lint Current Project"]

        subgraph D2["Run"]
            direction LR
            D1["tflint"]
        end

    end

    D1
    --> E1

    subgraph E["📁 Lint Terraform Folder"]

        subgraph E2["Run"]
            direction LR
            E1["tflint terraform"]
        end

    end

    E1
    --> F1

    subgraph F["📊 Generate JSON Report"]

        subgraph F2["Run"]
            direction LR
            F1["tflint --format json"]
        end

    end

    F1
    --> G([Demo Completed])

    %% ===================================
    %% Styles
    %% ===================================

    classDef command fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    class B1,C1,D1,E1,F1 command;

    class G success;
```

---

# 🎯 Expected Result

After completing the demonstration:

- ✅ TFLint launches successfully.
- ✅ Provider plugins initialize successfully.
- ✅ Terraform configuration is analyzed.
- ✅ Syntax issues and best practice recommendations are displayed.
- ✅ JSON output is generated successfully.
- ✅ Ready for integration into the **KNIGHT Local Terraform Quality Gate**.

---

# 📋 Verification Checklist

- [ ] `tflint --version` executed successfully.
- [ ] `tflint --init` completed successfully.
- [ ] Current project linted successfully.
- [ ] Terraform folder linted successfully.
- [ ] JSON report generated successfully.
- [ ] Ready for the KNIGHT TFLint demonstration.

---

# 💡 Demo Tips

- Begin by verifying the installation using `tflint --version`.
- Execute `tflint --init` before running the first lint analysis.
- Explain that **TFLint focuses on Terraform code quality**, unlike Checkov, tfsec, and Terrascan, which focus primarily on security and compliance.
- Demonstrate linting the current Terraform project.
- Highlight one warning or recommendation and explain why it improves Terraform code quality.
- Generate a JSON report to demonstrate CI/CD integration.
- Explain where TFLint fits within the **KNIGHT Local Terraform Quality Gate**.

---
---

# ⚠️ Troubleshooting

The following are common issues encountered during the installation and usage of **TFLint**.

| Error | Possible Cause | Resolution |
|--------|----------------|------------|
| `'tflint' is not recognized as an internal or external command` | `tflint.exe` is not available in the Windows PATH | Verify that `tflint.exe` exists in `C:\KNIGHT\Tools`, add the directory to the PATH, and restart Command Prompt. |
| `Plugin not found` | Provider plugins have not been initialized | Execute `tflint --init` before running the first lint scan. |
| `No Terraform files found` | Incorrect working directory | Navigate to the folder containing the Terraform (`*.tf`) files. |
| `Failed to load Terraform configuration` | Invalid Terraform configuration | Run `terraform init` and `terraform validate` before executing TFLint. |
| `Configuration file ".tflint.hcl" not found` | TFLint configuration file is missing | Create a `.tflint.hcl` configuration file or use the default configuration. |
| `Access is denied` | Insufficient permissions | Open **Command Prompt (CMD)** as Administrator and retry. |

---

# 💡 Common Resolution Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🔍 Verify TFLint Installation"]

        subgraph B2["Run"]
            direction LR
            B1["tflint --version"]
        end

    end

    B1
    --> C1

    subgraph C["🔌 Initialize Plugins"]

        subgraph C2["Run"]
            direction LR
            C1["tflint --init"]
        end

    end

    C1
    --> D1

    subgraph D["📂 Verify Current Directory"]

        subgraph D2["Run"]
            direction LR
            D1["dir"]
        end

    end

    D1
    --> E1

    subgraph E["⚙️ Initialize Terraform"]

        subgraph E2["Run"]
            direction LR
            E1["terraform init"]
        end

    end

    E1
    --> F1

    subgraph F["✅ Validate Terraform"]

        subgraph F2["Run"]
            direction LR
            F1["terraform validate"]
        end

    end

    F1
    --> G1

    subgraph G["📝 Re-run TFLint"]

        subgraph G2["Run"]
            direction LR
            G1["tflint"]
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
- [ ] Renamed the executable to **tflint.exe**.
- [ ] Copied **tflint.exe** to `C:\KNIGHT\Tools`.
- [ ] Added `C:\KNIGHT\Tools` to the Windows **PATH**.
- [ ] Restarted **Command Prompt (CMD)**.
- [ ] Verified the installation using `tflint --version`.
- [ ] Initialized the provider plugins using `tflint --init`.
- [ ] Successfully analyzed a Terraform project.
- [ ] Ready for the **KNIGHT Local Terraform Quality Gate**.

---


---

# 📚 References

[![📘 Documentation](https://img.shields.io/badge/📘_Documentation-TFLint-2E7D32?style=for-the-badge)](https://github.com/terraform-linters/tflint)
[![💻 GitHub Repository](https://img.shields.io/badge/💻_GitHub-terraform--linters/tflint-181717?style=for-the-badge&logo=github)](https://github.com/terraform-linters/tflint)

[![⬇️ Releases](https://img.shields.io/badge/⬇️_Download-TFLint_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/terraform-linters/tflint/releases)
[![📖 Terraform Documentation](https://img.shields.io/badge/📖_Terraform-Official_Documentation-623CE4?style=for-the-badge&logo=terraform&logoColor=white)](https://developer.hashicorp.com/terraform/docs)

---

# 🔄 TFLint in the KNIGHT Local Quality Gate

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

classDef quality fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef security fill:#00838F,stroke:#006064,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef docs fill:#EF6C00,stroke:#E65100,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

%% ===================================
%% Apply Styles
%% ===================================

class A,B,C terraform;

class D quality;

class E,F,G security;

class H docs;

class I success;
```

---

# 📌 Key Takeaways

| Topic | Summary |
|--------|---------|
| **Tool Category** | Terraform Code Quality & Linting Tool |
| **Primary Purpose** | Detect Terraform syntax issues, configuration mistakes, and provider-specific best practice violations |
| **Input** | Terraform configuration files (`*.tf`) |
| **Output** | Warnings, notices, and recommendations |
| **Plugin Support** | Terraform provider plugins |
| **Integration Point** | KNIGHT Local Terraform Quality Gate |
| **Verification Command** | `tflint --version` |
| **Plugin Initialization** | `tflint --init` |
| **Primary Analysis Command** | `tflint` |

---
