from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1', data=None):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket=socket(A_INET,SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end


    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '280':
    #    print('280 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFromCommand ='MAIL From:xc2217@nyu.edu\r\n'
    clientSocket.send(mailFromCommand.encode())
    recv2=clientSocket.recv(1024).decode()
    print (recv2)
    if recv2[:3] !='250':
        print ('250 reply not received from server after MAIL FROM command')
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptToCommand = 'RCPT TO:<xc2217@nyu.edu.\r\n'
    clientSocket.send (reptToCommand.encode())
    recv3=clientSocket.recv(1024).decode()
    print (recv3)
    if recv3 [:3] !='250':
        print ('250 reply not received from server after RCPT TP command')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand='DATA\r\n'clientSocket.send (detaComand.encode())
    recv4=clientSocket.recv(1024).decode()
    print (recv4)
    if recv4[:3] !='354':
        print ('354 reply not received from server after DATA command')

    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send (msg.encode())

    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv_msg=clientSocket.recv(1024). decode()
    print (recv_msg)
    if recv_msg[:3] !='250'
        print ('250'reply not received from server after sending messge data')
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand='QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    print(recv5)
    if recv5 [:3] !='221' :
        print ('221 reply not recevived from server after QUIT command')
        clientSocket.close()
        recv5=clientSocket.recv(1024).decode())


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')