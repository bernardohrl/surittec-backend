### Subindo Localmente a Aplicação

Primeiramente, assegurese que você possui Docker, Docker Compose, e Docker Machine instalados. Então, execute os seguintes comandos:

```
chmod +x /src/entrypoint.sh
docker-compose up --build
```

> Em caso de erro, tente executar o comando do docker-compose com sudo.

Acesse o servidor local no endereço apresentado abaixo:

http://localhost:5000/

<br>

### Configurando o Banco de Dados Local

Agora iremos configurar o Banco de Dados da aplicação, com o container rodando, execute os comandos para criar o banco e populá-lo, respectivamente:

```
docker-compose run base python manage.py recreatedb
docker-compose run base python manage.py seed

```

Para acessá-lo, utilize o comando: 

```
docker-compose exec db psql -U postgres
```


### Testando 

Com o container rodando, execute:

```
sudo docker-compose run base python manage.py test
```