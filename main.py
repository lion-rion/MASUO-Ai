from proto.pb_gen.to_racoonai_pb2 import RacoonMW_Packet
from proto.pb_gen.grSim_Commands_pb2 import grSim_Robot_Command, grSim_Commands
from proto.pb_gen.grSim_Packet_pb2 import grSim_Packet

from socket import AF_INET, IPPROTO_UDP, SO_REUSEADDR, SOCK_DGRAM,SOL_SOCKET, socket

BUFFSIZE: int = 2048

def main():
    while (True):
        #receive data from socket
        # AF_INET = IPv4
        # SOCK_DGRAM = UDP
        # IPPROTO_UDP = UDP

        __sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        __sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        __sock.bind(('127.0.0.1', 10006))
        packet: bytes = __sock.recv(BUFFSIZE)
        proto = RacoonMW_Packet()
        proto.ParseFromString(packet) #複合
        print(proto)

        #send data to grSim
        __sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
        __sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

        __sock.bind(('127.0.0.1', 20106))

        grsim_robot_command = grSim_Robot_Command()
        grsim_robot_command.id = 1
        grsim_robot_command.wheel1 = 1
        grsim_robot_command.wheel2 = 1
        grsim_robot_command.wheel3 = 1
        grsim_robot_command.wheel4 = 1
        grsim_robot_command.kickspeedx = 1
        grsim_robot_command.kickspeedz = 0
        grsim_robot_command.veltangent = 0
        grsim_robot_command.velnormal = 1
        grsim_robot_command.velangular = 0
        grsim_robot_command.spinner = False
        grsim_robot_command.wheelsspeed = False
        grSim_commands = grSim_Commands(
            timestamp = 0,
            robot_commands=[grsim_robot_command],
            isteamyellow = False
        )
        grsim_packet_packet = grSim_Packet(commands=grSim_commands)
        print(grsim_packet_packet.SerializeToString())
        #__sock.sendto(grsim_packet_packet.SerializeToString(),('127.0.0.1', 20106))

        

def recieve(dict):
    __sock = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)
    __sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # __sock.bind(("127.0.0.1", 30011))
    __sock.bind(dict)

    packet: bytes = __sock.recv(2048)
    proto = RacoonMW_Packet()
    proto.ParseFromString(packet)

if __name__ == "__main__":
    main()
