# Characteristic Impedance
## Short Definition
(From [Wikipedia](https://en.wikipedia.org/wiki/Characteristic_impedance)) -> The characteristic impedance of a uniform transmission line is the ratio of the amplitude of voltage and current of a single wave propagating along the line. 

(From [Engineering LibreTexts](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Book%3A_Electromagnetics_I_(Ellingson)/03%3A_Transmission_Lines/3.07%3A_Characteristic_Impedance) ) -> Characteristic impedance is the ratio of voltage to current for a wave that is propagating in single direction on a transmission line.
 
The characteristic impedance is determined by the geometry and material of the transmission line. A uniform line is not dependant on its length.

## Mathematics Basics
From [3.9: Lossless and Low-Loss Transmission Lines - Engineering LibreTexts](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Book%3A_Electromagnetics_I_(Ellingson)/03%3A_Transmission_Lines/3.09%3A__Lossless_and_Low-Loss_Transmission_Lines)

The general equation is given as follows :
$$
\begin{flalign}
Z_0 &= \sqrt{\frac{R + j \omega L}{G + j \omega C}} &
\end{flalign}
$$

Often the loss in the transmission line is small that can be neglected. Given the usage of a transmission line at a high frequency and the $R$ and $G$ correspond to the loss component, the following simplification can be done

$$
\begin{flalign}
R & << \omega L &\\
G & << \omega C &\\
Z_0 (@ \omega \rightarrow \infty) &= \sqrt{\frac{L}{C}} &
\end{flalign}
$$

Given the following formula : 
$$
\begin{flalign}
L & = \frac{\mu_0}{2 \pi} ln\left( \frac{b}{a} \right) &\\
C & = \frac{2 \pi \epsilon_s}{ln\left(\frac{b}{a} \right)} &\\
\end{flalign}
$$
The characteristic impedance is not dependant of the transmission line length.

**Parameters** | **Defintion** | **Unit** | **Definition**
--- | --- | --- | ---
$Z_0$ | Characteristic Impedance | [$\Omega$] |
$R$ | Resistance of the conductor| [$\Omega$] |
$G$ | Conductance (assumed very small) | [?] |
$L$ | Cable inductance | [H] |
$C$ | Cable capacitance | [F] |
$\omega$ | Pulsation | [rad/s ?] | $\omega = 2 \pi f$
$f$ | Frequency | [Hz] |
$\mu_0$ | Dielectric material permeability | [H/m] | $\mu_0 = 4 \pi x 10^{-7} H/m$ 
$\epsilon_s$ | Specific permittivity | [S/m] |
a | Inner conductor radius | [m] | 
b | Outter conductor radius | [m] |


![[cutCoaxialCable.png | 300]]


### Example with coaxial line
Calculation of the characteristic impedance from [3.10: Coaxial Line - Engineering LibreTexts](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Electro-Optics/Book%3A_Electromagnetics_I_(Ellingson)/03%3A_Transmission_Lines/3.10%3A__Coaxial_Line)


