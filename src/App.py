import pathlib
import time

import pyautogui


SCROLL_LIMIT = 8


if __name__ == '__main__':
    print(f'Locating Network Management button...')

    try:
        x, y = pyautogui.locateCenterOnScreen('./img/Network_Management.png')
        pyautogui.click(x, y)
    except pyautogui.ImageNotFoundException:
        print(f'Error locating Network Management button!')

        exit(1)

    print(f'Clicked on Network Management button!')

    print(f'Waiting until Network Management page is completely loaded...')

    time.sleep(20)

    print(f'Locating Network Complete button...')

    try:
        x, y = pyautogui.locateCenterOnScreen('./img/Network_Complete.png')
        pyautogui.doubleClick(x, y)
    except pyautogui.ImageNotFoundException:
        try:
            x, y = pyautogui.locateCenterOnScreen('./img/Network_Complete_other.png')
            pyautogui.doubleClick(x, y)
        except pyautogui.ImageNotFoundException:
            print(f'Error locating Network Complete button!')

            exit(1)

    print(f'Clicked on Network Complete button!')

    base_path = './img/NEV_Bestel'
    directory = pathlib.Path(base_path)

    for file in directory.glob('*.png'):
        print('Locating Physical Root button...')

        try:
            x, y = pyautogui.locateCenterOnScreen('./img/Physical_Root.png')
            pyautogui.moveTo(x, y)
            pyautogui.scroll(880)

            print(f'Scrolled up!')
        except pyautogui.ImageNotFoundException:
            try:
                x, y = pyautogui.locateCenterOnScreen('./img/Physical_Root_other.png')
                pyautogui.moveTo(x, y)
                pyautogui.scroll(880)

                print(f'Scrolled up!')
            except pyautogui.ImageNotFoundException as error:
                print(f'Error locating Physical Root button! -> {error}')

                exit(1)

        print(f'Current file: {file.name}.')

        for _ in range(SCROLL_LIMIT):
            try:
                print(f'Locating "{file.name}" button...')

                x, y = pyautogui.locateCenterOnScreen(f'{base_path}/{file.name}')
                pyautogui.doubleClick(x, y)

                print(f'Clicked on "{file.name}" button!')

                time.sleep(10)

                break
            except pyautogui.ImageNotFoundException:
                print(f'"{file.name}" button not found. Locating Physical Root button...')

                try:
                    x, y = pyautogui.locateCenterOnScreen('./img/Physical_Root.png')
                    pyautogui.moveTo(x, y)
                    pyautogui.scroll(-110)

                    print(f'Scrolled down!')
                except pyautogui.ImageNotFoundException:
                    try:
                        x, y = pyautogui.locateCenterOnScreen('./img/Physical_Root_other.png')
                        pyautogui.moveTo(x, y)
                        pyautogui.scroll(-110)

                        print(f'Scrolled down!')
                    except pyautogui.ImageNotFoundException as error:
                        print(f'Error locating Physical Root button! -> {error}')

                        exit(1)
