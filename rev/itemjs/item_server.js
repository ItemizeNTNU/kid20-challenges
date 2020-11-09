
var net = require('net');
var rl = require('readline');
const dotenv = require('dotenv')
dotenv.config()
const {spawn} = require('child_process')

let streamServer = net.createServer(function (socket) {
    const i = rl.createInterface(socket, socket);
    const cp = spawn("node",  ["item.js"])
    cp.stdout.on('data', (data) => {
        if (!socket.destroyed) {
            socket.write(data.toString())
        }
    })
    cp.on('error', (err) => {
        console.log(err)
        socket.destroy()
    })
    cp.on("close", () => {
        i.removeAllListeners()
        i.close()
        socket.end()
        socket.destroy()
    })
    
    i.on('line', (line) => {
        cp.stdin.write(line + "\n")
        cp.stdin.end()
    });
});
streamServer.maxConnections = 500;
streamServer.listen(7001, () => {
    console.log('Listening on 7001')
})