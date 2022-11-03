#!/bin/bash

mkdir tempdir
mkdir tempdir/templates
mkdir tempdir/static

cp ipAddInfo.py tempdir/.
cp -r templates/* tempdir/templates/.

echo "FROM python" >> tempdir/Dockerfile
echo "RUN pip install flask" >> tempdir/Dockerfile
echo "RUN pip install ipapi" >> tempdir/Dockerfile
echo "COPY ./templates /home/myapp/templates/" >> tempdir/Dockerfile
echo "COPY ipAddInfo.py /home/myapp/" >> tempdir/Dockerfile
echo "EXPOSE 5050" >> tempdir/Dockerfile
echo "CMD python /home/myapp/ipAddInfo.py" >> tempdir/Dockerfile

cd tempdir
docker build -t ipaddinfo .
docker run -t -d -p 5050:5050 --name ipapirunning ipaddinfo
docker ps -a