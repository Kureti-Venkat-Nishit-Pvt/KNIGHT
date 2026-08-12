# 🛡️ Checkov Installation Guide
![Security](https://img.shields.io/badge/Security-Checkov_|_Infrastructure_Security-2E7D32?style=for-the-badge)

**`Checkov`** is an open-source **Infrastructure as Code (IaC) `Security Scanner`** developed by Bridgecrew (Palo Alto Networks). It scans Terraform, Kubernetes, ARM Templates, CloudFormation, Dockerfiles, GitHub Actions and other Infrastructure as Code frameworks for security vulnerabilities, compliance violations and misconfigurations.

Within the **KNIGHT Framework**, Checkov performs static security analysis of Terraform code before infrastructure deployment, ensuring that security best practices are enforced during the Local Terraform Quality Gate.



# 📑 Table of Contents

[![📦 Overview](https://img.shields.io/badge/📦_Overview-Tool_Introduction-1565C0?style=for-the-badge)](#-overview)
[![🛠️ Prerequisites](https://img.shields.io/badge/🛠️_Prerequisites-System_Requirements-1565C0?style=for-the-badge)](#️-prerequisites)

[![📂 Local_Demo](https://img.shields.io/badge/📂_Local_Demo-Project_Setup-2E7D32?style=for-the-badge)](#-local-demo-project-setup)
[![📄 Demo_Files](https://img.shields.io/badge/📄_Demo_Files-Required_Files-2E7D32?style=for-the-badge)](#-demo-files-required)

[![🐍 Python_Installation](https://img.shields.io/badge/🐍_Python-Installation-3776AB?style=for-the-badge&logo=python&logoColor=white)](#-python-installation)

[![🛡️ Checkov_Installation](https://img.shields.io/badge/🛡️_Checkov-Installation-2E7D32?style=for-the-badge)](#-checkov-installation)

[![💻 Commands](https://img.shields.io/badge/💻_Commands-Variations-B71C1C?style=for-the-badge)](#-commands--variations)
[![📷 Sample_Output](https://img.shields.io/badge/📷_Sample-Output-B71C1C?style=for-the-badge)](#-sample-output)
[![🧪 Demo_Commands](https://img.shields.io/badge/🧪_Demo-Commands-B71C1C?style=for-the-badge)](#-demo-commands)
[![🎯 Expected_Result](https://img.shields.io/badge/🎯_Expected-Result-B71C1C?style=for-the-badge)](#-expected-result)

[![⚠️ Troubleshooting](https://img.shields.io/badge/⚠️_Troubleshooting-Common_Issues-EF6C00?style=for-the-badge)](#️-troubleshooting)
[![☑️ Installation_Checklist](https://img.shields.io/badge/☑️_Installation-Checklist-EF6C00?style=for-the-badge)](#-installation-checklist)

---

## 📊 Overview

| Question | Answer |
|----------|--------|
| **What is it?** | Checkov is an open-source Infrastructure as Code (IaC) `Security Scanner`. |
| **What is it used for?** | It scans Terraform and other IaC files for `security vulnerabilities`, `compliance violations` and `configuration issues`. |
| **When do we use it?** | `After` Terraform `validation` and `before` `deployment`. |
| **Why are we implementing it?** | To `identify` Terraform `security issues` before infrastructure is provisioned and demonstrate Infrastructure as Code security scanning within the KNIGHT Framework. |

---

# 🛠️ Prerequisites

Before installing **Checkov**, ensure the following requirements are met.

![Operating_System](https://img.shields.io/badge/Operating_System-Windows_10_|_Windows_11-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Terminal](https://img.shields.io/badge/Terminal-Command_Prompt_(CMD)_|_Required-1565C0?style=for-the-badge)

![Network](https://img.shields.io/badge/Network-Internet_Connection_|_Required-EF6C00?style=for-the-badge)

![Permissions](https://img.shields.io/badge/Permissions-Administrator_Access_|_Recommended-B71C1C?style=for-the-badge)

> **Note:** Python and **pip** are **not required before starting this guide**. They will be installed as part of the Checkov installation process.

---

# 📂 Local Demo Project Setup

The following project structure will be used throughout the Checkov demonstration.

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

C --> C1["checkov_report.txt"]

D --> D1["02-Checkov_Installation_Guide.md"]

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
| `checkov_report.txt` | ⭐ | Generated Checkov scan report |
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

C --> C1["📋 checkov_report.txt"]

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

![Installation](https://img.shields.io/badge/Installation-Python_pip-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Executable](https://img.shields.io/badge/Executable-checkov-B71C1C?style=for-the-badge)

![Verification](https://img.shields.io/badge/Verification-checkov_--version-623CE4?style=for-the-badge)

---

# 🌍 Official Resources

[![Documentation](https://img.shields.io/badge/📘_Documentation-Checkov-2E7D32?style=for-the-badge)](https://www.checkov.io/)

[![GitHub](https://img.shields.io/badge/💻_GitHub-bridgecrewio/checkov-181717?style=for-the-badge&logo=github)](https://github.com/bridgecrewio/checkov)

[![PyPI](https://img.shields.io/badge/🐍_PyPI-Checkov-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/checkov/)

---

# 🐍 Python Installation

Before installing **Checkov**, Python and **pip** must be installed on the local machine.

---

# 📋 Python Installation Workflow

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

# 📝 Step 1 – Download Python

Download the latest **Windows 64-bit Installer** from the official Python website.

[![Python Downloads](https://img.shields.io/badge/⬇️_Download-Python_Windows-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/windows/)

## 📦 Download Details

![Platform](https://img.shields.io/badge/🪟_Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Architecture](https://img.shields.io/badge/💻_Architecture-64--bit-1565C0?style=for-the-badge)

![Installer](https://img.shields.io/badge/📦_Installer-Executable_(.exe)-EF6C00?style=for-the-badge)

![Python](https://img.shields.io/badge/🐍_Python-Latest_Stable-3776AB?style=for-the-badge&logo=python&logoColor=white)

> **Note:** Always download the latest stable Windows release unless your organization specifies a particular Python version.

---

# 📝 Step 2 – Install Python

Run the downloaded installer.

## ⚠️ Important

Before clicking **Install Now**, enable the following option:

✅ **Add Python to PATH**

This ensures that both **Python** and **pip** are available from **Command Prompt (CMD)**.

Continue with the default installation settings until the installation completes.

---

# 📝 Step 3 – Verify Python Installation

Open a **new Command Prompt (CMD)** window.

Run the following command:

```cmd
python --version
```

### 📷 Expected Output

```text
Python 3.x.x
```

---

# 📝 Step 4 – Verify pip Installation

Run the following command:

```cmd
pip --version
```

### 📷 Expected Output

```text
pip xx.x.x from C:\Users\<username>\AppData\Local\Programs\Python\Python3xx\Lib\site-packages\pip (python 3.x)
```

---

# 🎯 Verification Checklist

| Check | Expected Result |
|--------|-----------------|
| Python installed successfully | ✅ |
| "Add Python to PATH" selected | ✅ |
| `python --version` executes | ✅ |
| `pip --version` executes | ✅ |
| Ready to install Checkov | ✅ |

---

# 💡 Installation Tips

- Always install the latest stable version of Python.
- Ensure **Add Python to PATH** is selected during installation.
- Restart **Command Prompt (CMD)** after installation.
- Verify both **Python** and **pip** before installing Checkov.
- Do not proceed to the Checkov installation until both verification commands execute successfully.

---

# 🛡️ Checkov Installation

After successfully installing **Python** and **pip**, you can now install **Checkov**.

---

# 📋 Checkov Installation Workflow

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

# 📝 Step 1 – Install Checkov

Install the latest stable version of **Checkov** using **pip**.

Run the following command:

```cmd
pip install checkov
```

---

## 📦 Installation Command

![Installer](https://img.shields.io/badge/🐍_Installer-pip-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Package](https://img.shields.io/badge/📦_Package-checkov-2E7D32?style=for-the-badge)

![Command](https://img.shields.io/badge/💻_Command-pip_install_checkov-B71C1C?style=for-the-badge)

> **Note:** An active internet connection is required to download the package from **PyPI**.

---

# 📝 Step 2 – Upgrade Checkov (Optional)

To upgrade an existing installation to the latest version, run:

```cmd
pip install --upgrade checkov
```

---

## 📦 Upgrade Command

![Upgrade](https://img.shields.io/badge/⬆️_Upgrade-checkov-2E7D32?style=for-the-badge)

![Command](https://img.shields.io/badge/💻_Command-pip_install_--upgrade_checkov-B71C1C?style=for-the-badge)

---

# 📝 Step 3 – Restart the Command Prompt

After installing **Checkov**, close the current **Command Prompt (CMD)** window.

## 📌 Restart Command Prompt

1. Close all open **`Command Prompt (CMD)`** windows.
2. Open a **`NEW` Command Prompt (CMD)** window.

> **⚠️ Important:** Restarting **Command Prompt** ensures that the newly installed **Checkov** executable is available for verification.

---

# 📝 Step 4 – Verify the Installation

Run the following command:

```cmd
checkov --version
```

---

## 📷 Expected Verification Output

```text
3.x.x
```

or

```text
Checkov 3.x.x
```

depending on the installed version.

---

## 📋 Verification Details

![Verification](https://img.shields.io/badge/Verification-checkov_--version-623CE4?style=for-the-badge)

![Expected](https://img.shields.io/badge/Expected-Checkov_3.x.x-2E7D32?style=for-the-badge)

---

# 🎯 Verification Checklist

- [ ] `pip install checkov` completed successfully.
- [ ] No installation errors were reported.
- [ ] Closed the existing Command Prompt (CMD).
- [ ] Opened a new Command Prompt (CMD).
- [ ] `checkov --version` executed successfully.
- [ ] Checkov version information displayed.
- [ ] Ready to perform Terraform security scanning.

---

# 💡 Installation Tips

- Install the latest stable release of **Checkov**.
- Ensure the installation completes without errors.
- Restart **Command Prompt (CMD)** before verification.
- Use `pip install --upgrade checkov` periodically to stay on the latest version.
- Verify the installation before scanning Terraform code.

---

# 💻 Commands & Variations

The following commands are commonly used while working with **Checkov**.

| Purpose | Command |
|----------|---------|
| Display Version | `checkov --version` |
| Scan Current Directory | `checkov -d .` |
| Scan Specific Folder | `checkov -d terraform` |
| Scan Single Terraform File | `checkov -f main.tf` |
| Quiet Mode | `checkov -d . --quiet` |
| Compact Output | `checkov -d . --compact` |
| Output as JSON | `checkov -d . -o json` |
| Output as CLI | `checkov -d . -o cli` |
| Output as JUnit XML | `checkov -d . -o junitxml` |
| Show Help | `checkov --help` |

---

# 📷 Sample Output

## ✅ Successful Scan

```text
       _               _
   ___| |__   ___  ___| | _____   __
  / __| '_ \ / _ \/ __| |/ / _ \ / /
 | (__| | | |  __/ (__|   < (_) / /
  \___|_| |_|\___|\___|_|\_\___/_/

By Bridgecrew.io | version: 3.x.x

terraform scan results:

Passed checks: 18

Failed checks: 2

Skipped checks: 0

Check: CKV_AWS_20
Resource: aws_s3_bucket.demo

Check: CKV_AWS_21
Resource: aws_security_group.demo
```

---

## 📊 Scan Summary

![Passed](https://img.shields.io/badge/Passed-18-success?style=for-the-badge)

![Failed](https://img.shields.io/badge/Failed-2-red?style=for-the-badge)

![Skipped](https://img.shields.io/badge/Skipped-0-lightgrey?style=for-the-badge)

---

# 🧪 Demo Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🔍 Verify Installation"]
        B1["checkov --version"]
    end

    B1 --> C1

    subgraph C["📂 Scan Current Project"]
        C1["checkov -d ."]
    end

    C1 --> D1

    subgraph D["📁 Scan Terraform Folder"]
        D1["checkov -d terraform"]
    end

    D1 --> E1

    subgraph E["📄 Scan Single Terraform File"]
        E1["checkov -f main.tf"]
    end

    E1 --> F1

    subgraph F["📊 Generate JSON Report"]
        F1["checkov -d . -o json"]
    end

    F1 --> G1

    subgraph G["💾 Save CLI Report"]
        G1["checkov -d . -o cli > checkov_report.txt"]
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

After completing the installation and running the demo commands:

- ✅ Checkov launches successfully.
- ✅ Terraform files are scanned without errors.
- ✅ Security findings are displayed.
- ✅ Passed, Failed, and Skipped checks are summarized.
- ✅ Reports can be exported in multiple formats.
- ✅ Ready to integrate into the KNIGHT Local Terraform Quality Gate.

---

# 📋 Verification Checklist

- [ ] `checkov --version` executed successfully.
- [ ] Current directory scanned successfully.
- [ ] Terraform folder scanned successfully.
- [ ] Security findings displayed.
- [ ] JSON report generated successfully.
- [ ] Report exported to `checkov_report.txt`.
- [ ] Ready for the KNIGHT security demonstration.

---

# 💡 Demo Tips

- Begin the demonstration with `checkov --version`.
- Scan the entire project using `checkov -d .`.
- Explain the meaning of **Passed**, **Failed**, and **Skipped** checks.
- Highlight one failed security check and discuss why it is important.
- Demonstrate exporting the scan results to a report file.
- Explain how Checkov fits into the KNIGHT Local Terraform Quality Gate before deployment.

---

# ⚠️ Troubleshooting

The following are common issues encountered during the installation and usage of **Checkov**.

| Error | Possible Cause | Resolution |
|--------|----------------|------------|
| `'python' is not recognized as an internal or external command` | Python is not installed or PATH is not configured | Install Python and ensure **Add Python to PATH** is selected during installation. |
| `'pip' is not recognized as an internal or external command` | pip is missing or PATH is not configured | Reinstall Python and verify pip is included in the installation. |
| `'checkov' is not recognized as an internal or external command` | Checkov installation failed or Command Prompt was not restarted | Restart Command Prompt and verify the installation using `pip show checkov`. |
| `ERROR: Could not find a version that satisfies the requirement checkov` | Internet connection unavailable or outdated Python version | Verify your internet connection and install the latest stable version of Python. |
| `Access is denied` | Insufficient permissions | Run **Command Prompt** as Administrator and retry the installation. |

---

# 💡 Common Resolution Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🐍 Verify Python"]
        B1["python --version"]
    end

    B1 --> C1

    subgraph C["📦 Verify pip"]
        C1["pip --version"]
    end

    C1 --> D1

    subgraph D["🛡️ Verify Checkov Installation"]
        D1["pip show checkov"]
    end

    D1 --> E1

    subgraph E["⬆️ Upgrade pip"]
        E1["python -m pip install --upgrade pip"]
    end

    E1 --> F1

    subgraph F["🚀 Upgrade Checkov"]
        F1["pip install --upgrade checkov"]
    end

    F1 --> G1

    subgraph G["🔄 Reinstall Checkov"]

        G11["pip uninstall checkov"]

        -->

        G12["pip install checkov"]

    end

    G12 --> H([Resolution Completed])

    %% ===================================
    %% Styles
    %% ===================================

    classDef command fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    %% ===================================
    %% Apply Styles
    %% ===================================

    class B1,C1,D1,E1,F1,G11,G12 command;

    class H success;
```

---

# 📋 Installation Checklist

- [ ] Downloaded the latest Python installer.
- [ ] Installed Python successfully.
- [ ] Enabled **Add Python to PATH** during installation.
- [ ] Verified the Python installation using `python --version`.
- [ ] Verified the pip installation using `pip --version`.
- [ ] Installed Checkov using `pip install checkov`.
- [ ] Restarted **Command Prompt (CMD)**.
- [ ] Verified the installation using `checkov --version`.
- [ ] Successfully scanned a Terraform project using `checkov -d .`.
- [ ] Generated a Checkov report successfully.

---

# 📚 References

[![📘 Documentation](https://img.shields.io/badge/📘_Documentation-Checkov-2E7D32?style=for-the-badge)](https://www.checkov.io/)

[![💻 GitHub Repository](https://img.shields.io/badge/💻_GitHub-bridgecrewio/checkov-181717?style=for-the-badge&logo=github)](https://github.com/bridgecrewio/checkov)

[![🐍 PyPI Package](https://img.shields.io/badge/🐍_PyPI-Checkov-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/checkov/)

[![📖 Python Documentation](https://img.shields.io/badge/🐍_Python-Official_Documentation-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://docs.python.org/3/)

[![⬇️ Python Downloads](https://img.shields.io/badge/⬇️_Download-Python_Windows-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/windows/)

---

