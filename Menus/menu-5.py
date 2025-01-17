#!/usr/bin/env python
import kalipi
from kalipi import *


#############################
## Global display settings ##

#++++++++++++++++++++++++++++#
#+   Select color scheme    +#

# Tron theme orange
##tron_regular = tron_ora
##tron_light = tron_yel
##tron_inverse = tron_whi

# Tron theme blue
tron_regular = tron_blu
tron_light = tron_whi
tron_inverse = tron_yel

#+           End            +#
#++++++++++++++++++++++++++++#

## Global display settings ##
#############################

#############################
##    Local Functions      ##

def check_mana():
    try:
        check = "sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_get_state | grep 'ENABLE'"
        status = kalipi.run_cmd(check)
        if ("ENABLE" in status):
            return True
        else:
            return False
    except:
        return False

def check_mana_loud():
    try:
        check = "sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_state | grep 'ENABLE'"
        status = kalipi.run_cmd(check)
        if ("ENABLE" in status):
            return True
        else:
            return False
    except:
        return False

##    Local Functions      ##
#############################


#############################
##        Buttons          ##

# define all of the buttons
titleButton = Button("                   EvilAP - Custom", originX, originX, buttonHeight, buttonWidth * 3 + spacing * 2, tron_inverse, tron_inverse, titleFont)
button1 = Button(labelPadding * " " + "  AP Open", originX, originY, buttonHeight, buttonWidth, magenta, tron_inverse, labelFont)
button2 = Button(labelPadding * " " + "  AP Secure", originX + buttonWidth + spacing, originY, buttonHeight, buttonWidth, magenta, tron_inverse, labelFont)
button3 = Button(labelPadding * " " + "       Mana", originX + (buttonWidth * 2) + (spacing * 2), originY, buttonHeight, buttonWidth, magenta, tron_inverse, labelFont)
button4 = Button(labelPadding * " " + "       Beef", originX, originY + buttonHeight + spacing, buttonHeight, buttonWidth, magenta, tron_inverse, labelFont)
button5 = Button(labelPadding * " " + "   Firelamb", originX + buttonWidth + spacing, originY + buttonHeight + spacing, buttonHeight, buttonWidth, magenta, tron_inverse, labelFont)
button6 = Button(labelPadding * " " + "  Mana Loud", originX + (buttonWidth * 2) + (spacing * 2), originY + buttonHeight + spacing, buttonHeight, buttonWidth, magenta, tron_inverse,labelFont)
button7 = Button(labelPadding * " " + "       <<<", originX, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, magenta,tron_inverse, labelFont)
button8 = Button(labelPadding * " " + "  DNS2Proxy", originX + buttonWidth + spacing, originY + (buttonHeight * 2) + (spacing * 2), buttonHeight, buttonWidth, magenta, tron_inverse, labelFont)


# def make_button(button):
#     if button.disable == 1:
#         button.color = grey

#     pygame.draw.rect(screen.canvas, tron_regular, (button.xpo-10,button.ypo-10,button.width,button.height),3)
#     pygame.draw.rect(screen.canvas, magenta, (button.xpo-9,button.ypo-9,button.width-1,button.height-1),1)
#     pygame.draw.rect(screen.canvas, tron_regular, (button.xpo-8,button.ypo-8,button.width-2,button.height-2),1)
#     font=pygame.font.Font(None,button.fntSize)
#     label=font.render(str(button.text), 1, (button.color))
#     screen.blit(label,(button.xpo,button.ypo+7))

