#!venv/bin/python
from pathlib import Path

import argparse
import asyncio
import logging

from aiohttp import web

from api.app import create_app
from api.settings import load_config

try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    logging.warning("Uvloop is not available")


parser = argparse.ArgumentParser(
    description="Simple Aiohttp server",
    formatter_class=argparse.RawDescriptionHelpFormatter,
)
parser.add_argument("--host", help="Host to listen")
parser.add_argument("--port", help="Port to accept connections")
parser.add_argument(
    "--reload",
    action="store_true",
    help="Reload server when code is changed. For development purposes",
)
parser.add_argument(
    "-c",
    "--config",
    dest="config_file",
    help="Path to configuration file",
)

args = parser.parse_args()
config = load_config(path=Path(args.config_file).parent, custom_config=args.config_file)

# Autoreload
if args.reload:
    import aioreloader

    aioreloader.start()


if __name__ == "__main__":
    # print(args.config_file)
    # print('final', config)
    app = create_app(config=config)
    web.run_app(
        app=app,
        host=config.get("host", args.host),
        port=config.get("port", args.port),
    )
