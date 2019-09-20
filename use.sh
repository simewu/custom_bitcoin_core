NC='\e[0m'
CYA='\e[0;36m'

echo " WELCOME TO MY BITCOIN CONSOLE"
echo "\n________________________________________________________________________________
"
read -p " > " cmd
while true; do
	prev=$cmd
	bitcoin/src/bitcoin-cli -datadir=/media/sim/BITCOIN/ "$cmd"
	echo "________________________________________________________________________________
"
	read -p " > " cmd
	if [ -z "$cmd" ]; then
		cmd=$prev
		echo " > $cmd"
	fi
done