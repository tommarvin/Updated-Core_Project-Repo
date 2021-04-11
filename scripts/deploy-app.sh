#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@project-vm2:./docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@project-vm2 <<EOF
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml Updated-Core_Project-Repo
EOF