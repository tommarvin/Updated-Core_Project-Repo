scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@project-vm2:/home/jenkins/Project-Folder/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@project-vm2 << EOF
    docker stack deploy --compose-file /home/jenkins/Project-Folder/docker-compose.yaml 1-service
EOF