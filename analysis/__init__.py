import constants
from pathlib import Path
from typing import List, Tuple
from matplotlib.figure import Figure

class AnalysisBase:
    def __init__(self):
        self.data_frame = constants.data_frame
        self.output_directory = constants.output_directory
        self.plots: List[Tuple[Path, Figure]] = []

    def save_plots(self):
        for path, figure in self.plots:
            # Ensure the directory exists
            path.parent.mkdir(parents=True, exist_ok=True)
            
            figure.savefig(path, bbox_inches="tight")
            print(f"Saved plot to: {path}")

        self.plots = []
        return self

## While importing inside a package
## modules should be prefixed with a dot (.)
## so they are relative-path'd.

from .counts import *
from .power_levels import *
from .stats import *