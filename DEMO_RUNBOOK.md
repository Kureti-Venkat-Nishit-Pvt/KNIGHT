# KNIGHT Live Demo Run-Book

## 🎯 Presentation Overview
**Target Audience**: Kolappan and Manager  
**Demo Duration**: ~15-20 minutes  
**Goal**: Demonstrate why teams adopt Terragrunt over raw Terraform for enterprise infrastructure

---

## 🚨 PRE-DEMO CHECKLIST

### Technical Prerequisites
- [ ] GitHub repository secrets configured (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
- [ ] Local CLI tools installed: Terraform, Terragrunt, pre-commit, tflint, tfsec
- [ ] AWS IAM user `KNIGHT_mark_1` has required permissions
- [ ] Current branch: `K_Test_1`
- [ ] No existing AWS resources (clean slate for demo)

### Demo Environment Setup
```bash
# Verify current branch
git branch
# Should show: * K_Test_1

# Verify clean working directory
git status
# Should show: working tree clean

# Verify GitHub Actions status
# Open: https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT/actions
```

---

## 📋 STEP 1: Pre-Commit Check (Local Governance)

### Commands to Run
```bash
# Navigate to project root
cd C:\Users\Kureti Venkat Nishit\CascadeProjects\KNIGHT

# Run all pre-commit hooks
pre-commit run --all-files
```

### Expected Output
```
terraform fmt....................................................................Passed
terraform validate.................................................................Passed
tflint...........................................................................Passed
tfsec............................................................................Passed
```

### 🗣️ Key Talking Points
> "Before any code leaves my machine, it goes through automated governance gates. These pre-commit hooks catch formatting errors, syntax issues, linting problems, and security vulnerabilities before they ever reach the repository."

> "This is our first line of defense - ensuring code quality and security at the developer's desktop, not in production."

### What to Show
- Terminal output showing all hooks passing
- The `.pre-commit-config.yaml` file to explain what each hook does
- Explain how this prevents bad code from entering the pipeline

---

## 📋 STEP 2: The Terraform Anti-Pattern (The Failed Pipeline)

### Commands to Run
```bash
# Show the hardcoded backend configuration
cat terraform/stage/backend.tf
cat terraform/prod/backend.tf
```

### What to Show
- Open GitHub Actions tab: https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT/actions
- Show recent failed pipeline runs (if any exist)
- Display the `.github/workflows/terraform-pipeline.yml` file
- Show the duplicated backend configurations in `terraform/stage/backend.tf` and `terraform/prod/backend.tf`

### 🗣️ Key Talking Points
> "This is the anti-pattern we're demonstrating. Look at how the backend configuration is hardcoded and copy-pasted into every environment directory. The `stage` and `prod` directories have identical backend blocks with different bucket names."

> "This approach has three major problems: First, it's repetitive and error-prone. Second, we had to manually create these S3 buckets and DynamoDB tables before the pipeline could run. Third, when state locks get corrupted - like that checksum mismatch we saw earlier - we have to manually intervene in DynamoDB."

> "Raw Terraform forces us to manage infrastructure manually, which defeats the purpose of Infrastructure as Code."

### Anti-Pattern Issues to Highlight
- **Duplicated Code**: Same backend block in multiple directories
- **Manual Setup**: Requires AWS Console intervention before pipeline runs
- **Brittle State Locks**: Checksum mismatches require manual DynamoDB cleanup
- **Configuration Drift**: Easy for environments to diverge accidentally
- **No Recovery**: State lock errors break the entire pipeline

---

## 📋 STEP 3: The Terragrunt Solution (DRY & Automated Engine)

### Commands to Run
```bash
# Show the Terragrunt root configuration
cat terragrunt/terragrunt.hcl

# Show environment-specific configurations
cat terragrunt/stage/terragrunt.hcl
cat terragrunt/prod/terragrunt.hcl

# Run Terragrunt plan (auto-provisions backend on first run)
cd terragrunt
terragrunt run-all plan
```

### Expected Output
```
[terragrunt] [/terragrunt/stage] Running command: terraform plan
[terragrunt] [/terragrunt/prod] Running command: terraform plan

[terragrunt] [/terragrunt/stage] 
Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Plan: 4 to add, 0 to change, 0 to destroy.

[terragrunt] [/terragrunt/prod]
Plan: 4 to add, 0 to change, 0 to destroy.
```

### 🗣️ Key Talking Points
> "Now let me show you the solution. Instead of hardcoding backends in every directory, Terragrunt uses a single root configuration file that all environments inherit."

> "Look at this `path_relative_to_include()` function - it automatically generates unique state keys for each environment. `stage` gets `stage/terraform.tfstate` and `prod` gets `prod/terraform.tfstate` - no manual configuration needed."

> "When we run `terragrunt run-all plan`, it automatically creates the S3 bucket and DynamoDB table for state management. Zero manual AWS Console interaction required."

### Terragrunt Advantages to Highlight
- **Single Source of Truth**: One `terragrunt.hcl` defines backend for all environments
- **Auto-Provisioning**: Creates state backend resources automatically on first run
- **Dynamic State Keys**: `path_relative_to_include()` generates isolated state paths
- **DRY Configuration**: No code duplication between environments
- **Built-in Recovery**: More robust state lock handling

### What to Show
- The single `terragrunt.hcl` file vs multiple Terraform backend files
- The `include` blocks in environment-specific files
- Terminal output showing automatic backend creation
- Module reuse in `terragrunt/modules/s3-bucket/`

---

## 📋 STEP 4: Live GitHub Actions Deployment

### Commands to Run
```bash
# Make a small change to trigger the pipeline
# (Optional: Add a comment or make a minor configuration change)
echo "# Demo change" >> README.md

# Commit and push to trigger pipelines
git add README.md
git commit -m "Demo: trigger live deployment"
git push origin K_Test_1
```

### What to Show
- Open GitHub Actions tab: https://github.com/Kureti-Venkat-Nishit-Pvt/KNIGHT/actions
- Show both pipelines running in parallel:
  - `terraform-pipeline.yml` (with bootstrap job)
  - `terragrunt-pipeline.yml`
- Watch the jobs turn green in real-time
- Open AWS Console to show newly created S3 buckets:
  - `knight-tfstate-stage-manual`
  - `knight-tfstate-prod-manual`
  - `knight-tfstate-{account-id}` (Terragrunt)

### 🗣️ Key Talking Points
> "Now I'm pushing a small change to trigger both pipelines. Watch how they run in parallel in GitHub Actions."

> "The Terraform pipeline now has a bootstrap job that automatically creates the required S3 buckets and DynamoDB tables - this was the manual step we had to do before."

> "The Terragrunt pipeline doesn't need a bootstrap job because it auto-provisions everything on the first run. See how both pipelines are turning green?"

> "Let's switch to the AWS Console to see the actual resources that were created. Notice how Terragrunt created a single bucket for all environments, while Terraform required separate buckets for each environment."

### Pipeline Comparison Points
- **Terraform Pipeline**: Bootstrap job + explicit environment handling
- **Terragrunt Pipeline**: Single `run-all` command handles all environments
- **Resource Creation**: Both create S3 buckets, but Terragrunt does it dynamically
- **State Management**: Terragrunt uses account-scoped bucket, Terraform uses environment-specific buckets

---

## 📋 STEP 5: Automated Destruction Kill-Switch

### Commands to Run
```bash
# Switch to destruction branch
git checkout AWS_Destroy_KNIGHT_mark_1

# Push to trigger destruction pipeline
git push origin AWS_Destroy_KNIGHT_mark_1

# Switch back to development branch
git checkout K_Test_1
```

### What to Show
- Open GitHub Actions tab to show `knight-destroy-pipeline.yml` running
- Show the destruction pipeline configuration
- Watch resources being torn down in real-time
- Verify in AWS Console that S3 buckets are being deleted
- Show final clean state (zero resources)

### 🗣️ Key Talking Points
> "For cost control and safety, we have an automated destruction pipeline. This is our emergency kill-switch that removes all AWS resources when we're done."

> "The destruction pipeline only triggers on the `AWS_Destroy_KNIGHT_mark_1` branch - so it can't run accidentally during normal development."

> "Watch how it tears down both the Terraform and Terragrunt resources in parallel. This ensures we never leave expensive infrastructure running after the demo."

> "This is critical for cost optimization in development environments - we can spin up infrastructure for testing and tear it down immediately when done."

### Safety Features to Highlight
- **Branch-Gated**: Only triggers on specific branch
- **Explicit Action**: Requires intentional branch switch and push
- **Complete Cleanup**: Removes all S3 buckets and DynamoDB tables
- **Cost Control**: Prevents ongoing AWS charges

---

## 🎯 CONCLUSION & Q&A

### Summary Points
1. **Raw Terraform Anti-Pattern**: Hardcoded backends, manual setup, brittle state locks
2. **Terragrunt Solution**: DRY configuration, auto-provisioning, robust state management
3. **Governance**: Pre-commit hooks ensure code quality before deployment
4. **Automation**: Pipelines handle everything from zero to production
5. **Cost Control**: Destruction pipeline prevents ongoing charges

### 🗣️ Closing Statement
> "KNIGHT demonstrates that while raw Terraform works for simple cases, Terragrunt provides essential enterprise-grade features: DRY configuration, automatic state management, better governance, and safer multi-environment deployments."

> "The choice between them isn't just about syntax - it's about operational excellence, team productivity, and reducing the risk of manual errors in production infrastructure."

### Common Questions & Answers

**Q: Why not just use Terraform workspaces?**
> "Workspaces share the same state backend, which creates risk of cross-environment contamination. If you accidentally apply prod changes to the workspace state, you can break production. Terragrunt gives us complete state isolation."

**Q: Is Terragrunt worth the learning curve?**
> "Absolutely. For a single environment, maybe not. But for multi-environment, multi-team setups, the time saved on manual state management and the reduction in configuration errors pays for itself quickly."

**Q: Can we migrate existing Terraform to Terragrunt?**
> "Yes, migration is straightforward. We extract modules, create the root Terragrunt configuration, and use `terraform state mv` to migrate existing state. The bootstrapping script I created can help with the transition."

**Q: What about the destruction pipeline - is that safe?**
> "Very safe. It only triggers on a specific branch that we don't use for normal development. We'd have to intentionally switch to that branch and push to trigger it. It's designed as a cost-control measure, not something that would run accidentally."

---

## 🔧 TROUBLESHOOTING GUIDE

### If Pre-Commit Hooks Fail
```bash
# Install hooks if not already installed
pre-commit install

# Run hooks manually to see detailed errors
pre-commit run --all-files --verbose
```

### If Terraform Pipeline Fails
```bash
# Check bootstrap job logs in GitHub Actions
# Verify AWS credentials are configured correctly
# Ensure S3 buckets and DynamoDB tables exist

# Manual state lock resolution (if needed)
cd terraform/prod
terraform force-unlock <LOCK_ID>
```

### If Terragrunt Pipeline Fails
```bash
# Check AWS credentials
# Verify IAM user permissions
# Check for existing state conflicts

# Clean local cache
rm -rf .terragrunt-cache
terragrunt run-all plan
```

### If Destruction Pipeline Fails
```bash
# Manual cleanup via AWS CLI
aws s3 ls
aws s3 rb s3://bucket-name --force

aws dynamodb list-tables
aws dynamodb delete-table --table-name table-name
```

---

## 📊 DEMO SUCCESS METRICS

### Technical Success Criteria
- [ ] Pre-commit hooks pass without errors
- [ ] Terraform pipeline completes successfully
- [ ] Terragrunt pipeline completes successfully
- [ ] S3 buckets created in AWS Console
- [ ] DynamoDB tables visible in AWS Console
- [ ] Destruction pipeline removes all resources
- [ ] Final state: zero AWS resources

### Presentation Success Criteria
- [ ] Clear explanation of anti-pattern vs solution
- [ ] Live demonstration of automated provisioning
- [ ] Visible comparison between Terraform and Terragrunt
- [ ] Effective cost control demonstration
- [ ] Audience engagement and questions answered

---

## 🎁 BONUS: Quick Reference Card

### Terraform Commands
```bash
terraform init -input=false          # Initialize backend
terraform plan -input=false           # Generate execution plan
terraform apply -auto-approve         # Apply changes
terraform destroy -auto-approve       # Destroy resources
terraform force-unlock <LOCK_ID>      # Release state lock
```

### Terragrunt Commands
```bash
terragrunt run-all plan              # Plan all modules
terragrunt run-all apply             # Apply all modules
terragrunt run-all destroy           # Destroy all modules
terragrunt hclfmt                    # Format all HCL files
```

### AWS Commands
```bash
aws s3 ls                            # List S3 buckets
aws dynamodb list-tables             # List DynamoDB tables
aws s3 rb s3://bucket-name --force   # Delete bucket with contents
```

---

**End of Demo Run-Book**
