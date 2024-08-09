"""API server entry point."""

import logging
import os
from pathlib import Path

from connexion import FlaskApp  # type: ignore
from dotenv import load_dotenv  # type: ignore
from foca import Foca

load_dotenv()
logger = logging.getLogger(__name__)


def init_app() -> FlaskApp:
    """Initialize and return the FOCA app.

    This function initializes the FOCA app by loading the configuration
    from the environment variable `TUS_FOCA_CONFIG_PATH` if set, or from
    the default path if not. It raises a `FileNotFoundError` if the
    configuration file is not found.

    Returns:
        A Connexion application instance.

    Raises:
        FileNotFoundError: If the configuration file is not found.
    """
    # Determine the configuration path
    config_path_env1 = os.getenv("TUS_FOCA_CONFIG_PATH")
    print(config_path_env1)
    if config_path_env := os.getenv("TUS_FOCA_CONFIG_PATH"):
        print(config_path_env)
        config_path = Path(config_path_env).resolve()
    else:
        config_path = (
            Path(__file__).parents[1] / "deployment" / "config.yaml"
        ).resolve()

    # Check if the configuration file exists
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found at: {config_path}")

    foca = Foca(
        config_file=config_path,
    )
    return foca.create_app()


def main() -> None:
    """Run FOCA application."""
    app = init_app()
    app.run(port=app.port)


if __name__ == "__main__":
    main()
