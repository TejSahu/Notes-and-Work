/*
terraform {
  backend "s3" {
    encrypt = true
    bucket = "tostoretfstate"
    key = "terraformstatefolder"
    dynamodb_table = "terraform-state-lock-dynamo"
    region = "ap-south-1"
  }
}*/