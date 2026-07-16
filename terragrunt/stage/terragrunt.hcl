# Stage environment — inherits ALL backend/provider config from the root file.
# No copy-pasted backend here: that is the whole point of Terragrunt.
include "root" {
  path = find_in_parent_folders()
}

terraform {
  source = "${get_terragrunt_dir()}/../modules//s3-bucket"
}

inputs = {
  environment = "stage"
}
