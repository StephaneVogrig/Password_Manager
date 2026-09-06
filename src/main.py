import sys
import logging

from app import App
from gui import Gui

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

def main() -> int:
    argv = sys.argv
    argc = len(argv)

    if argc > 2:
        print("Usage: password_manager [file]", file=sys.stderr)
        return 1

    try:
        app = App(filepath=argv[1] if argc == 2 else None)
        gui = Gui(app=app)
        gui.mainloop()
    except Exception:
        logger.exception("Une erreur inattendue est survenue")
        return 1

    logger.info("script terminé avec succès")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
