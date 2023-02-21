
echo variables from Dockerfile ...

echo path:$path
echo branch:$branch
echo script:$script

echo pulling sources ...

cd /deploy && \
    git pull --ff-only

cd /modules && \
    git pull --ff-only

echo creating workdir ...
cd /"$branch"

#echo creating symlinks ...
#ln -s /modules my
echo pwd:$(pwd)
ls -la

echo updating packages ...
pip install -r requirements.txt

echo executing $script in $(python --version) ...

python $script
