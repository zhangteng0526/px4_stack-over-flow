import socket
import time
import random

mode = "PX4"
ip = "127.0.0.1"
port = 18570



def udpSocketOpen():
    global ip, port, sock, mode

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(5)

    # sock.bind((ip,port))
    print('Socket Target {}:{}'.format(ip, port))
    print('Fuzzing Target : {}\n'.format(mode))



def send_single_packet():
    line_number = 0
    with open('output.txt', 'r') as file:
        # 逐行读取文件
        for line in file:
            # 去除每行末尾的换行符 '\n'
            packet_hex = line.strip()
            # 将十六进制字符串转换为字节
            if(line_number>97970):
                time.sleep(3)
            # 接下来你可以对packet进行处理，例如发送或分析等
            # 例如，这里我们只是打印出来
            sock.sendto(bytes.fromhex(packet_hex), (ip, port))
            line_number +=1
            try:
                data, addr = sock.recvfrom(4096)
                print(f"Received response: {data}")
            except socket.timeout:
                print("No response received within timeout period.")




def main():
    udpSocketOpen()

    send_single_packet()

    sock.close()


if __name__ == '__main__':
    main()