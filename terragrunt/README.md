# Terragrunt Module Architecture and Usage Guide

This directory exists for educational and demonstration purposes to explain what Terragrunt is, why it is used over raw Terraform, and how it reduces code duplication across multi-environment deployments.

---

## Core Concepts & Educational Overview

### What is Terragrunt

Terragrunt is a thin wrapper for Terraform that enforces DRY (Don't Repeat Yourself) code practices and manages backend state configurations dynamically. It provides a way to keep your Terraform code DRY by allowing you to define your Terraform modules once and then use them across multiple environments with different configurations.

### Why Terragrunt

Terragrunt eliminates duplicate `backend.tf` definitions across environments (`stage/` vs `prod/`) using dynamic parent inheritance (`path_relative_to_include()`). Instead of hardcoding backend configurations in every environment directory, Terragrunt allows you to define the backend once in a root configuration file and have all child environments inherit it automatically.

This approach offers several advantages:

- **Single source of truth**: Backend configuration is defined once in the root `terragrunt.hcl`
- **Dynamic state paths**: State file paths are automatically generated based on directory structure
- **Auto-provisioning**: Terragrunt can automatically create the S3 bucket and DynamoDB table for state management on first run
- **DRY principles**: Eliminates copy-paste errors and reduces maintenance overhead

---

## Demo Execution & Usage Instructions

To run the Terragrunt demo locally, execute the following commands:

```bash
cd terragrunt/
terragrunt run-all init
terragrunt run-all plan
terragrunt run-all apply
```

The `run-all` command orchestrates concurrent execution across multiple environment sub-directories simultaneously. This means that commands like `plan` and `apply` are executed in parallel for all environments (stage, prod, etc.), significantly reducing the time required for multi-environment deployments.

### Command Breakdown

- `terragrunt run-all init`: Initializes the Terraform working directory for all modules, downloading providers and setting up the backend state
- `terragrunt run-all plan`: Generates execution plans for all modules to show what changes will be made
- `terragrunt run-all apply`: Applies the changes to all modules based on the generated plans

---

## Provisioned Resources Summary

Note: No active long-running AWS resources are created during this demonstration. The execution validates dynamic backend bootstrapping (S3 bucket and DynamoDB locking table creation) and dry-run execution plans (`terragrunt run-all plan`). Active infrastructure resources are immediately cleaned up via our automated teardown pipeline.

The demonstration focuses on:

- **Backend state management**: Automatic creation of S3 bucket for Terraform state storage
- **State locking**: DynamoDB table for preventing concurrent state modifications
- **DRY configuration**: Inheritance patterns that eliminate code duplication
- **Multi-environment orchestration**: Concurrent execution across stage and prod environments

---

## Directory Structure

```
terragrunt/
├── terragrunt.hcl             # Root configuration with backend and provider definitions
├── stage/
│   └── terragrunt.hcl         # Stage-specific configuration (includes root)
├── prod/
│   └── terragrunt.hcl         # Prod-specific configuration (includes root)
└── modules/
    └── s3-bucket/             # Reusable Terraform module for S3 bucket creation
        ├── main.tf
        ├── variables.tf
        ├── outputs.tf
        └── versions.tf
```

## Key Configuration Patterns

### Root Configuration (terragrunt.hcl)

The root `terragrunt.hcl` file defines the backend configuration once:

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

### Environment-Specific Configuration

Child environments use the `include` block to inherit from the root:

```hcl
include {
  path = find_in_parent_folders()
}

inputs = {
  environment = "stage"
  project     = "KNIGHT"
}
```

This pattern ensures that all environments share the same backend configuration while allowing environment-specific input variables.
