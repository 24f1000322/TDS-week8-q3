# 24f1000322@ds.study.iitm.ac.in
# Marimo-style notebook (provided as a Python script with notebook cell markers)
# Email above is included as a comment as requested.

# %%
# Cell 1 — Imports and base variables
# Data flow: This cell defines the baseline data and constants used by downstream cells.
# Any change here (e.g., base_factor) will affect the derived data in Cell 2 and the UI behaviors.
import math
from IPython.display import display, Markdown
import ipywidgets as widgets

# Baseline constant used across notebook
base_factor = 2  # -> used by Cell 2 to generate the base data series

# %%
# Cell 2 — Derived data dependent on Cell 1
# Data flow: This cell reads `base_factor` from Cell 1 and constructs `base_series`.
# If `base_factor` changes (re-run Cell 1 + this cell), the `base_series` will change.
N = 11
base_series = [base_factor * i for i in range(N)]

# A small helper that depends on base_series and a runtime multiplier (from the slider in Cell 3)
def compute_scaled_series(multiplier):
    """Compute a scaled version of base_series using an external multiplier.
    Inputs:
      - base_series: derived from Cell 2 (depends on base_factor from Cell 1)
      - multiplier: controlled interactively from Cell 3 (slider)
    Output:
      - scaled list used for plotting / markdown summaries in Cell 3
    """
    return [round(x * multiplier, 3) for x in base_series]

# %%
# Cell 3 — Interactive slider widget and dynamic markdown output
# Data flow: This cell depends on Device/outputs from previous cells. It reads `base_series`
# (created in Cell 2) and calls `compute_scaled_series(multiplier)` which uses `base_series`.
# When the slider changes, the markdown display below updates to reflect the new state.

# Create an interactive slider widget
multiplier_slider = widgets.FloatSlider(
    value=1.0,
    min=0.0,
    max=5.0,
    step=0.1,
    description='Multiplier:',
    continuous_update=True,
)

# Output area for dynamic markdown
md_output = widgets.Output()

# A function that produces dynamic markdown based on widget state
def update_markdown(change=None):
    # Read current multiplier from the slider
    m = multiplier_slider.value
    scaled = compute_scaled_series(m)  # depends on base_series defined in Cell 2

    # Build a markdown string summarizing the results
    md_text = f"""
# Dynamic Summary (live)

**Multiplier:** `{m}`

**Base factor (from Cell 1):** `{base_factor}`

**Base series (Cell 2):** `{base_series}`

**Scaled series (computed):** `{scaled}`

**Mean of scaled series:** `{round(sum(scaled)/len(scaled), 3)}`

> Note: changing `base_factor` in Cell 1 and re-running Cell 2 will change the base series, which
> will in turn change this dynamic summary when the slider is moved or `update_markdown()` is called.
"""

    # Render the markdown into the output widget
    with md_output:
        md_output.clear_output()
        display(Markdown(md_text))

# Wire up the slider to call update_markdown when its value changes
multiplier_slider.observe(update_markdown, names='value')

# Initial render
update_markdown()

# Display the interactive UI
ui = widgets.VBox([multiplier_slider, md_output])
display(ui)

# %%
# Cell 4 — Example: programmatic change to base_factor to demonstrate variable dependency
# Data flow: This cell illustrates how modifying upstream variables affects downstream outputs.
# If you change base_factor here and then re-run Cell 2 and Cell 3, you'll see updated results.

# Example change (comment/uncomment to test):
# base_factor = 3
# After changing `base_factor` re-run Cell 2 and then re-run Cell 3 to refresh the UI results.

# End of notebook
