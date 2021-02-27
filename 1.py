buttons={'1':(72,518),'2':(193,518),'3':(327,534),'4':(58,459),'5':(188,453),'+':(383,542),'=':(357,585),'-':(357,444),"*":(357,391),"/":(357,334),"x":(357,279)}
import pyautogui as pt
pt.FAILSAFE =False
a = pt.size()
c=input("계산식을 입력")
x,y=buttons['x']
pt.moveTo(x,y, duration=0.3)
pt.click()


for i in c:
    x,y=buttons[i]
    pt.moveTo(x,y, duration=0.3)
    pt.click()


x,y=buttons['=']
pt.moveTo(x,y, duration=0.3)
pt.click()
