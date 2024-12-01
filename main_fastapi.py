#!/usr/bin/env -S uv run


from threading import Thread


from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from uvicorn import Config, Server
from typing import ClassVar
from heap_view import HeapView


class Main:

    def __init__(self) -> None:
        self.app: FastAPI = FastAPI()
        self.app.add_api_route("/", self.home)
        self.app.add_api_route("/heap", self.heap)

    async def home(self) -> PlainTextResponse:
        result = "asdf\n"
        return PlainTextResponse(result)

    async def heap(self) -> PlainTextResponse:
        result = HeapView.get_heap_view()
        return PlainTextResponse(result)

    @staticmethod
    def start_uvicorn():
        config = Config(
            Main().app,
            host="0.0.0.0",
            port=8000,
        )
        server = Server(config)
        server.run()


if __name__ == "__main__":

    Thread(target=Main.start_uvicorn).start()
