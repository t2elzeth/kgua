cd "$HOME"/kgua/backend || exit

git pull origin master

docker-compose up --build -d
