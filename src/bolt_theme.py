import matplotlib as mpl
import matplotlib.font_manager as fm
from matplotlib.colors import LinearSegmentedColormap

# Official Bolt brand colors from guidelines
BOLT_GREEN        = '#2A9C64'
BOLT_DARK_GREEN   = '#0C2C1C'
BOLT_ACCENT_GREEN = '#74EFAA'
BOLT_WHITE        = '#FFFFFF'
BOLT_BLACK        = '#000000'


def apply_bolt_theme():
    preferred_fonts = ['Inter', 'Helvetica Neue', 'Helvetica', 'Arial', 'DejaVu Sans']
    available = [f.name for f in fm.fontManager.ttflist]
    chosen_font = next((f for f in preferred_fonts if f in available), 'DejaVu Sans')

    mpl.rcParams.update({
        'figure.facecolor':   BOLT_WHITE,
        'axes.facecolor':     BOLT_WHITE,
        'savefig.facecolor':  BOLT_WHITE,
        'axes.edgecolor':     '#E0E0E0',
        'axes.labelcolor':    BOLT_BLACK,
        'axes.titlecolor':    BOLT_DARK_GREEN,
        'axes.titlesize':     14,
        'axes.titleweight':   'semibold',
        'axes.labelsize':     11,
        'axes.titlepad':      16,
        'axes.spines.top':    False,
        'axes.spines.right':  False,
        'xtick.color':        BOLT_BLACK,
        'ytick.color':        BOLT_BLACK,
        'xtick.labelsize':    9,
        'ytick.labelsize':    9,
        'axes.grid':          True,
        'grid.color':         '#EEEEEE',
        'grid.linestyle':     '--',
        'grid.linewidth':     0.6,
        'text.color':         BOLT_BLACK,
        'font.family':        chosen_font,
        'font.weight':        'medium',
        'legend.facecolor':   BOLT_WHITE,
        'legend.edgecolor':   '#E0E0E0',
        'legend.labelcolor':  BOLT_BLACK,
        'legend.fontsize':    9,
        'figure.titlesize':   16,
        'figure.titleweight': 'semibold',
        'figure.dpi':         130,
    })


def get_bolt_cmap():
    return LinearSegmentedColormap.from_list(
        'bolt_light',
        [BOLT_WHITE, BOLT_ACCENT_GREEN, BOLT_GREEN, BOLT_DARK_GREEN]
    )