## Create a Hotspot on Pi
https://www.elektronik-kompendium.de/sites/raspberry-pi/2002171.htm

## How to use scp
https://stackabuse.com/copying-a-directory-with-scp/
```scp -r /path/to/local/source user@ssh.example.com:/path/to/remote/destination``` 
----
## Some requierments
```
sudo apt install vlc
sudo apt install python3-pip
pip3 install python-vlc
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
nvm install node
nvm use node
npm install -g pm2
npm i -g corepack
```
## run the project with npm or yarn

cd musicbox/frontend
```
npm install
npm run build
```
---
##Deploy the frontend
https://desertbot.io/blog/nodejs-git-and-pm2-headless-raspberry-pi-install

```
pm2 start npm --name index.js -- start
pm2 save
pm2 resurrect
pm2 startup
pm2 save
sudo reboot
```



