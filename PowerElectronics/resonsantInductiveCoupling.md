# Resonsant Inductive Coupling
Capacitor is added to each induction coil to create LC circuit with a specific resonance frequency.

**TBD**

## Resonant Frequency

### Short Definition
(From [cadence.com](https://resources.pcb.cadence.com/blog/2021-what-is-resonant-frequency)) -> Resonant frequency (in electronic) is expressed when circuit exhibits a maximum oscillatory response at a specific frequency. This kind of effect occurs with inductive and capacitive circuit. 

*Note : An object has a resonant frequency called "natural frequency"*

## Mathematics Basics
The reactance of an inductance and capacitance is calculated as follows :
$$
\begin{flalign}
X_L &= 2 \pi f L & \\
X_C &= \frac{1}{2 \pi f C}
\end{flalign}
$$
The resonant frequency between two components (in this example between an inductance and a capacitance) is found as follows :
$$
\begin{flalign}
f_R &= f \left(@ X_L = X_C  \right) &
\end{flalign}
$$

**Parameters** | **Defintion** | **Unit** | **Definition**
--- | --- | --- | ---
$X_L$ | Inductive Reactance | [$\Omega$] |
$X_C$ | Capacitive Reactance | [$\Omega$] |
$f$ | Frequency | [Hz] |
$L$ | Inductance | [H] |
$C$ | Capacitance | [F] |
$f_R$ | Resonant frequency | [Hz] |

### Example with RLC serial circuit
Based on the formulas presented above, the reactance of component such as capacity and inducance can be calculated over a frequency range. The resonant frequency for the selected component is where is curve intersected. 

In this example, $R = 100\Omega$, $L = 100\mu H$ and $C = 10nF$. Consequently, the resonant frequency and reactance are $159.154 kHz$ and $100\Omega$ respectively. This point is marked with the red dot in the graph below.

![[LCReactance.png | 500]]

Using LTC Spice, the circuit can be simulated easily at different frequency with a voltage amplitude of 10.

##### 1st case : $f = f_R$ 
$@f = f_R = 159.154kHz$
![[RLCat160kHz.png]]

In this first case : 
$î = 100mA$

The current analysis can be done as follow :
$$
\begin{flalign}
X_e &= X_R + X_L + X_C & \\
X_R &= R = 100 \Omega & \\
X_L &= 2 \pi f \cdot L = 100 \Omega & \\
X_C &= \frac{1}{2 \pi f \cdot C} = 100 \Omega & \\
& \\
X_e &= 100 \Omega & \\
î & = \frac{V}{|X_e|} = \frac{10}{100} = 100mA
\end{flalign}
$$


***TODO** : Add phase explanation*

##### 2nd case : $f << f_R$ 
$@f = 10kHz$
![[RLCat10kHz.png]]

In this second case : 
$î = 6.3mA$

The current analysis can be done as follow :
$$
\begin{flalign}
X_e &= X_R + X_L - X_C & \\
X_R &= R = 100 \Omega & \\
X_L &= 2 \pi f \cdot L = 6.25 \Omega & \\
X_C &= \frac{1}{2 \pi f \cdot C} = 1.6k\Omega & \\
& \\
X_e & -1680 \Omega & \\
î & = \frac{V}{|X_e|} = \frac{10}{1680} = 5.9mA
\end{flalign}
$$

***TODO** : Add phase explanation*