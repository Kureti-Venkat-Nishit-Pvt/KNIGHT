# 📜 OPA Installation Guide

OPA (Open Policy Agent) is an open-source **Policy-as-Code** engine used to define and enforce policies across cloud infrastructure, Kubernetes, APIs, CI/CD pipelines, and Infrastructure as Code (IaC). Within the KNIGHT framework, OPA evaluates Terraform resources against custom Rego policies before infrastructure is deployed, helping ensure that organizational governance and compliance requirements are consistently enforced.


## 📑 Table of Contents

[![📦 Overview](https://img.shields.io/badge/📦_Overview-Tool_Introduction-1565C0?style=for-the-badge)](#-overview)
[![🛠️ Prerequisites](https://img.shields.io/badge/🛠️_Prerequisites-System_Requirements-1565C0?style=for-the-badge)](#️-prerequisites)

[![📂 Local Demo Project Setup](https://img.shields.io/badge/📂_Local_Demo-Project_Setup-2E7D32?style=for-the-badge)](#-local-demo-project-setup)
[![📄 Demo Files Required](https://img.shields.io/badge/📄_Demo_Files-Required_Files-2E7D32?style=for-the-badge)](#-demo-files-required)

[![🌐 Download Information](https://img.shields.io/badge/🌐_Download-Information-6A1B9A?style=for-the-badge)](#-download-information)
[![📋 Installation Workflow](https://img.shields.io/badge/📋_Installation-Workflow-6A1B9A?style=for-the-badge)](#-installation-workflow)
[![📝 Installation Steps](https://img.shields.io/badge/📝_Installation-Step--by--Step-6A1B9A?style=for-the-badge)](#-installation-steps)

[![💻 Commands & Variations](https://img.shields.io/badge/💻_Commands-Variations-B71C1C?style=for-the-badge)](#-commands--variations)
[![📷 Sample Output](https://img.shields.io/badge/📷_Sample-Output-B71C1C?style=for-the-badge)](#-sample-output)
[![🧪 Demo Commands](https://img.shields.io/badge/🧪_Demo-Commands-B71C1C?style=for-the-badge)](#-demo-commands)
[![🎯 Expected Result](https://img.shields.io/badge/🎯_Expected-Result-B71C1C?style=for-the-badge)](#-expected-result)

[![⚠️ Troubleshooting](https://img.shields.io/badge/⚠️_Troubleshooting-Common_Issues-EF6C00?style=for-the-badge)](#️-troubleshooting)
[![☑️ Installation Checklist](https://img.shields.io/badge/☑️_Installation-Checklist-EF6C00?style=for-the-badge)](#-installation-checklist)

---

# 🎯 Tool Information

![Governance](https://img.shields.io/badge/Governance-OPA_|_Policy_as_Code-6A1B9A?style=for-the-badge&logo=openpolicyagent&logoColor=white)


---

# 📊 Overview

| Question | Answer |
|----------|--------|
| **What is it?** | Open Policy Agent (OPA) is an open-source Policy-as-Code engine used to evaluate policies written in the Rego language. |
| **What is it used for?** | It validates infrastructure, cloud resources, Kubernetes manifests, APIs, and Terraform configurations against predefined organizational policies. |
| **When do we use it?** | OPA is executed after Terraform validation and security scanning, but before deployment, ensuring infrastructure complies with governance requirements. |
| **Why are we implementing it?** | To demonstrate Policy-as-Code within the KNIGHT Framework by validating Terraform resources before they are committed or deployed. |

---

# 🛠️ Prerequisites

Before installing **OPA**, ensure the following software and prerequisites are available on your local machine.

![Operating System](https://img.shields.io/badge/Operating_System-Windows_10_|_Windows_11-0078D4?style=for-the-badge&logo=windows&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-Command_Prompt_(CMD)_|_Required-1565C0?style=for-the-badge&logo=windows-terminal&logoColor=white)

![Source Control](https://img.shields.io/badge/Software-Git_|_Installed-2E7D32?style=for-the-badge&logo=git&logoColor=white)
![Infrastructure as Code](https://img.shields.io/badge/Software-Terraform_|_Installed-623CE4?style=for-the-badge&logo=terraform&logoColor=white)
![Code Editor](https://img.shields.io/badge/Software-Visual_Studio_Code_|_Installed-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

![Network](https://img.shields.io/badge/Network-Internet_Connection_|_Required-EF6C00?style=for-the-badge&logo=icloud&logoColor=white)

![Permissions](https://img.shields.io/badge/Permissions-Administrator_Access_|_Optional-B71C1C?style=for-the-badge&logo=windows11&logoColor=white)

---

# 📂 Local Demo Project Setup

The following project structure will be used throughout the OPA demonstration.

```mermaid
flowchart TB

A["📁 Terraform_Demo"]

A --> B["📂 terraform"]
A --> C["📂 policy"]
A --> D["📂 docs"]

B --> B1["main.tf"]
B --> B2["provider.tf"]
B --> B3["variables.tf"]
B --> B4["outputs.tf"]

C --> C1["policy.rego"]
C --> C2["input.json"]

D --> D1["01-OPA_Installation_Guide.md"]

classDef root fill:#4A148C,stroke:#6A1B9A,stroke-width:4px,color:#ffffff,font-weight:bold;
classDef folder fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;
classDef file fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#ffffff,font-weight:bold;

class A root;
class B,C,D folder;
class B1,B2,B3,B4,C1,C2,D1 file;
```

---

# 📄 Demo Files Required

The following files will be created specifically for the OPA demonstration.

| File | Required | Purpose |
|------|:--------:|---------|
| `policy.rego` | ✅ | Contains the Policy-as-Code rules written in Rego. |
| `input.json` | ✅ | Sample JSON input evaluated against the Rego policy. |
| `main.tf` | ✅ | Sample Terraform resource used during the demonstration. |
| `README.md` | ✅ | Documentation for the demo project. |

---

# 📁 Demo File Structure

```mermaid
flowchart TB

A["📁 Terraform_Demo"]

A --> B["📂 terraform"]
A --> C["📂 policy"]
A --> D["📄 README.md"]

B --> B1["📜 main.tf"]
B --> B2["⚙️ provider.tf"]
B --> B3["📝 variables.tf"]
B --> B4["📤 outputs.tf"]

C --> C1["📜 policy.rego"]
C --> C2["📄 input.json"]

%% ===========================
%% Styles
%% ===========================

classDef root fill:#4A148C,stroke:#6A1B9A,stroke-width:4px,color:#ffffff,font-weight:bold;

classDef folder fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef terraform fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#ffffff,font-weight:bold;

classDef policy fill:#EF6C00,stroke:#E65100,stroke-width:2px,color:#ffffff,font-weight:bold;

classDef readme fill:#00838F,stroke:#006064,stroke-width:2px,color:#ffffff,font-weight:bold;

%% ===========================
%% Apply Styles
%% ===========================

class A root;

class B,C folder;

class B1,B2,B3,B4 terraform;

class C1,C2 policy;

class D readme;
```

---

# 🌐 Download Information

| Property | Value |
|----------|-------|
| **Tool Name** | Open Policy Agent |
| **Category** | Governance |
| **Latest Binary** | Windows AMD64 |
| **Executable Name** | `opa.exe` |
| **Installation Location** | `C:\KNIGHT\Tools` |
| **Environment Variable** | Add `C:\KNIGHT\Tools` to the Windows PATH |
| **Verification Command** | `opa version` |

---

# 🌍 Official Resources

[![Official Documentation](https://img.shields.io/badge/📘_Documentation-OPA-6A1B9A?style=for-the-badge&logo=openpolicyagent&logoColor=white)](https://www.openpolicyagent.org/docs/latest/)
[![GitHub Repository](https://img.shields.io/badge/💻_GitHub-open--policy--agent/opa-181717?style=for-the-badge&logo=github)](https://github.com/open-policy-agent/opa)
[![Downloads](https://img.shields.io/badge/⬇️_Download-OPA_Releases-0D47A1?style=for-the-badge)](https://github.com/open-policy-agent/opa/releases)

---

➡️ **Next:** **Part 2 – Installation Workflow & Step-by-Step Installation**


---

# 📋 Installation Workflow

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

# 📝 Step 1 – Download OPA

Download the latest **Windows AMD64** binary from the official OPA GitHub Releases page below is the link.

[![OPA Releases](https://img.shields.io/badge/⬇️_Download-OPA_Releases-6A1B9A?style=for-the-badge&logo=github)](https://github.com/open-policy-agent/opa/releases)

### 📌 Expected Download

## 📦 Download Details

![Platform](https://img.shields.io/badge/🪟_Platform-Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)
![Architecture](https://img.shields.io/badge/💻_Architecture-AMD64-1565C0?style=for-the-badge)

![File Type](https://img.shields.io/badge/📦_File_Type-ZIP_Archive-EF6C00?style=for-the-badge)
![Binary](https://img.shields.io/badge/⚙️_Binary-opa__windows__amd64.exe-6A1B9A?style=for-the-badge)

> **Note:** The executable filename may vary depending on the OPA release version.
---

# 📝 Step 2 – Extract the Archive

Extract the downloaded ZIP file using Windows Explorer or any archive manager.

```mermaid
flowchart LR

A["📥 Download ZIP"]
-->
B["📦 Right Click ZIP"]
-->
C["📂 Extract All"]
-->
D["📁 Temporary Folder"]

classDef download fill:#6A1B9A,stroke:#4A148C,stroke-width:3px,color:#ffffff,font-weight:bold;
classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

class A download;
class B,C,D process;
```

---

# 📝 Step 3 – Rename the Executable

Rename the extracted executable to:

```text
opa.exe
```

This provides a consistent executable name across documentation and demonstrations.

---

# 📝 Step 4 – Copy the Executable

Create the KNIGHT tools directory if it does not already exist.

```cmd
mkdir C:\KNIGHT\Tools
```

Copy the executable into the folder.

```text
C:\KNIGHT\Tools\opa.exe
```

---

# 📝 Step 5 – Configure the Windows PATH

Add the KNIGHT tools folder to the Windows **Environment Variables**.

## ⚙️ Configure PATH Environment Variable

```mermaid
flowchart TD

    A([Start])

    --> B

    subgraph B["🪟 Open Windows Settings"]

        B1["Open"]
        --> B2["Windows Search"]

        B2
        --> B3["Edit the system environment variables"]

    end

    B
    --> C

    subgraph C["⚙️ Navigate to PATH"]

        C1["Click"]
        --> C2["Environment Variables"]

        C2
        --> C3["System Variables"]

        C3
        --> C4["Select Path"]

        C4
        --> C5["Click Edit"]

        C5
        --> C6["Click New"]

    end

    C
    --> D

    subgraph D["➕ Add PATH"]

        D1["Add"]

        -->

        D2["C:\KNIGHT\Tools"]

    end

    D
    --> E

    subgraph E["💾 Save Changes"]

        E1["Click OK"]

        -->

        E2["Click OK"]

    end

    E
    --> F

    subgraph F["💻 Restart Terminal"]

        F1["Restart"]

        -->

        F2["CMD / PowerShell / Windows Terminal"]

    end

    F
    --> G([PATH Configured Successfully])

    %% ===========================
    %% Styles
    %% ===========================

    classDef cmd fill:#B71C1C,stroke:#D32F2F,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef process fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef path fill:#EF6C00,stroke:#E65100,stroke-width:3px,color:#ffffff,font-weight:bold;

    classDef success fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

    %% ===========================
    %% Apply Styles
    %% ===========================

    class D2 cmd;

    class B1,B2,B3,C1,C2,C3,C4,C5,C6,D1,E1,E2,F1,F2 process;

    class G success;
```

---

# 📝 Step 6 – Restart the Command Prompt

After updating the **Windows PATH Environment Variable**, any currently open **Command Prompt (CMD)** windows must be restarted to load the updated environment variables.

## 📌 Restart Command Prompt

1. Close all open **`Command Prompt (CMD)`** windows.
2. Open a **`NEW` Command Prompt (CMD)** window.

> **⚠️ Important:** Existing Command Prompt windows will **not** detect the updated **PATH** automatically. Always open a **new Command Prompt** before proceeding to the verification step.

---

# 📝 Step 7 – Verify the Installation

Run the following command:

```cmd
opa version
```

---

# 📷 Expected Verification Output

```text
Version: 1.x.x
Build Commit: xxxxxxxxx
Build Timestamp: 2026-xx-xx
Go Version: go1.xx.x
Platform: windows/amd64
```
```text
C:\Users\Kureti Venkat Nishit>opa version
Version: 1.19.0
Build Commit: 1e32c796e8979b1bda2f768138500b1deb95ff24-dirty
Build Timestamp: 2026-07-30T19:38:54Z
Build Hostname:
Go Version: go1.26.5
Platform: windows/amd64
Rego Version: v1
WebAssembly: available
```

---

# 🎯 Verification Checklist

| Check | Expected Result |
|--------|-----------------|
| `opa version` executes | ✅ |
| No "command not recognized" error | ✅ |
| Version information displayed | ✅ |
| PATH configured correctly | ✅ |
| Ready for policy evaluation | ✅ |

---

# 💡 Installation Tips

- Always download the latest stable Windows AMD64 release.
- Keep all third-party CLI tools in `C:\KNIGHT\Tools` for consistency.
- Restart the terminal after modifying the PATH.
- Verify the installation immediately before proceeding with the demo.
- Use a consistent folder structure across all KNIGHT tool installations.
