# ⚔️ KNIGHT

> **K**olappan · **N**ishit · **I**nfrastructure · **G**itHub · **H**ybrid · **T**erraform

---

# 🚀 Project Badges

![Branch](https://img.shields.io/badge/Branch-K_Test_2-0A66C2?style=for-the-badge&logo=git)
![Terraform](https://img.shields.io/badge/Terraform-v1.13+-623CE4?style=for-the-badge&logo=terraform)
![Terragrunt](https://img.shields.io/badge/Terragrunt-Latest-009688?style=for-the-badge)
![AWS](https://img.shields.io/badge/AWS-S3-orange?style=for-the-badge&logo=amazonaws)
![GitHub](https://img.shields.io/badge/GitHub-KNIGHT-181717?style=for-the-badge&logo=github)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-2088FF?style=for-the-badge&logo=githubactions)

---
# Pipeline Status

[![Terraform Pipeline](https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT/actions/workflows/terraform-pipeline.yml/badge.svg?branch=K_Test_2)](https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT/actions/workflows/terraform-pipeline.yml?query=branch%3AK_Test_2)
[![Terragrunt Pipeline](https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT/actions/workflows/terragrunt-pipeline.yml/badge.svg?branch=K_Test_2)](https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT/actions/workflows/terragrunt-pipeline.yml?query=branch%3AK_Test_2)

---

# 📖 What is KNIGHT?

KNIGHT is a hands-on **Infrastructure as Code (IaC)** demonstration project designed to showcase **why modern DevOps teams adopt Terragrunt on top of Terraform**.

The repository intentionally implements the **same AWS infrastructure twice**, allowing engineers to compare the traditional Terraform approach with the Terragrunt DRY approach.

Instead of simply explaining the concepts, KNIGHT demonstrates them side-by-side through real infrastructure deployments, GitHub Actions pipelines, and security validation.

---

# 🎯 Project Objectives

- ✅ Learn Terraform Fundamentals
- ✅ Understand Infrastructure as Code
- ✅ Compare Terraform vs Terragrunt
- ✅ Understand Remote State Management
- ✅ Build Reusable Infrastructure Modules
- ✅ Learn GitHub Actions CI/CD
- ✅ Implement Security & Quality Gates
- ✅ Deploy AWS Infrastructure Automatically

---

# ⚖️ Terraform vs Terragrunt

| Feature | 🌍 Terraform | 🚀 Terragrunt |
|----------|--------------|---------------|
| Backend Configuration | Duplicate | Centralized |
| DRY Principle | ❌ | ✅ |
| Auto Backend Creation | ❌ | ✅ |
| Environment Management | Manual | Automatic |
| State Key Generation | Manual | Automatic |
| Module Reusability | ✅ | ✅ |
| GitHub Actions Support | ✅ | ✅ |
| Enterprise Scalability | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |

---

# 🏗️ Overall Architecture

```mermaid
flowchart LR

Developer["👨‍💻 Developer"]

Commit["Git Commit"]

Hooks["Pre-Commit Hooks"]

GitHub["GitHub Repository"]

Actions["GitHub Actions"]

Terraform["Terraform Pipeline"]

Terragrunt["Terragrunt Pipeline"]

AWS["AWS Account"]

Resources["AWS Resources"]

Developer --> Commit

Commit --> Hooks

Hooks --> GitHub

GitHub --> Actions

Actions --> Terraform

Actions --> Terragrunt

Terraform --> AWS

Terragrunt --> AWS

AWS --> Resources

classDef dev fill:#4CAF50,color:white,stroke:#2E7D32,stroke-width:2px

classDef git fill:#24292F,color:white

classDef ci fill:#1976D2,color:white

classDef tf fill:#7B42BC,color:white

classDef tg fill:#009688,color:white

classDef aws fill:#FF9800,color:black

class Developer,Commit,Hooks dev

class GitHub git

class Actions ci

class Terraform tf

class Terragrunt tg

class AWS,Resources aws
```

---

# 📂 Repository Layout

```mermaid
flowchart TB

ROOT["📁 KNIGHT Repository"]

ROOT --> TF["📁 terraform"]

ROOT --> TG["📁 terragrunt"]

ROOT --> GH["📁 .github"]

ROOT --> DOCS["📁 docs"]

ROOT --> CFG["⚙️ Configuration Files"]

%% -----------------------------
%% Terraform Structure
%% -----------------------------

TF --> TF_STAGE["📁 stage"]

TF --> TF_PROD["📁 prod"]

TF_STAGE --> TF_MAIN["main.tf"]

TF_STAGE --> TF_VAR["variables.tf"]

TF_STAGE --> TF_OUT["outputs.tf"]

TF_STAGE --> TF_BACK["backend.tf"]

TF_PROD --> PROD_MAIN["main.tf"]

TF_PROD --> PROD_VAR["variables.tf"]

TF_PROD --> PROD_OUT["outputs.tf"]

TF_PROD --> PROD_BACK["backend.tf"]

%% -----------------------------
%% Terragrunt Structure
%% -----------------------------

TG --> ROOT_HCL["terragrunt.hcl"]

TG --> MODULES["📁 modules"]

TG --> TG_STAGE["📁 stage"]

TG --> TG_PROD["📁 prod"]

MODULES --> MOD_S3["📁 s3-bucket"]

MOD_S3 --> MOD_MAIN["main.tf"]

MOD_S3 --> MOD_VAR["variables.tf"]

MOD_S3 --> MOD_OUT["outputs.tf"]

MOD_S3 --> MOD_VER["versions.tf"]

%% -----------------------------
%% GitHub Workflows
%% -----------------------------

GH --> TF_PIPE["terraform-pipeline.yml"]

GH --> TG_PIPE["terragrunt-pipeline.yml"]

%% -----------------------------
%% Documentation
%% -----------------------------

DOCS --> DOC1["Terraform Guide"]

DOCS --> DOC2["Terragrunt Guide"]

DOCS --> DOC3["Comparison Matrix"]

%% -----------------------------
%% Configuration Files
%% -----------------------------

CFG --> PRE[".pre-commit-config.yaml"]

CFG --> README["README.md"]

%% -----------------------------
%% Colors
%% -----------------------------

classDef terraform fill:#7B42BC,color:white,stroke:#512DA8

classDef terragrunt fill:#009688,color:white,stroke:#00695C

classDef github fill:#24292F,color:white

classDef docs fill:#2196F3,color:white

classDef config fill:#607D8B,color:white

class TF,TF_STAGE,TF_PROD,TF_MAIN,TF_VAR,TF_OUT,TF_BACK,PROD_MAIN,PROD_VAR,PROD_OUT,PROD_BACK terraform

class TG,ROOT_HCL,MODULES,TG_STAGE,TG_PROD,MOD_S3,MOD_MAIN,MOD_VAR,MOD_OUT,MOD_VER terragrunt

class GH,TF_PIPE,TG_PIPE github

class DOCS,DOC1,DOC2,DOC3 docs

class CFG,PRE,README config
```

---

# 📂 Repository Layout

```mermaid
flowchart LR

ROOT["📁 KNIGHT Repository"]

%%----------------------------------
%% Root Layout (Left → Right)
%%----------------------------------

ROOT --> GH["📁 .github/workflows"]

ROOT --> TF["📁 terraform"]

ROOT --> TG["📁 terragrunt"]

ROOT --> DOCS["📁 docs"]

ROOT --> CFG["⚙️ Configuration Files"]

%%----------------------------------
%% GitHub Workflows
%%----------------------------------

GH --> TF_PIPE["📄 terraform-pipeline.yml"]

GH --> TG_PIPE["📄 terragrunt-pipeline.yml"]

%%----------------------------------
%% Terraform
%%----------------------------------

TF --> TF_STAGE["📁 stage"]

TF --> TF_PROD["📁 prod"]

TF_STAGE --> TF_MAIN["📄 main.tf"]

TF_STAGE --> TF_VAR["📄 variables.tf"]

TF_STAGE --> TF_OUT["📄 outputs.tf"]

TF_STAGE --> TF_BACK["📄 backend.tf"]

TF_PROD --> PROD_MAIN["📄 main.tf"]

TF_PROD --> PROD_VAR["📄 variables.tf"]

TF_PROD --> PROD_OUT["📄 outputs.tf"]

TF_PROD --> PROD_BACK["📄 backend.tf"]

%%----------------------------------
%% Terragrunt
%%----------------------------------

TG --> ROOT_HCL["📄 terragrunt.hcl"]

TG --> TG_STAGE["📁 stage"]

TG --> TG_PROD["📁 prod"]

TG --> MODULES["📁 modules"]

TG_STAGE --> TG_STAGE_HCL["📄 terragrunt.hcl"]

TG_PROD --> TG_PROD_HCL["📄 terragrunt.hcl"]

MODULES --> MOD_S3["📁 s3-bucket"]

MOD_S3 --> MOD_MAIN["📄 main.tf"]

MOD_S3 --> MOD_VAR["📄 variables.tf"]

MOD_S3 --> MOD_OUT["📄 outputs.tf"]

MOD_S3 --> MOD_VER["📄 versions.tf"]

%%----------------------------------
%% Documentation
%%----------------------------------

DOCS --> DOC1["📄 Terraform Guide"]

DOCS --> DOC2["📄 Terragrunt Guide"]

DOCS --> DOC3["📄 Comparison Matrix"]

%%----------------------------------
%% Configuration
%%----------------------------------

CFG --> PRE["📄 .pre-commit-config.yaml"]

CFG --> README["📄 README.md"]

%%----------------------------------
%% Colors
%%----------------------------------

classDef terraform fill:#7B42BC,color:white,stroke:#512DA8

classDef terragrunt fill:#009688,color:white,stroke:#00695C

classDef github fill:#24292F,color:white

classDef docs fill:#2196F3,color:white

classDef config fill:#607D8B,color:white

class TF,TF_STAGE,TF_PROD,TF_MAIN,TF_VAR,TF_OUT,TF_BACK,PROD_MAIN,PROD_VAR,PROD_OUT,PROD_BACK terraform

class TG,ROOT_HCL,TG_STAGE,TG_PROD,TG_STAGE_HCL,TG_PROD_HCL,MODULES,MOD_S3,MOD_MAIN,MOD_VAR,MOD_OUT,MOD_VER terragrunt

class GH,TF_PIPE,TG_PIPE github

class DOCS,DOC1,DOC2,DOC3 docs

class CFG,PRE,README config
```

---
# 💡 The Core Idea — DRY Backends

One of the biggest challenges with traditional Terraform is backend duplication.

Every environment contains its own `backend.tf`. As environments grow, maintaining identical backend configurations becomes repetitive and error-prone.

Terragrunt eliminates this duplication by defining the backend once and allowing every environment to inherit it automatically.

---

# 🌍 Traditional Terraform

## Backend Configuration

Each environment owns an independent backend configuration.

```mermaid
flowchart TB

ROOT["📁 terraform"]

ROOT --> STAGE["📁 stage"]

ROOT --> PROD["📁 prod"]

STAGE --> ST_BACKEND["backend.tf"]

PROD --> PR_BACKEND["backend.tf"]

ST_BACKEND -. Duplicate .-> PR_BACKEND

classDef root fill:#673AB7,color:white,stroke:#4527A0,stroke-width:2px
classDef folder fill:#7E57C2,color:white
classDef backend fill:#9575CD,color:white

class ROOT root
class STAGE,PROD folder
class ST_BACKEND,PR_BACKEND backend
```

### Example

```hcl
terraform {
  backend "s3" {
    bucket         = "knight-tfstate-stage"
    key            = "stage/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "knight-lock-stage"
  }
}
```

### Challenges

- ❌ Duplicate backend configuration
- ❌ Manual state management
- ❌ Repeated maintenance
- ❌ Configuration drift
- ❌ Higher operational overhead

---

# 🚀 Terragrunt

## Backend Configuration

Terragrunt centralizes backend configuration into a single root file.

```mermaid
flowchart TB

ROOT["📁 terragrunt"]

ROOT --> ROOT_HCL["terragrunt.hcl"]

ROOT --> STAGE["📁 stage"]

ROOT --> PROD["📁 prod"]

STAGE --> ST_HCL["terragrunt.hcl"]

PROD --> PR_HCL["terragrunt.hcl"]

ROOT_HCL -. include .-> ST_HCL

ROOT_HCL -. include .-> PR_HCL

classDef root fill:#00897B,color:white,stroke:#00695C,stroke-width:2px
classDef folder fill:#26A69A,color:white
classDef hcl fill:#4DB6AC,color:white

class ROOT root
class STAGE,PROD folder
class ROOT_HCL,ST_HCL,PR_HCL hcl
```

### Example

```hcl
remote_state {

  backend = "s3"

  config = {

    bucket = "knight-tfstate-${get_aws_account_id()}"

    key = "${path_relative_to_include()}/terraform.tfstate"

    region = "us-east-1"

    encrypt = true

    dynamodb_table = "knight-locks"

  }

}
```

### Advantages

- ✅ Backend defined once
- ✅ Automatic inheritance
- ✅ Dynamic state paths
- ✅ DRY architecture
- ✅ Easier maintenance
- ✅ Enterprise scalability

---

# 📊 Terraform vs Terragrunt

| Feature | 🟣 Terraform | 🟢 Terragrunt |
|----------|--------------|---------------|
| 🌍 Backend Configuration | Duplicate `backend.tf` files | Centralized backend configuration |
| 🔑 State Management | Manual state keys | Automatic state key generation |
| 📂 Configuration | Repeated across environments | Inherited using `include` |
| ♻️ Code Reuse | Limited | High (DRY principle) |
| 🚀 Deployment | Per environment | `run-all` across environments |
| 🏗️ Module Management | Manual | Built-in dependency management |
| 📈 Scalability | Good | Excellent for large infrastructures |
| 🔧 Maintenance | Higher | Lower |
| 👨‍💻 Learning Curve | Easier | Slightly steeper |
| 🏢 Recommended For | Small to medium projects | Medium to enterprise-scale projects |---

# ☁️ AWS Prerequisites

## Required AWS Services

![Amazon S3](https://img.shields.io/badge/Amazon_S3-Required-569A31?style=for-the-badge&logo=amazons3)
![Amazon DynamoDB](https://img.shields.io/badge/DynamoDB-Required-4053D6?style=for-the-badge&logo=amazondynamodb)
![AWS IAM](https://img.shields.io/badge/IAM-Required-DD344C?style=for-the-badge&logo=amazonaws)
![Terraform State](https://img.shields.io/badge/Terraform_State-S3_Backend-623CE4?style=for-the-badge&logo=terraform)

---

## Required GitHub Repository Secrets

![AWS_ACCESS_KEY_ID](https://img.shields.io/badge/AWS_ACCESS_KEY_ID-Configured-success?style=for-the-badge&logo=github)
![AWS_SECRET_ACCESS_KEY](https://img.shields.io/badge/AWS_SECRET_ACCESS_KEY-Configured-success?style=for-the-badge&logo=github)
![AWS_DEFAULT_REGION](https://img.shields.io/badge/AWS_DEFAULT_REGION-us--east--1-success?style=for-the-badge&logo=github)

---

# 🛠 Required Software

![Terraform](https://img.shields.io/badge/Terraform-v1.13+-623CE4?style=for-the-badge&logo=terraform)
![Terragrunt](https://img.shields.io/badge/Terragrunt-Latest-009688?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Latest-F05032?style=for-the-badge&logo=git)
![AWS CLI](https://img.shields.io/badge/AWS_CLI-Latest-FF9900?style=for-the-badgego=python)
![pre--commit](https://img.shields.io/badge/pre--commit-Latest-FAB040?style=for-the-badge&logo=pre-commit)
![TFLint](https://img.shields.io/badge/TFLint-Latest-5C4EE5?style=for-the-badge)
![tfsec](https://img.shields.io/badge/tfsec-Latest-0091EA?style=for-the-badge)

---

# 🔐 AWS Environment Variables

```bash
export AWS_ACCESS_KEY_ID="xxxxxxxxxxxxxxxx"
```
```bash
export AWS_SECRET_ACCESS_KEY="xxxxxxxxxxxxxxxx"
```
```bash
export AWS_DEFAULT_REGION="us-east-1"
```

---

# 🔧 Install Git Hooks

Install the local Git hooks before committing any code.

```bash
pre-commit install
```

Once installed, every commit automatically executes:

- ✅ Terraform Format
- ✅ Terraform Validate
- ✅ TFLint
- ✅ tfsec
- ✅ Checkov
- ✅ Terrascan
- ✅ terraform-docs

This ensures every commit passes the repository quality gates before reaching GitHub.

---

# 🖥️ Local Development Workflow

Every infrastructure change begins on your local machine.

Before any code reaches GitHub, KNIGHT enforces multiple validation, formatting, security, and documentation checks to ensure high-quality Infrastructure as Code.

```mermaid
flowchart LR

A["👨‍💻 Write Terraform Code"]

B["📝 terraform fmt"]

C["⚙️ terraform init"]

D["✅ terraform validate"]

E["🔍 TFLint"]

F["🛡️ tfsec"]

G["📖 terraform-docs"]

H["📦 Git Commit"]

A --> B

B --> C

C --> D

D --> E

E --> F

F --> G

G --> H

classDef dev fill:#4CAF50,color:white

classDef tf fill:#7B42BC,color:white

classDef sec fill:#D32F2F,color:white

classDef docs fill:#1976D2,color:white

classDef git fill:#24292F,color:white

class A dev

class B,C,D,E tf

class F sec

class G docs

class H git
```

---

# 🚀 Local Terraform Workflow

The traditional Terraform workflow is executed individually for each environment.

```mermaid
flowchart LR

A["👨‍💻 Write Terraform"]

B["📝 terraform fmt"]

C["⚙️ terraform init"]

D["✅ terraform validate"]

E["📋 terraform plan"]

F["👀 Review Plan"]

G["🚀 terraform apply"]

A --> B

B --> C

C --> D

D --> E

E --> F

F --> G

classDef terraform fill:#7B42BC,color:white

class A,B,C,D,E,F,G terraform
```
---

# 🔒 Local Quality Gates

Every commit passes through multiple quality checks before reaching GitHub.

```mermaid
flowchart LR

FMT["terraform fmt"]

VAL["terraform validate"]

LINT["TFLint"]

TFSEC["tfsec"]

CHECKOV["Checkov"]

TSCAN["Terrascan"]

DOCS["terraform-docs"]

FMT --> VAL

VAL --> LINT

LINT --> TFSEC

TFSEC --> CHECKOV

CHECKOV --> TSCAN

TSCAN --> DOCS

classDef quality fill:#7B42BC,color:white

classDef security fill:#D32F2F,color:white

classDef documentation fill:#1976D2,color:white

class FMT,VAL,LINT quality

class TFSEC,CHECKOV,TSCAN security

class DOCS documentation
```

---

# 🪝 Git Pre-Commit Hooks

KNIGHT automatically executes validation checks before allowing a commit.

```mermaid
flowchart LR

A["👨‍💻 Developer"]

B["📦 Git Commit"]

C["🪝 Pre-Commit Hook"]

D["📝 terraform fmt"]

E["✅ terraform validate"]

F["🔍 TFLint"]

G["🛡️ tfsec"]

H{"✔️ Passed?"}

I["🎉 Commit Accepted"]

J["🔧 Fix Issues"]

A --> B

B --> C

C --> D

D --> E

E --> F

F --> G

G --> H

H -- Yes --> I

H -- No --> J

J --> D

classDef dev fill:#4CAF50,color:white

classDef validation fill:#7B42BC,color:white

classDef security fill:#D32F2F,color:white

classDef decision fill:#FF9800,color:black

classDef success fill:#2E7D32,color:white

classDef failed fill:#F57C00,color:white

class A,B dev

class C,D,E,F validation

class G security

class H decision

class I success

class J failed
```

---

# 📊 Tool Execution Order

The following tools execute sequentially during local validation.

| Category          | Tool               | Purpose                                       |
| ----------------- | ------------------ | --------------------------------------------- |
| 📝 Formatting     | terraform fmt      | Standardizes Terraform code formatting        |
| ⚙️ Initialization | terraform init     | Initializes providers and backend             |
| ✅ Validation      | terraform validate | Validates Terraform configuration             |
| 🔍 Linting        | TFLint             | Enforces Terraform best practices             |
| 🛡️ Security      | tfsec              | Scans for Terraform security vulnerabilities  |
| 🔒 Policy         | Checkov            | Policy-as-Code and compliance validation      |
| 🔐 Compliance     | Terrascan          | Security, governance, and compliance scanning |
| 📖 Documentation  | terraform-docs     | Automatically generates module documentation  |

---

# 🚀 GitHub Actions CI/CD Workflow

After the local quality gates pass, every push to the **K_Test_2** branch automatically triggers the GitHub Actions pipelines.

The workflow validates the Terraform code, performs security scanning, generates documentation, and deploys the infrastructure to AWS.

```mermaid
flowchart LR

DEV["👨‍💻 Developer"]

PUSH["📦 Push to K_Test_2"]

GH["GitHub Repository"]

ACT["⚙️ GitHub Actions"]

TF["🟣 Terraform Pipeline"]

TG["🟢 Terragrunt Pipeline"]

AWS["☁️ AWS"]

DEV --> PUSH

PUSH --> GH

GH --> ACT

ACT --> TF

ACT --> TG

TF --> AWS

TG --> AWS

classDef developer fill:#4CAF50,color:white

classDef github fill:#24292F,color:white

classDef actions fill:#1976D2,color:white

classDef terraform fill:#7B42BC,color:white

classDef terragrunt fill:#009688,color:white

classDef aws fill:#FF9800,color:black

class DEV,PUSH developer

class GH github

class ACT actions

class TF terraform

class TG terragrunt

class AWS aws
```

---

# 🟣 Terraform GitHub Actions Pipeline

The Terraform workflow validates each environment independently before deployment.

```mermaid
flowchart LR

A["🚀 Trigger"]

B["📥 Checkout Repository"]

C["🔑 Configure AWS Credentials"]

D["📝 Terraform fmt"]

E["⚙️ Terraform Init"]

F["✅ Terraform Validate"]

G["📋 Terraform Plan"]

H{"Push to K_Test_2?"}

I["🚀 Terraform Apply"]

J["🎉 Completed"]

A --> B

B --> C

C --> D

D --> E

E --> F

F --> G

G --> H

H -- Yes --> I

H -- No --> J

I --> J

classDef github fill:#24292F,color:white

classDef terraform fill:#7B42BC,color:white

classDef decision fill:#FF9800,color:black

classDef success fill:#2E7D32,color:white

class A,B,C github

class D,E,F,G,I terraform

class H decision

class J success
```
---

# 🔒 Security Validation Pipeline

Every workflow executes a series of security and compliance tools before deployment.

```mermaid
flowchart LR

FMT["📝 terraform fmt"]

VAL["✅ terraform validate"]

LINT["🔍 TFLint"]

TFSEC["🛡️ tfsec"]

CHECKOV["🔒 Checkov"]

TERRASCAN["🔐 Terrascan"]

DOCS["📖 terraform-docs"]

PLAN["📊 Terraform Plan"]

APPLY["🚀 Deployment"]

FMT --> VAL

VAL --> LINT

LINT --> TFSEC

TFSEC --> CHECKOV

CHECKOV --> TERRASCAN

TERRASCAN --> DOCS

DOCS --> PLAN

PLAN --> APPLY

classDef terraform fill:#7B42BC,color:white

classDef security fill:#D32F2F,color:white

classDef docs fill:#1976D2,color:white

classDef deploy fill:#2E7D32,color:white

class FMT,VAL,LINT terraform

class TFSEC,CHECKOV,TERRASCAN security

class DOCS docs

class PLAN,APPLY deploy
```

---

# 📦 Complete CI/CD Flow

The complete KNIGHT automation workflow.

```mermaid
flowchart LR

DEV["👨‍💻 Developer"]

CODE["Terraform Code"]

LOCAL["🖥 Local Validation"]

PRE["🪝 Pre-Commit"]

GIT["GitHub"]

ACTION["GitHub Actions"]

PIPE["Terraform / Terragrunt"]

AWS["AWS"]

STATE["Remote State"]

DEV --> CODE

CODE --> LOCAL

LOCAL --> PRE

PRE --> GIT

GIT --> ACTION

ACTION --> PIPE

PIPE --> AWS

AWS --> STATE

classDef developer fill:#4CAF50,color:white

classDef validation fill:#7B42BC,color:white

classDef github fill:#24292F,color:white

classDef actions fill:#1976D2,color:white

classDef aws fill:#FF9800,color:black

class DEV,CODE developer

class LOCAL,PRE validation

class GIT github

class ACTION,PIPE actions

class AWS,STATE aws
```

---

# ☁️ AWS Deployment Architecture

KNIGHT uses **GitHub Actions**, **Terraform**, and **Terragrunt** to provision and manage AWS infrastructure using a secure remote backend.

```mermaid
flowchart LR

DEV["👨‍💻 Developer"]

GH["🐙 GitHub Repository"]

GHA["⚙️ GitHub Actions"]

TF["🟣 Terraform / 🟢 Terragrunt"]

S3["🪣 Amazon S3<br/>Terraform State"]

DDB["🔒 Amazon DynamoDB<br/>State Lock"]

AWS["☁️ AWS Account"]

RES["🏗️ AWS Resources"]

DEV --> GH

GH --> GHA

GHA --> TF

TF --> S3

TF --> DDB

TF --> AWS

AWS --> RES

classDef developer fill:#4CAF50,color:white
classDef github fill:#24292F,color:white
classDef actions fill:#1976D2,color:white
classDef terraform fill:#7B42BC,color:white
classDef backend fill:#FFB300,color:black
classDef aws fill:#FF9800,color:black

class DEV developer
class GH github
class GHA actions
class TF terraform
class S3,DDB backend
class AWS,RES aws
```

---

# 🌎 End-to-End KNIGHT Workflow

The following diagram illustrates the complete Infrastructure-as-Code lifecycle from development to deployment.

```mermaid
flowchart LR

A["👨‍💻 Write Infrastructure"]

B["📝 Local Validation"]

C["🪝 Pre-Commit Hooks"]

D["📦 Push to GitHub"]

E["⚙️ GitHub Actions"]

F["🔒 Security Validation"]

G["📋 Terraform / Terragrunt Plan"]

H["🚀 Apply Infrastructure"]

I["☁️ AWS"]

J["🎉 Deployment Complete"]

A --> B

B --> C

C --> D

D --> E

E --> F

F --> G

G --> H

H --> I

I --> J

classDef developer fill:#4CAF50,color:white
classDef validation fill:#7B42BC,color:white
classDef github fill:#24292F,color:white
classDef security fill:#D32F2F,color:white
classDef deploy fill:#2E7D32,color:white
classDef aws fill:#FF9800,color:black

class A developer
class B,C validation
class D,E github
class F security
class G,H deploy
class I,J aws
```

---

# 📋 Repository Highlights

![🟣 Terraform](https://img.shields.io/badge/🟣-Terraform-623CE4?style=for-the-badge&logo=terraform)
![🟢 Terragrunt](https://img.shields.io/badge/🟢-Terragrunt-009688?style=for-the-badge)
![⚙️ GitHub Actions](https://img.shields.io/badge/⚙️-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions)
![🔒 Security Scanning](https://img.shields.io/badge/🔒-Security_Scanning-D32F2F?style=for-the-badge)
![🪣 Remote State](https://img.shields.io/badge/🪣-Amazon_S3-FF9900?style=for-the-badge&logo=amazonaws)
![🔐 State Locking](https://img.shields.io/badge/🔐-DynamoDB-4053D6?style=for-the-badge&logo=amazondynamodb)
![📖 terraform-docs](https://img.shields.io/badge/📖-terraform--docs-1976D2?style=for-the-badge)
![☁️ AWS](https://img.shields.io/badge/☁️-AWS-FF9900?style=for-the-badge&logo=amazonaws)

---

# 📈 Future Roadmap

| Status | Feature |
|--------|---------|
| ⏳ | Multi-Region AWS Deployment |
| ⏳ | Multi-Account AWS Support |
| ⏳ | GitHub OIDC Authentication |
| ⏳ | Automated Cost Estimation |
| ⏳ | Drift Detection |
| ⏳ | Infrastructure Testing with Terratest |
| ⏳ | Infracost Integration |
| ⏳ | AWS Well-Architected Best Practices |
| ⏳ | Reusable Enterprise Modules |
| ⏳ | Complete GitHub Actions Reusable Workflows |

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Kureti Venkat Nishit**

Cloud • DevOps • GitHub Actions • Terraform • Terragrunt • AWS

---

<div align="center">

## ⭐ If you found this repository helpful, please consider giving it a Star!

**Happy Learning and Happy Automating! 🚀**

</div>
