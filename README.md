# KNIGHT

> **K**olappan · **N**ishit · **I**nfrastructure · **G**itHub · **H**ybrid · **T**erraform

---

## Checkov Security Demo

This repository demonstrates the difference between a standard Terraform CI pipeline and a security-focused pipeline that uses [Checkov](https://www.checkov.io/) to scan infrastructure-as-code for misconfigurations.

> **No AWS account required.** Checkov analyzes code statically inside the GitHub runner — nothing is deployed to the cloud.

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       ├── checkov-scan.yml      # Security pipeline with Checkov scanning
│       └── standard-deploy.yml   # Standard pipeline (fmt + validate only)
├── main.tf                       # Intentionally insecure Terraform resources
├── providers.tf                  # AWS provider and Terraform version constraints
├── README.md                     # Project overview and secured code reference
└── STEPS.md                      # Step-by-step demo guide (presenter's cheat sheet)
```

| File | Purpose |
|------|---------|
| `providers.tf` | Configures the AWS provider (`us-east-1`) and pins Terraform/AWS provider versions |
| `main.tf` | Defines EC2, Security Group, and S3 resources with deliberate security flaws |
| `.github/workflows/standard-deploy.yml` | Runs `terraform fmt`, `init`, and `validate` — no security scanning |
| `.github/workflows/checkov-scan.yml` | Runs the same Terraform init, then scans all `.tf` files with Checkov |

## Why the Standard Workflow Passes but Checkov Fails

Both workflows start from the same Terraform code, but they validate different things:

| Workflow | What it checks | Result |
|----------|----------------|--------|
| **Standard Pipeline** | Syntax (`fmt`), provider init, and schema validation (`validate`) | **Passes** — the Terraform is syntactically correct and valid |
| **Security Pipeline (Checkov)** | Security and compliance policies against AWS best practices | **Fails** — Checkov detects intentional misconfigurations |

`terraform validate` only confirms that your configuration is well-formed and internally consistent. It does **not** evaluate whether your resources follow security best practices. Checkov fills that gap by applying hundreds of policy checks (CIS benchmarks, SOC2, etc.) to your IaC.

## Three Security Vulnerabilities in `main.tf`

### 1. Unencrypted EC2 Root Volume

```hcl
root_block_device {
  encrypted = false   # CKV_AWS_79
}
```

The root EBS volume is not encrypted at rest. Any data stored on the instance disk is readable if the volume is detached or compromised.

### 2. SSH Open to the Internet (0.0.0.0/0)

```hcl
ingress {
  from_port   = 22
  to_port     = 22
  protocol    = "tcp"
  cidr_blocks = ["0.0.0.0/0"]   # CKV_AWS_24
}
```

Port 22 is exposed to the entire internet, making the instance a target for brute-force SSH attacks.

### 3. S3 Bucket Without Server-Side Encryption

```hcl
resource "aws_s3_bucket" "insecure_bucket" {
  bucket        = "insecure-bucket-demo"
  force_destroy = true
  # No encryption configured — CKV_AWS_19
}
```

Objects stored in the bucket are not encrypted at rest, violating data protection requirements.

## Getting Started — Push to GitHub

Follow these steps to initialize the repo and trigger the GitHub Actions workflows:

```bash
# 1. Initialize a local git repository
git init

# 2. Stage all files
git add .

# 3. Create the initial commit
git commit -m "Add Checkov security demo with intentionally insecure Terraform"

# 4. Create a new repository on GitHub (via the web UI or gh CLI), then link it:
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPO>.git

# 5. Rename the default branch to main and push
git branch -M main
git push -u origin main
```

After pushing, open the **Actions** tab on GitHub. You will see:

- **Standard Pipeline (No Security Scan)** — green checkmark
- **Security Pipeline (With Checkov)** — red X with detailed findings

## Secured `main.tf`

Replace the contents of `main.tf` with the following to remediate all three vulnerabilities:

```hcl
resource "aws_instance" "demo_web_server" {
  ami                         = "ami-0c7217cdde317cfec"
  instance_type               = "t3.micro"
  associate_public_ip_address = true

  root_block_device {
    encrypted = true
  }
}

resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  ingress {
    description = "SSH from private network only"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["10.0.0.0/8"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "insecure_bucket" {
  bucket        = "insecure-bucket-demo"
  force_destroy = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "insecure_bucket" {
  bucket = aws_s3_bucket.insecure_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
```

After applying these fixes, re-push to `main`. The Checkov workflow should pass.
