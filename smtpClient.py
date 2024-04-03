from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start, to create socket using IPv4 and using TCP connection
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    # Fill in end, to set up buffer size to receive, and convert the response to a string, check first three characters
    recv = clientSocket.recv(1024).decode()
    if recv[:3] != '220':


    clientSocket.recv(1024).decode()
    # print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    clientSocket.recv(1024).decode()
    # print(recv1)
    # if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # To send a MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand = 'MAIL FROM: <xc2217@nyu.edu>\r\n'
    clientSocket.send(mailFromCommand.encode())

    # Fill in end, to wait for and receive the server's response,decode response to string from bytes,check 250 response
    recv2 = clientSocket.recv(1024).decode()
    if recv2[:3] != '220':


    # Send RCPT TO command and handle server response.
    # Fill in start
    'RCPT TO: <xyclarke@gmail.com>\r\n'
    # Fill in end.  To wait for the server's response and check the response and the first 3 characters for the '250'
    recv3 = clientSocket.recv(1024).decode()
    if recv3[:3] != '250':


    # Send DATA command and handle server response.
    # Using RCPT TP command following the SMTP protocol. To convert string to stream
    # Fill in start
    dataCommand = 'DATA\r\n'
    clientSocket.send(dataCommand.encode())
    # Fill in end, expecting response, check 354 response before proceeding.
    recv4 = clientSocket.recv(1024).decode()
    if recv4[:3] != '354':


    # Send message data.
    # Fill in start, to separate the body by a blank line
    message = ('FROM: <xc2217@nyu>\r\n'
               'TO: <xyclarke@gmail.com\r\n'
               'Subject:Hello\r\n\r\n')
    clientSocket.send(message.encode())
    # Fill in end, to receive the server's response and decode it to s string,and check 250 response
    recv5 = clientSocket.recv(1024).decode()
    if recv5[:3] != '250':


    # Message ends with a single period, send message end and handle server response.
    # Fill in start, to tell SMTP server that the message content is finished.
    endMessage = '\r\n.\r\n'
    clientSocket.send(endMessage.encode())
    # Fill in end,to handle the response, covert bytes to a string, check 250 response
    recvMessage = clientSocket.recv(1024).decode()
    if recvMessage[:3] != '250':


    # Send QUIT command and handle server response.
    # Fill in start, to convert a byte to stream for network transmission
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    # Fill in end,
    # Check if recv(1024) method to receive the server's response and coverts it from bytes to a string. check 221
    recvQuit = clientSocket.recv(1024).decode()
    if recvQuit[:3] != '221':
        

    # To close the socket
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(port=1025, mailserver='127.0.0.1')
