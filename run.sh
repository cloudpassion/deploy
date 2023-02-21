
echo variables from Dockerfile ...

echo path:$path
echo branch:$branch
echo script:$script

echo pulling sources ...

ls /deploy/run.sh

cd /deploy && \
    git co "${branch}" && \
    git pull

cd /modules && \
    git co "${branch}" && \
    git pull

ls /deploy/run.sh
echo going to workdir ...

cd "/$branch"
echo pwd:$(pwd)

echo creating symlinks ...
ln -s /modules my

echo updating packages ...
pip install -r requirements.txt

echo executing $script in $(python --version) ...

python $script
