# 🚀 Terragrunt Module Architecture and Usage Guide

This directory provides a **practical, hands-on demonstration of Terragrunt and its integration with Terraform**. The goal is to show how Terragrunt can simplify the management of Terraform infrastructure as the number of **modules, environments, and deployment dependencies** grows.

Throughout this guide, the focus is on understanding how Terragrunt helps build a **clean, scalable, and maintainable Infrastructure as Code (IaC) architecture** by introducing:

- ♻️ **DRY Configuration** — Reduce duplication across Terraform environments.
- 🗂️ **Structured Environment Management** — Organize Dev, QA, UAT, and Production configurations consistently.
- 🗄️ **Centralized State Configuration** — Define and reuse remote-state settings across environments.
- 🔗 **Dependency Management** — Establish relationships and execution order between Terraform modules.
- 📦 **Reusable Terraform Modules** — Separate infrastructure logic from environment-specific configuration.
- ⚡ **Multi-Module Orchestration** — Execute Terraform operations across multiple modules using Terragrunt.
- 🔐 **Consistent Infrastructure Practices** — Apply common configuration and deployment patterns across environments.

> The objective is not to replace Terraform, but to demonstrate **where Terragrunt adds value on top of Terraform** and how it can help teams manage infrastructure more effectively at scale.

## 📚 Core Concepts & Educational Overview
**Terraform defines and provisions infrastructure, while Terragrunt helps organize, configure, and orchestrate Terraform across multiple modules and environments.**---

### 🏗️ What is Terragrunt?

**Terragrunt** is a thin wrapper around Terraform that provides additional capabilities for managing **large-scale, multi-environment infrastructure deployments**.

It helps teams:

* ♻️ Reduce duplicated Terraform configuration
* 📂 Organize infrastructure by environment
* 🗄️ Centralize remote state configuration
* 🔗 Manage dependencies between Terraform modules
* 🌎 Maintain Dev, QA, UAT, and Production environments
* ⚡ Execute Terraform operations across multiple modules

The primary goal is to keep the infrastructure code **DRY — Don't Repeat Yourself**.

---

## 🎯 Why Use Terragrunt?

A traditional Terraform implementation may require repeating the same configuration across multiple environments.

```mermaid
flowchart LR

%% ========================================
%% Traditional Terraform Configuration
%% ========================================

subgraph DEV["📁 Dev Environment"]
direction TB

    DEV_BACKEND["🗄️ Backend Configuration"]:::config
    DEV_PROVIDER["⚙️ Provider Configuration"]:::provider
    DEV_MODULE["📦 Terraform Module"]:::module

    DEV_BACKEND --> DEV_PROVIDER
    DEV_PROVIDER --> DEV_MODULE

end


subgraph QA["📁 QA Environment"]
direction TB

    QA_BACKEND["🗄️ Backend Configuration"]:::config
    QA_PROVIDER["⚙️ Provider Configuration"]:::provider
    QA_MODULE["📦 Terraform Module"]:::module

    QA_BACKEND --> QA_PROVIDER
    QA_PROVIDER --> QA_MODULE

end


subgraph PROD["📁 Production Environment"]
direction TB

    PROD_BACKEND["🗄️ Backend Configuration"]:::config
    PROD_PROVIDER["⚙️ Provider Configuration"]:::provider
    PROD_MODULE["📦 Terraform Module"]:::module

    PROD_BACKEND --> PROD_PROVIDER
    PROD_PROVIDER --> PROD_MODULE

end


%% ========================================
%% Force Horizontal Environment Layout
%% ========================================

DEV -.-> QA
QA -.-> PROD


%% ========================================
%% Styling Configuration
%% ========================================

classDef config fill:#FFC000,stroke:#BF9000,color:#000000,stroke-width:2px
classDef provider fill:#1565C0,stroke:#0D47A1,color:#FFFFFF,stroke-width:2px
classDef module fill:#7030A0,stroke:#351C75,color:#FFFFFF,stroke-width:2px


%% ========================================
%% Environment Container Styling
%% ========================================

style DEV fill:#D9EAF7,stroke:#2F75B5,stroke-width:3px,color:#000000
style QA fill:#E2F0D9,stroke:#70AD47,stroke-width:3px,color:#000000
style PROD fill:#F4CCCC,stroke:#C00000,stroke-width:3px,color:#000000


%% ========================================
%% Invisible Layout Links
%% ========================================

linkStyle 6 stroke-width:0
linkStyle 7 stroke-width:0
```

