Launch gunicorn web server by below command
```bash
gunicorn --bind=0.0.0.0:9696 predict:app
```

Create Docker file
```bash
docker build -t text-converter-service:v1 .
```

Launch Docker image
```bash
docker run -it --rm -p 9696:9696  text-converter-service:v1
```

Now you can test your web service
```bash
python3 test.py
```

It will give you some prediction.
`{'prediction': [1.32, 0.393, 0.9312]}`