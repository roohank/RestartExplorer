import globalPluginHandler
import globalCommands
from scriptHandler import script
import subprocess
import time
import ui
import threading

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

    @script(
        description="Restart the Windows Explorer process"
    )
    def script_restartExplorer(self, gesture):
        ui.message("Restarting Explorer...")
        threading.Thread(target=self._runRestartCommand).start()

    def _runRestartCommand(self):
        try:
            subprocess.run(["taskkill", "/f", "/im", "explorer.exe"], 
                           creationflags=subprocess.CREATE_NO_WINDOW)
            time.sleep(0.5)
            subprocess.Popen(["explorer.exe"], 
                             creationflags=subprocess.CREATE_NO_WINDOW)
            ui.message("Explorer restarted successfully.")
        except Exception as e:
            ui.message(f"Error restarting Explorer: {str(e)}")