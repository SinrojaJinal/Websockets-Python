import websockets
import asyncio
import base64

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        img_path = input("What's your img_path? ")
        print(f"< {img_path}")

        with open(img_path , 'rb') as img:
            base64_str = base64.b64encode(img.read())

        await websocket.send(base64_str)
        
        greeting = await websocket.recv()
        print(f"> {greeting}")

asyncio.get_event_loop().run_until_complete(hello())