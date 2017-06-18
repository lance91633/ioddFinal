agar-joystick-driver
===
## Environment 
- Ubuntu 16.04LTS (4.4.0-79-generic)
- nodejs v4.2.6
- gcc version 5.4.0

## Quick Start
### agar-io-clone
    cd agar-io-clone
- Install the dependent modules

    `npm install`
- Start the agar server

    `npm start`
### joystick-handler
    cd ../src 
- Compile the joystick-handler.c

    `gcc joystick-handler.c`
- Start our implemented driver 

    `node driver.js`
- If you would like to play the agar, you can open the browser, keying `http://localhost:3000/` in your URL
![](https://i.imgur.com/18Tv95G.png)

## Configuration 
- You can change your `serverport` in the file `agar.io-clone/src/server/server.js` if you wanna change the http listen port

## Installation
- nodejs

`sudo apt-get install nodejs`