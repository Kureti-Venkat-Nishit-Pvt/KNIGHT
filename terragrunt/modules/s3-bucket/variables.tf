variable "project" {
  description = "Project name used as a prefix for resource names."
  type        = string
  default     = "knight"
}

variable "environment" {
  description = "Deployment environment name (e.g. stage, prod)."
  type        = string
}
