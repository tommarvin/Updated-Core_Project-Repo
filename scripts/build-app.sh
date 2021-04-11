# Removes all images that could be using one of the required ports
docker-compose down --rmi all

# builds the images
docker-compose build

docker-compose push
