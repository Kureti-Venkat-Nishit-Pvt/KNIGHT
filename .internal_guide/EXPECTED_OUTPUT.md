# KNIGHT Expected Output Guide

## Terraform Raw Demo Expected Outputs

### Stage Environment Setup

```bash
$ cd terraform/stage
$ terraform init

Initializing the backend...
Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Using previously-installed hashicorp/aws v5.0.0

Terraform has been successfully initialized!
```

### Terraform Plan Output

```bash
$ terraform plan

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_s3_bucket.storage will be created
  + resource "aws_s3_bucket" "storage" {
      + bucket                          = "knight-raw-stage-storage"
      + force_destroy                   = false
      + id                              = (known after apply)
      + region                          = "us-east-1"
    }

  # aws_s3_bucket_public_access_block.storage will be created
  + resource "aws_s3_bucket_public_access_block" "storage" {
      + block_public_acls       = true
      + block_public_policy     = true
      + bucket                  = (known after apply)
    }

Plan: 3 to add, 0 to change, 0 to destroy.
```

### Terraform Apply Output

```bash
$ terraform apply

aws_s3_bucket.storage: Creating...
aws_s3_bucket.storage: Creation complete after 2s
aws_s3_bucket_versioning.versioning: Creating...
aws_s3_bucket_versioning.versioning: Creation complete after 1s
aws_s3_bucket_server_side_encryption_configuration.encryption: Creating...
aws_s3_bucket_server_side_encryption_configuration.encryption: Creation complete after 1s
aws_s3_bucket_public_access_block.storage: Creating...
aws_s3_bucket_public_access_block.storage: Creation complete after 1s

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
```

### Terraform Output

```bash
$ terraform output

bucket_name = "knight-raw-stage-storage"
bucket_arn = "arn:aws:s3:::knight-raw-stage-storage"
bucket_region = "us-east-1"
```

## Terragrunt Demo Expected Outputs

### Root Configuration Check

```bash
$ cd terragrunt
$ cat terragrunt.hcl

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
```

### Terragrunt Run-All Plan Output

```bash
$ terragrunt run-all plan

[terragrunt] [/terragrunt/stage] Running command: terraform plan
[terragrunt] [/terragrunt/prod] Running command: terraform plan

[terragrunt] [/terragrunt/stage] module.s3-bucket.aws_s3_bucket.storage: Refreshing state...

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.s3-bucket.aws_s3_bucket.storage will be created
  + resource "aws_s3_bucket" "storage" {
      + bucket = "knight-stage-storage"
    }

Plan: 4 to add, 0 to change, 0 to destroy.

[terragrunt] [/terragrunt/prod] module.s3-bucket.aws_s3_bucket.storage: Refreshing state...

Terraform will perform the following actions:

  # module.s3-bucket.aws_s3_bucket.storage will be created
  + resource "aws_s3_bucket" "storage" {
      + bucket = "knight-prod-storage"
    }

Plan: 4 to add, 0 to change, 0 to destroy.
```

### Terragrunt Run-All Apply Output

```bash
$ terragrunt run-all apply

[terragrunt] [/terragrunt/stage] Running command: terraform apply
[terragrunt] [/terragrunt/prod] Running command: terraform apply

[terragrunt] [/terragrunt/stage] module.s3-bucket.aws_s3_bucket.storage: Creating...
[terragrunt] [/terragrunt/stage] module.s3-bucket.aws_s3_bucket.storage: Creation complete after 2s
[terragrunt] [/terragrunt/stage] Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

[terragrunt] [/terragrunt/prod] module.s3-bucket.aws_s3_bucket.storage: Creating...
[terragrunt] [/terragrunt/prod] module.s3-bucket.aws_s3_bucket.storage: Creation complete after 2s
[terragrunt] [/terragrunt/prod] Apply complete! Resources: 4 added, 0 changed, 0 destroyed.
```

### Automatic Backend Creation

```bash
[terragrunt] [/terragrunt/stage] Automatically creating S3 bucket for state backend: knight-tfstate-123456789012
[terragrunt] [/terragrunt/stage] Automatically creating DynamoDB table for state locking: knight-terragrunt-locks
[terragrunt] [/terragrunt/stage] Backend successfully initialized
```

## Pre-Commit Hooks Expected Output

### Pre-Commit Run

```bash
$ pre-commit run --all-files

terraform fmt....................................................................Passed
terraform validate.................................................................Passed
tflint...........................................................................Passed
tfsec............................................................................Passed
```

### Individual Hook Details

```bash
$ pre-commit run terraform_fmt --files terraform/stage/main.tf

terraform fmt....................................................................Passed
- Reformatted terraform/stage/main.tf
```

