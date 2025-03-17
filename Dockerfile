FROM python:3.11.9

COPY app /app/

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install redis==4.6.0 redlock-py redis-om

# # redisgraph was deprecated and causes the issue to install Python packages.
# # Use this instead of above if you want to test redisgraph
# RUN pip install redis redlock-py==1.0.8 redis-om==0.2.1 redisgraph==2.4.4

CMD ["sleep", "infinity"]
