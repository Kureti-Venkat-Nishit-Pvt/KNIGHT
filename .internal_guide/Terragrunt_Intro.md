# Terragrunt Introduction for KNIGHT Demo

## What is Terragrunt?

Terragrunt is a thin wrapper for Terraform that provides extra tools for keeping your Terraform configurations DRY (Don't Repeat Yourself), working with multiple Terraform modules, and managing remote state.

## Core Concepts

### 1. DRY Configuration

Terragrunt allows you to define your Terraform configuration once and reuse it across multiple environments.

### 2. Remote State Management

Terragrunt can automatically create and manage your Terraform remote state backend (S3 + DynamoDB).

### 3. Dependency Management

Terragrunt can automatically handle dependencies between different Terraform modules.

## KNIGHT Terragrunt Architecture

### Root Configuration (`terragrunt.hcl`)

```hcl
# Define remote state backend ONCE for all environments
remote_state {
  backend = "s3"
  config = {
    bucket         = "knight-tfstate-${get_aws_account_id()}"
    key            = "${path_relative_to_include()}/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "knight-terragrunt-locks"
  }
}

# Define provider configuration ONCE
generate "provider" {
  path      = "provider.tf"
  if_exists = "skip"
  contents  = <<EOF
provider "aws" {
  region = "us-east-1"
}
EOF
}
```

### Environment Configuration (`stage/terragrunt.hcl`)

```hcl
# Include root configuration
include "root" {
  path = find_in_parent_folders()
}

# Define environment-specific inputs
inputs = {
  environment = "stage"
}

# Specify which Terraform module to use
terraform {
  source = "${get_terragrunt_dir()}/../modules//s3-bucket"
}
```

### Module Definition (`modules/s3-bucket/main.tf`)

```hcl
resource "aws_s3_bucket" "storage" {
  bucket = var.bucket_name
}

resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.storage.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {
  bucket = aws_s3_bucket.storage.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "public_access" {
  bucket                  = aws_s3_bucket.storage.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
```

## Key Terragrunt Functions

### `get_aws_account_id()`

Dynamically retrieves the current AWS account ID, allowing the same configuration to work across different accounts.

### `path_relative_to_include()`

Returns the relative path from the included configuration to the current configuration. This enables automatic state key generation:

- `stage/terragrunt.hcl` → state key: `stage/terraform.tfstate`
- `prod/terragrunt.hcl` → state key: `prod/terraform.tfstate`

### `find_in_parent_folders()`

Searches up the directory tree for the specified file, enabling hierarchical configuration inheritance.

## Terragrunt Commands

| Command | Description |
|---------|-------------|
| `terragrunt run-all plan` | Run `terraform plan` across all modules in the dependency graph |
| `terragrunt run-all apply` | Run `terraform apply` across all modules, respecting dependency order |
| `terragrunt run-all destroy` | Run `terraform destroy` across all modules in reverse dependency order |
| `terragrunt hclfmt` | Format all Terragrunt configuration files (similar to `terraform fmt`) |

## Benefits Over Raw Terraform

### 1. Single Source of Truth

Define backend and provider configuration once, inherit everywhere.

### 2. Automatic State Management

No manual S3 bucket or DynamoDB table creation required.

### 3. Environment Isolation

Automatic state key generation prevents environment conflicts.

### 4. Code Reuse

Modules can be shared across environments with environment-specific inputs.

### 5. Dependency Handling

Automatic dependency resolution ensures correct deployment order.

## Common Patterns

### Multi-Environment Setup

```
terragrunt/
├── terragrunt.hcl           # Root configuration
├── live/
│   ├── prod/
│   │   └── terragrunt.hcl  # Includes root, defines prod inputs
│   ├── stage/
│   │   └── terragrunt.hcl  # Includes root, defines stage inputs
│   └── dev/
│       └── terragrunt.hcl  # Includes root, defines dev inputs
└── modules/
    ├── vpc/
    ├── database/
    └── app-server/
```

### Multi-Account Setup

Use `get_aws_account_id()` to automatically configure account-specific resources:

```hcl
inputs = {
  account_id = get_aws_account_id()
  region     = "us-east-1"
}
```

## Migration from Raw Terraform

### Step 1: Create Terragrunt Structure

```bash
mkdir -p terragrunt/live/{prod,stage}
mkdir -p terragrunt/modules/{your-modules}
```

### Step 2: Extract Modules

Move reusable Terraform code into `modules/` directories.

### Step 3: Create Root Configuration

Create `terragrunt.hcl` with backend and provider definitions.

### Step 4: Create Environment Configurations

Create environment-specific `terragrunt.hcl` files that include the root.

### Step 5: Test with Plan

```bash
cd terragrunt
terragrunt run-all plan
```

### Step 6: Migrate State (Optional)

Use `terraform state mv` to migrate existing state to the new backend.

## Best Practices

1. Keep modules small — each module should manage a single resource or closely related resources
2. Use descriptive names for modules and directories
3. Pin Terraform and provider versions in `versions.tf` files
4. Document module inputs and outputs in README files
5. Test modules in isolation before integrating into larger deployments

## Troubleshooting

### State Lock Issues

```bash
terragrunt force-unlock <LOCK_ID>
```

### Dependency Cycles

Terragrunt will detect and report dependency cycles. Reorganize your module structure to break cycles.

### Authentication Issues

Ensure AWS credentials are properly configured before running Terragrunt commands.

## Resources

- Official Documentation: https://terragrunt.gruntwork.io/
- GitHub Repository: https://github.com/gruntwork-io/terragrunt
- Community: https://terragrunt.gruntwork.io/docs/community/
