#gnome-terminal -e ./use.sh -t "Custom Bitcoin Console"
gnome-terminal -t "Custom Bitcoin Console" -- python3 bitcoin_console.py

bitcoin/src/bitcoind -datadir=/media/sim/BITCOIN/