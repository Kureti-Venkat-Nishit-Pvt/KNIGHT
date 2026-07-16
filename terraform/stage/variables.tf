variable "aws_region" {
  description = "AWS region to deploy resources into."
  type        = string
  default     = "us-east-1"
}

variable "project" {
  description = "Project name used as a prefix for resource names."
  type        = string
  default     = "knight"
}

variable "environment" {
  description = "Deployment environment name (e.g. stage, prod)."
  type        = string
  default     = "stage"
}
