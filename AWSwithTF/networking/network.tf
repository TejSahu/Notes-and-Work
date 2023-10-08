# First creating a VPC and subnets and other network components
resource "aws_vpc" "TFVPC" {
    cidr_block = "10.0.0.0/16"
    tags = {
        Name = "CreatedwithTf"
    }
}

resource "aws_internet_gateway" "TfGateway" {
    vpc_id = aws_vpc.TFVPC.id
    tags = {
        Name = "CreatedwithTf"
    }
}

resource "aws_route_table" "rtpb" {
    vpc_id = aws_vpc.TFVPC.id
    route {
      cidr_block = "0.0.0.0/0"
      gateway_id = aws_internet_gateway.TfGateway.id

    }
  
}

resource "aws_subnet" "TFpublicsubnet" {
    cidr_block = "10.0.0.0/20"
    availability_zone = "ap-south-1b"
    vpc_id = aws_vpc.TFVPC.id
    map_public_ip_on_launch = true
    tags = {
        Name = "CreatedwithTf"
    }
}

resource "aws_route_table_association" "pubrt" {
    subnet_id = aws_subnet.TFpublicsubnet.id
    route_table_id = aws_route_table.rtpb.id
  
}

resource "aws_subnet" "TFprivatesubnet1" {
    cidr_block = "10.0.16.0/20"
    availability_zone = "ap-south-1a"
    vpc_id = aws_vpc.TFVPC.id
    map_public_ip_on_launch = false
    tags = {
        Name = "CreatedwithTf"
    }
}