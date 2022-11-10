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


