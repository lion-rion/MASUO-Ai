package main

import (
	"masuo/proto/pb_gen"
	pb "masuo/proto/pb_gen"
	"net"
	"time"

	"google.golang.org/protobuf/proto"
)

func main() {
	/*   テストするロボットのipアドレスを入力   */
	/*   192.168.0.10<ロボット番号>:20011   */
	//conn, err := net.Dial("udp4", "127.0.0.1:20106") シュミレータ
	conn, err := net.Dial("udp4", "127.0.0.1:20106")
	if err != nil {
		panic(err)
	}
	var robotid uint32 = 0
	var kickspeedx float32 = 0
	var kickspeedz float32 = 0
	var veltangent float32 = 0
	var velnormal float32 = 0
	var velangular float32 = 0
	var spinner bool = false
	var wheelsspeed bool = false

	for i := 0; i < 300; i++ {
		robotid = 3 //robot id
		kickspeedx = 0
		kickspeedz = 0
		veltangent = 1
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
		marshalpacket, _ := proto.Marshal(packet)
		//println(marshalpacket)

		_, err = conn.Write([]byte(marshalpacket))
		println("send : %v", marshalpacket)
		if err != nil {
			panic(err)
		}
		time.Sleep(3 * time.Millisecond)

	}

	//to stop

	for i := 0; i < 10; i++ {

		var num uint32 = 0
		for num = 0; num < 11; num++ {
			robotid = num //robot id
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
}
