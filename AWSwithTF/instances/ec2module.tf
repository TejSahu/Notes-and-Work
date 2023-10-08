resource "aws_instance" "TFEC2" {
    ami = "ami-0376ec8eacdf70aae"
    instance_type = "t2.micro"
    key_name = "DLKey"
  
}