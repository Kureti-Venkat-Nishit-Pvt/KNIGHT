resource "aws_instance" "demo_web_server" {
  ami                         = "ami-0c7217cdde317cfec"
  instance_type               = "t3.micro"
  associate_public_ip_address = true

  root_block_device {
    encrypted = false
  }
}

resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"

  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_s3_bucket" "insecure_bucket" {
  bucket        = "insecure-bucket-demo"
  force_destroy = true
}
