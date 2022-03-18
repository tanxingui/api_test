FROM python:3.7.4
RUN echo '这是一个本地构建的nginx镜像' \
    && pip install flask
ADD ./luzhihao.tar /root/
CMD python /root/luzhihao/app.py

