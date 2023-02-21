
echo variables from Dockerfile ...

echo path:$path
echo branch:$branch
echo script:$script

echo pulling sources ...

cd /deploy && \
    git pull

cd /modules && \
    git pull

echo creating workdir ...
ls -la
ls -la "${branch}"

ln -s "${path}" /"${branch}"
cd "/$branch"
echo pwd:$(pwd)

echo creating symlinks ...
ln -s /modules my

echo updating packages ...
pip install -r requirements.txt

echo executing $script in $(python --version) ...

python $script
