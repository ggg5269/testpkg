from threading import Thread, Event
import time
from pywinauto import application as autoWin


class ButtonClicker(Thread):
    def __init__(self, popup_title='Microsoft Excel'):
        """持去獲取當前同名視窗並點擊確認按鈕

        Args:
            popup_title (str, optional): 視窗名稱. Defaults to 'Microsoft Excel'.
        """
        Thread.__init__(self)
        self._stop_event = Event()
        self.popup_title = popup_title
    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self) -> None:
        while True:
            time.sleep(3)
            try:
                app = autoWin.Application()
                con = app.connect(title=self.popup_title)

                msg_data = con.Dialog.Static2.texts()[0]
                print(msg_data)
                while True:
                    con.Dialog.Button.click()
                    # con.Dialog.Button.click()

            except Exception as e:
                # print('Excel didnt stuck')
                pass