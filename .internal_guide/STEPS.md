# KNIGHT Presenter Guide: Step-by-Step Walkthrough

## Overview

This guide provides the complete step-by-step walkthrough for presenting the KNIGHT infrastructure demonstration.

## Prerequisites Check

- AWS credentials for IAM user `KNIGHT_mark_1` configured
- Local CLI tools installed: Terraform (≥1.5.0), Terragrunt (≥0.50.0), pre-commit, tflint, tfsec
- GitHub repository cloned and on appropriate branch

## Phase 1: Repository Overview (5 minutes)

### 1.1 Branch Strategy

- **K_Test_1**: Active development branch for Terraform vs Terragrunt demo
- **AWS_Destroy_KNIGHT_mark_1**: Emergency destruction pipeline branch
- **checkov**: Initial Checkov security demo (legacy)
- **Terragrunt**: Initial Terragrunt setup (legacy)

### 1.2 Repository Structure

```
KNIGHT/
├── terraform/              # Raw Terraform (anti-pattern)
│   ├── stage/             # Hardcoded backend
│   └── prod/              # Duplicate backend code
├── terragrunt/            # Terragrunt (DRY pattern)
│   ├── terragrunt.hcl     # Single backend definition
│   ├── stage/             # Inherits from root
│   ├── prod/              # Inherits from root
│   └── modules/           # Reusable modules
├── .github/workflows/     # CI/CD pipelines
└── .pre-commit-config.yaml # Local governance hooks
```

## Phase 2: Raw Terraform Demo (10 minutes)

### 2.1 Show the Anti-Pattern

```bash
cd terraform/stage
cat backend.tf
```

**Key Point**: Backend configuration is hardcoded with specific bucket names.

### 2.2 Manual State Backend Setup

```bash
# Must manually create S3 bucket and DynamoDB table
aws s3api create-bucket --bucket knight-tfstate-stage-manual --region us-east-1
aws dynamodb create-table --table-name knight-tf-locks-stage ...
```

### 2.3 Terraform Operations

```bash
terraform init
terraform plan
terraform apply
```

**Pain Points to Highlight**:

- Repetitive backend configuration across environments
- Manual state backend provisioning
- Copy-paste errors risk
- No code reuse

## Phase 3: Terragrunt Demo (10 minutes)

### 3.1 Show the DRY Pattern

```bash
cd terragrunt
cat terragrunt.hcl
```

**Key Point**: Single backend definition using `get_aws_account_id()` and `path_relative_to_include()`.

### 3.2 Automatic Backend Bootstrap

```bash
terragrunt run-all plan
```

**Magic Moment**: Terragrunt automatically creates the state backend on first run!

### 3.3 Terragrunt Operations

```bash
terragrunt run-all apply
```

**Benefits to Highlight**:

- Single source of truth for backend config
- Automatic state backend provisioning
- Code reuse via modules
- Environment-specific state keys auto-generated

## Phase 4: Governance & CI/CD (10 minutes)

### 4.1 Pre-Commit Hooks

```bash
cat .pre-commit-config.yaml
pre-commit run --all-files
```

**Governance Gates**:

- `terraform_fmt`: Code formatting
- `terraform_validate`: Syntax correctness
- `tflint`: Linting for best practices
- `tfsec`: Security scanning

### 4.2 GitHub Actions Pipelines

```bash
cat .github/workflows/terraform-pipeline.yml
cat .github/workflows/terragrunt-pipeline.yml
```

**CI/CD Flow**:

1. Developer commits locally
2. Pre-commit hooks validate code
3. Push to `K_Test_1` branch
4. Parallel pipelines trigger
5. Terraform: fmt → init → validate → plan → apply
6. Terragrunt: run-all plan → run-all apply

## Phase 5: Cost Optimization & Destruction (5 minutes)

### 5.1 Emergency Kill Switch

```bash
git checkout AWS_Destroy_KNIGHT_mark_1
cat .github/workflows/knight-destroy-pipeline.yml
```

**Safety Features**:

- Only triggers on specific branch
- Requires explicit push to destruction branch
- Authenticates via repository secrets (`KNIGHT_mark_1`)
- Parallel destroy: Terraform matrix + `terragrunt run-all destroy`

### 5.2 Execution

```bash
git push origin AWS_Destroy_KNIGHT_mark_1
```

**Result**: Complete teardown of all AWS resources to prevent ongoing costs.

## Phase 6: Q&A and Discussion (10 minutes)

### Key Discussion Points

1. **Scalability**: How does this pattern scale to 50+ environments?
2. **Team Collaboration**: How does Terragrunt improve team workflows?
3. **State Management**: What are the state isolation benefits?
4. **Migration Path**: How to migrate existing Terraform to Terragrunt?
5. **Cost Control**: Importance of automated destruction pipelines

## Presenter Notes

### Timing Tips

- Keep demos focused on the "why" not just the "how"
- Emphasize the pain points of raw Terraform
- Highlight the automation benefits of Terragrunt
- Show the governance gates in action

### Common Questions

- **Q**: Why not just use Terraform workspaces?
  - **A**: Workspaces share state backend, risk of cross-environment contamination
- **Q**: Is Terragrunt worth the learning curve?
  - **A**: Yes, especially for multi-environment, multi-team setups
- **Q**: Can I use both approaches?
  - **A**: Yes, as shown in KNIGHT, but Terragrunt is recommended for new projects

### Technical Deep Dive Options

If audience wants more detail:

- Show the actual state files in S3
- Demonstrate the lock mechanism in DynamoDB
- Explain the `path_relative_to_include()` function
- Show module reuse patterns

## Conclusion

KNIGHT demonstrates that while raw Terraform works for simple cases, Terragrunt provides essential enterprise-grade features:

- DRY configuration
- Automatic state management
- Better governance
- Safer multi-environment deployments

The destruction pipeline ensures cost control by providing a reliable emergency teardown mechanism.
