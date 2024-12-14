const Gpio = require('onoff').Gpio;
const led = new Gpio(529, 'out');
const blink = () => {
    led.writeSync(led.readSync() ^ 1); // Toggle LED
};

const interval = setInterval(blink, 1000);

process.on('SIGINT', () => {
    clearInterval(interval);
    led.writeSync(0);
    led.unexport();
});
