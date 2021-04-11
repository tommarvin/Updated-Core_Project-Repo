#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@manager:docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@manager << EOF
    docker stack deploy --compose-file docker-compose.yaml 1-service
EOF