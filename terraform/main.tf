# Premier test (semaine 2) : un bucket S3 sur LocalStack.
resource "aws_s3_bucket" "artifacts" {
  bucket = "tasks-api-artifacts-${var.environment}"

  tags = {
    Project     = "tasks-api"
    Environment = var.environment
  }
}
