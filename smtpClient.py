
import socket


def smtp_client(port=1025, mailserver='127.0.0.1'):
    # To create a socket object called client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # To connect to the SMTP server
    client_socket.connect((mailserver, port))

    # To prepare the email message
    msg = "\r\nGreeting from the cold New York.\r\n"
    endmsg = "\r\n.\r\n"

    # To close the socket at the end
    client_socket.close()

    # To call the function with default parameter
    smtp_client()

    # Choose a mail server (e.g. Google Mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start

    # To connect to the SMTP server
    client_socket.connect((mailserver, port))

    # To prepare the email message
    email_message = """Subject: Greeting from the cold New York"\r\n\r\n
    msg +="\r\n"
    
    msg += "This is the body of the message."""

    # To receive the initial greeting from the SMTP server
    recv = client_socket.recv(1024).decode()
    print(recv)

    # #You can use these print statement to validate return codes from the server.
    print('Server:', recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    helo_command = 'HELO "localhost"\r\n'
    client_socket.send(helo_command.encode())
    recv = client_socket.recv(1024).decode()
    print(recv)

    # To verify if the server's response starts with the '250; reply code
    if recv[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    # To send HELO comment and print server response
    helo_command = 'HELO localhost\r\n'
    client_socket.send(helo_command.encode())
    recv = client_socket.recv(1024).decode()
    print(recv)

    # Fill in end
    if recv[:3] != '250':
        print('250 reply not received from server.')

    # Define the sender email address
    sender = '<swashbuckler080808@gmail.com>'

    # To prepare the message from command the sender's email
    from_header = "From:<swashbuckler080808@gmail.com>\r\n"
    to_header = "To:<xyclarke@yahoo.com>\r\n"
    subject = "Subject: Greeting from the cold New York\r\n'"

    # To wait for and handle the server response
    recv = client_socket.recv(1024).decode()
    print(recv)
    if recv[:3] != '250':
        print('250 reply not received from server after MAIL FROM command.')

    # Send RCPT TO command and handle server response.
    # To send RCPT TO helo_command
    # To define the recipient email address
    recipient = '<xyclarke@yahoo.com>'

    # To use the recipient in the RCPT TO command
    rept_to_command = f'RCPT TO: {recipient}\r\n"'
    client_socket.send(rept_to_command.encode())

    # To wait for and handle the server response
    recv = client_socket.recv(1024).decode()
    print(recv)
    if recv[:3] != '250':
        print(recv)
    if recv[:3] != '250':
        print('250 reply not received from server after RCPT TO command.')

    # Fill in start
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    # Fill in end

    # Send the DATA command and include the message body followed by endmsg
    client_socket.send("DATA\r\n".encode())
    recv = client_socket.recv(1024).decode()
    print(recv)
    if recv[:3] != '354':
        # The server is ready to receive the message content
        # Send my email headers and body, followed by endmsg to indicate the end of the message
        client_socket.send((msg + "\r\n.\r\n").encode())

    # To wait for the server's final response after sending the message content
    recv = client_socket.recv(1024).decode()
    print(recv)

    # Verify if the email was accepted for delivery
    if recv[:3] != '250':
        print('250 reply not received from server DATA command after')

    # To assume the server responded with '354',send the email headers and message body
    # To define the email subject
    subject = "Subject: Greeting from cold New York\r\n"

    # To define the sender and recipient email headers
    from_header = "From:<swashbuckler080808@gmail.com>\r\n"
    to_header = "To:<xyclarke@yahoo.com>\r\n"
    # To define the email body
    body = "\r\nThis is the body of the message."

    # To combine headers and body into one full message
    full_message = from_header + to_header + subject + body

    # Send message data.
    # Fill in start
    # Fill in end
    client_socket.send(email_message.encode())
    recv = client_socket.recv(1024).decode()
    print(recv)
    if recv[:3] != '250':
        print('250 reply not received from server after sending message body.')

    # To send the message content after the server responds with "354"
    client_socket.send(full_message.encode())

    # To include the end of message delimiter
    endmsg = "\r\n.\r\n"
    client_socket.send(endmsg.encode())

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    # Fill in end
    # To send the message content after the server responds with '354'
    client_socket.send(full_message.encode())

    # To end the message with a single period on a line by itself
    endmsg = '\r\n.\r\n"client_socket.send(endmsg.encode()) recv=client_socket.recv()'

    # To wait for and hangle the server response to the end of the message
    data_command = "DATA\r\n"
    recv = client_socket.recv(1024).decode()
    print("Response after sending message body:", recv)

    # To check if the server's response is'250(',indicating that the message was accepted for delivery
    if recv[:3] != '250':
        print('250 reply not received from server after end of message data.')

    # Send QUIT command and handle server response.
    # Fill in start
    # Fill in end

    # To QUIT command to indicate we are done and want to close the connection
    quit_command = "QUIT\r\n"
    client_socket.send(quit_command.encode())

    # To wait for and handle the server's response to the QUIT command
    recv = client_socket.recv(1024).decode()

    # To check if the server's response is '221', indicating that the server is closing the connection
    if recv[:3] != '221':
        print("221 reply received from server,closing connection.")
    else:
        print("Unexpected response from server:", recv)

    # To close the socket as the SMTP session is completed
    client_socket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')