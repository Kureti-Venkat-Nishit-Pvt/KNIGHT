# KNIGHT Governance Standards — OPA / Tfsec Evaluation Sheet

> **Scope:** Local pre-commit gates and CI/CD policy alignment for Project KNIGHT.
> **IAM context:** All AWS operations authenticate as **`KNIGHT_mark_1`** via repository secrets.

---

## Governance Stack Overview

| Layer | Tool | Runs where | Purpose |
|-------|------|------------|---------|
| Format | `terraform_fmt` | Local (pre-commit) | Enforce canonical HCL style |
| Correctness | `terraform_validate` | Local (pre-commit) | Catch invalid configuration before push |
| Lint | `terraform_tflint` | Local (pre-commit) | AWS/provider best-practice linting |
| Security | `terraform_tfsec` | Local (pre-commit) | Static IaC security analysis (Tfsec) |
| Policy (future) | **OPA / Conftest** | CI (optional gate) | Rego-based custom org policy |
| Branch guard | GitHub Actions `on.branches` | CI | `K_Test_1` deploy · `AWS_Destroy_KNIGHT_mark_1` destroy only |

---

## Pre-Commit Hook Matrix (`.pre-commit-config.yaml`)

| Hook ID | Provider | Evaluates | Pass criteria | KNIGHT coverage |
|---------|----------|-----------|---------------|-----------------|
| `terraform_fmt` | pre-commit-terraform | All `*.tf`, `*.tfvars` | Zero formatting diffs | `terraform/**`, `terragrunt/modules/**` |
| `terraform_validate` | pre-commit-terraform | Syntax + provider schema | `Success! The configuration is valid.` | stage + prod raw TF |
| `terraform_tflint` | pre-commit-terraform | Lint rules via `.tflint.hcl` | 0 issues | S3 bucket resources |
| `terraform_tfsec` | pre-commit-terraform | CIS-style security rules | 0 critical/high findings | Encryption, public access block |

### Local execution

```bash
pre-commit install          # one-time per clone
pre-commit run --all-files  # full governance sweep before push
```

---

## Tfsec Evaluation Sheet (KNIGHT S3 Resources)

| Rule ID | Severity | Check | KNIGHT implementation | Status |
|---------|----------|-------|----------------------|--------|
| `AWS-S3-001` | HIGH | Block public ACLs | `aws_s3_bucket_public_access_block` — all four flags `true` | ✅ Pass |
| `AWS-S3-002` | HIGH | Enable versioning | `aws_s3_bucket_versioning` — `Enabled` | ✅ Pass |
| `AWS-S3-003` | HIGH | Server-side encryption | `aws_s3_bucket_server_side_encryption_configuration` — `AES256` | ✅ Pass |
| `AWS-S3-014` | MEDIUM | Bucket logging | Not required for demo scope | ⚪ N/A (accepted) |
| `AWS-S3-017` | HIGH | No public bucket policy | Public access block + no public policy resource | ✅ Pass |
| `AWS-IAM-001` | LOW | Wildcard IAM actions | No IAM resources defined in KNIGHT IaC | ⚪ N/A |
| `AWS-DynamoDB-001` | MEDIUM | Point-in-time recovery | Lock tables only — demo acceptable | ⚪ N/A (accepted) |

### Expected Tfsec console output

```
tfsec............................................................................Passed
- 0 potential problems detected
```

### Remediation playbook

| Finding | Action |
|---------|--------|
| Unencrypted bucket | Add `aws_s3_bucket_server_side_encryption_configuration` |
| Public access risk | Add `aws_s3_bucket_public_access_block` with all blocks enabled |
| Missing versioning | Add `aws_s3_bucket_versioning` with `status = "Enabled"` |

---

## OPA / Conftest Policy Evaluation (Reference)

OPA is **not wired into KNIGHT CI yet** — this sheet documents the policies a future `conftest test` gate would enforce.

| Policy ID | Rego intent | KNIGHT compliance | Notes |
|-----------|-------------|-------------------|-------|
| `KNIGHT-001` | Deny unencrypted S3 buckets | ✅ Compliant | SSE enabled in both TF paths |
| `KNIGHT-002` | Deny `0.0.0.0/0` security group ingress | ⚪ N/A | No SG resources in demo |
| `KNIGHT-003` | Require `Project = KNIGHT` tag on managed resources | ✅ Terragrunt backend tags | Raw TF uses bucket-level tags in module |
| `KNIGHT-004` | Deny hardcoded secrets in `.tf` files | ✅ Compliant | Credentials via env / GitHub Secrets only |
| `KNIGHT-005` | Require remote state (no `local` backend) | ✅ Compliant | S3 backends in both approaches |
| `KNIGHT-006` | Deny `apply` on PR events | ✅ Compliant | `if: github.event_name == 'push'` in workflows |
| `KNIGHT-007` | Destroy only on `AWS_Destroy_KNIGHT_mark_1` | ✅ Compliant | `knight-destroy-pipeline.yml` branch lock |

### Sample Conftest invocation (future)

```bash
# Install: https://www.openpolicyagent.org/docs/latest/#running-opa
conftest test terraform/ terragrunt/modules/ -p policies/
```

### Sample Rego policy stub (`policies/s3_encryption.rego`)

```rego
package knight.s3

deny[msg] {
  resource := input.resource_changes[_]
  resource.type == "aws_s3_bucket"
  not bucket_has_encryption(resource)
  msg := sprintf("S3 bucket %s must enable server-side encryption", [resource.address])
}
```

---

## CI/CD Branch Governance

| Workflow | Branch lock | Destructive? | Apply gate |
|----------|-------------|--------------|------------|
| `terraform-pipeline.yml` | `K_Test_1` only | No (apply on push) | PR = plan only |
| `terragrunt-pipeline.yml` | `K_Test_1` only | No (apply on push) | PR = plan only |
| `knight-destroy-pipeline.yml` | `AWS_Destroy_KNIGHT_mark_1` only | **Yes** | Push-only, parallel destroy |

---

## Presenter Talking Points (Governance)

1. **Shift-left:** Pre-commit catches fmt/validate/lint/security issues before code reaches GitHub.
2. **Tfsec:** Demonstrates automated security scanning without a separate commercial tool.
3. **OPA-ready:** KNIGHT is structured so org policies (Rego) can be added without changing Terraform modules.
4. **Branch isolation:** Deploy and destroy paths are physically separated by branch name — no accidental `destroy` on feature work.
5. **Secrets hygiene:** `KNIGHT_mark_1` credentials live in GitHub Secrets / local env — never in `.tf` files (enforced by `KNIGHT-004`).

---

## Audit Checklist (pre-demo)

- [ ] `pre-commit run --all-files` → all hooks Passed
- [ ] Tfsec reports 0 critical/high on S3 resources
- [ ] Workflows trigger only on `K_Test_1` (deploy) and `AWS_Destroy_KNIGHT_mark_1` (destroy)
- [ ] `.internal_guide/` listed in root `.gitignore`
- [ ] No `.tfvars` or `.env` files staged for commit
