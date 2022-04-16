That start this project you need install some library. Open terminal and enter next:
 
 - sudo apt-get install docker-ce docker-ce-cli containerd.io

When you download application in your computer - need rename file 'env.example' to '.env':
    
- in terminal /Test_Incora  enter 'mv env.example .env'

Connect to local database:
1. You need create local postgresql database with name 'db_incora'
2. In .env-file change params: DATABASE.USER, DATABASE.PASSWORD

Run backend:

1. In /Test_Incora enter : sudo docker-compose up --build

2. You get error 'ValueError: Dependency on app with no migrations: user'
3. In new terminal window enter: sudo docker-compose exec web bash
4. Enter: cd Test_Incora.
5. Enter: python3 manage.py makemigrations
6. Enter: python3 manage.py migrate
7. Close this terminal and restart docker-compose: sudo docker-compose up --build
