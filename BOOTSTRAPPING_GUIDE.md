# KNIGHT Automated Bootstrapping Guide

## Overview

This document describes the automated bootstrapping implementation that eliminates manual AWS resource creation for the KNIGHT demo project. The pipelines now automatically create required S3 buckets and DynamoDB tables before running Terraform operations.

## Problem Solved

Previously, the Terraform pipeline required manual creation of state backend resources:
- `knight-tfstate-stage-manual` S3 bucket
- `knight-tfstate-prod-manual` S3 bucket  
- `knight-tf-locks-stage` DynamoDB table
- `knight-tf-locks-prod` DynamoDB table

This manual step was an anti-pattern that has been eliminated through automation.

## Solution Implemented

### 1. Bootstrapping Script

Created `scripts/bootstrap-terraform-backend.sh` with the following features:

- **Idempotent Operations**: Checks if resources exist before creation
- **Regional Handling**: Properly handles `us-east-1` vs other regions
- **Security Best Practices**: 
  - Enables S3 bucket versioning
  - Enables default encryption (AES256)
  - Blocks public access
- **Error Handling**: Set `set -e` for immediate failure on errors
- **Clear Logging**: Provides detailed progress output

### 2. Pipeline Updates

#### Terraform Pipeline (`.github/workflows/terraform-pipeline.yml`)

Added a `bootstrap` job that:
1. Runs before the Terraform job
2. Configures AWS credentials
3. Executes the bootstrapping script
4. Creates required S3 buckets and DynamoDB tables

The Terraform job now depends on the bootstrap job via `needs: bootstrap`.

#### Terragrunt Pipeline

No changes required - Terragrunt already has built-in auto-provisioning capabilities.

### 3. Documentation Updates

Updated comments in `terraform/stage/backend.tf` and `terraform/prod/backend.tf` to reflect that manual resource creation is no longer required.

## Pipeline Flow

### Terraform Pipeline

```
1. Bootstrap Job (runs first)
   ├── Checkout code
   ├── Configure AWS credentials
   └── Run bootstrap script
       ├── Create/verify S3 buckets
       └── Create/verify DynamoDB tables

2. Terraform Job (runs after bootstrap succeeds)
   ├── Checkout code
   ├── Setup Terraform
   ├── Format check
   ├── Init (now succeeds - backend exists)
   ├── Validate
   ├── Plan
   └── Apply (push events only)
```

### Terragrunt Pipeline

```
1. Plan Job
   ├── Checkout code
   └── Terragrunt run-all plan
       (Auto-provisions state backend on first run)

2. Apply Job (push events only)
   ├── Checkout code
   └── Terragrunt run-all apply
```

## Required GitHub Secrets

Both pipelines require the following GitHub repository secrets:

| Secret Name | Description | Example |
|-------------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | AWS access key for IAM user KNIGHT_mark_1 | `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` |
| `AWS_SECRET_ACCESS_KEY` | AWS secret key for IAM user KNIGHT_mark_1 | `XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX` |

### How to Configure Secrets

1. Go to your GitHub repository
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add each secret with its corresponding value
5. Click **Add secret**

## IAM User Permissions Required

The IAM user `KNIGHT_mark_1` must have the following permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:*",
        "dynamodb:*",
        "iam:GetUser"
      ],
      "Resource": "*"
    }
  ]
}
```

## Testing the Pipeline

### Prerequisites

1. Configure GitHub repository secrets
2. Ensure IAM user has required permissions
3. No existing AWS resources required (pipeline creates them)

### Running the Pipeline

```bash
# Ensure you're on the correct branch
git checkout K_Test_1

# Push to trigger the pipeline
git push origin K_Test_1
```

### Expected Behavior

1. **Bootstrap Job**: Creates S3 buckets and DynamoDB tables
2. **Terraform Job**: Successfully initializes and deploys infrastructure
3. **Terragrunt Job**: Auto-provisions its own state backend and deploys

## Verification Steps

After pipeline completion, verify resources were created:

```bash
# List S3 buckets
aws s3 ls

# Expected output:
# 2024-01-15 10:30:00 knight-tfstate-stage-manual
# 2024-01-15 10:30:05 knight-tfstate-prod-manual
# 2024-01-15 10:31:00 knight-tfstate-<account-id>

# List DynamoDB tables
aws dynamodb list-tables

# Expected output:
# {
#   "TableNames": [
#     "knight-tf-locks-stage",
#     "knight-tf-locks-prod",
#     "knight-terragrunt-locks"
#   ]
# }
```

## Comparison: Terraform vs Terragrunt

| Aspect | Terraform Pipeline | Terragrunt Pipeline |
|--------|-------------------|---------------------|
| **State Backend Creation** | Manual script in pipeline | Built-in auto-provisioning |
| **Backend Configuration** | Hardcoded per environment | Dynamic single source of truth |
| **Code Reuse** | Copy-pasted backend blocks | DRY via include blocks |
| **Setup Complexity** | Requires bootstrapping script | Zero configuration |

## Cleanup

To remove all resources and stop costs:

```bash
git checkout AWS_Destroy_KNIGHT_mark_1
git push origin AWS_Destroy_KNIGHT_mark_1
```

This triggers the destruction pipeline that removes all AWS resources.

## Troubleshooting

### Bootstrap Job Fails

**Issue**: AWS credentials not configured correctly
**Solution**: Verify GitHub secrets are set correctly and IAM user has required permissions

**Issue**: Bucket name already exists in different account
**Solution**: The script is idempotent - it will use existing buckets if they exist

### Terraform Init Fails

**Issue**: Bootstrap job didn't complete successfully
**Solution**: Check bootstrap job logs in GitHub Actions

**Issue**: Backend configuration mismatch
**Solution**: Verify bucket names in `backend.tf` match script configuration

### Regional Issues

**Issue**: Bucket creation fails in non-us-east-1 regions
**Solution**: The script handles regional constraints automatically. Ensure `AWS_DEFAULT_REGION` is set correctly.

## Benefits

1. **Zero Manual Setup**: No AWS Console required before running pipelines
2. **Idempotent**: Safe to run multiple times
3. **Security**: Automatically applies security best practices
4. **Consistency**: Ensures all environments have identical backend configuration
5. **Demo-Ready**: Perfect for live demonstrations without manual intervention

## Future Improvements

Potential enhancements:
- Add support for custom bucket names via environment variables
- Implement bucket lifecycle policies for cost optimization
- Add CloudTrail logging for audit trail
- Support for multiple regions
- Integration with AWS Organizations for multi-account setups
