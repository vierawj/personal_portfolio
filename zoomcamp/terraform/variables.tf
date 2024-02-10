variable "credencials" {
  description = "My Credencial GCP"
  default     = "./keys/my-creds.json"
}
variable "Project" {
  description = "Project"
  default     = "first-project-411317"
}

variable "Region" {
  description = "region"
  default     = "us-central1"
}

variable "Location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My_BigQuery Dataset Name"
  default     = "demo_dataset"
}


variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "first-project-411317-terra-bucket"
}