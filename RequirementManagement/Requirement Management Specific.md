## Requirement Affectation Groups
- CPM (Car Pad Module) -> Requirements that only affect the CPM
- GPM (Ground Pad Module) -> Requirements that only affect the GPM
- CPM and GPM -> Requirements that affect the whole ICS2 system

## Requirement Scope Variant
There are two aspects on which the system is affected by the variant management, the mains supply of the GPM and the z-height corresponding the to distance between the GPM and the CPM. this distance is directly related to the chassis type. 
- Mains supply
	- AC phase not relevant
	- Single-phase
	- Three-phase
- Z-height
	- Z-height not relevant : independant of this height
	- Z1 : the smallest height
	- Z1+
	- Z2
	- Z2+
	- Z3 : the highest height

## Requirement's Attributes
- Requirement Type
- ASIL BRUSA
- SIL BRUSA
- Cybersecurity Assurance Level
- Verification Criteria (consisting of
	- Stage of Testing
	- Verification Method
	- Verification Environment
	- Pre-Conditions
	- Pass Fail Criteria
- Comment from External Supplier
- Status from External Supplier
- BRUSA Comment to External Supplier
- BRUSA Status to External Supplier
- Functional Area (covers variant handling for CPM, GPM, see chapter 4.7.2)
- Variant Handling (currently implemented are
	- Variant Z-Height
	- Variant AC phases)
- Allocates to SYS.3 Element (Architecture allocation)
- Categories
- Target System Release

