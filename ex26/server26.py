"""EX 2.6 server implementation
   Author: Ohad Solomon Gleicher
   Date: 14.11.2020
"""

import socket
import protocol


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", protocol.PORT))
    server_socket.listen()
    print("Server is up and running")
    (client_socket, client_address) = server_socket.accept()
    print("Client connected")

    while True:
        response = ""
        valid_msg, cmd = protocol.get_msg(client_socket)  # check if the request is valid and returns the command
        if valid_msg:
            print(cmd)
            valid = protocol.check_cmd(cmd)  # check if the command exists
            if valid and not cmd == "EXIT":
                response = protocol.create_server_rsp(cmd)  # return result of command
                print(response)
            elif cmd == "EXIT":
                break
            else:
                response = "Wrong command"
        else:
            response = "Wrong protocol"
            client_socket.recv(1024)  # Attempt to empty the socket from possible garbage
        client_socket.send(protocol.create_msg(response).encode())
    print("Closing\n")
    client_socket.close()
    server_socket.close()




if __name__ == "__main__":
    main()
