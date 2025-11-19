
import math
from IPython.display import display, Markdown
import ipywidgets as widgets

# Baseline constant used across notebook
base_factor = 2  # -> used by Cell 2 to generate the base data series

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

exponent_slider = widgets.FloatSlider(
    value=1.0,
    min=0.5,
    max=3.0,
    step=0.1,
    description='Exponent:',
    continuous_update=True,
)

exp_md_output = widgets.Output()

def update_exponent_md(change=None):
    exp = exponent_slider.value
    transformed = [round(x ** exp, 3) for x in base_series]

    md_text = f"""
# Exponent Slider Summary

**Exponent:** `{exp}`

**Transformed series (base_series^exponent):** `{transformed}`

**Max value:** `{max(transformed)}`
"""

    with exp_md_output:
        exp_md_output.clear_output()
        display(Markdown(md_text))

exponent_slider.observe(update_exponent_md, names='value')
update_exponent_md()

display(widgets.VBox([exponent_slider, exp_md_output]))

# End of notebook
