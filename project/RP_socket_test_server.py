import socket
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 6
GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

HOST = '172.30.1.48' 
# Server IP or Hostname
PORT = 12345 
# Pick an open Port (1000+ recommended), must match the client sport
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#managing error exception
try:
    s.bind((HOST, PORT))
except socket.error:
    print('Bind failed ')

s.listen(5)
print ('Socket awaiting messages')
(conn, addr) = s.accept()
print('Connected')

# awaiting for message
while True:
    recvMsg = conn.recv(1024).decode()
   
    print('I sent a message back in response to: ' + recvMsg)
    replyMsg = ''

    # process your message
    if recvMsg == 'Hello':
        replyMsg = 'Hi, back!'
    elif recvMsg == 'This is important':
        replyMsg = 'OK, I have done the important thing you have asked me!'
    #and so on and on until...
    elif recvMsg == 'quit':
        conn.send('Terminating'.encode())        
    elif recvMsg == 'LED ON':
        GPIO.output(LED, GPIO.HIGH)
        replyMsg =  'LED ON Okay !!'
    elif recvMsg == 'LED OFF':
        GPIO.output(LED, GPIO.LOW)
        replyMsg =  'LED OFF ~'
    else:
        replyMsg = 'Unknown command'

    # Sending reply
    conn.send(replyMsg.encode(encoding='utf_8', errors='strict'))
 
GPIO.cleanup()
conn.close() 
# Close connections
