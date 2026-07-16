output "bucket_id" {
  description = "Name (ID) of the S3 storage bucket."
  value       = aws_s3_bucket.app_storage.id
}

output "bucket_arn" {
  description = "ARN of the S3 storage bucket."
  value       = aws_s3_bucket.app_storage.arn
}