### 🔄 Terragrunt Approach

You can immediately follow it with the **Terragrunt solution**, which makes the contrast much clearer:

Terragrunt allows common configuration to be defined once and inherited by multiple environments.

```mermaid
flowchart LR

ROOT["📄 Root terragrunt.hcl<br/>Shared Configuration"]:::root

DEV["📁 Dev"]:::environment
QA["📁 QA"]:::environment
UAT["📁 UAT"]:::environment
PROD["📁 Prod"]:::environment

MODULES["📦 Reusable Terraform Modules"]:::module

ROOT --> DEV
ROOT --> QA
ROOT --> UAT
ROOT --> PROD

DEV --> MODULES
QA --> MODULES
UAT --> MODULES
PROD --> MODULES


classDef root fill:#1F4E79,stroke:#0B2D4D,color:#FFFFFF,stroke-width:3px
classDef environment fill:#2F75B5,stroke:#1F4E79,color:#FFFFFF,stroke-width:2px
classDef module fill:#7030A0,stroke:#351C75,color:#FFFFFF,stroke-width:2px
```

### 🔑 Key Benefits

* **🧩 Single Source of Truth** — Common configuration is defined centrally.
* **♻️ DRY Configuration** — Reduces repeated Terraform configuration.
* **🗄️ Centralized State Management** — Remote state configuration can be shared.
* **🔗 Dependency Management** — Modules can be executed according to their dependencies.
* **🌎 Environment Isolation** — Each environment maintains its own configuration and state.
* **⚡ Multi-Module Execution** — Multiple Terraform modules can be planned or applied together.

---

# 📂 Terragrunt Directory Architecture

A typical Terragrunt project separates **live environment configuration** from **reusable Terraform modules**.

```mermaid
flowchart LR

subgraph LIVE["📂 live/ — Environment Configuration"]
direction TB

    ROOT["📄 terragrunt.hcl<br/>Root Configuration"]:::config

    subgraph DEV["📁 dev/"]
    direction TB
        DEV_NET["📁 network/"]:::folder
        DEV_NET_FILE["📄 terragrunt.hcl"]:::file

        DEV_COMPUTE["📁 compute/"]:::folder
        DEV_COMPUTE_FILE["📄 terragrunt.hcl"]:::file

        DEV_NET --> DEV_NET_FILE
        DEV_COMPUTE --> DEV_COMPUTE_FILE
    end

    subgraph QA["📁 qa/"]
        QA_CFG["📄 terragrunt.hcl"]:::file
    end

    subgraph UAT["📁 uat/"]
        UAT_CFG["📄 terragrunt.hcl"]:::file
    end

    subgraph PROD["📁 prod/"]
        PROD_CFG["📄 terragrunt.hcl"]:::file
    end

    ROOT --> DEV
    ROOT --> QA
    ROOT --> UAT
    ROOT --> PROD

end


subgraph MODULES["📦 modules/ — Reusable Terraform Modules"]
direction TB

    NETWORK["📁 network/"]:::module
    STORAGE["📁 storage/"]:::module
    COMPUTE["📁 compute/"]:::module
    DATABASE["📁 database/"]:::module

end


LIVE --> MODULES


classDef config fill:#FFC000,stroke:#BF9000,color:#000000,stroke-width:2px
classDef folder fill:#70AD47,stroke:#385723,color:#FFFFFF,stroke-width:2px
classDef file fill:#1565C0,stroke:#0D47A1,color:#FFFFFF,stroke-width:2px
classDef module fill:#7030A0,stroke:#351C75,color:#FFFFFF,stroke-width:2px

style LIVE fill:#EAF3FF,stroke:#1F4E79,stroke-width:3px,color:#000000
style MODULES fill:#F3E5FF,stroke:#7030A0,stroke-width:3px,color:#000000
style DEV fill:#D9EAF7,stroke:#2F75B5,stroke-width:2px,color:#000000
style QA fill:#D9EAD3,stroke:#70AD47,stroke-width:2px,color:#000000
style UAT fill:#FFF2CC,stroke:#BF9000,stroke-width:2px,color:#000000
style PROD fill:#F4CCCC,stroke:#C00000,stroke-width:2px,color:#000000
```

---

## 🗂️ Directory Structure

