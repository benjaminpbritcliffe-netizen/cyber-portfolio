
# Key Cyber Security Standards and Frameworks

NIST: The "Global Library" of ideas (mostly used by big US firms).

ISO: The "Gold Standard" for UK/EU businesses.

FISMA: The US Law (you just have to memorize this for the marks!).

FISMA is the Building Law:
It says, "By law, your house must be safe, or you’ll be fined/shut down."

NIST is the Blueprint:
It is the book of instructions that tells you how to make the house safe
(e.g., "use these specific locks").

ISO is the Inspector's Plaque:
It's the sign you hang on the door,
to show everyone the house passed an international inspection.

Summary Cheat Sheet for your Revision:

Is it a law? Yes (US Federal Law).

Who does it apply to? US Agencies and their Third-party Contractors/Service Providers.

What happens if you fail?
You lose your funding or your government contracts
(Loss of ATO - Authorization to Operate).

What is the goal? To protect "National Security" data.

The Comparison Breakdown

| Term  | Category          | "Cheat Code" for CompTIA                                                                         |
|-------|-------------------|--------------------------------------------------------------------------------------------------|
| NIST  | Framework / Guide | The "Blueprints." It's free advice from the US government on how to build security.              |
| ISO   | Standard          | The "Certificate." It's a global test you pay to take so you can prove you're secure to clients. |
| FISMA | Law / Regulation  | The "Mandate." It is a US law that says government agencies must follow NIST.                    |

## FISMA - Federal Information Security Management Act

The Federal Information Security Management Act (FISMA)
defines a framework of guidelines and security standards,
to protect government information and operations.

FISMA was passed as the Federal Information Security Management Act in 2002
as part of the E-Government Act.

It requires all federal agencies to:

- develop
- document
- and implement agency-wide information security programs.

This law has been amended as of 2014 (sometimes called FISMA Reform),
passed in response to the increasing amount of cyber attacks on the federal government.

FISMA defines three security objectives for information and information systems:

Confidentiality: Preserving authorized restrictions
on information access and disclosure,
including means for protecting personal privacy and proprietary information.

Integrity: Guarding against improper information modification or destruction,
and includes ensuring information nonrepudiation and authenticity.

Availability: Ensuring timely and reliable access to and use of information.

### What FISMA Entails (The "Must-Haves")

In a CompTIA scenario,
if the question mentions a US Government agency,
or a Contractor (like Boeing or Lockheed Martin),
they are talking about FISMA.

FISMA requires these 3 specific things:

#### System Inventory & Categorization

You must list every computer/server you own and rank them by how "dangerous"
it would be if they were hacked (Low, Moderate, or High impact).

Exam Tip: This ranking uses the "High Water Mark" rule.
If a system's Availability is "High" risk but its Confidentiality is "Low,"
the whole system is treated as High Risk.

#### The System Security Plan (SSP)

This is a massive document that explains exactly which security controls
(from the NIST library) you are using to protect those systems.
It’s the "Living Document" of your security.

#### Continuous Monitoring

FISMA is obsessed with the idea that security isn't a one-time check.
You must monitor your systems 24/7/365 and report on their health annually.

### FISMA vs. NIST: The Relationship

This is the most common "trick" on the exam.

FISMA is the Requirement (The "What").

NIST SP 800-53 is the Toolbox (The "How").

## PCI DSS – Payment Card Industry Data Security Standard

The PCI DSS is a globally recognized standard,
designed to secure credit and debit card transactions against data theft and fraud.
Any business handling credit card information must follow the PCI DSS checklist
to secure financial data during processing, transmission, and storage.

## HIPAA – Health Insurance Portability and Accountability Act

HIPAA is a U.S. federal law,
that mandates the protection of sensitive patient health information.
It applies to covered entities such as hospitals, clinics, insurers,
and their business associates, including IT vendors and cloud service providers.
HIPAA ensures that patients' electronic health records (EHRs),
are kept confidential and secure, both in storage and in transit.

## ISO -  International Organization for Standardization

ISO 27001 is an international standard,
published by the International Organization for Standardization (ISO)
that outlines the procedures for establishing, implementing, maintaining,
and continually improving an Information Security Management System (ISMS).
It’s applicable across industries and especially valued by organizations,
looking to demonstrate a proactive approach to data protection.

## NIST - National Institute of Standards and Technology

The NIST Cybersecurity Framework (CSF) provides guidelines, best practices,
and standards to help organizations effectively manage cybersecurity risks.
Though originally designed for critical infrastructure,
it has since been adopted widely across public and private sectors.
Unlike other frameworks, NIST is flexible and voluntary, making it useful for tailoring
to fit an organization's size and risk profile.

### Key Differences to Remember

Certification vs. Alignment
ISO 27001: You can put a badge on your website.
It proves to external partners that you meet a specific international bar.

NIST CSF: You can't be "certified" in NIST. You use it to build a stronger program.
It is often preferred by U.S. federal agencies and their contractors.

Cost and Accessibility
ISO is a private organization; you actually have to buy the PDF of the standards.
Getting certified involves hiring auditors which can cost $10k–$50k+.

NIST is a U.S. government agency (National Institute of Standards and Technology).
Their materials are free and public.

Complexity and Maturity
NIST CSF is widely considered "easier" to start with because it uses plain language,
organized into six functions: Govern, Identify, Protect, Detect, Respond, and Recover.

ISO 27001 is more rigid.
It requires a formal Information Security Management System (ISMS),
 and extensive documentation of processes.

Which one should you choose?
Choose ISO 27001 if you are doing business internationally
or if your clients are demanding a "security certificate" before they sign a contract.

Choose NIST CSF if you are a U.S.-based company,
a startup on a budget,
or just want a flexible framework to help your team prioritize security tasks.

### Examples

Question: A security analyst is tasked with selecting a framework
that provides a globally recognized certification
to demonstrate that the company's Information Security Management System (ISMS)
meets specific requirements.

Which of the following should the analyst choose?

A. NIST CSF

B. ISO 27001

C. NIST SP 800-53

D. CSA CCM

Correct Answer: B. ISO 27001.
Why? Because it mentions certification and ISMS, both of which are specific to ISO.

### Resources

[Invensis]<https://www.invensis.net/blog/key-cybersecurity-standards>
