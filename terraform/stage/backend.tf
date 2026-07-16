# ANTI-PATTERN (raw Terraform): the backend is hardcoded and copy-pasted into
# every environment directory. The state bucket and lock table must be created
# MANUALLY before `terraform init` will succeed. Compare this with the
# `terragrunt/` folder, where the exact same backend is generated dynamically
# and auto-provisioned from a single root file.
terraform {
  backend "s3" {
    bucket         = "knight-tfstate-stage-manual"
    key            = "stage/s3-bucket/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "knight-tf-locks-stage"
  }
}
