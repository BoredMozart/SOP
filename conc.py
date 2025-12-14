import numpy as np

w = 500e-6 # width of channel in m

def conc(y, t):
    c0 = 1 # Concentration in mol/m^3
    D = 1.4315e-10 # Diffusion coefficient in m^2/s

    n = 200 # number of terms in series
    i = np.arange(1, n+1)

    # (2i - 1) terms
    m = 2*i-1

    term = (2 * c0 / (m * np.pi)) \
           * np.sin(m * np.pi * y / w) \
           * np.exp(-((m * np.pi / w) ** 2) * D * t)
    
    c = c0 / 2 -np.sum(term, axis=0)

    return c

y = -w / 2 # Position
t = 90 # time in seconds

print(conc(y, t))