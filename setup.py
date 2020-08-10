# -*- coding: utf-8 -*-

import os
from pathlib import Path

try:
    from orbis_eval.core.orbis_setup import OrbisSetupBaseClass
    OrbisSetupBaseClass().run(Path(__file__).parent)
except Exception as exception:
    print("Orbis not found. Please install Orbis first.")
    print(f"({exception})")

