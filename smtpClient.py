import socket


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    
    # Fill in start
    # To create clientSoket and establish a TCP connection
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    recv = clientSocket.recv(1024).decode()
    print(recv) 
    # Fill in end

    # print(recv) # You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #  print('220 reply not received from server.')

    # To send HELO command and print server response
    heloCommand = b'HELO example.com\r\n'
    clientSocket.send(heloCommand)
    recv1 = clientSocket.recv(1024).decode()
    print(recv1) 
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # To send MAIL FROM command and handle server response
    # Fill in start
    sender = 'xc2217@nyu.edu'
    clientSocket.sendall(f'MAIL FROM:<{sender}>\r\n'.encode())
    recv_data = clientSocket.recv(1024).decode()
    print(recv_data)
    # Fill in end

    # To send RCPT TO command and handle server response
    # Fill in start
    recipient = 'niewenlai@gmail.com'
    clientSocket.sendall(f'RCPT TO:<{recipient}>\r\n'.encode())
    recv_data = clientSocket.recv(1024).decode()
    print(recv_data)
    # Fill in end

    # To send DATA command and handle server response.
    # Fill in start
    clientSocket.sendall(b'DATA\r\n')
    recv_data = clientSocket.recv(1024).decode()
    print(recv_data)
    # Fill in end

    # To Send message data
    # Fill in start
    subject = 'Test Email'
    message = 'This is a test email sent from Python.'
    clientSocket.sendall(f'Subject: {subject}\r\n'.encode())
    clientSocket.sendall(f'From: {sender}\r\n'.encode())
    clientSocket.sendall(f'To: {recipient}\r\n'.encode())
    clientSocket.sendall('\r\n'.encode())
    clientSocket.sendall(message.encode())
    clientSocket.sendall(b'\r\n.\r\n')
    print(msg)
    print(endmsg)
    # Fill in end

    # To message ends with a single period, send message end and handle server response
    # Fill in start
    recv_data = clientSocket.recv(1024).decode()
    print(recv_data)
    # Fill in end

    # To send a QUIT command and handle server response.
    # Fill in start
    clientSocket.sendall(b'QUIT\r\n')
    recv_data = clientSocket.recv(1024).decode()
    print(recv_data)
    # Fill in end


if __name__ == '__main__':
    smtp_client(port=1025, mailserver='127.0.0.1')