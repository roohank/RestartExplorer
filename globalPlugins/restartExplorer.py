import globalPluginHandler
import globalCommands
from scriptHandler import script
import subprocess
import time
import ui

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    @script(
        description="ریستارت کردن فرآیند اکسپلورر ویندوز",
        gesture="kb:NVDA+alt+r"
    )
    def script_restartExplorer(self, gesture):
        # اطلاع دادن به کاربر که دستور در حال اجرا است
        ui.message("در حال ریستارت اکسپلورر...")
        
        # اجرای دستور در یک ترد جداگانه تا رابط NVDA فریز نشود
        import threading
        threading.Thread(target=self._runRestartCommand).start()

    def _runRestartCommand(self):
        """اجرای دستورات سیستمی برای کشتن و راه‌اندازی مجدد اکسپلورر"""
        try:
            # دستور taskkill برای بستن اکسپلورر
            subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], 
                           creationflags=subprocess.CREATE_NO_WINDOW)
            
            # مکث کوتاه برای بسته شدن کامل فرآیند
            time.sleep(0.5)
            
            # راه‌اندازی مجدد اکسپلورر
            subprocess.Popen(["explorer.exe"], 
                             creationflags=subprocess.CREATE_NO_WINDOW)
            
            ui.message("اکسپلورر با موفقیت ریستارت شد.")
            
        except Exception as e:
            ui.message(f"خطا در ریستارت اکسپلورر: {str(e)}")