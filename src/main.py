from time import sleep
from sftp import send_to_sftp
import pyautogui as gui


def move() -> None:
    # Click -> Network Management.
    sleep(4)
    gui.moveTo(215, 535)
    gui.click()

    # Wait until Network Management page is completely loaded.
    print('Loading Network Management page...')
    sleep(10)
    print('Network Management page loaded!')

    # Click -> Service.
    gui.moveTo(853, 144)
    gui.click()

    # Click -> WDM Trail.
    gui.moveTo(923, 647)
    gui.click()

    # Wait until WDM Trail page is completely loaded.
    print('Loading WDM Trail page...')
    sleep(10)
    print('WDM Trail page loaded!')

    # Click -> Manage WDM Trail.
    gui.moveTo(212, 373)
    gui.click()

    # Wait until Manage WDM Trail page is completely loaded.
    print('Loading Manage WDM Trail page...')
    sleep(10)
    print('Manage WDM Trail page loaded!')

    # Click -> Filter All.
    gui.moveTo(992, 955)
    gui.click()

    # Wait until filter is applied.
    print('Filtering...')
    sleep(10)
    print('Filter applied!')

    # Click -> Save As.
    gui.moveTo(1864, 574)
    gui.click()

    # Click -> File name [...].
    '''gui.moveTo(830, 750)
    gui.click()

    # Click -> File Type.
    gui.moveTo(550, 740)
    gui.click()

    # Click -> CSV Files (*.csv).
    gui.moveTo(550, 760)
    gui.click()

    # Click -> Save.
    gui.moveTo(800, 805)
    gui.click()'''

    # Click -> OK.
    gui.moveTo(1025, 669)
    gui.click()

    # Wait until Manage WDM Trail file is downloaded.
    print('Downloading Manage WDM Trail file...')
    sleep(60)
    print('Manage WDM Trail page downloaded!')


if __name__ == '__main__':
    print(gui.size(), ' -> ', gui.position())
    move()
    #sleep(10)
    #send_to_sftp()
