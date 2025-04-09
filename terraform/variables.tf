variable "credentials" {
  description = "My Credentials"
  default = "../include/gcp/de-creds.json"
}

variable "project" {
  description = "Project"
  default = "de-project-2025-455709" //Your project id
}

variable "region" {
  description = "Region"
  default = "us-central1"
}

variable "location" {
  description = "Project Location"
  default = "US"
}

variable "bq_dataset_name" {
  description = "DE Project dataset"
  default = "music"
}

variable "gcs_bucket_name" {
  description = "DE Project Bucket Name"
  default = "tase_music_data" // Bucket name
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default = "STANDARD"
}