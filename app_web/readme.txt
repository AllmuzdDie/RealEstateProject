Для создания образа сервера с моделью используйте команду
docker build -t my_flask_app .

для создания контейнера и проброски портов на локалхост
docker run -d -p 5000:5000 --name flask_app my_flask_app