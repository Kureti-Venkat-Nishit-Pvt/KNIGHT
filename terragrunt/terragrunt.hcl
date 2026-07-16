# =============================================================================
# KNIGHT — Root Terragrunt configuration (single source of truth)
# =============================================================================
# Every child environment (stage, prod, ...) inherits this file via an
# `include` block, so the backend and provider are defined exactly ONCE.
#
# Terragrunt AUTO-PROVISIONS the state backend: on the first run it creates the
# S3 bucket (versioned + encrypted) and the DynamoDB lock table if they do not
# already exist — no manual bootstrapping required.
# =============================================================================

remote_state {
  backend = "s3"

  generate = {
    path      = "backend.tf"
    if_exists = "overwrite_terragrunt"
  }

  config = {
    # Globally-unique, account-scoped bucket. `path_relative_to_include()`
    # expands to the child directory (e.g. "stage" / "prod"), so each
    # environment gets a dynamically isolated state key automatically.
    bucket = "knight-tfstate-${get_aws_account_id()}"
    key    = "${path_relative_to_include()}/terraform.tfstate"
    region = "us-east-1"

    encrypt        = true
    dynamodb_table = "knight-terragrunt-locks"

    s3_bucket_tags = {
      Project   = "KNIGHT"
      ManagedBy = "terragrunt"
    }

    dynamodb_table_tags = {
      Project   = "KNIGHT"
      ManagedBy = "terragrunt"
    }
  }
}

# Generate a single AWS provider block for every child module (DRY).
generate "provider" {
  path      = "provider.tf"
  if_exists = "overwrite_terragrunt"
  contents  = <<EOF
provider "aws" {
  region = "us-east-1"
}
EOF
}

# Inputs shared by all environments.
inputs = {
  project    = "knight"
  aws_region = "us-east-1"
}
