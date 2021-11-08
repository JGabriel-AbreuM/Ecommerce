# Ecommerce Django 3.2

Projeto que realiza as operações de CRUD com produtos e as respectivas categorais

Possui REST como API

## Execução

1. criar um ambiente vrtual, e instalar as bibliotecas necessárias (disponíveis em requirements.txt)
      
      pip install -r requirements.txt
      
2. clonar o repositório por meio de um git clone
3. Feito isso rode os comandos:
    
    python manage.py makemigrations
    
    
    python manage.py migrate
    
    
4. Após feita as migrações do seu banco de dados, apensa rode um:

    python manage.py runserver
    
5. E está pronto o sorvetinho! (rs) Agora o site está rodando no servidor, pelo menos localmente
