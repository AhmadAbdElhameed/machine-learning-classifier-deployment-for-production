FROM continuumio/anaconda3

COPY . /usr/local/python

EXPOSE 5000

WORKDIR /usr/local/python

RUN pip install -r requirments.txt

CMD ["python","predict_flask.py"]


