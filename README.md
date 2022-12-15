# MASUO-Ai

This is a test program allow to send robot_commands to grism & real machine.

**robot_commands**

```go
var robotid uint32 = 0
var kickspeedx float32 = 0
var kickspeedz float32 = 0
var veltangent float32 = 0
var velnormal float32 = 0
var velangular float32 = 0
var spinner bool = false
var wheelsspeed bool = false
```

link : https://github.com/RoboCup-SSL/grSim/blob/master/src/proto/grSim_Commands.proto

## Usage

1. modify ip address to `<ip address>:<port_num>` accordingly.
The ip address is depends on your environment.

### example

```go
// to grsim
16 conn, err := net.Dial("udp4", "127.0.0.1:20106")
```

```go
// to real
16 conn, err := net.Dial("udp4", "192.168.0.105:20011")
```
2. modify robots_commands (lines 30 t0 37 )

```go
robotid = 3 //robot id
kickspeedx = 0
kickspeedz = 0
veltangent = 0
velnormal = 0
velangular = 0
spinner = false
wheelsspeed = false
```


