package main

import (
	"masuo/proto/pb_gen"
	pb "masuo/proto/pb_gen"
	"net"
	"time"

	"google.golang.org/protobuf/proto"
)

//192.168.0.105:20011
func main() {
	//conn, err := net.Dial("udp4", "192.168.0.104:20011")
	conn, err := net.Dial("udp4", "192.168.0.105:20011")
	if err != nil {
		panic(err)
	}
	var i int = 0

	var robotid uint32 = 3
	var kickspeedx float32 = 0
	var kickspeedz float32 = 0
	var veltangent float32 = 0
	var velnormal float32 = 0
	var velangular float32 = 0
	var spinner bool = false
	var wheelsspeed bool = false

	for {
		robotid = 3
		kickspeedx = 0
		kickspeedz = 0
		veltangent = 0.5
		velnormal = 0
		velangular = 0
		spinner = false
		wheelsspeed = false

		pe := &pb.GrSim_Robot_Command{
			Id:          &robotid,
			Kickspeedx:  &kickspeedx,
			Kickspeedz:  &kickspeedz,
			Veltangent:  &veltangent,
			Velnormal:   &velnormal,
			Velangular:  &velangular,
			Spinner:     &spinner,
			Wheelsspeed: &wheelsspeed,
		}

		var timestamp float64 = float64(time.Now().UnixNano() / 1e6)
		var isteamyellow bool = false

		command := &pb.GrSim_Commands{
			Timestamp:     &timestamp,
			Isteamyellow:  &isteamyellow,
			RobotCommands: []*pb.GrSim_Robot_Command{pe},
		}
		packet := &pb_gen.GrSim_Packet{
			Commands: command,
		}
		// p := &pb.GrSim_Robot_Command{
		// 	Id: 1.0,
		// }
		marshalpacket, _ := proto.Marshal(packet)
		//println(marshalpacket)

		_, err = conn.Write([]byte(marshalpacket))
		println("send : %v", marshalpacket)
		if err != nil {
			panic(err)
		}
		time.Sleep(3 * time.Millisecond)
		i++
		if i > 300 {
			break
		}
	}

	for {
		robotid = 3
		kickspeedx = 0
		kickspeedz = 0
		veltangent = 0
		velnormal = 0
		velangular = 0
		spinner = false
		wheelsspeed = false

		pe := &pb.GrSim_Robot_Command{
			Id:          &robotid,
			Kickspeedx:  &kickspeedx,
			Kickspeedz:  &kickspeedz,
			Veltangent:  &veltangent,
			Velnormal:   &velnormal,
			Velangular:  &velangular,
			Spinner:     &spinner,
			Wheelsspeed: &wheelsspeed,
		}

		var timestamp float64 = float64(time.Now().UnixNano() / 1e6)
		var isteamyellow bool = false

		command := &pb.GrSim_Commands{
			Timestamp:     &timestamp,
			Isteamyellow:  &isteamyellow,
			RobotCommands: []*pb.GrSim_Robot_Command{pe},
		}
		packet := &pb_gen.GrSim_Packet{
			Commands: command,
		}
		// p := &pb.GrSim_Robot_Command{
		// 	Id: 1.0,
		// }
		marshalpacket, _ := proto.Marshal(packet)
		//println(marshalpacket)

		_, err = conn.Write([]byte(marshalpacket))
		println("send : %v", marshalpacket)
		if err != nil {
			panic(err)
		}
		time.Sleep(3 * time.Millisecond)
	}
}
