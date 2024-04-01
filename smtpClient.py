import socket

def smtp_client(port=1025, mailserver='localhost'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start # To create a socket object called ClientSocket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # To connect to the SMTP server
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    # print('220 reply not received from server.')

 # To send Helo command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)

    # To check if the first three characters of the response are '250'( SMTP protocol success code)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # SMTP conversation steps should continue here

    #You can use these print statement to validate return codes from the server.
    #ifrecv[:3] != 220:
       #print('220 reply not received from server.')

    # Send HELO command and print server response.
    helo_command = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv1)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    sender_email = "xc2217@nyu.edu"
    mail_from_command = b'MAIL FROM:<' + sender_email.encode() + b'>'
    clientSocket.send(mail_from_command)
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != 250:
        print('250 reply not received from server.')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcpt_to_command = "RCPT TO:<niewenlai@gmail.com>\r\n"
    clientSocket.send(rcpt_to_command.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != 250:
        print('250 reply not received from server.')
    # Fill in end

# To send DATA command and handle server response.
    # Fill in start
    data_command = "DATA\r\n"
    clientSocket.send(data_command.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] ==354:
        print('354 reply not received from server.')
    clientSocket.send("\r\n.\r\n".encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)

    #To check for successful delivery with 250 response
    print("No 354 reply response from server")

 # To send message data. # Fill in start
    message_headers = "From: <<xc2217@nyu.edu>>\r\n"
    "To:<swashbuckler080808@gmail.com>\r\n"
    "Subject: Greetings from New York\r\n"
    message_body = "Hello Alice, How are you? Are you enjoying your Computer Networking class?\n"
    full_message = message_headers + message_body + "\r\n" + message_body + "\r\n.\r\n"

    clientSocket.send(full_message.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != 250:
        print('250 reply not received from server. Message not sent successfully.')
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # To signal the end of the message with a period, to send message and handle server response
    message_end = "\r\n.\r\n"
    clientSocket.send(message_end.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != 250:
        print('250 reply not received from server.. Message not sent successfully.')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    # To send the "QUIT" command, to signal the end of the SMTP session, and to hande the server response properly
    quit_command = "QUIT\r\n"
    clientSocket.send(quit_command.encode())
    recv = clientSocket.recv(1024).decode()
    print(recv)
    if recv[:3] != 221:
        print('221 reply not received from server. Session not ended properly.')
    # To close the socket
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(port=1025, mailserver='127.0.0.1')
