# Указывает Docker использовать официальный образ python 3 с dockerhub в качестве базового образа
FROM python:3
# Устанавливает переменную окружения, которая гарантирует, что вывод из python
# будет отправлен прямо в терминал без предварительной буферизации
ENV PYTHONUNBUFFERED 1

# Запускает команду pip install для всех библиотек, перечисленных в requirements.txt
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Устанавливает рабочий каталог контейнера — "app"
RUN mkdir /app
WORKDIR /app
COPY . /app/

# RUN adduser -D rinoreinz
#
# USER rinoreinz