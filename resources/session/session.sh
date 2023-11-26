

clear
echo -e "\e[1m"
echo "  🌷🌸🌷🌸    "
echo "    🌸🌷🌸🌷🌸"
echo " Λ🌷🌸🌷🌸🌷  "
echo "( ˘ ᵕ ˘🌷🌸🌷 "
echo "ヽ  つ＼     ／ "
echo "  UU   / 🎀 \ "
echo "𝙀𝙑𝙊 𝙋𝙍𝙊 𝙐𝙎𝙀𝙍𝘽𝙊𝙏"
echo -e "\e[0m"
sec=5
spinner=(⣻ ⢿ ⡿ ⣟ ⣯ ⣷)
while [ $sec -gt 0 ]; do
    echo -ne "\e[33m ${spinner[sec]} Starting dependency installation in $sec seconds...\r"
    sleep 1
    sec=$(($sec - 1))
done
echo -e "\e[1;32mInstalling Dependencies ---------------------------\e[0m\n" # Don't Remove Dashes / Fix it
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/EvoXDpro/EvoXD//main/resources/session/ssgen.py
pip uninstall telethon -y && install telethon
clear
python3 ssgen.py
