from time import sleep

import pyautogui as gui


def move() -> None:
    # Click -> Network Management.
    gui.moveTo(145, 720)
    gui.click()

    # Wait until Network Management page is completely loaded.
    print('Loading Network Management page...')
    sleep(10)
    print('Network Management page loaded!')

    # Click -> Service.
    gui.moveTo(605, 415)
    gui.click()

    # Click -> WDM Trail.
    gui.moveTo(655, 800)
    gui.click()

    # Wait until WDM Trail page is completely loaded.
    print('Loading WDM Trail page...')
    sleep(10)
    print('WDM Trail page loaded!')

    # Click -> Manage WDM Trail.
    gui.moveTo(155, 595)
    gui.click()

    # Wait until Manage WDM Trail page is completely loaded.
    print('Loading Manage WDM Trail page...')
    sleep(10)
    print('Manage WDM Trail page loaded!')

    # Click -> Filter All.
    gui.moveTo(715, 950)
    gui.click()

    # Wait until filter is applied.
    print('Filtering...')
    sleep(10)
    print('Filter applied!')

    # Click -> Save As.
    gui.moveTo(1310, 729)
    gui.click()

    # Click -> File name [...].
    gui.moveTo(830, 750)
    gui.click()

    # Click -> File Type.
    gui.moveTo(550, 740)
    gui.click()

    # Click -> CSV Files (*.csv).
    gui.moveTo(550, 760)
    gui.click()

    # Click -> Save.
    gui.moveTo(800, 805)
    gui.click()

    # Click -> OK.
    gui.moveTo(745, 810)
    gui.click()

    # Wait until Manage WDM Trail file is downloaded.
    print('Downloading Manage WDM Trail file...')
    sleep(60)
    print('Manage WDM Trail page downloaded!')


if __name__ == '__main__':
    print(gui.size(), ' -> ', gui.position())
    
    move()
