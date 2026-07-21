#!/bin/bash
set -e

# =============================================================================
# KNIGHT - Automated Terraform Backend Bootstrapping Script
# =============================================================================
# This script idempotently creates the required S3 buckets and DynamoDB tables
# for the Terraform pipeline's remote state backend. It checks if resources
# exist before attempting creation and handles regional constraints.
# =============================================================================

# Configuration
REGION="${AWS_DEFAULT_REGION:-us-east-1}"
STAGE_BUCKET="knight-tfstate-stage-manual"
PROD_BUCKET="knight-tfstate-prod-manual"
STAGE_TABLE="knight-tf-locks-stage"
PROD_TABLE="knight-tf-locks-prod"

echo "=========================================="
echo "KNIGHT Terraform Backend Bootstrapping"
echo "=========================================="
echo "Region: ${REGION}"
echo ""

# Function to create S3 bucket with proper regional handling
create_s3_bucket() {
    local bucket_name=$1
    local region=$2
    
    echo "Checking S3 bucket: ${bucket_name}"
    
    # Check if bucket exists
    if aws s3api head-bucket --bucket "${bucket_name}" --region "${region}" 2>/dev/null; then
        echo "✓ Bucket ${bucket_name} already exists"
        
        # Ensure versioning is enabled
        aws s3api put-bucket-versioning \
            --bucket "${bucket_name}" \
            --versioning-configuration Status=Enabled \
            --region "${region}" 2>/dev/null || true
        
        # Ensure encryption is enabled
        aws s3api put-bucket-encryption \
            --bucket "${bucket_name}" \
            --server-side-encryption-configuration '{
                "Rules": [{
                    "ApplyServerSideEncryptionByDefault": {
                        "SSEAlgorithm": "AES256"
                    }
                }]
            }' \
            --region "${region}" 2>/dev/null || true
        
        echo "✓ Verified versioning and encryption for ${bucket_name}"
    else
        echo "→ Creating bucket ${bucket_name}"
        
        if [ "${region}" = "us-east-1" ]; then
            # us-east-1 doesn't require LocationConstraint
            aws s3api create-bucket \
                --bucket "${bucket_name}" \
                --region "${region}"
        else
            # Other regions require LocationConstraint
            aws s3api create-bucket \
                --bucket "${bucket_name}" \
                --region "${region}" \
                --create-bucket-configuration LocationConstraint="${region}"
        fi
        
        # Enable versioning
        aws s3api put-bucket-versioning \
            --bucket "${bucket_name}" \
            --versioning-configuration Status=Enabled \
            --region "${region}"
        
        # Enable default encryption
        aws s3api put-bucket-encryption \
            --bucket "${bucket_name}" \
            --server-side-encryption-configuration '{
                "Rules": [{
                    "ApplyServerSideEncryptionByDefault": {
                        "SSEAlgorithm": "AES256"
                    }
                }]
            }' \
            --region "${region}"
        
        # Block public access
        aws s3api put-public-access-block \
            --bucket "${bucket_name}" \
            --public-access-block-configuration '{
                "BlockPublicAcls": true,
                "IgnorePublicAcls": true,
                "BlockPublicPolicy": true,
                "RestrictPublicBuckets": true
            }' \
            --region "${region}"
        
        echo "✓ Created and configured ${bucket_name}"
    fi
    echo ""
}

# Function to create DynamoDB table for state locking
create_dynamodb_table() {
    local table_name=$1
    local region=$2
    
    echo "Checking DynamoDB table: ${table_name}"
    
    # Check if table exists
    if aws dynamodb describe-table \
        --table-name "${table_name}" \
        --region "${region}" 2>/dev/null; then
        echo "✓ Table ${table_name} already exists"
    else
        echo "→ Creating table ${table_name}"
        
        aws dynamodb create-table \
            --table-name "${table_name}" \
            --region "${region}" \
            --attribute-definitions AttributeName=LockID,AttributeType=S \
            --key-schema AttributeName=LockID,KeyType=HASH \
            --billing-mode PAY_PER_REQUEST \
            --tags Key=Project,Value=KNIGHT Key=ManagedBy,Value=terraform-pipeline
        
        echo "✓ Created ${table_name}"
    fi
    echo ""
}

# Create stage environment resources
echo "--- Stage Environment ---"
create_s3_bucket "${STAGE_BUCKET}" "${REGION}"
create_dynamodb_table "${STAGE_TABLE}" "${REGION}"

# Create prod environment resources
echo "--- Production Environment ---"
create_s3_bucket "${PROD_BUCKET}" "${REGION}"
create_dynamodb_table "${PROD_TABLE}" "${REGION}"

echo "=========================================="
echo "✓ Bootstrapping completed successfully!"
echo "=========================================="
echo "Created/Verified resources:"
echo "  - S3: ${STAGE_BUCKET}"
echo "  - S3: ${PROD_BUCKET}"
echo "  - DynamoDB: ${STAGE_TABLE}"
echo "  - DynamoDB: ${PROD_TABLE}"
echo "=========================================="
