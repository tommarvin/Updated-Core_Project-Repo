#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml pc@project-vm2:./docker-compose.yaml
ssh -i ~/.ssh/id_rsa pc@project-vm2 <<EOF
    docker stack deploy --compose-file /home/pc/Project-Folder/docker-compose.yaml 1-service
EOF