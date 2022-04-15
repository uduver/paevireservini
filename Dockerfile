FROM python:3.10
EXPOSE 8080

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run the app
CMD [ "/bin/bash", "start.sh" ]
