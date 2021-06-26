echo $PROJECT_ROOT
cd "$PROJECT_ROOT" || exit

git pull origin master

docker-compose up --build -d
