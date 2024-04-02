# UrFU_MLOps
Практические работы по предмету "Автоматизация машинного обучения"
## Участники команды
- Гарнышев Дмитрий Александрович, РИМ-130907
- Коренев Иван Александрович, РИМ-130908
- Репьева Марина Владимировна, РИМ-130906
- Юрин Михаил Евгеньевич, РИМ-130907
## Практическая работа № 1 (lab1)
Простейший конвейер для автоматизации работы с моделью машинного обучения. Отдельные этапы конвейера машинного обучения описываются в разных python–скриптах, которые потом соединяются с помощью bash-скрипта.
В данной работе представлено решение задачи прогнозирования средней суточной температуры с помощью линейной регрессии.
### Используемые библиотеки 
- numpy
- pandas
- scikit-learn
- joblib
### Содержание работы
- **data_creation.py** - python-скрипт, который создает различные наборы данных, описывающие изменение средней суточной температуры в течение месяца для разных городов (часть наборов данных сохраняется в папку "*train*", другая часть в папку "*test*")
- **model_preprocessing.py** - python-скрипт, который выполняет предобработку данных с помощью sklearn.preprocessing.StandardScaler
- **model_preparation.py** - python-скрипт, который создает и обучает модель машинного обучения на построенных данных из папки “*train*”
- **model_testing.py** - python-скрипт, проверяющий модель машинного обучения на построенных данных из папки “*test*”
- **pipeline.sh** - bash-скрипт, последовательно запускающий все python-скрипты
### Использование
Для того чтобы запустить данный pipeline необходимо:
1. Клонировать данный репозиторий на ПК или ВМ (с ОС Linux)
2. Сделать файл **pipeline.sh** исполняемым, выполнив в терминале в каталоге с файлами проекта команду
```
chmod a+x pipeline.sh
```
4. Запустить bash-скрипт **pipeline.sh**, выполнив в терминале в каталоге с файлами проекта любую из представленных команд:
```
./pipeline.sh
```
```
sh pipeline.sh
```
```
bash pipeline.sh
```
### Пример результата работы pipeline.sh
![image](https://github.com/Bulrush3/MLOps_18/assets/136446022/560ed242-60ff-4309-8377-b3f918ebd260)

## Практическая работа № 3 (lab3)
В рамках данной практической работы было развернуто web-приложение для классификации настроения текста на английском языке на основе streamlit в контейнере докер.
### Используемые библиотеки 
- streamlit
- transformers[torch]
- torch
### Содержание работы
1. Подготовлен python код web-приложения для классификации настроения текста на английском языке.
     * Ссылка на оригинальный github-репозиторий web-приложения: <https://github.com/themrinch/streamlit>
2. Создан Dockerfile (см. каталог lab3 текущего репозитория)
3. Создан docker образ c помощью выполненной в каталоге с файлами проекта команды `sudo docker build -t streamlit .`
4. Запущен docker контейнер с помощью выполненной в каталоге с файлами проекта команды
```
sudo docker run -p 8501:8501 streamlit
```
и проверена его работа: 
![image](https://github.com/Bulrush3/MLOps_18/assets/136446022/832ef481-09f0-4784-9f63-f72a767e0707)
Пример работы контейнера в терминале:
![image](https://github.com/Bulrush3/MLOps_18/assets/136446022/15f53db6-0f99-409f-8a66-e7d5f37f129a)

Кроме того, представлена реализация docker-compose (см. каталог lab3 текущего репозитория) для web-приложения классификации настроения текста на английском языке.

Также полученный docker образ был размещен в хранилище артефактов dockerhub: <https://hub.docker.com/r/themrinch/mlops-urfu-docker-streamlit/tags>
### Использование
При первом использовании данного проекта необходимо:
1. Клонировать данный репозиторий на ПК или ВМ (с ОС Linux), если работаете с ним впервые; в ином случае проверить репозиторий на наличие обновлений или вовсе пропустить данный этап.
2. Установить docker и docker-compose на ПК или ВМ с ОС Linux. Подробнее ознакомиться с установкой docker и docker-compose можно по следующим ссылкам:
    * [docker](https://docs.docker.com/engine/install/ubuntu/)
    * [docker-compose](https://docs.docker.com/compose/install/linux/)
3. В каталоге с файлами проекта выполнить сборку контейнера с помощью команды `sudo docker compose build`
4. В каталоге с файлами проекта запустить контейнер с помощью команды `sudo docker compose up` или `sudo docker compose up -d`
5. Теперь можно воспользоваться web-приложением для классификации настроения текста на английском языке на основе streamlit с помощью браузера по адресу <http://0.0.0.0:8501>. Для этого достаточно ввести в соответсвущее поле свой текст на английском языке и нажать на кнопку "Отправить" (или нажать на клавиатуре на клавишу "Enter"); будет выведен список возможных настроений текста с их показателями уверенности модели в том, что текст соответствует данному настроению.
7. Для того, чтобы остановить контейнер достаточно воспользоваться командой `sudo docker compose down` в каталоге с файлами проекта.

Пример работы контейнера в терминале:
![image](https://github.com/Bulrush3/MLOps_18/assets/136446022/0b829883-4e7c-431f-ac7d-f5532dc15bbe)

#### Примечание
В данном репозитории настроена автоматическая сборка docker образа при push'e в ветку 'main'.
