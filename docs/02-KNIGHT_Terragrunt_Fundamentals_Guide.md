# 🌳 Terragrunt


![Azure](https://img.shields.io/badge/Microsoft_Azure-Service_Principal-0078D4?style=for-the-badge&logo=microsoftazure)

![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?style=for-the-badge&logo=terraform)
![Terragrunt](https://img.shields.io/badge/Terragrunt-Wrapper-4CAF50?style=for-the-badge&logo=terraform)

![GitHub](https://img.shields.io/badge/GitHub-Secrets-181717?style=for-the-badge&logo=github)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-2088FF?style=for-the-badge&logo=github-actions)
---

# 📖 Document Information

![Project](https://img.shields.io/badge/Project-KNIGHT-blue?style=for-the-badge)
[![Repository](https://img.shields.io/badge/Repository-Kureti--Venkat--Nishit--Pvt%2FKNIGHT-success?style=for-the-badge&logo=github)](https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT)

![Master Branch](https://img.shields.io/badge/Baseline-main-orange?style=for-the-badge&logo=git)
![Feature Branch](https://img.shields.io/badge/Feature-Azure_VM_Deploy-blueviolet?style=for-the-badge&logo=git)

![Target VM](https://img.shields.io/badge/VM-KNIGHT--WinDev--VM-0078D4?style=for-the-badge&logo=windows)
![Platform](https://img.shields.io/badge/Platform-Microsoft_Azure-0078D4?style=for-the-badge&logo=microsoftazure)
![Operating System](https://img.shields.io/badge/OS-Windows_Server_2022-0078D6?style=for-the-badge&logo=windows)

---

## Overview

| Question | Answer |
|----------|--------|
| **What is it?** | Terragrunt is a thin wrapper for Terraform that helps reduce code duplication, manage remote state, orchestrate multiple Terraform modules, and simplify Infrastructure as Code management. |
| **What is it used for?** | It provides reusable configurations, centralized remote state management, dependency management, and the ability to execute Terraform across multiple environments and modules. |
| **When do we use it?** | When managing multiple environments (Development, QA, UAT, Production), multiple AWS/Azure accounts, or large infrastructure deployments with many Terraform modules. |
| **Why are we implementing it?** | To improve maintainability, reduce duplicated code (DRY principle), standardize Terraform deployments, and simplify infrastructure management at scale. |

---

## Terragrunt Architecture

```mermaid
flowchart TD

A[Developer]

A --> B[Terragrunt]

B --> C[Shared Configuration]

B --> D[Terraform Modules]

C --> E[Development]

C --> F[QA]

C --> G[UAT]

C --> H[Production]

E --> I[Terraform]

F --> I

G --> I

H --> I

I --> J[Cloud Infrastructure]
```

---

## Typical Folder Structure

```text
live/
├── terragrunt.hcl
├── dev/
│   ├── network/
│   │   └── terragrunt.hcl
│   └── compute/
│       └── terragrunt.hcl
├── qa/
├── uat/
└── prod/

modules/
├── network/
├── storage/
├── compute/
└── database/
```

---

## Commands & Variations

| Purpose | Command |
|---------|---------|
| Initialize Terraform using Terragrunt | `terragrunt init` |
| Generate execution plan | `terragrunt plan` |
| Apply infrastructure | `terragrunt apply` |
| Destroy infrastructure | `terragrunt destroy` |
| Run command across all modules | `terragrunt run-all plan` |
| Apply all modules | `terragrunt run-all apply` |
| Destroy all modules | `terragrunt run-all destroy` |
| Validate all modules | `terragrunt run-all validate` |
| Format all Terragrunt files | `terragrunt hclfmt` |

---

## Sample Output

```text
INFO[0000] Downloading Terraform configurations...

INFO[0002] Initializing Terraform...

INFO[0005] Running command:

terraform plan

Plan: 3 to add, 0 to change, 0 to destroy.
```

---

# 📊 Terraform vs Terragrunt

| Feature | Terraform | Terragrunt |
|---------|-----------|------------|
| Infrastructure Provisioning | ✅ | ✅ (uses Terraform internally) |
| State Management | Manual Configuration | Automated & Centralized |
| Code Reusability | Modules | Modules + Shared Configuration |
| Multi-Environment Support | Manual | Built-in |
| Dependency Management | Limited | Built-in |
| DRY (Don't Repeat Yourself) | Limited | Excellent |
| Remote State Configuration | Repeated in every project | Centralized |
| Execute Multiple Modules | Manual | `run-all` Commands |
| Learning Curve | Easy | Moderate |
| Suitable For | Small to Medium Projects | Medium to Enterprise Projects |

---

## Terraform vs Terragrunt Workflow

```mermaid
flowchart LR

subgraph Terraform

A1[Terraform Module]

A1 --> A2[terraform init]

A2 --> A3[terraform plan]

A3 --> A4[terraform apply]

end

subgraph Terragrunt

B1[Terragrunt]

B1 --> B2[Shared Config]

B2 --> B3[Multiple Terraform Modules]

B3 --> B4[run-all plan]

B4 --> B5[run-all apply]

end
```

---

# 📊 Advantages & Disadvantages

## Advantages

| Advantage | Description |
|-----------|-------------|
| ✅ DRY Configuration | Eliminates repeated Terraform code across environments. |
| ✅ Centralized Remote State | Configure the backend once and reuse it everywhere. |
| ✅ Dependency Management | Automatically handles module dependencies. |
| ✅ Multi-Environment Support | Easily manage Dev, QA, UAT, and Production. |
| ✅ Shared Variables | Centralizes common variables across environments. |
| ✅ Simplified Commands | `run-all` executes Terraform across multiple modules. |

---

## Disadvantages

| Limitation | Description |
|------------|-------------|
| ❌ Additional Learning Curve | Teams must learn Terragrunt concepts and configuration. |
| ❌ Extra Dependency | Requires Terragrunt to be installed in addition to Terraform. |
| ❌ More Abstraction | Debugging can be slightly more complex because Terragrunt wraps Terraform. |
| ❌ Smaller Community | Terraform has a much larger ecosystem and community support. |

---