# LemonAI Testovoe


## HTTP Endpoint
### Запуск с помощью DOCKER
1. Сначала загрузите проект из Хаба:
```shell
docker pull kubanemil/lemonai_testovoe
```
2. Затем запустите контейнер:
```shell
docker run --name lemon_container -p 0.0.0.0:80:80 kubanemil/lemonai_testovoe
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


### Ручной запуск
1. Установите requirements:
```shell
pip install -r requirements.txt
```
2. Запустите API:
```shell
uvicorn api:app --reload
```



## Класс FuncOptimizer

Принимает массив А в качестве аргумента и высчитывает оптимальные значения для ***a, b, c***.
Пример:
```python
data = [[2, 8], [3, 8], [4, 8], [5, -2], [6, -2], [7, -2]]
opt = FuncOptimizer(data)
opt.a, opt.b, opt.c
```
Используйте метод .plot() для отображения графика:
```python
opt.plot()
```
Тестировка по команде: ```shell pytest tests.py```