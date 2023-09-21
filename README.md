# LemonAI Testovoe


# HTTP Endpoint
### Запуск с помощью DOCKER
1. Сначала загрузите проект из Хаба:
```shell
docker pull kubanemil/lemonAI_testovoe
```
2. Затем запустите контейнер:
```shell
docker run --name lemon_container -p 0.0.0.0:80:80 lemonAI_testovoe
```
3. Документация API в: http://127.0.0.1/


### Docker локально:
1. Отклонируйте репу:
```shell
git clone https://github.com/kubanemil/lemonAI_testovoe
cd lemonAI_testovoe
```
2. Создайте docker image:
```shell
docker build -t lemonai .
```
3. Запустите контейнер:
```shell
docker run --name lemon_container -dp 0.0.0.0:80:80 lemonai
```
4. Документация API в: http://127.0.0.1/


### Ручной запуск
1. Отклонируйте репу:
```shell
git clone https://github.com/kubanemil/lemonAI_testovoe
cd lemonAI_testovoe
```
2. Создайте и активруйте venv:
```shell
python3 -m venv venv
source venv/bin/activate
```
3. Установите requirements:
```shell
pip install -r requirements.txt
```
4. Запустите API:
```shell
uvicorn api:app --reload
```
6. Документация API в: http://127.0.0.1/