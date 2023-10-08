resource "aws_s3_bucket" "statebucket" {
    bucket = "tostoretfstate"
    force_destroy = true
    
    /*depends_on = [ 
      var.dynamodbname
    ]*/
}

/*resource "aws_s3_bucket_acl" "s3acl" {
  bucket = aws_s3_bucket.statebucket.id
  acl = "private"
  
}
resource "aws_s3_bucket_policy" "bucketpolicy" {
    bucket = aws_s3_bucket.statebucket.id 
    policy = <<EOF
    {
    "Id": "Policy1679672135543",
    "Version": "2012-10-17",
    "Statement": [
    {
      "Sid": "Stmt1679672016226",
      "Action": [
        "s3:ListBucket"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::tostoretfstate",
      "Principal": {
        "AWS": [
          "arn:aws:iam::091075798211:user/TejSahu"
        ]
      }
    },
    {
      "Sid": "Stmt1679672077306",
      "Action": [
        "s3:DeleteObject",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::tostoretfstate/terraformstatefolder/",
      "Principal": {
        "AWS": [
          "arn:aws:iam::091075798211:user/TejSahu"
        ]
      }
    }
    ]
    }
  EOF
}*/