```mermaid
flowchart LR

%% ========================================
%% Root Directory
%% ========================================

subgraph ROOT["📂 terragrunt/"]
direction TB

    ROOT_CONFIG["📄 terragrunt.hcl"]:::config


    %% ========================================
    %% Live Environment Structure
    %% ========================================

    subgraph LIVE["📂 live/"]
    direction TB

        subgraph DEV["📁 dev/"]
        direction TB

            subgraph NETWORK["📁 network/"]
            direction TB
                DEV_NETWORK_FILE["📄 terragrunt.hcl"]:::file
            end

            subgraph COMPUTE["📁 compute/"]
            direction TB
                DEV_COMPUTE_FILE["📄 terragrunt.hcl"]:::file
            end

        end


        subgraph QA["📁 qa/"]
        direction TB
            QA_FILE["📄 terragrunt.hcl"]:::file
        end


        subgraph UAT["📁 uat/"]
        direction TB
            UAT_FILE["📄 terragrunt.hcl"]:::file
        end


        subgraph PROD["📁 prod/"]
        direction TB
            PROD_FILE["📄 terragrunt.hcl"]:::file
        end

    end


    %% ========================================
    %% Reusable Terraform Modules
    %% ========================================

    subgraph MODULES["📦 modules/"]
    direction TB

        NETWORK_MODULE["📁 network/"]:::module
        STORAGE_MODULE["📁 storage/"]:::module
        COMPUTE_MODULE["📁 compute/"]:::module
        DATABASE_MODULE["📁 database/"]:::module

    end

end


%% ========================================
%% Directory Relationships
%% ========================================

ROOT_CONFIG --> LIVE
LIVE --> MODULES


%% ========================================
%% Styling Configuration
%% ========================================

classDef config fill:#FFC000,stroke:#BF9000,color:#000000,stroke-width:2px
classDef file fill:#1565C0,stroke:#0D47A1,color:#FFFFFF,stroke-width:2px
classDef module fill:#7030A0,stroke:#351C75,color:#FFFFFF,stroke-width:2px


%% ========================================
%% Container Styling
%% ========================================

style ROOT fill:#EAF3FF,stroke:#1F4E79,stroke-width:3px,color:#000000

style LIVE fill:#D9EAF7,stroke:#2F75B5,stroke-width:3px,color:#000000
style DEV fill:#E2F0D9,stroke:#70AD47,stroke-width:2px,color:#000000
style NETWORK fill:#F3F9EE,stroke:#70AD47,stroke-width:2px,color:#000000
style COMPUTE fill:#F3F9EE,stroke:#70AD47,stroke-width:2px,color:#000000
style QA fill:#E2F0D9,stroke:#70AD47,stroke-width:2px,color:#000000
style UAT fill:#FFF2CC,stroke:#BF9000,stroke-width:2px,color:#000000
style PROD fill:#F4CCCC,stroke:#C00000,stroke-width:2px,color:#000000

style MODULES fill:#F3E5FF,stroke:#7030A0,stroke-width:3px,color:#000000
```
---

# ⚙️ Terraform vs Terragrunt Workflow

Terragrunt does not replace Terraform. Instead, it **orchestrates Terraform modules and configurations**.

## 🏗️ Terraform Workflow

```mermaid
flowchart LR

subgraph TERRAFORM["🏗️ Terraform Execution Flow"]
direction LR

    MODULE["📦 Terraform Module<br/>Infrastructure Code"]:::module

    INIT["⚙️ terraform init<br/>Initialize Providers"]:::command

    VALIDATE["✅ terraform validate<br/>Validate Configuration"]:::verify

    PLAN["📋 terraform plan<br/>Preview Changes"]:::command

    APPLY["🚀 terraform apply<br/>Provision Resources"]:::success

    MODULE --> INIT
    INIT --> VALIDATE
    VALIDATE --> PLAN
    PLAN --> APPLY

end


classDef module fill:#7030A0,stroke:#351C75,color:#FFFFFF,stroke-width:2px
classDef command fill:#1565C0,stroke:#0D47A1,color:#FFFFFF,stroke-width:2px
classDef verify fill:#00897B,stroke:#00695C,color:#FFFFFF,stroke-width:2px
classDef success fill:#2E7D32,stroke:#1B5E20,color:#FFFFFF,stroke-width:2px

style TERRAFORM fill:#EDE7FF,stroke:#623CE4,stroke-width:3px,color:#000000
```

