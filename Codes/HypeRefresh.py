# ba_meta require api 7

from _ba import chatmessage as msg
import ba
import _ba
import os 


class _use():
    
    def _home():
        messages = _ba.get_chat_messages()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            if c.startswith('/'):
                return _use.refresh()
            else:
                pass
            
            
            
            
    def refresh():
        
        messages = _ba.get_chat_messages()
        if len(messages)>1:
            lmsg = messages[len(messages)-1]
            
            c = lmsg.split(' ')[1]
            a = lmsg.split(' ')[2:]
            
            if c in ['/ref', '/refresh]:
                msg("Server Refreshing Mods!, Enter In one minute.")
                
                
                
                
def refr():
    ba.timer(0.3, _use._home, True)

# ba_meta export plugin

class TimerCmd(ba.Plugin):
    """My awesome plugin."""
    ba.internal.set_party_icon_always_visible(True)
    refr()   