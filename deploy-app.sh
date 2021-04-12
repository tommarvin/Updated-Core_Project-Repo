#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml pc@manager:docker-compose.yaml
ssh -i ~/.ssh/id_rsa pc@manager << EOF
    docker stack deploy --compose-file docker-compose.yaml project-stack
EOF