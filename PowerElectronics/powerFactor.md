# Power Factor (PF)
## Short Definition 
(From: [Wikipedia](https://en.wikipedia.org/wiki/Power_factor)) -> The Power Factor of an [AC power](https://en.wikipedia.org/wiki/AC_power "AC power") system is defined as the ratio of the _[real power](https://en.wikipedia.org/wiki/Real_power "Real power")_ absorbed by the load to the _[apparent power](https://en.wikipedia.org/wiki/Apparent_power "Apparent power")_ flowing in the circuit. 

*The PF is the ratio between the real and apparent power. It manifest when a circuit has inductive or capacitive components in AC. More the PF is high, better the power performance of the system.*

## Mathematical definition
(From: [Wikipedia](https://en.wikipedia.org/wiki/Power_factor))
$$
\begin{flalign}
PF & = \frac{P}{Pa} &\\ 
P_a & = I_{rms} \cdot V_{rms}
\end{flalign}
$$

**Parameters** | **Defintion** | **Unit**
--- | --- | ---
$PF$ | Power Factor | [-]
$P$ | Real Power (measured with wattmeters) | [W]
$S$ | Apparent Power | [VA]
$I_{rms}$ | RMS Current (measured with amperemeters) | [A]
$V_{rms}$ | RMS Voltage (measured with voltmeters) | [V]

## Graphical Representations
The apparent power is composed of two different powers :
- The Real Power P which is the real part of the apparent power
- The Reactive Power Q which is the imaginary part of the apparent power

The *Power Triangle* is the representation of these power in a vector space.
![[powerTriangle.png]]
There are two type of power factor :
1. *Lagging PF* : current is advanced in phase with respect to voltage -> Consume reactive power : $Q > 0$ -> Load is inductive
2. *Leading PF* : voltage is advanced in phase with respect to current -> Supply reactive power : $Q < 0$ -> Load is capacitve

**Mathematic description**
$$
\begin{flalign}
S &= P + jQ &\\
|S| &= \sqrt{P^2 + Q^2} &\\
PF &= cos \theta = \frac{P}{|S|} = cos\left( arctan\left(\frac{Q}{P}\right)\right) &\\
Q &= P \cdot tan(arccos(PF))
\end{flalign}
$$

**Parameters** | **Defintion** | **Unit**
--- | --- | ---
$PF$ | Power Factor | [-]
$P$ | Real Power (measured with wattmeters) | [W]
$S$ | Apparent Power | [VA]
$Q$ | Reactive Power | [var]


# Power Factor Correction (PFC)
## Short definition
(From: [PFC Tutorial](https://www.electronics-tutorials.ws/accircuits/power-factor-correction.html)) -> PFC is a technique which uses capacitors or inductances in order to reduce or increase the reactive power respectively.

The objective is to set the PF as close as possible to 1 (for a power delivery device). This allows to reduce the loss and improve voltage regulation at the load ([Power factor - Wikipedia](https://en.wikipedia.org/wiki/Power_factor)). 


Check this link, some good explanation.
https://www.monolithicpower.com/en/power-factor-correction