## 🚀 Terragrunt Workflow

```mermaid
flowchart LR

subgraph TERRAGRUNT["🚀 Terragrunt Orchestration Flow"]
direction LR

    CONFIG["📄 terragrunt.hcl<br/>Shared Configuration"]:::config

    ENV["📂 Environment<br/>Dev / QA / UAT / Prod"]:::environment

    MODULES["📦 Multiple Terraform Modules"]:::module

    PLAN["📋 terragrunt run --all plan<br/>Plan Multiple Modules"]:::command

    APPLY["🚀 terragrunt run --all apply<br/>Apply Multiple Modules"]:::success

    CONFIG --> ENV
    ENV --> MODULES
    MODULES --> PLAN
    PLAN --> APPLY

end


classDef config fill:#FFC000,stroke:#BF9000,color:#000000,stroke-width:2px
classDef environment fill:#2F75B5,stroke:#1F4E79,color:#FFFFFF,stroke-width:2px
classDef module fill:#7030A0,stroke:#351C75,color:#FFFFFF,stroke-width:2px
classDef command fill:#1565C0,stroke:#0D47A1,color:#FFFFFF,stroke-width:2px
classDef success fill:#2E7D32,stroke:#1B5E20,color:#FFFFFF,stroke-width:2px

style TERRAGRUNT fill:#E0F7FF,stroke:#00AEEF,stroke-width:3px,color:#000000
```

---

# 🛠️ Demo Execution & Usage

Navigate to the Terragrunt working directory:

```bash
cd terragrunt
```

Initialize the configuration:

```bash
terragrunt run --all init
```

Generate execution plans:

```bash
terragrunt run --all plan
```

Apply the infrastructure:

```bash
terragrunt run --all apply
```

Destroy the demonstration infrastructure when finished:

```bash
terragrunt run --all destroy
```

> 💡 **Demo Recommendation:** Run `plan` before `apply` during demonstrations so that the generated infrastructure changes can be reviewed before provisioning resources.

---

## 🔄 Terragrunt Execution Flow

```mermaid
flowchart TD

START(["🚀 Start Demo"]):::start

INIT["⚙️ terragrunt run --all init"]:::command

PLAN["📋 terragrunt run --all plan"]:::command

DECISION{"❓ Plan<br/>Reviewed?"}:::decision

APPLY["🚀 terragrunt run --all apply"]:::success

DESTROY["🗑️ terragrunt run --all destroy"]:::cleanup

END(["✅ Demo Completed"]):::end


START --> INIT
INIT --> PLAN
PLAN --> DECISION

DECISION -->|✅ Yes| APPLY
DECISION -->|❌ No| PLAN

APPLY --> DESTROY
DESTROY --> END


classDef start fill:#1F4E79,stroke:#0B2D4D,color:#FFFFFF,stroke-width:3px
classDef command fill:#1565C0,stroke:#0D47A1,color:#FFFFFF,stroke-width:2px
classDef decision fill:#F9A825,stroke:#F57F17,color:#000000,stroke-width:3px
classDef success fill:#2E7D32,stroke:#1B5E20,color:#FFFFFF,stroke-width:2px
classDef cleanup fill:#B71C1C,stroke:#7F0000,color:#FFFFFF,stroke-width:2px
classDef end fill:#00897B,stroke:#00695C,color:#FFFFFF,stroke-width:3px
```

---

# 🧩 Key Configuration Patterns

## 📄 Root `terragrunt.hcl`

The root configuration acts as the **common configuration layer** for the environments.

```hcl
remote_state {
  backend = "s3"

  config = {
    bucket = "knight-tfstate-${get_aws_account_id()}"
    key    = "${path_relative_to_include()}/terraform.tfstate"
    region = "us-east-1"

    encrypt        = true
    dynamodb_table = "knight-terragrunt-locks"
  }
}
```

### 🔍 Configuration Breakdown

