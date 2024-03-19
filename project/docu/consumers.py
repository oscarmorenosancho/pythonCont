from channels.generic.websocket import AsyncWebsocketConsumer
import json

class JoinAndLeave(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("server says connected")
        self.group_name = 'alltoghether'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'channel_msg',
                    'msg': "Server sends Welcome to channel"
                }
            )

    async def receive(self, text_data=None, bytes_data=None):
        print("server says client message received: ", text_data)

    async def channel_msg(self, event):
        msg = event['msg']
        await self.send(text_data = json.dumps ({
            'msg': msg 
        }))

    async def disconnect(self, code):
        await self.channel_layer.group_send(
                self.group_name,
                {
                    'type': 'channel_msg',
                    'msg': "Server sends Goodbye to channel"
                }
            )
        await self.channel_layer.group_discard(
            self.group_name,
            'alltoghether'
        )
        print("server says disconnected")