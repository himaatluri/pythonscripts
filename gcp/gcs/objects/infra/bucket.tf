provider "google" {
  project = "qlys-dev"
}
resource "google_storage_bucket" "test_bucket" {
  name          = "hatluri-target-gcs-bucket"
  location      = "US"
  force_destroy = true
}

output "bucket_name" {
  value = google_storage_bucket.test_bucket.url
}