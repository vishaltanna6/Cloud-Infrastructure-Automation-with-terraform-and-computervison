import PyWaMG as wp
import datetime as dt
now = dt.datetime.now()
wp.wa_login(isHeadless=False)

number="+918866663221"

fpath="D:/ARTH/SummerInternship2021/task6/Face Recognition/img.jpg"
msg = "ALERT! ALERT! ALERT!"

wp.send_txt(number,msg,wait=0,times=1,appendMessageNumber = True,isInContacts = True,showLogs = True)
wp.send_file(number,fpath,isInContacts=False,showLogs=True) 