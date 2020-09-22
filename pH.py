#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Points de mesure
c, pH = ([0.1, 0.05, 0.01, 0.005, 0.001, 0.0001], [1.68, 1.92, 2.22, 2.6, 3.02, 3.65])# A remplir
# Trace du modele
cth = np.arange(1e-4, 1, 0.0001)
pHth = -np.log10(cth)

plt.xlabel('Concentration en quantite de matiere c (mol/L)')
plt.ylabel('pH de la solution')
plt.title('Evolution du pH en fonction de la concentration en ion H3O+')
plt.plot(cth, pHth, color='red', label='Modelisation')
plt.scatter(x=c, y=pH, marker='+', label='Mesures')
plt.legend()
plt.show()