```bash
$ pre-commit run terraform_validate --files terraform/stage/main.tf

terraform validate.................................................................Passed
- Success! The configuration is valid.
```

```bash
$ pre-commit run tflint --files terraform/stage/main.tf

tflint...........................................................................Passed
- 0 issue(s) found in 1 file(s)
```

```bash
$ pre-commit run tfsec --files terraform/stage/main.tf

tfsec............................................................................Passed
- 0 potential problems detected
```

## GitHub Actions Pipeline Expected Output

### Terraform Pipeline Success

```yaml
Run terraform -chdir="terraform/stage" fmt -check
  ✅ Terraform format check passed

Run terraform -chdir="terraform/stage" init
  ✅ Terraform init successful for stage

Run terraform -chdir="terraform/stage" validate
  ✅ Terraform validation successful for stage

Run terraform -chdir="terraform/stage" plan
  ✅ Terraform plan successful for stage

Run terraform -chdir="terraform/stage" apply
  ✅ Terraform apply successful for stage
```

### Terragrunt Pipeline Success

```yaml
Run terragrunt run-all plan
  [terragrunt] [/terragrunt/stage] Plan successful
  [terragrunt] [/terragrunt/prod] Plan successful
  ✅ Terragrunt run-all plan successful

Run terragrunt run-all apply
  [terragrunt] [/terragrunt/stage] Apply successful
  [terragrunt] [/terragrunt/prod] Apply successful
  ✅ Terragrunt run-all apply successful
```

## Destruction Pipeline Expected Output

### Destroy Pipeline Execution (parallel jobs)

```yaml
Job: Terraform destroy (stage)
  aws_s3_bucket.storage: Destroying... [id=knight-raw-stage-storage]
  aws_s3_bucket.storage: Destruction complete after 3s
  ✅ Terraform destroy successful for stage

Job: Terraform destroy (prod)
  aws_s3_bucket.storage: Destroying... [id=knight-raw-prod-storage]
  aws_s3_bucket.storage: Destruction complete after 3s
  ✅ Terraform destroy successful for prod

Job: Terragrunt run-all destroy
  [terragrunt] [/terragrunt/prod] Destroying module.s3-bucket...
  [terragrunt] [/terragrunt/prod] Destroy complete
  [terragrunt] [/terragrunt/stage] Destroying module.s3-bucket...
  [terragrunt] [/terragrunt/stage] Destroy complete
  ✅ Terragrunt run-all destroy successful
```

## AWS Resource Verification

### S3 Buckets Created

```bash
$ aws s3 ls

2024-01-15 10:30:00 knight-raw-stage-storage
2024-01-15 10:30:05 knight-raw-prod-storage
2024-01-15 10:31:00 knight-stage-storage
2024-01-15 10:31:05 knight-prod-storage
```

### State Backend Buckets

```bash
$ aws s3 ls

2024-01-15 10:25:00 knight-tfstate-123456789012
2024-01-15 10:25:05 knight-tfstate-stage-manual
2024-01-15 10:25:10 knight-tfstate-prod-manual
```

### DynamoDB Lock Tables

```bash
$ aws dynamodb list-tables

{
  "TableNames": [
    "knight-terragrunt-locks",
    "knight-tf-locks-stage",
    "knight-tf-locks-prod"
  ]
}
```

## Cost Analysis

### Estimated Monthly Costs (Before Destruction)

- S3 Storage (4 buckets × ~1GB): $0.12
- S3 Requests (1000 PUT + 1000 GET): $0.005
- DynamoDB (3 tables × 25 RCU/WCU): $0.15
- **Total**: ~$0.27/month

### After Destruction

- All resources destroyed: $0.00/month
- Cost savings: 100%

## Troubleshooting Common Issues

### State Lock Errors

```bash
Error: Error acquiring the state lock
Error message: operation error DynamoDB: ConditionalCheckFailedException

Solution: terragrunt force-unlock <LOCK_ID>
```

### Authentication Errors

```bash
Error: error configuring Terraform AWS Provider
Error: could not validate provider credentials

Solution: Check AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY
```

### Backend Initialization Errors

```bash
Error: error initializing S3 backend
Error: Access Denied

Solution: Verify IAM user has S3 and DynamoDB permissions
```

## Success Indicators

### Demo Success Criteria

- ✅ Both Terraform and Terragrunt create S3 buckets successfully
- ✅ Pre-commit hooks pass without errors
- ✅ GitHub Actions pipelines complete successfully
- ✅ State backends are properly configured
- ✅ Resources are properly isolated by environment
- ✅ Destruction pipeline removes all resources
- ✅ No manual state backend creation required for Terragrunt
- ✅ All governance gates function correctly
