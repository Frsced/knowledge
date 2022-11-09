# Basics
## Requirement Criterias
1. (Written in English)
2. Comprehensibly in Engineering Language
3. Clear and unambiguously
4. Atomic, complete, consistent and correct
5. Express the quantity (where appropriate)
6. Generic parameters instead of numbered values -> When the parameter is customer related the generic parameters is prefered. Otherwise, the numbered values is tolered. For example due to a standard requirement (i.e. Intensity of the magnetic field because of pacemaker owner)

## Requirement Properties
1. Interdependancies -> With other requirement such as system or safety ones
2. Technical Feasability
3. Project Feasability
4. Verifiability -> "Testable" or "not Testable" -> **This is an essential property of system requirements**
5. Impact
6. Safety -> related to Hazard Analysis and Risk Analysis (HARA)
7. Cyber Security -> related to Thread Analysis and Risk Assessment (TARA)
9. Risk Identification

## Requirement Types
1. Functional : Th function that the system shall execute
2. Non-functional : the requirements that act as constraints
3. Safety : technical safety requirement (TSR) and architecture derived from the functional safety requirements (FSR) and the HARA
4. Security : security requirements derived from the FSR and the TARA

## Requirement Priorities
1. Mandatory / Must have / shall
2. Highly desirable / should have / should
3. Optional / nice to have / can

## Requirement Implementation Groups
- System Engineering
- SW
- HW
- Mechanical 
- Testing
- Functional Safety
- Production
- Logistics
- Quality
- Project Management

## Requirements Links
There are three main requirement links : 
1. Fullfillement link
2. Allocation link 
3. Verification link

# Requirements Concept
## Requirement Elicitation
Considered as the first step of the requirement redefinition. Requirement Elicitation are constitute by :
- Internal Requirement -> From the company
- External Requirement -> From the customer
- Relevant document -> Based on the system purpose such as the standards and so on. 


## System Requirements Analysis
This step converts the high-level requirements (Requirement Elicitation) into 
- system's functions (functional requirements)
- system's capabilities (non-functional requirements)

## System Architectural Design
This step :
- Establish a detailed system architecture
- Identify the allocation between system requirements and system's element (system requirement -> system's element)

**Functional Requirement** <- Allocate <- **System Architectural Design** <- verified <- **System Integration Tests**

System Architectural Design contains
- System Elements (High-level elements required to achieve all system's functions) -> The elements are divided into two families : First level Elements (They have a functionality in the system) and the Sensing Elements (They have no specific functionality in the system instead of capturing data)
- Dynamic Behavior (Interaction between the separate internal elements) -> a dynamic behavior element shall always be a children to a first level or sensing element.
- Hardware Software Interface (HSI)

the design follows (approximatively) the ["Arcadia Method"](https://www.eclipse.org/capella/arcadia.html) : 
1. Operational analysis -> Use cases
2. Functional & Non-functional Analysis -> System Environment Definition & Functional Architecture Allocation
3. Logical Architecture -> High-level system elements & interfaces
4. Physical Architecture -> Dedicated to the specific domain (HW/SW/MEC)

The attributes of the System Architectural Elements are the following : 
- Architectural Element Type
- Verification Criteria* 
	- Stage of Testing
	- Verification Environment)
- Comment from External Supplier
- Status from External Supplier
- BRUSA Comment to External Supplier
- BRUSA Status to External Supplier
- Functional Area (covers variant handling for CPM, GPM)
- Variant Handling 
	- Variant Z-Height
	- Variant AC phases

## System Testing (System Integration and Integration Test)
**Purpose** : Test the system architecture design -> Ensure the compliance if the integrated systme items with the system architectural design. 
**Inclusion** : "How to test the architecture of the system in detailed level"

