# python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:
ML: sklearn, pandas, numpy API: flask Данные: с kaggle - https://www.kaggle.com/shrutikunapuli/coffee-and-code-dataset

Задача: предсказать поспособствует ли кофе решению проблемы / поиску бага в коде (поле fraudulent). Бинарная классификация

Описание датасета

CoffeeCupsPerDay - сколько дней респондент не пил кофе
CoffeeTime - время, когда было выпито кофе
CodingWithoutCoffee - пишете ли вы код, без кофе
CoffeeType - тип кофе
CoffeeSolveBugs - бывает ли, что кофе помогает решить проблему
Gender - пол
Country - страна
AgeRange - возраст

Модель: xgb.XGBRegressor()

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/Bkristy91/ML_kurs.git
$ cd ML_kurs
$ docker build -t ml_kurs/gb_docker_flask_example .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models ml_kurs/gb_docker_flask_example
```

### Переходим на localhost:8181
