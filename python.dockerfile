FROM python:3.7-alpine
WORKDIR /code
RUN pip install flask
EXPOSE 8000
ENTRYPOINT ["tail", "-f", "/dev/null"]
# ENTRYPOINT [ "python" ] 
# CMD [ "app.py" ]