```mermaid
flowchart TB

ROOT["📄 Root terragrunt.hcl"]:::root

BACKEND["🗄️ S3 Remote State"]:::storage
KEY["🔑 Dynamic State Key<br/>path_relative_to_include()"]:::config
REGION["🌎 AWS Region<br/>us-east-1"]:::config
ENCRYPT["🔐 State Encryption<br/>encrypt = true"]:::security
LOCK["🔒 State Locking<br/>DynamoDB"]:::security


ROOT --> BACKEND
ROOT --> KEY
ROOT --> REGION
ROOT --> ENCRYPT
ROOT --> LOCK


classDef root fill:#1F4E79,stroke:#0B2D4D,color:#FFFFFF,stroke-width:3px
classDef storage fill:#7030A0,stroke:#351C75,color:#FFFFFF,stroke-width:2px
classDef config fill:#FFC000,stroke:#BF9000,color:#000000,stroke-width:2px
classDef security fill:#B71C1C,stroke:#7F0000,color:#FFFFFF,stroke-width:2px
```

> ⚠️ **Note:** Remote-state locking configuration depends on the Terraform/AWS/Terragrunt versions used in the demo. Validate the chosen backend configuration against the versions installed in the environment before presenting it as a production pattern.

---

## 🌎 Environment-Specific Configuration

Each environment can inherit the root configuration using `include`.

```hcl
include {
  path = find_in_parent_folders()
}

inputs = {
  environment = "dev"
  project     = "KNIGHT"
}
```

The same pattern can be used for QA, UAT, and Production while changing only the environment-specific inputs.

```mermaid
flowchart TD

ROOT["📄 Root<br/>terragrunt.hcl"]:::root

DEV["📁 Dev<br/>environment = dev"]:::environment
QA["📁 QA<br/>environment = qa"]:::environment
UAT["📁 UAT<br/>environment = uat"]:::environment
PROD["📁 Prod<br/>environment = prod"]:::environment


ROOT --> DEV
ROOT --> QA
ROOT --> UAT
ROOT --> PROD


classDef root fill:#1F4E79,stroke:#0B2D4D,color:#FFFFFF,stroke-width:3px
classDef environment fill:#2F75B5,stroke:#1F4E79,color:#FFFFFF,stroke-width:2px
```

---

# 🔗 Dependency Management

One of Terragrunt's useful capabilities is managing dependencies between infrastructure components.

For example:

```mermaid
flowchart LR

NETWORK["🌐 Network"]:::network

COMPUTE["💻 Compute"]:::compute

DATABASE["🗄️ Database"]:::database


NETWORK --> COMPUTE
COMPUTE --> DATABASE


classDef network fill:#1565C0,stroke:#0D47A1,color:#FFFFFF,stroke-width:2px
classDef compute fill:#70AD47,stroke:#385723,color:#FFFFFF,stroke-width:2px
classDef database fill:#7030A0,stroke:#351C75,color:#FFFFFF,stroke-width:2px
```

The dependency relationship can ensure that infrastructure is processed in an appropriate order.

---

# 📊 Terragrunt Advantages & Disadvantages

```mermaid
flowchart LR

ROOT["🚀 Terragrunt"]:::title


subgraph ADV["✅ Advantages"]
direction TB

A1["🧩 DRY Configuration<br/>Less duplicate Terraform code"]:::advantage
A2["🗄️ Centralized State<br/>Reusable backend configuration"]:::advantage
A3["🔗 Dependency Management<br/>Automatic module ordering"]:::advantage
A4["🌎 Multi Environment<br/>Dev / QA / UAT / Prod"]:::advantage
A5["⚡ Multi-Module Execution<br/>Simplified orchestration"]:::advantage

A1 --> A2
A2 --> A3
A3 --> A4
A4 --> A5

end


subgraph DIS["❌ Disadvantages"]
direction TB

D1["📚 Learning Curve<br/>Additional concepts"]:::disadvantage
D2["🔧 Extra Dependency<br/>Terraform + Terragrunt"]:::disadvantage
D3["🕵️ Debugging Complexity<br/>Additional abstraction layer"]:::disadvantage
D4["🌐 Smaller Ecosystem<br/>Compared with Terraform"]:::disadvantage

D1 --> D2
D2 --> D3
D3 --> D4

end


ROOT --> ADV
ROOT --> DIS


classDef title fill:#1F4E79,stroke:#0B2D4D,color:#FFFFFF,stroke-width:3px
classDef advantage fill:#70AD47,stroke:#385723,color:#FFFFFF,stroke-width:2px
classDef disadvantage fill:#C00000,stroke:#7F0000,color:#FFFFFF,stroke-width:2px

style ADV fill:#1E3A1E,stroke:#70AD47,stroke-width:3px,color:#FFFFFF
style DIS fill:#3A1E1E,stroke:#C00000,stroke-width:3px,color:#FFFFFF
```

