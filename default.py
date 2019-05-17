
import subprocess
import xbmc
import xbmcaddon

class Monitor(xbmc.Monitor):

   def __init__(self, *args, **kwargs):
      xbmc.Monitor.__init__(self)
      self.id = xbmcaddon.Addon().getAddonInfo('id')
      E_CODE_ = xbmcaddon.Addon().getSetting('E_CODE')
      if E_CODE_ == "code":
         xbmcaddon.Addon().openSettings('id')

   def onSettingsChanged(self):
      subprocess.call(['systemctl', 'restart', self.id])

if __name__ == '__main__':
   Monitor().waitForAbort()
