from yarl import URL
from aiohttp import web

from .views import check_name, what_time_is_it, fibonacci_sequence, dict_update


def setup_routes(app: web.Application) -> None:
    """Setup routes for application."""
    # API
    base = URL("/api/v1")

    app.router.add_view(to_path(base / "names" / "{name}"), check_name.CheckNameView)
    app.router.add_view(to_path(base / "whatTimeIsIt"), what_time_is_it.WhatTimeIsItView)
    app.router.add_view(to_path(base / "how-to-fibo"), fibonacci_sequence.FibonacciSequenceView)
    app.router.add_view(to_path(base / "lets_dict"), dict_update.DictUpdateView)


def to_path(url: URL, *, has_trailing_slash: bool = True) -> str:
    """
    Convert URL instance into string path, suitable for aiohttp.web router.

    When `has_trailing_slash` is `True` - append trailing slash for URL, if it not
    already appended.
    """
    # Do not append trailing slash if it already added
    if url.parts[-1]:
        url = url / "" if has_trailing_slash else url
    return url.human_repr()
