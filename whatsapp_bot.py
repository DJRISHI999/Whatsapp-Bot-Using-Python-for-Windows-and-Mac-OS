import pyautogui as pt
import cv2
import os
from pyscreeze import locateOnScreen
from whatsapp_responses import response
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
import mysql.connector as ms

u  = input("Enter the user of MySQL")
p = input("Enter the password of MySQL")
con = ms.connect(host = localhost,user = u, passwd = p, database = 'wpbot') 
# DON'T FORGET TO PUT ON YOUR PASSWORD 
# DON'T FORGET TO ADD DATABASE WPBOT IN YOUR MYSQL INTERFACE
if con.is_connected():
    print('CONNECTION ESTABLISED SUCCESSFULLY....')
cur = con.cursor()
cur.execute("DESCRIBE records")
s = 'INSERT INTO records (SENDER_NAME,SENDER_MESSAGE,BOT_REPLY) values(%s,%s,%s)'
for i in cur:
    print(i)
# Mouse click workaround from MAC OS
mouse = Controller()


# Instructions for our whatsapp bot
class WhatsApp:
    

    

    # Defines the starting values
    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ""
        self.senders_name = ""
        self.last_message = ""

    # opens whatsapp

    def open_whatsapp(self):
        try:
            position = pt.locateOnScreen('whatsapp.png', confidence=.7)
            pt.moveTo(position, duration=self.speed)
            pt.leftClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_open_whatsapp):',e)

        

    # Navigate to the green dots for new messages
    def check_new_message(self):
        while True:
            try:            
                position = pt.locateOnScreen('green_dot.png', confidence=.7)
                if position is not None:
                    pt.moveTo(position[0:2], duration = self.speed)
                    pt.moveRel(-100,0,duration=self.speed)
                    pt.doubleClick(interval=self.click_speed)
                    break
                else:
                    position1 = pt.locateOnScreen('whatsapp.png', confidence=.7)
                    pt.moveTo(position1, duration=self.speed)
                    pt.leftClick(interval=self.click_speed)                    
                    print('no new message yet')
                    sleep(10)
                    position1 = pt.locateOnScreen('whatsapp.png', confidence=.7)
                    pt.moveTo(position1, duration=self.speed)
                    pt.leftClick(interval=self.click_speed)
            except Exception as e:
                print('Exception(check_new_message):',e)


    def find_sendrs_name(self):
        pt.moveTo(458,61,duration=self.speed)
        pt.leftClick(interval=self.click_speed)
        pt.moveTo(1141,333,duration=self.speed)
        pt.tripleClick(interval=self.click_speed)
        pt.rightClick(interval=self.click_speed)
        pt.moveRel(10,10, duration=self.speed)
        pt.leftClick(interval=self.click_speed)
        self.senders_name = pc.paste()
        pt.moveTo(994,54,duration=self.speed)
        pt.leftClick(interval=self.click_speed)
# mouse goes on input box

    def nav_input_box(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(100,10, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box):',e)


    def nav_message_reply(self):
        try:
            position = pt.locateOnScreen('paperclip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(35,-50, duration=self.speed)
            pt.tripleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_input_box):',e)

    
    def get_message(self):
            pt.rightClick(interval=self.click_speed)
            pt.moveRel(10,10, duration=self.speed)
            pt.leftClick(interval=self.click_speed)
            sleep(1)
            self.message = pc.paste()
            print('user says:', self.message)
            

            


    def send_message(self):
        try:
            # checking the last message was same or not
            if self.message!=self.last_message:
                position = pt.locateOnScreen('paperclip.png',confidence = .7)
                x = position[0]
                y = position[1]
                pt.moveTo(x+200,y+20,duration=.5)
                pt.click()
                bot_response = response(self.message)
                pt.typewrite(bot_response,interval=.1)
                pt.typewrite('\n',interval=.1)
                print('YOU SAID:',bot_response)
                pt.moveTo(104,472,duration=self.speed)
                pt.leftClick(interval=self.click_speed)
                t = (self.senders_name,self.message,bot_response)
                cur.execute(s,t)
                con.commit()
                
                
            
            else:
                print('no new message...')
        except Exception as e:
            print('Exception (recording):',e)

    def close_whatsapp(self):
        try:
            position = pt.locateOnScreen('whatsapp.png', confidence=.7)
            pt.moveTo(position, duration=self.speed)
            pt.leftClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (close_whatsapp):',e)

wa_bot = WhatsApp(speed=.5, click_speed=.4)
while True:
    wa_bot.open_whatsapp()
    wa_bot.check_new_message()
    wa_bot.find_sendrs_name()
    wa_bot.nav_message_reply()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()
    wa_bot.close_whatsapp()
    sleep(10)
