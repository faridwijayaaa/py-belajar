import skfuzzy as fuzz
import numpy as np

x = np.range(11)
mfx = fuzz.trimf(x, [0, 5, 10])
