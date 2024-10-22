"""
A module implementing a simple web application.
"""

# built-in
from pathlib import Path
from typing import Optional

# third-party
from runtimepy.net.arbiter.info import AppInfo
from runtimepy.net.html import append_kind
from runtimepy.net.http.header import RequestHeader
from runtimepy.net.http.response import ResponseHeader
from runtimepy.net.server import RuntimepyServerConnection
from svgen.element import Element
from svgen.element.html import Html, div
from vcorelib.asyncio.cli import run_command


def script(path: Path | str, is_async: bool = True) -> Element:
    """Create a script element."""

    elem = Element(tag="script", src=str(path), text="/* null */")
    if is_async:
        elem.booleans.add("async")
    return elem


async def build_app(app: AppInfo, is_async: bool = True) -> Element:
    """Build the application."""

    app_path = Path(
        "build", "wasm", "apps", app.config_param("wasm_app", "", strict=True)
    )

    # Run ninja to re-build.
    await run_command(app.logger, "ninja", str(app_path.with_suffix(".html")))

    return script(app_path.with_suffix(".js"), is_async=is_async)


async def setup(app: AppInfo) -> int:
    """Perform server application setup steps."""

    del app

    async def main(
        document: Html,
        request: RequestHeader,
        response: ResponseHeader,
        request_data: Optional[bytes],
    ) -> Html:
        """A simple 'Hello, world!' application."""

        # Not currently used.
        del request
        del response
        del request_data

        # Create the application.
        append_kind(document.head, "main", kind="css", tag="style")

        # Remove at some point.
        div(text="Hello, world!", parent=document.body)

        # Add WebAssembly application.
        # document.body.children.append(await build_app(app))

        document.body.children.append(script("tasks/test.js"))

        return document

    # Set default application.
    RuntimepyServerConnection.default_app = main
    return 0
