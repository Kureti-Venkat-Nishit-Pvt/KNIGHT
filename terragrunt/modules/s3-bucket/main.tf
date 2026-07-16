# Reusable S3 storage module shared by every environment.
# NOTE: this module intentionally declares NO `provider` and NO `backend`
# block — Terragrunt generates both from the root terragrunt.hcl.

# tfsec:ignore:aws-s3-enable-bucket-logging Access logging omitted: demo bucket, no log target provisioned.
resource "aws_s3_bucket" "app_storage" {
  bucket = "${var.project}-${var.environment}-storage"

  tags = {
    Project     = var.project
    Environment = var.environment
    ManagedBy   = "terragrunt"
  }
}

resource "aws_s3_bucket_versioning" "app_storage" {
  bucket = aws_s3_bucket.app_storage.id

  versioning_configuration {
    status = "Enabled"
  }
}

# tfsec:ignore:aws-s3-encryption-customer-key AES256 (SSE-S3) is sufficient for this demo; no CMK required.
resource "aws_s3_bucket_server_side_encryption_configuration" "app_storage" {
  bucket = aws_s3_bucket.app_storage.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "app_storage" {
  bucket = aws_s3_bucket.app_storage.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
