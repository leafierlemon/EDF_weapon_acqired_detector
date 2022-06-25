from time import sleep
import win32gui
import win32con
from PIL import ImageGrab


class Capture:
    def __init__(self, window_name):
        self.WINDOW_NAME = window_name

    def screenshot_client(self, filename=None):

        flg_mini=False
        # window
        hwnd = win32gui.FindWindow(None, self.WINDOW_NAME)
        win32gui.SetForegroundWindow(hwnd)
        if win32gui.IsIconic(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_NORMAL)
            flg_mini=True            
            sleep(0.1)
        sleep(0.1)
        client_rect = win32gui.GetClientRect(hwnd)
        client_point = win32gui.ClientToScreen(hwnd, (0, 0))
        box=(
            client_point[0]+client_rect[0],
            client_point[1]+client_rect[1],
            client_point[0]+client_rect[2],
            client_point[1]+client_rect[3]
        )

        img = ImageGrab.grab(all_screens=True)
        img_crop=img.crop(box)
        if flg_mini:
            win32gui.ShowWindow(hwnd,win32con.SW_MINIMIZE)
            hwnd
        if filename:
            img_crop.save(filename)
        # print(box)
        # print(client_point)
        return img_crop


if __name__ == "__main__":
    c = Capture("ウィンドウ プロジェクター (シーン) - シーン 2")
    c.screenshot_client("./tmp/test.png")
