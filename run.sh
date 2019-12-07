#gnome-terminal -e ./use.sh -t "Custom Bitcoin Console"
gnome-terminal -t "Custom Bitcoin Console" -- python3 bitcoin_console.py
if [ ! -d "bitcoin/src" ]
then
    cd ..
fi

if [ -d "/media/sf_Bitcoin" ]
then
    bitcoin/src/bitcoind -datadir=/media/sf_Bitcoin/ # Virtual machine shared folder
elif [ -d "../blocks" ]
then
    bitcoin/src/bitcoind -datadir=.. # Super computer shared folder
else
    bitcoin/src/bitcoind -datadir=/media/sim/BITCOIN/
fi
