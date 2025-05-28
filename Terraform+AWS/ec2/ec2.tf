provider "aws" {
    region = "eu-west-2"
    access_key = "*"
    secret_key = "*"
}

resource "aws_instance" "ec2" {
    ami = "ami-0fc32db49bc3bfbb1"
    instance_type = "t2.micro"
    count = 1

    tags = {
        name = "terraform_ec2"
    }
}

resource "aws_s3_bucket" "c" {
    bucket = "new_bucket"
    acl = "private"
}