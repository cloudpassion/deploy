
echo variables from Dockerfile ...

echo path:$path
echo branch:$branch
echo script:$script

echo update sources ...

cd /deploy && \
   git pull

cd /modules && \
   git pull

cd $path
echo pwd:$(pwd)

echo update packages ...
pip install -r requirements.txt

echo execute python ...
python $script
