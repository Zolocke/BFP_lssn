import sys
from pathlib import Path

_PARENT = Path(__file__).resolve().parent.parent
if str(_PARENT) not in sys.path:
    sys.path.insert(0, str(_PARENT))

from backend_flask_project import create_app

app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
