FROM python
RUN pip install flask
RUN pip install ipapi
COPY ./templates /home/myapp/templates/
COPY ipAddInfo.py /home/myapp/
EXPOSE 5050
CMD python /home/myapp/ipAddInfo.py
