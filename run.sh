
echo all:$@
echo all2:$*
echo 1:$1:
echo 2:$2:

echo T:$TEST
echo p:$path
echo b:$branch

cd /deploy && \
   git pull

cd /modules && \
   git pull

#RUN cd moviemon && \
#    pip install -r requirements.txt