---

# 🧪 Provisioned Resources & Demo Scope

This demonstration is designed to focus on **Terragrunt architecture and orchestration** rather than maintaining long-running cloud infrastructure.

The demo can demonstrate:

* 🗄️ Remote Terraform state management
* 🔒 State locking
* 🧩 DRY configuration
* 🌎 Multi-environment configuration
* 🔗 Module dependencies
* ⚡ Multi-module execution
* 📋 Terraform plan generation
* 🚀 Terraform infrastructure deployment
* 🗑️ Automated teardown

### 🧹 Cleanup

After completing the demonstration, remove the demonstration infrastructure:

```bash
terragrunt run --all destroy
```

Verify that the demonstration resources have been removed before considering the demo complete.

---

# 🏁 End-to-End Terragrunt Architecture

```mermaid
flowchart LR

USER["👨‍💻 Developer"]:::start

CONFIG["📄 terragrunt.hcl<br/>Shared Configuration"]:::config

ENV["🌎 Environment<br/>Dev / QA / UAT / Prod"]:::environment

MODULES["📦 Terraform Modules<br/>Network / Compute / Storage / Database"]:::module

INIT["⚙️ run --all init"]:::command

PLAN["📋 run --all plan"]:::command

APPLY["🚀 run --all apply"]:::success

INFRA["☁️ Cloud Infrastructure"]:::cloud


USER --> CONFIG
CONFIG --> ENV
ENV --> MODULES
MODULES --> INIT
INIT --> PLAN
PLAN --> APPLY
APPLY --> INFRA


classDef start fill:#1F4E79,stroke:#0B2D4D,color:#FFFFFF,stroke-width:3px
classDef config fill:#FFC000,stroke:#BF9000,color:#000000,stroke-width:2px
classDef environment fill:#2F75B5,stroke:#1F4E79,color:#FFFFFF,stroke-width:2px
classDef module fill:#7030A0,stroke:#351C75,color:#FFFFFF,stroke-width:2px
classDef command fill:#1565C0,stroke:#0D47A1,color:#FFFFFF,stroke-width:2px
classDef success fill:#2E7D32,stroke:#1B5E20,color:#FFFFFF,stroke-width:2px
classDef cloud fill:#00897B,stroke:#00695C,color:#FFFFFF,stroke-width:3px
```

---

## 🎯 Learning Objectives

After completing this demonstration, you should understand:

* [ ] What Terragrunt is and how it complements Terraform
* [ ] Why DRY configuration is useful for multi-environment infrastructure
* [ ] How `terragrunt.hcl` inheritance works
* [ ] How `path_relative_to_include()` can create environment-specific state paths
* [ ] How Terragrunt organizes reusable Terraform modules
* [ ] How dependencies can be represented between modules
* [ ] How to execute Terraform operations across multiple modules
* [ ] How to manage Dev, QA, UAT, and Production configurations
* [ ] How remote state and state locking fit into the architecture
* [ ] How to safely plan, apply, and destroy demonstration infrastructure

---

## 🚀 Key Takeaway

> **Terraform provisions infrastructure. Terragrunt organizes, configures, and orchestrates Terraform at scale.**

The key architectural pattern demonstrated in this directory is:

```mermaid
flowchart LR

TERRAFORM["🏗️ Terraform<br/>Infrastructure as Code"]:::terraform

TERRAGRUNT["🚀 Terragrunt<br/>Orchestration & DRY Configuration"]:::terragrunt

ENV["🌎 Multi-Environment<br/>Dev / QA / UAT / Prod"]:::environment

CLOUD["☁️ Cloud Infrastructure"]:::cloud


TERRAGRUNT --> TERRAFORM
TERRAGRUNT --> ENV
TERRAFORM --> CLOUD


classDef terraform fill:#623CE4,stroke:#352080,color:#FFFFFF,stroke-width:2px
classDef terragrunt fill:#00AEEF,stroke:#006699,color:#FFFFFF,stroke-width:3px
classDef environment fill:#2F75B5,stroke:#1F4E79,color:#FFFFFF,stroke-width:2px
classDef cloud fill:#00897B,stroke:#00695C,color:#FFFFFF,stroke-width:3px
```

**Terragrunt is most valuable when Terraform infrastructure grows beyond a small number of modules and environments, where configuration reuse, dependency management, state consistency, and orchestration become increasingly important.**
