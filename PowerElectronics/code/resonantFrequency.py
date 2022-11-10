#!/usr/bin/env python3

__author__ = "Frederic Schenker"
__fileName__ = "resonantFrequency.py"
__copyright__ = "Copyright 2022"
__license__ = "GPL"
__version__ = "1.0.0"
__date__ = "10 Nov. 2022"
__maintainer__ = "Frederic Schenker"
__email__ = "schenker.f@bluewin.ch"
__status__ = "Production"

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

## --- Definition ---
# Parameters
L = 100e-6   # Inductance [H]
C = 10e-9   # Capacitance [F]

f = np.linspace(10e3, 1e6, 100)   # Frequency array [Hz]

## --- Calculation ---
# Reactance
X_L = 2 * np.pi * f * L          # Inductive reactance
X_C = 1 / (2 * np.pi * f * C)   # Capacitive reactance

# Resonant frequency
f_r = fsolve(lambda x : (2 * np.pi * x * L) - (1 / (2 * np.pi * x * C)), 1)
X = 2 * np.pi * f_r * L

## --- Monitoring ---
# Reactance and Resonant Frequency
plt.plot(f, X_L, label="Inductive Reactance")
plt.plot(f,X_C, label="Capacitive Reactance")
plt.plot(f_r, X, 'ro', label="Resonant Point")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Reactance (Ohm)")
plt.legend()
plt.grid()
plt.show()