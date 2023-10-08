terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.60.0"
    }
  }
}


provider "aws" {
  region = "ap-south-1"
  profile = "terraform"
  shared_credentials_files = [ "/home/tej/Documents/AWSwithTF/.aws/credentials" ]
}


/*module "instances" {
  source = "/home/tej/Downloads/AWSwithTF/instances"
}*/

/*module "Dynamo" {
  source = "/home/tej/Downloads/AWSwithTF/Dynamo"
}*/

/*module "networking" {
  source = "/home/tej/Downloads/AWSwithTF/networking"
}*/

module "bucket" {
  source = "/home/tej/Documents/AWSwithTF/bucket"
}
