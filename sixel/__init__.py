from .sixel import *

import matplotlib
import matplotlib.pyplot as plt

plt.rcParams.validate.update([('sixel.transparent', matplotlib.rcsetup.validate_bool)])
plt.rcParams.validate.update([('sixel.colors', matplotlib.rcsetup.validate_int)])
