import os
from typing import TYPE_CHECKING

from jinja2.ext import Extension

if TYPE_CHECKING:
    from jinja2 import Environment


class EnvExtension(Extension):
    """Jinja2 Extension for environment variables."""

    def __init__(self, environment: Environment) -> None:
        """Jinja2 Extension constructor."""
        super().__init__(environment)

        def env(name: str, default: str | None = None) -> str | None:
            """Fetch environment variable by name with an optional default."""
            return os.environ.get(name, default)

        environment.globals.update(env=env)
