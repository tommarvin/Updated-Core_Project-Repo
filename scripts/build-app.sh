# Removes all images that could be using one of the required ports
docker-compose down --rmi all

# builds the images
docker-compose build

# login to docker
docker login

# Pushes the images
docker-compose push