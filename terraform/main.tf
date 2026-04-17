provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "agri_server" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.micro"

  key_name = "agri-key"

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install docker.io -y
              systemctl start docker
              systemctl enable docker
              usermod -aG docker ubuntu
              EOF

  tags = {
    Name = "Agri-Server"
  }
}