cd $HOME/kgua/backend || exit

echo $(pwd)

git pull origin master

docker-compose up --build -d
