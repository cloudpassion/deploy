
echo variables from Dockerfile ...

echo path:$path
echo branch:$branch
echo script:$script

echo pulling sources ...

cd /deploy && \
   git pull

cd /modules && \
   git pull

echo going to workdir ...

cd "/$branch"
echo pwd:$(pwd)

echo updating packages ...
pip install -r requirements.txt

echo executing $script in $(python --version) ...

python $script
