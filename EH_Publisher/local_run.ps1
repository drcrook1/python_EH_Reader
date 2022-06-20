docker stop eh_publisher
docker rm eh_publisher

docker build -t eh_publisher .
docker run --name eh_publisher --env-file ./dev.env eh_publisher