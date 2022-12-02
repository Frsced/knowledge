# Inductive Charging
## Short Definition
(From [Wikipedia](https://en.wikipedia.org/wiki/Inductive_charging)) -> Inductive charging is a type of wireless power transfer which uses electromagnetic induction to provide electricity to portable devices. 

## Concept
### Power Transmission
The concept of inductive chaging is presented in the figure below : 

![[inductiveChargingConcept.png]]

### Transmission Distance
The distance between the charging and portable station can differ in the application. In order to increase the distance between devices, the ["resonant inductive coupling"](resonsantInductiveCoupling)  shall be used.

## Wireless Power Transfert (WPT)
### Short Definition
(From [Wikipedia](https://en.wikipedia.org/wiki/Wireless_power_transfer)) -> Transmission of electrical energy without wires as a physical link. This is the basic concept of the inductive charging. 

There is two kind of WPT : 
- Near-Field (non-radiative technique over short distance) : transfer by magnetic fields using inductive coupling between coils of wire (inductive coupling) or electric field (capacitive coupling). The first one is most widely used in wireless technology. Example of use : phone, electric toothbrushes, RFID, induction cooking, ... 
- Far-Field (radiative technique, power beaming) : transfer by beams of electromagnetic radiation (microwaves or laser beams). Used over longer distance but must be aimed at the receiver. Example of use : solar power satellites and wireless powered drone aircraft.

### Mathematics Basics
**Ampere's law** (Ampere's circuital law) relates the magnetic field around a closed loop to the electric current passing through this loop (and inversely). (From [Ampere's Law: Definition, Equation, and Application (sciencefacts.net)](https://www.sciencefacts.net/amperes-law.html) )

The basic formula is expressed as follows :
$$
\begin{flalign}
\oint \overrightarrow{B} \cdot \overrightarrow{dl} &= \mu_0 \cdot I &
\end{flalign}
$$
**TBD** : meaning of surface integrale

In the most case the equation is simplified by the following (because $\overrightarrow{B}$ and $\overrightarrow{dl}$ are in the same direction) : 
$B \cdot l = \mu_0 \cdot I$

For a strainght wire, the field turns around the wire and traces a circle, then :
$l = 2\pi r$
$B(2\pi r) = \mu_0 I \implies B = \frac{\mu_0 I}{2 \pi r}$

**Faraday's law**


**Parameters** | **Defintion** | **Unit** | **Definition**
--- | --- | --- | ---
$I$ | Electric current | [$A$] |
$B$ | Magnetic field | [$T$] |
$\mu_0$ | Permeability of free space | [H/m] | $4 \pi \cdot 10^{-7} H/m$
$J$ | Current Density | [?] |
l | ? | [?] | 

