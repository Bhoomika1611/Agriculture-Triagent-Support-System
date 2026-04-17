provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "agri_server" {
  ami           = "ami-0c02fb55956c7d316" # Ubuntu AMI (valid in us-east-1)
  instance_type = "m7i-flex.large"

  key_name = "agri-key"

  root_block_device {
    volume_size = 30
    volume_type = "gp3"
  }

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install -y docker.io
              systemctl start docker
              systemctl enable docker
              usermod -aG docker ubuntu
              EOF

  tags = {
    Name = "Agri-Server-Ubuntu"
  }
}