import os
import signal
import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

# async def main():
#     async with websockets.serve(echo, "localhost", 8765):
#         await asyncio.Future()  # run forever

async def main():
    # Set the stop condition when receiving SIGTERM.
    loop = asyncio.get_running_loop()
    stop = loop.create_future()
    loop.add_signal_handler(signal.SIGTERM, stop.set_result, None)

    port = int(os.environ.get("PORT", "8001"))
    async with websockets.serve(echo, "", port):
        await stop

asyncio.run(main())