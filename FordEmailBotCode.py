import requests
from math import floor
import time
import smtplib as smptp
from email.message import EmailMessage

book_url = 'https://fordspamtext.000webhostapp.com/'
r = requests.get(book_url)
book_data = r.text.encode('ascii', 'ignore').decode('ascii')
word_list = book_data.split(" ")

msg_size = floor(len(word_list) / 1000)
final_msg_size = len(word_list) - (msg_size * 999)
print(f"Words per message: {msg_size}\nFinal message size: {final_msg_size}")

user_list = ['fordmenaservices@gmail.com', 'ford.dubai.showroom@gmail.com']
password_list = ['Virajsuckscock', '#$ford.dubai.showroom123']

for i in user_list:
    index_number = user_list.index(i)
    password = password_list[index_number]
    to_address = 'pefot73393@opposir.com'
    smtp_host = 'smtp.gmail.com' 
    smtp_port = 587

    subject = 'Ford Motor Company - URGENT'
    msg_text = ''
    start_pos = 0
    msg_count = 101
        
    for b in range(20):
        server = smptp.SMTP(host=smtp_host, port=smtp_port)
        server.starttls()
        server.login(user=i, password=password)

        for i in range(50):
            if msg_count == 1000:
                start_pos = (len(word_list)-final_msg_size)
                msg_text = ' '.join(word_list[start_pos:])
            elif msg_count == 600:
                server.close()
            else:
                start_pos = msg_count * msg_size
                msg_text = ' '.join(word_list[start_pos:start_pos + msg_size])

            msg = EmailMessage()
            msg['From'] = i
            msg['To'] = to_address
            msg['Subject'] = subject + ' ' + str(msg_count+1)
            msg.set_payload(msg_text)

            msg_count +=1
            server.send_message(msg)

            time.sleep(0.5)

        time.sleep(60)
        
        server.close()

##user = 'fordmenaservices@gmail.com'
##password = 'Virajsuckscock'
##fr_address = 'fordmenaservices@gmail.com'
##to_address = 'aditya.v_jcd@jumeirahcollege.com'
##smtp_host = 'smtp.gmail.com' 
##smtp_port = 587
##
##subject = 'Ford Motor Company - URGENT'
##msg_text = ''
##start_pos = 0
##msg_count = 101
##    
##for b in range(20):
##    server = smptp.SMTP(host=smtp_host, port=smtp_port)
##    server.starttls()
##    server.login(user=user, password=password)
##
##    for i in range(50):
##        if msg_count == 1000:
##            start_pos = (len(word_list)-final_msg_size)
##            msg_text = ' '.join(word_list[start_pos:])
##        else:
##            start_pos = msg_count * msg_size
##            msg_text = ' '.join(word_list[start_pos:start_pos + msg_size])
##
##        msg = EmailMessage()
##        msg['From'] = user
##        msg['To'] = to_address
##        msg['Subject'] = subject + str(msg_count+1)
##        msg.set_payload(msg_text)
##
##        msg_count +=1
##        server.send_message(msg)
##
##        time.sleep(0.5)
##
##    time.sleep(60)
##    
##    server.close()
##
