FROM ubuntu
RUN apt update && apt dist-upgrade -y
RUN apt install python3 python3-pip -y
RUN pip3 install flask django
RUN mkdir /usr/share/webapp && chown -R 1000:1000 /usr/share/webapp
COPY ./webapp/app.py /usr/share/webapp
COPY ./webapp/webapp_uploads /usr/share/webapp
RUN mkdir /usr/share/webapp_uploaded && chown -R 1000:1000 /usr/share/webapp_uploaded
ARG UID=1000
ARG GID=1000
RUN groupadd -g "${GID}" python && useradd --no-log-init -u "${UID}" -g "${GID}" python
USER python
WORKDIR /usr/share/webapp
CMD python3 app.py && python3 webapp_uploads/manage.py runserver

