import websockets
import asyncio
import base64

# /home/jinalubuntu/opencv/opencv/files/FrontFace.jpg
# /home/jinalubuntu/WebScraping/google-images-download/images/flow-chart.png

async def receiving_img(websocket, path):
    base64_str = await websocket.recv()
    print(f"> {base64_str}")

    imgdata = base64.b64decode(base64_str)
    count = 0
    filename = f'images/img{count}.jpg'
    print(filename)
    with open(filename , 'wb+') as img:
        img.write(imgdata)
        img.close()
    count += 1
    print(count)
    greeting = f"Done!"

    await websocket.send(greeting)
    print(f"< {greeting}")


start_server = websockets.serve(receiving_img, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()