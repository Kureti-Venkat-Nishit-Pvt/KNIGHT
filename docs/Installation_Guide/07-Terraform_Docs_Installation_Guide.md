# 📖 terraform-docs Installation Guide

![Documentation](https://img.shields.io/badge/Documentation-terraform--docs_|_Terraform_Documentation-2E7D32?style=for-the-badge)

terraform-docs is an open-source documentation generator that automatically creates documentation for Terraform modules. It extracts variables, outputs, providers, requirements, resources, and module information directly from Terraform source code and formats it into Markdown, HTML, JSON, YAML, or other supported output formats.

Within the **KNIGHT Framework**, terraform-docs is executed after all validation, linting, security scanning, and compliance checks have completed successfully. It automatically generates consistent and up-to-date Terraform module documentation, ensuring infrastructure code remains well documented and easy to maintain.

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
| **What is it?** | terraform-docs is an open-source documentation generator for Terraform modules. |
| **What is it used for?** | It automatically generates documentation from Terraform source code. |
| **When do we use it?** | After validation, linting, security scanning, and before publishing or deployment. |
| **Why are we implementing it?** | To automate Terraform documentation, eliminate manual documentation effort, and maintain accurate infrastructure documentation within the KNIGHT Local Terraform Quality Gate. |

---

# 🛠️ Prerequisites

Before installing **terraform-docs**, ensure the following requirements are available.

![Operating_System](https://img.shields.io/badge/Operating_System-Windows_10_|_Windows_11-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Terminal](https://img.shields.io/badge/Terminal-Command_Prompt_(CMD)_|_Required-1565C0?style=for-the-badge)

![Infrastructure](https://img.shields.io/badge/Software-Terraform_|_Installed-623CE4?style=for-the-badge&logo=terraform&logoColor=white)

![Documentation](https://img.shields.io/badge/Output-Markdown_Documentation-2E7D32?style=for-the-badge)

![Network](https://img.shields.io/badge/Network-Internet_Connection_|_Required-EF6C00?style=for-the-badge)

![Permissions](https://img.shields.io/badge/Permissions-Administrator_Access_|_Recommended-B71C1C?style=for-the-badge)

---

# 📂 Local Demo Project Setup

The following project structure will be used throughout the terraform-docs demonstration.

```mermaid
flowchart TB

A["📁 Terraform_Demo"]

A --> B["📂 terraform"]

A --> C["📂 docs"]

A --> D["📂 reports"]

B --> B1["main.tf"]
B --> B2["provider.tf"]
B --> B3["variables.tf"]
B --> B4["outputs.tf"]

C --> C1["README.md"]

D --> D1["terraform-docs_output.md"]

classDef root fill:#4A148C,stroke:#6A1B9A,stroke-width:4px,color:#ffffff,font-weight:bold;
classDef folder fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;
classDef terraform fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#ffffff,font-weight:bold;
classDef docs fill:#EF6C00,stroke:#E65100,stroke-width:2px,color:#ffffff,font-weight:bold;

class A root;
class B,C,D folder;
class B1,B2,B3,B4,C1,D1 docs;
```

---

# 📄 Demo Files Required

| File | Required | Purpose |
|------|:--------:|---------|
| `main.tf` | ✅ | Terraform resources |
| `provider.tf` | ✅ | Terraform providers |
| `variables.tf` | ✅ | Terraform input variables |
| `outputs.tf` | ✅ | Terraform outputs |
| `README.md` | ⭐ | Generated documentation |
| `.terraform-docs.yml` | ⭐ | terraform-docs configuration |
| `terraform-docs_output.md` | ⭐ | Generated documentation output |

---

# 📁 Demo File Structure

```mermaid
flowchart TB

A["📁 Terraform_Demo"]

A --> B["📂 terraform"]

A --> C["📂 docs"]

A --> D["📄 README.md"]

B --> B1["📜 main.tf"]
B --> B2["⚙️ provider.tf"]
B --> B3["📝 variables.tf"]
B --> B4["📤 outputs.tf"]

C --> C1["⚙️ .terraform-docs.yml"]
C --> C2["📖 terraform-docs_output.md"]

classDef root fill:#4A148C,stroke:#6A1B9A,stroke-width:4px,color:#ffffff,font-weight:bold;
classDef folder fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;
classDef terraform fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#ffffff,font-weight:bold;
classDef config fill:#EF6C00,stroke:#E65100,stroke-width:2px,color:#ffffff,font-weight:bold;
classDef output fill:#00838F,stroke:#006064,stroke-width:2px,color:#ffffff,font-weight:bold;
classDef readme fill:#6A1B9A,stroke:#4A148C,stroke-width:2px,color:#ffffff,font-weight:bold;

class A root;
class B,C folder;
class B1,B2,B3,B4 terraform;
class C1 config;
class C2 output;
class D readme;
```

---

# 🌐 Download Information

![Category](https://img.shields.io/badge/Category-Documentation-2E7D32?style=for-the-badge)

![Installation](https://img.shields.io/badge/Installation-Windows_Binary-623CE4?style=for-the-badge)

![Executable](https://img.shields.io/badge/Executable-terraform--docs.exe-B71C1C?style=for-the-badge)

![Verification](https://img.shields.io/badge/Verification-terraform--docs_--version-623CE4?style=for-the-badge)

---

# 🌍 Official Resources

[![📘 Documentation](https://img.shields.io/badge/📘_Documentation-terraform--docs-2E7D32?style=for-the-badge)](https://terraform-docs.io/)

[![💻 GitHub Repository](https://img.shields.io/badge/💻_GitHub-terraform--docs/terraform--docs-181717?style=for-the-badge&logo=github)](https://github.com/terraform-docs/terraform-docs)

[![⬇️ Releases](https://img.shields.io/badge/⬇️_Download-terraform--docs_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/terraform-docs/terraform-docs/releases)

[![📖 Terraform Documentation](https://img.shields.io/badge/📖_Terraform-Official_Documentation-623CE4?style=for-the-badge&logo=terraform&logoColor=white)](https://developer.hashicorp.com/terraform/docs)

---
---

# 📖 terraform-docs Installation

Before using **terraform-docs**, download the Windows binary, configure the executable, verify the installation, and generate your first Terraform module documentation.

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
            H21["terraform-docs --version"]
        end

        H1 --> H2

    end

    H21
    --> I

    subgraph I["📖 Generate Documentation"]
        direction LR

        subgraph I1["Run"]
            direction LR
            I11["terraform-docs markdown table ."]
        end

    end

    I11
    --> J([terraform-docs Installed Successfully])

    %% ===================================
    %% Styles
    %% ===================================

    classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef url fill:#6A1B9A,stroke:#8E24AA,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    class B11,F11,F21,G71,H21,I11 cmd;

    class C,D url;

    class G1,G2,G3,G4,G5,G6,G8,G9,G10,H11 process;

    class J success;
```

---

# 📝 Step 1 – Download terraform-docs

Download the latest **Windows AMD64** release from the official GitHub Releases page.

[![terraform-docs Releases](https://img.shields.io/badge/⬇️_Download-terraform--docs_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/terraform-docs/terraform-docs/releases)

## 📦 Download Details

![Platform](https://img.shields.io/badge/🪟_Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)

![Architecture](https://img.shields.io/badge/💻_Architecture-AMD64-1565C0?style=for-the-badge)

![File Type](https://img.shields.io/badge/📦_File_Type-ZIP_Archive-EF6C00?style=for-the-badge)

![Binary](https://img.shields.io/badge/⚙️_Binary-terraform--docs.exe-623CE4?style=for-the-badge)

---

# 📝 Step 2 – Extract the ZIP Archive

Extract the downloaded ZIP archive to a temporary location.

---

# 📝 Step 3 – Copy the Binary

Copy **`terraform-docs.exe`** to:

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
terraform-docs --version
```

---

# 📷 Expected Verification Output

```text
terraform-docs version v0.xx.x
```

---

# 📝 Step 7 – Generate Documentation

Navigate to your Terraform project folder and run:

```cmd
terraform-docs markdown table .
```

This command automatically generates documentation for the Terraform module in **Markdown Table** format.

---

# 📷 Expected Output

```text
README.md generated successfully
```

or

```text
Outputs generated in Markdown format.
```

depending on the command used.

---

# 📋 Verification Checklist

- [ ] Downloaded the Windows AMD64 binary.
- [ ] Extracted the ZIP archive.
- [ ] Renamed the executable to **terraform-docs.exe**.
- [ ] Copied **terraform-docs.exe** to `C:\KNIGHT\Tools`.
- [ ] Added `C:\KNIGHT\Tools` to the Windows PATH.
- [ ] Restarted **Command Prompt (CMD)**.
- [ ] Verified the installation using `terraform-docs --version`.
- [ ] Generated Terraform documentation successfully.
- [ ] Ready for automatic Terraform documentation generation.

---

# 💡 Installation Tips

- Download the latest stable **Windows AMD64** release.
- Store all KNIGHT CLI tools under **`C:\KNIGHT\Tools`**.
- Restart **Command Prompt (CMD)** after updating the PATH.
- Generate documentation after updating Terraform resources, variables, or outputs.
- Automate documentation generation as part of your CI/CD pipeline.

---
---

# 💻 Commands & Variations

The following commands are commonly used while working with **terraform-docs**.

| Purpose | Command |
|----------|---------|
| Display Version | `terraform-docs --version` |
| Generate Markdown Table | `terraform-docs markdown table .` |
| Update README.md | `terraform-docs markdown table --output-file README.md .` |
| Generate JSON Output | `terraform-docs json .` |
| Generate YAML Output | `terraform-docs yaml .` |
| Generate HTML Output | `terraform-docs html .` |
| Generate Markdown Document | `terraform-docs markdown document .` |
| Show Help | `terraform-docs --help` |

---

# 📷 Sample Output

## ✅ Generated Terraform Documentation

````text
# Terraform Module

## Requirements

| Name | Version |
|------|---------|
| terraform | >= 1.5.0 |

---

## Providers

| Name | Version |
|------|---------|
| aws | ~> 5.0 |

---

## Resources

| Name | Type |
|------|------|
| aws_resource_group.example | Resource |

---

## Inputs

| Name | Description | Type | Default |
|------|-------------|------|---------|
| location | Azure Region | string | n/a |

---

## Outputs

| Name | Description |
|------|-------------|
| resource_group_name | Resource Group Name |

````

---

# 🧪 Demo Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🔍 Verify Installation"]

        subgraph B2["Run"]
            direction LR
            B1["terraform-docs --version"]
        end

    end

    B1
    --> C1

    subgraph C["📂 Generate Markdown Table"]

        subgraph C2["Run"]
            direction LR
            C1["terraform-docs markdown table ."]
        end

    end

    C1
    --> D1

    subgraph D["📝 Update README.md"]

        subgraph D2["Run"]
            direction LR
            D1["terraform-docs markdown table --output-file README.md ."]
        end

    end

    D1
    --> E1

    subgraph E["📊 Generate JSON Output"]

        subgraph E2["Run"]
            direction LR
            E1["terraform-docs json ."]
        end

    end

    E1
    --> F1

    subgraph F["📄 Generate YAML Output"]

        subgraph F2["Run"]
            direction LR
            F1["terraform-docs yaml ."]
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

- ✅ terraform-docs launches successfully.
- ✅ Terraform module documentation is generated automatically.
- ✅ README.md is updated with the latest module information.
- ✅ Variables, outputs, providers, resources, and requirements are extracted automatically.
- ✅ Documentation is generated in multiple output formats (Markdown, JSON, YAML, HTML).
- ✅ Ready for integration into the **KNIGHT Local Terraform Quality Gate**.

---

# 📋 Verification Checklist

- [ ] `terraform-docs --version` executed successfully.
- [ ] Markdown table generated successfully.
- [ ] README.md updated successfully.
- [ ] JSON documentation generated successfully.
- [ ] YAML documentation generated successfully.
- [ ] HTML documentation generated successfully.
- [ ] Terraform variables documented successfully.
- [ ] Terraform outputs documented successfully.
- [ ] Terraform providers documented successfully.
- [ ] Ready for the **KNIGHT terraform-docs** demonstration.

---

# 💡 Demo Tips

- Begin by verifying the installation using `terraform-docs --version`.
- Demonstrate generating a **Markdown Table** from the Terraform module.
- Show how terraform-docs automatically updates the **README.md** file.
- Explain that terraform-docs extracts:
  - Variables
  - Outputs
  - Providers
  - Resources
  - Requirements
- Demonstrate generating documentation in **JSON**, **YAML**, and **HTML** formats.
- Explain how terraform-docs keeps documentation synchronized with the Terraform source code.
- Highlight that terraform-docs eliminates manual documentation updates and improves consistency across Terraform modules.
- Conclude by showing how terraform-docs integrates as the final stage of the **KNIGHT Local Terraform Quality Gate**, producing deployment-ready documentation.

---


# ⚠️ Troubleshooting

The following are common issues encountered during the installation and usage of **terraform-docs**.

| Error | Possible Cause | Resolution |
|--------|----------------|------------|
| `'terraform-docs' is not recognized as an internal or external command` | `terraform-docs.exe` is not available in the Windows PATH | Verify that `terraform-docs.exe` exists in `C:\KNIGHT\Tools`, add the directory to the PATH, and restart Command Prompt. |
| `No Terraform configuration files found` | Current directory does not contain any `.tf` files | Navigate to the Terraform module directory before running terraform-docs. |
| `README.md was not generated` | Incorrect command or output location | Verify the command syntax and ensure the output directory exists. |
| `Failed to parse Terraform configuration` | Invalid Terraform syntax | Run `terraform init` and `terraform validate` before generating documentation. |
| `Configuration file ".terraform-docs.yml" not found` | Optional configuration file is missing | Create a `.terraform-docs.yml` configuration file or use the default settings. |
| `Access is denied` | Insufficient permissions | Open **Command Prompt (CMD)** as Administrator and retry. |

---

# 💡 Common Resolution Commands

```mermaid
flowchart LR

    A([Start])

    --> B1

    subgraph B["🔍 Verify terraform-docs Installation"]

        subgraph B2["Run"]
            direction LR
            B1["terraform-docs --version"]
        end

    end

    B1
    --> C1

    subgraph C["📂 Verify Current Directory"]

        subgraph C2["Run"]
            direction LR
            C1["dir"]
        end

    end

    C1
    --> D1

    subgraph D["⚙️ Initialize Terraform"]

        subgraph D2["Run"]
            direction LR
            D1["terraform init"]
        end

    end

    D1
    --> E1

    subgraph E["✅ Validate Terraform"]

        subgraph E2["Run"]
            direction LR
            E1["terraform validate"]
        end

    end

    E1
    --> F1

    subgraph F["📖 Generate Documentation"]

        subgraph F2["Run"]
            direction LR
            F1["terraform-docs markdown table ."]
        end

    end

    F1
    --> G1

    subgraph G["📝 Update README.md"]

        subgraph G2["Run"]
            direction LR
            G1["terraform-docs markdown table --output-file README.md ."]
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
- [ ] Renamed the executable to **terraform-docs.exe**.
- [ ] Copied **terraform-docs.exe** to `C:\KNIGHT\Tools`.
- [ ] Added `C:\KNIGHT\Tools` to the Windows **PATH**.
- [ ] Restarted **Command Prompt (CMD)**.
- [ ] Verified the installation using `terraform-docs --version`.
- [ ] Generated Terraform documentation successfully.
- [ ] Updated the `README.md` file successfully.
- [ ] Generated documentation in Markdown format.
- [ ] Ready for the **KNIGHT Local Terraform Quality Gate**.

---

# 📚 References

[![📘 Documentation](https://img.shields.io/badge/📘_Documentation-terraform--docs-2E7D32?style=for-the-badge)](https://terraform-docs.io/)
[![💻 GitHub Repository](https://img.shields.io/badge/💻_GitHub-terraform--docs/terraform--docs-181717?style=for-the-badge&logo=github)](https://github.com/terraform-docs/terraform-docs)

[![⬇️ Releases](https://img.shields.io/badge/⬇️_Download-terraform--docs_Releases-623CE4?style=for-the-badge&logo=github)](https://github.com/terraform-docs/terraform-docs/releases)
[![📖 Terraform Documentation](https://img.shields.io/badge/📖_Terraform-Official_Documentation-623CE4?style=for-the-badge&logo=terraform&logoColor=white)](https://developer.hashicorp.com/terraform/docs)

---

# 🏁 Conclusion

Congratulations! 🎉

You have successfully:

- ✅ Downloaded the **terraform-docs** Windows binary.
- ✅ Installed **terraform-docs** on your local machine.
- ✅ Configured the Windows **PATH** environment variable.
- ✅ Verified the installation using **Command Prompt (CMD)**.
- ✅ Generated Terraform module documentation automatically.
- ✅ Updated the **README.md** file directly from Terraform source code.
- ✅ Generated documentation in multiple output formats.
- ✅ Completed the final stage of the **KNIGHT Local Terraform Quality Gate**.

terraform-docs is now ready to automatically generate accurate, consistent, and up-to-date documentation for your Terraform modules, eliminating manual documentation effort and improving maintainability.

---

# 🔄 Complete KNIGHT Local Terraform Quality Gate

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

H["⚖️ OPA"]

-->

I["📖 terraform-docs"]

-->

J["🚀 Deployment Ready"]

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

# 📌 Complete KNIGHT Tool Summary

| Tool | Category | Purpose |
|------|----------|---------|
| **terraform fmt** | Formatting | Standardizes Terraform code formatting |
| **terraform init** | Initialization | Downloads providers and initializes the working directory |
| **terraform validate** | Validation | Validates Terraform configuration syntax |
| **TFLint** | Code Quality | Detects Terraform syntax issues and provider best practices |
| **Checkov** | Security | Identifies Infrastructure as Code security and compliance issues |
| **tfsec** | Security | Detects Terraform-specific security vulnerabilities |
| **Terrascan** | Governance | Enforces security, governance, and compliance policies |
| **OPA** | Policy as Code | Evaluates custom organizational policies |
| **terraform-docs** | Documentation | Automatically generates Terraform documentation |

---

# 🎯 KNIGHT Demo Checklist

- [ ] Terraform installed and verified.
- [ ] OPA installed and policy evaluation completed.
- [ ] Checkov installed and security scan executed.
- [ ] tfsec installed and Terraform security analysis completed.
- [ ] Terrascan installed and compliance scan completed.
- [ ] TFLint installed and Terraform lint analysis completed.
- [ ] terraform-docs installed and documentation generated.
- [ ] Local Terraform Quality Gate executed successfully.
- [ ] Demo project validated end-to-end.
- [ ] Ready for the KNIGHT live demonstration.

---
