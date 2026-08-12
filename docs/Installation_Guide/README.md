# 🛠️ Terraform KNIGHT Tools Installation Guide 📦

This folder contains the complete installation guides for all Terraform Quality, Security, Compliance, Policy-as-Code, and Documentation tools used throughout the **KNIGHT Framework**.

---


# 🎯 Tools Covered

![Governance](https://img.shields.io/badge/Governance-📜_OPA_|_Policy_as_Code-6A1B9A?style=for-the-badge&logo=openpolicyagent&logoColor=white)

![Security](https://img.shields.io/badge/Security-🛡️_Checkov_|_Infrastructure_Security-2E7D32?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-🔐_tfsec_|_Terraform_Security-2E7D32?style=for-the-badge)

![Compliance](https://img.shields.io/badge/Compliance-📋_Terrascan_|_Infrastructure_Compliance-EF6C00?style=for-the-badge)
![Quality](https://img.shields.io/badge/Quality-📝_TFLint_|_Terraform_Linting-1565C0?style=for-the-badge)

![Documentation](https://img.shields.io/badge/Documentation-📖_terraform--docs_|_Documentation_Generator-00838F?style=for-the-badge)

---

# 📊 Complete Tool Comparison Matrix

| Tool              | Category       | Primary Purpose                  | Demo Files                         | Installation | Validation Command       | Output                 |
| ----------------- | -------------- | -------------------------------- | ---------------------------------- | ------------ | ------------------------ | ---------------------- |
| 🛡 OPA            | Policy as Code | Infrastructure Policy Validation | `policy.rego`, `input.json`        | Binary       | `opa version`            | Allow / Deny           |
| 🔍 Checkov        | Security       | Terraform Security Scan          | `main.tf`                          | Python (pip) | `checkov --version`      | Security Findings      |
| 🔐 tfsec          | Security       | Terraform Misconfiguration Scan  | `main.tf`                          | Binary       | `tfsec --version`        | Security Findings      |
| 🛡 Terrascan      | Compliance     | Compliance Validation            | `main.tf`                          | Binary       | `terrascan version`      | Compliance Report      |
| 📝 TFLint         | Quality        | Terraform Linting                | `.tflint.hcl`                      | Binary       | `tflint --version`       | Lint Report            |
| 📖 terraform-docs | Documentation  | Documentation Generator          | `README.md`, `.terraform-docs.yml` | Binary       | `terraform-docs version` | Markdown Documentation |

---

# 📂 Local Demo Project Setup

```mermaid
flowchart TB

A["📁 Terraform_Demo"]

A --> B["📂 terraform"]
A --> C["📂 policy"]
A --> D["📂 docs"]
A --> E["⚙ Configuration"]

B --> B1["main.tf"]
B --> B2["provider.tf"]
B --> B3["variables.tf"]
B --> B4["outputs.tf"]
B --> B5["versions.tf"]

C --> C1["policy.rego"]
C --> C2["input.json"]

E --> E1[".tflint.hcl"]
E --> E2[".terraform-docs.yml"]

classDef root fill:#4A148C,stroke:#7B1FA2,stroke-width:4px,color:#fff;
classDef folder fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#fff;
classDef file fill:#2E7D32,stroke:#1B5E20,stroke-width:2px,color:#fff;

class A root;
class B,C,D,E folder;
class B1,B2,B3,B4,B5,C1,C2,E1,E2 file;
```

---

# 🔄 Complete Local Terraform Quality Gate Workflow


```mermaid
flowchart LR

A["👨‍💻 Developer"]

-->

B["📝 terraform fmt"]

-->

C["⚙ terraform init"]

-->

D["✅ terraform validate"]

-->

E["🔍 TFLint"]

-->

F["🛡 Checkov"]

-->

G["🔐 tfsec"]

-->

H["🛡 Terrascan"]

-->

I["📜 OPA"]

-->

J["📖 terraform-docs"]

-->

K["🚀 Git Commit"]

classDef dev fill:#4A148C,stroke:#6A1B9A,stroke-width:3px,color:#fff;
classDef terraform fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#fff;
classDef security fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#fff;
classDef docs fill:#F57C00,stroke:#E65100,stroke-width:3px,color:#fff;
classDef final fill:#C62828,stroke:#8E0000,stroke-width:3px,color:#fff;

class A dev;
class B,C,D terraform;
class E,F,G,H,I security;
class J docs;
class K final;
```
---

# 📚 Installation Guides

| Step | Guide                                     | Category      | Purpose                   |
| ---- | ----------------------------------------- | ------------- | ------------------------- |
| 1️⃣  | `01-OPA_Installation_Guide.md`            | Governance    | Install Open Policy Agent |
| 2️⃣  | `02-Checkov_Installation_Guide.md`        | Security      | Install Checkov           |
| 3️⃣  | `03-tfsec_Installation_Guide.md`          | Security      | Install tfsec             |
| 4️⃣  | `04-Terrascan_Installation_Guide.md`      | Compliance    | Install Terrascan         |
| 5️⃣  | `05-TFLint_Installation_Guide.md`         | Quality       | Install TFLint            |
| 6️⃣  | `06-Terraform-Docs_Installation_Guide.md` | Documentation | Install terraform-docs    |


---

# 📋 Installation Order

```mermaid
flowchart LR

A["📜 OPA"]
-->
B["🛡️ Checkov"]
-->
C["🔐 tfsec"]
-->
D["📋 Terrascan"]
-->
E["📝 TFLint"]
-->
F["📖 terraform-docs"]

%% ===========================
%% Category Colors
%% ===========================

classDef governance fill:#6A1B9A,stroke:#4A148C,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef security fill:#2E7D32,stroke:#1B5E20,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef compliance fill:#EF6C00,stroke:#E65100,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef quality fill:#1565C0,stroke:#0D47A1,stroke-width:3px,color:#ffffff,font-weight:bold;

classDef documentation fill:#00838F,stroke:#006064,stroke-width:3px,color:#ffffff,font-weight:bold;

%% ===========================
%% Apply Colors
%% ===========================

class A governance;

class B,C security;

class D compliance;

class E quality;

class F documentation;
```
---

# 📚 Post installation Cumulative Verification 

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

```text

C:\Users\Kureti Venkat Nishit>checkov --version

File association not found for extension .py
3.3.9

C:\Users\Kureti Venkat Nishit>tfsec --version

======================================================
tfsec is joining the Trivy family

tfsec will continue to remain available
for the time being, although our engineering
attention will be directed at Trivy going forward.

You can read more here:
https://github.com/aquasecurity/tfsec/discussions/1994
======================================================
v1.28.14
```

```text
C:\Users\Kureti Venkat Nishit>terrascan version

version: v1.19.9
```

```text
C:\Users\Kureti Venkat Nishit>tflint --version

TFLint version 0.64.0
+ ruleset.terraform (0.15.0-bundled)
```

```text
C:\Users\Kureti Venkat Nishit>terraform-docs --version

terraform-docs version v0.24.0 9d44551 windows/amd64
```

---
# 📖 References

### 🌍 Terraform

[![Documentation](https://img.shields.io/badge/📘_Documentation-Terraform-623CE4?style=for-the-badge&logo=terraform&logoColor=white)](https://developer.hashicorp.com/terraform/docs)
[![GitHub](https://img.shields.io/badge/💻_GitHub-hashicorp/terraform-181717?style=for-the-badge&logo=github)](https://github.com/hashicorp/terraform)

---

### 📜 OPA

[![Documentation](https://img.shields.io/badge/📘_Documentation-OPA-6A1B9A?style=for-the-badge&logo=openpolicyagent&logoColor=white)](https://www.openpolicyagent.org/docs/latest/)
[![GitHub](https://img.shields.io/badge/💻_GitHub-open--policy--agent/opa-181717?style=for-the-badge&logo=github)](https://github.com/open-policy-agent/opa)

---

### 🛡️ Checkov

[![Documentation](https://img.shields.io/badge/📘_Documentation-Checkov-2E7D32?style=for-the-badge)](https://www.checkov.io/)
[![GitHub](https://img.shields.io/badge/💻_GitHub-bridgecrewio/checkov-181717?style=for-the-badge&logo=github)](https://github.com/bridgecrewio/checkov)

---

### 🔐 tfsec

[![Documentation](https://img.shields.io/badge/📘_Documentation-tfsec-2E7D32?style=for-the-badge)](https://aquasecurity.github.io/tfsec/)
[![GitHub](https://img.shields.io/badge/💻_GitHub-aquasecurity/tfsec-181717?style=for-the-badge&logo=github)](https://github.com/aquasecurity/tfsec)

---

### 📋 Terrascan

[![Documentation](https://img.shields.io/badge/📘_Documentation-Terrascan-EF6C00?style=for-the-badge)](https://runterrascan.io/)
[![GitHub](https://img.shields.io/badge/💻_GitHub-tenable/terrascan-181717?style=for-the-badge&logo=github)](https://github.com/tenable/terrascan)

---

### 📝 TFLint

[![Documentation](https://img.shields.io/badge/📘_Documentation-TFLint-1565C0?style=for-the-badge)](https://github.com/terraform-linters/tflint/blob/master/README.md)
[![GitHub](https://img.shields.io/badge/💻_GitHub-terraform--linters/tflint-181717?style=for-the-badge&logo=github)](https://github.com/terraform-linters/tflint)

---

### 📖 terraform-docs

[![Documentation](https://img.shields.io/badge/📘_Documentation-terraform--docs-00838F?style=for-the-badge)](https://terraform-docs.io/)
[![GitHub](https://img.shields.io/badge/💻_GitHub-terraform--docs/terraform--docs-181717?style=for-the-badge&logo=github)](https://github.com/terraform-docs/terraform-docs)
---