# Define each button press action
def button(number):

    if number == 1:
        if button1.disable == 1:
            return

        # Hostapd Open
        script=os.environ["MENUDIR"] + "mana/manaSimple.sh"
        if kalipi.toggle_script(script):
                button1.color = green
                button1.draw()
                pygame.display.update()
        else:
                button1.color = magenta
                button1.draw()
                pygame.display.update()
        return

    if number == 2:
        if button2.disable == 1:
            return

        # Hostapd Secure
        script=os.environ["MENUDIR"] + "mana/manaSecure.sh"

        if kalipi.toggle_script(script):
        # Stop Service
                button2.color = green
                button2.draw()
                pygame.display.update()
        else:
        #Start Service
                button2.color = magenta
                button2.draw()
                pygame.display.update()

    if number == 3:
        if button3.disable == 1:
            return

        #Mana Attack
        if check_mana():
        # Stop Mana
                kalipi.run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_disable")
                button3.color = magenta
                button3.draw()
                pygame.display.update()
        else:
        # Start Mana
                run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_enable")
                button3.color = green
                button3.draw()
                pygame.display.update()

    if number == 4:
        if button4.disable == 1:
            return

        # Beef
        if kalipi.toggle_service("beef-xss"):
                button4.color = green
                button4.draw()
                pygame.display.update()

        else:
                button4.color = magenta
                button4.draw()
                pygame.display.update()
        return

    if number == 5:
        if button5.disable == 1:
            return

        # FireLamb
        firelamb="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/firelamb.sh"
        if kalipi.toggle_script(firelamb):
                button5.draw()
                pygame.display.update()
        else:
                button5.draw()
                pygame.display.update()
        return

    if number == 6:
        if button6.disable == 1:
            return

        #Mana Loud Attack
        if check_mana_loud():
        #Stop Mana
                kalipi.run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_off")
                button6.draw()
                pygame.display.update()
        else:
        #Start Mana Loud Attack
                kalipi.run_cmd("sudo /usr/lib/mana-toolkit/hostapd_cli -p /var/run/hostapd mana_loud_on")
                button6.draw()
                pygame.display.update()

    if number == 7:
        if button7.disable == 1:
            return

        # Previous page
        pygame.quit()
        page=os.environ["MENUDIR"] + "menu-4.py"
        os.execvp("python", ["python", page])
        sys.exit()

    if number == 8:
        if button8.disable == 1:
            return

                #DNS2Proxy
        script=os.environ["MENUDIR"] + "dns2proxy/dns2proxy.sh"
        if kalipi.toggle_script(script):
        #Stop Service
                button8.color = green
                button8.draw()
                pygame.display.update()
        else:
        #Start Service
                button8.color = magenta
                button8.draw()
                pygame.display.update()
        return


##        Buttons          ##
#############################


def menu5(argv):
    
    # Init screen
    kalipi.screen()
    # Outer Border
    kalipi.border(magenta)

    #############################
    ##        Buttons          ##

    # Buttons and labels
    # See variables at the top of the document to adjust the menu

    # Title
    titleButton.draw()

    #############################
    ##        Buttons          ##

    # Buttons and labels
    # See variables at the top of the document to adjust the menu

    # First Row
    # Button 1
    button1.disable = 0  # "1" disables button

    if button1.disable == 1:
        button1.draw()
    else:
        # Add button launch code here
        if kalipi.check_process("hostapd", "mana.conf"):
            button1.draw()
        else:
            button1.color = magenta
            button1.draw()

    # Button 2
    button2.disable = 0  # "1" disables button

    if button2.disable == 1:
        button2.draw()
    else:
        # Add button launch code here
        if kalipi.check_process("hostapd", "wpa2.conf"):
            button2.color = green
            button2.draw()
        else:
            button2.color = magenta
            button2.draw()

    # Button 3
    button3.disable = 1  # "1" disables button

    if button3.disable == 1:
        button3.draw()
    else:
        # Add button launch code here
        if check_mana():
            button3.color = green
            button3.draw()
        else:
            button3.color = magenta
            button3.draw()

    # Second Row
    # Button 4
    button4.disable = 0  # "1" disables button

    if button4.disable == 1:
        button4.draw()
    else:
        # Add button launch code here
        if kalipi.check_service("beef-xss"):
            button4.color = green
            button4.draw()
        else:
            button4.color = magenta
            button4.draw()

    # Button 5
    button5.disable = 0  # "1" disables button

    if button5.disable == 1:
        button5.draw()
    else:
        # Add button launch code here
        firelamb="/usr/bin/sudo bash " + os.environ["MENUDIR"] + "mana/firelamb.sh"
        if kalipi.check_script(firelamb):
            button5.color = green
            button5.draw()
        else:
            button5.color = red
            button5.draw()

    # Button 6
    button6.disable = 1  # "1" disables button

    if button6.disable == 1:
        button6.draw()
    else:
        # Add button launch code here
        if check_mana_loud():
            button6.color = green
            button6.draw()
        else:
            button6.color = magenta
            button6.draw()

    # Third Row
    # Button 7
    button7.disable = 0  # "1" disables button

    if button7.disable == 1:
        button7.draw()
    else:
        # Add button launch code here
        button7.draw()

    # Button 8
    button8.disable = 0  # "1" disables button

    if button8.disable == 1:
        button8.draw()
    else:
        # Add button launch code here
        if check_process("python", "dns2proxy.py"):
            button8.color = green
            button8.draw()
        else:
            button8.color = magenta
            button8.draw()



    ##        Buttons          ##
    #############################


    #############################
    ##        Input loop       ##

    while 1:
        butNo=kalipi.inputLoop("menu-4.py")
        button(butNo)

    ##        Input loop       ##
    #############################

if __name__ == "__main__":
    menu5(sys.argv[1:])

