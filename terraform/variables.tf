variable "localstack_endpoint" {
  description = "URL de LocalStack"
  type        = string
  default     = "http://localhost:4566"
}

variable "environment" {
  description = "Environnement (dev ou prod)"
  type        = string
  default     = "dev"
}
