# /usr/bin/g++ -g src/*.cpp -I include -o main

#cleanup old file
sudo rm -r build
sudo rm -r cppGood.egg-info
sudo rm -r dist

echo compiling

# python3 setup.py build
sudo python3 setup.py install

echo "\n"
# echo "\n\nPROGRAM\n"

python3 python/main.py