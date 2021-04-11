scp -i ~/.ssh/ansible_id_rsa docker-compose.yaml pc@project-vm:/home/pc/Project-Folder/docker-compose.yaml
ssh -i ~/.ssh/absible_id_rsa pc@project-vm << EOF
    docker stack deploy --compose-file /home/pc/Project-Folder/docker-compose.yaml 1-service
EOF