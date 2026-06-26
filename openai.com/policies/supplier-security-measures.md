<!-- source: https://openai.com/policies/supplier-security-measures/ -->

Updated: June 23, 2025

# Supplier security measures

These Supplier Security Measures apply to Supplier when it provides goods, services, or software to OpenAI and are incorporated into the applicable agreement between Supplier and OpenAI (the “Agreement”). Terms used here but not defined here are defined in the Agreement.

Supplier will maintain and operate an Information Security Program, which will be reviewed at least annually, or earlier if prompted by a Security Incident or a material change in applicable law. Oversight of the Information Security Program will be assigned to appropriately qualified senior personnel. 

To meet its security and privacy obligations under the Agreement, Supplier’s Information Security Program will include the following:

## 1. Policies and Codes of Conduct

* Maintain written information-security and privacy policies aligned with the Information Security Program and all applicable Data-Protection Laws.
* Communicate these policies and the Supplier Code of Conduct to all relevant personnel and require formal acknowledgement.
* Monitor compliance and remediate non-compliance through documented processes; policy violations will be addressed with appropriate disciplinary action.

## 2. Risk Management

* Maintain and operate a risk management program that includes regular risk assessments and controls for risk identification, analysis, monitoring, reporting, and corrective action.
* At least annually, perform risk assessments (either internally or with contracted, independent resources) to identify risks to OpenAI Data, risks to Supplier’s business assets (e.g., technical infrastructure), threats against those elements (both internal and external), the likelihood of those threats occurring, and the impact upon the organization.
* Triage security risks to OpenAI Data and prioritize their remediation.

## 3. Personnel

* Maintain and operate industry standard practices for vetting, training, and managing personnel.
* Conduct, to the extent legally permissible in each worker’s jurisdiction, pre-employment background screenings for all personnel who will access OpenAI Data or support Supplier’s performance.
* Provide annual security and privacy training for Supplier Personnel, and supplemental security training as appropriate.
* Require Supplier Personnel to execute a confidentiality agreement, or to ensure Supplier Personnel are subject to confidentiality obligations consistent with those Supplier is subject to in connection with its performance for OpenAI, as a condition of employment or engagement and to follow policies on the protection of customer and other third-party data.
* Verify the identity of its employees and contingent workers.
* Not employ or source Supplier Personnel located in any country or territory: (a) designated as comprehensively sanctioned by the U.S. Office of Foreign Assets Control (OFAC); (b) subject to a Level 4/ Do Not Travel advisory by the U.S. State Department; or (c) in regions experiencing active armed conflict.
* Allow OpenAI to perform ad-hoc security checks on Supplier Personnel and promptly share any information OpenAI reasonably requests in support of these checks.
* OpenAI may conduct supplemental security screens for Supplier Personnel who are remote, provided that OpenAI doing so does not limit or exclude Supplier’s obligation to conduct its own background-check and identification verifications under these Security Measures or the Agreement.

## 4. System and Workstation Control

Supplier will secure all corporate laptops, mobile devices, on-premises servers, and other hardware that process OpenAI Data by:

* Centrally managing every endpoint and server—including on-prem infrastructure—through an approved endpoint-management platform.
* Automatically enforcing baseline security configurations and timely patches on operating systems, applications, and firmware across workstations *and* servers.
* Requiring encryption at rest: full-disk encryption on laptops and workstations, and volume or storage-level encryption on servers and storage devices.
* Disabling or strictly controlling portable and removable media on all assets.

## 5. Identity, Authentication, and Authorization Controls

* Maintain and operate industry standard practices for identity, authentication and access-management control.
* Document policies and procedures governing access management for Supplier Personnel and service accounts.
* Maintain an accurate and current list of all Supplier Personnel with Systems access.
* Disable or revoke credentials within one business day of transfer or termination.
* Use single sign-on (SSO) for all interactive logins to internal systems and third-party services that support delivery of the Services.
* Enforce multi-factor authentication by the identity provider as part of the SSO login flow.
* Implement role-based access control (RBAC) with least-privilege and separation-of-duties principles.
* Only use privileged (“root”/“administrator”) accounts when technically required under approved change-control procedures; prohibit non-privileged users from executing privileged functions.
* Require formal review and approval for any access request to systems storing OpenAI Data, plus periodic (at least quarterly) access audits to confirm appropriateness of privileges.
* Establish procedures to report and revoke compromised credentials (e.g., passwords, API keys) and to verify user identity before issuing resets or temporary credentials.
* For OpenAI end-users, reliance on a third-party identity-access-management service; Supplier does not store user-provided passwords.

## 6. Security Incidents

* Maintain and operate a Security Incident response plan for responding to and resolving events that compromise the confidentiality, availability, or integrity of the Supplier’s performance or OpenAI Data.
* Upon becoming aware of an actual or suspected Security Incident, provide written notice without undue delay and, in any case, within 48 hours of becoming aware of the Security Incident. Where possible, such notice will include all available details required under Data Protection Laws for OpenAI to comply with its own notification obligations to regulatory authorities or individuals affected by the Security Incident.
* Take reasonable measures to mitigate the risks of further Security Incidents. Where the Security Incident is due to Supplier’s breach of these Supplier Security Measures, Supplier will reimburse (subject to the limitations of liability included in the Agreement) OpenAI for its actual, out of pocket remediation costs and expenses incurred as a result of actions required to be taken under Data Protection Laws or agreed upon between the parties with respect to a Security Incident, including, where applicable: (i) the creation and transmission of legally required notices to affected individuals; (ii) call center support to respond to inquiries; and (iii) legally required credit monitoring services for affected individuals. OpenAI shall have sole discretion to control the timing, content and manner of any notices provided under this paragraph.

## 7. Logging, Audit, and Accountability

* Create and retain audit records for all systems, networks, and supporting infrastructure used to deliver the Services, enabling monitoring, analysis, investigation, and reporting of unlawful or unauthorized activity.
* Log all privileged actions in a manner that links every event to a named individual.
* Record and continuously monitor privileged activity on endpoints, servers, and supporting infrastructure to detect unauthorized changes or policy violations.
* Continuously monitor security and availability—including network traffic and service logs—and act promptly on any alerts.
* Review and analyze security and operational logs on a regular basis to detect suspicious activity, policy violations, or events that could affect the confidentiality, integrity, or availability of OpenAI Data.
* Provide audit logs to OpenAI upon request.

## 8. Secure Development Lifecycle (SDLC)

* Maintain and operate a documented Secure Development / Security-by-Design process covering planning, coding, testing, deployment, and maintenance of software or services it provides to OpenAI.
* The SDLC must include threat modelling, code review, automated dependency-vulnerability scanning, and security testing (static, dynamic, and container or IaC scanning) before code is promoted to production.
* Results of these activities, along with remediation evidence for high-risk findings, shall be retained for at least 12 months and made available to OpenAI upon request.

## 9. Cloud Infrastructure and Network Security

* Segregate environments—keeping production and non-production environments separate and ensuring OpenAI data only resides in production environments.
* Logically separate OpenAI Data from all other customer data and enforce distinct user-level boundaries within each OpenAI customer organization.
* Ensure primary backend resources are deployed behind private network controls (VPN, private link, or equivalent zero-trust architecture).
* Network security policies and firewalls are configured for least-privilege access against a pre-established set of permissible traffic flows.
* Non-permitted traffic flows are blocked.

## 10. Vulnerability Management

* Maintain and operate an industry standard vulnerability management program designed to ensure the prompt remediation of vulnerabilities affecting the services Supplier provides.
* Maintain and implement a vulnerability management program that scans regularly for vulnerabilities, subscribes to a vulnerability notification service, prioritizes remediation based on risk, and establishes remediation timeframes based on risk rating.
* Once a patch is released, and the associated security vulnerability has been reviewed and assessed for its applicability and importance, the patch is applied and verified in a timeframe which is commensurate with the risk posed to Systems.
* Deploy a log management solution and retain logs produced by intrusion detection systems for a minimum period of one year.

## 11. Physical and Environmental Security

* Maintain physical security at every location where OpenAI Data may be stored or accessed.
* Control access to offices and data centers through badge, biometric, or equivalent authentication.
* Log and escort all visitors.
* Operate 24 × 7 video surveillance and physical intrusion-detection systems.
* Handle and dispose of physical media securely, using locked storage, tracked transfers, and certified destruction.

## 12. Availability, Business Continuity, and Disaster Recovery

Supplier will safeguard the confidentiality, integrity, and availability of the Services and any OpenAI Data through:

* Availability Management
  + Continuously monitor, analyze, and evaluate system performance and availability.
  + Detect and report faults in a timely manner and restore services promptly after an interruption.
  + Track, self-attest to, and document service uptime, incidents, and adherence to agreed service-level objectives.
  + Provide OpenAI, upon request, with relevant performance metrics that demonstrate compliance with service levels.
* Business continuity and disaster recovery (BC/DR)
  + Maintain documented BC/DR plans that address emergencies or other events capable of disrupting the Services or compromising OpenAI Data.
  + Back up critical systems and data on a regular schedule consistent with the BC/DR plans.
  + Test the BC/DR plans at least annually and remediate any material gaps identified during testing.
  + Obtain OpenAI’s prior written consent before making any change that would materially reduce the protection those plans provide, which consent will not be unreasonably withheld.

## 13. Third Party and Technology-Supply-Chain Risk Management

* Maintain and operate an industry standard risk-management program for all sub-processors, subcontractors, and critical sub-suppliers with access to OpenAI Data or who support the software or services
* Enter into written agreements with each third party that require security safeguards at least as stringent as those in these Supplier Security Measures.
* Subject all third parties to Supplier’s formal security assessment process before onboarding and at regular intervals thereafter, retaining the resulting documentation.
* Identify, upon OpenAI’s request, every critical sub-supplier, its country of origin, and any key dependency relevant to Supplier’s performance.
* Maintain processes that evaluate ICT and product supply-chain risks and promptly notify OpenAI of any disruption, vulnerability, or emerging threat that could compromise the confidentiality, integrity, or availability of the software, services, Supplier’s performance, or OpenAI Data.

## 14. Data Encryption

* Protect OpenAI Data in transit across any public or private network using strong, industry-recognized cryptographic protocols (TLS 1.2 or higher, SSH 2, IPsec, or equivalent). Legacy or insecure protocols (e.g., SSL v3, TLS 1.0/1.1) must be disabled.
* Encrypt all OpenAI Data stored on any persistent medium—including databases, object stores, file systems, endpoint devices, and backups—using strong, industry-recognized algorithms (e.g., AES-256 or equivalent) and cryptographic modules validated to FIPS 140-2/3, ISO/IEC 19790, or comparable standards.
* Manage encryption keys using a dedicated key-management system; access to keys shall be restricted to authorized personnel and rotated at least annually or upon suspected compromise. Supplier shall ensure that snapshots, replicas, and offline backups are protected under the same controls.

## 15. Data Retention

At the expiry or termination of the Agreement, Supplier will, at OpenAI’s option, delete or return all OpenAI Data (excluding any back-up or archival copies which shall be deleted in accordance with Supplier’s data retention schedule), except where Supplier is required to retain copies under applicable laws, in which case Supplier will isolate and protect that OpenAI Data from any further Processing except to the extent required by applicable laws. Supplier will provide OpenAI the ability to configure data retention periods within the product, if applicable to the services Supplier provides.

## 16. Secure Disposal

* Implements controls designed to ensure the secure disposal of OpenAI Data in accordance with applicable law considering available technology so that OpenAI Data cannot be read or reconstructed.
* Securely erase electronic media before disposal using methods described in NIST SP 800-88 standard or equivalent by overwriting or degaussing, or physically destroyed prior to disposal or reassignment to another system.

## 17. Internal Security Evaluations and Change Notification

* Regularly assess the effectiveness of its security controls—through automated scanning, manual reviews, and policy compliance checks—against industry-standard frameworks and its own policies.
* Notify OpenAI in advance of any material change to its infrastructure, architecture, third-party dependencies, data flows, or security posture that could reasonably affect the confidentiality, integrity, or availability of OpenAI Data.

## 18. Independent Audits and Certifications

At least annually, Supplier will:

* Engage a qualified, independent auditor to review its security controls against a recognized industry standard (e.g., SOC 2 Type 2 or ISO 27001 surveillance / recertification).
* Provide a summary or full reports (as appropriate) to OpenAI upon request.

## 19. Penetration Testing

If Supplier provides Hosted Services or online services, Supplier will:

* Arrange annual third-party penetration tests covering: (i) the Hosted Services or services; (ii) the entire internet-facing perimeter; and (iii) Supplier’s internal corporate network.
* Share evidence that the tests occurred, plus executive summaries of findings, under NDA.
* Remediate critical and high-severity vulnerabilities affecting OpenAI Data within 60 days of discovery or promptly inform OpenAI of compensating controls and residual risk.

## 20. OpenAI Verification Rights

* During the Agreement term and for one year thereafter, OpenAI (or its designated auditor) may, with reasonable notice, review relevant books, records, and facilities to confirm compliance with these Supplier Security Measures. Reviews will be limited to information reasonably necessary for that purpose and conducted under confidentiality obligations.
* Supplier will also make commercially reasonable efforts to complete security questionnaires that OpenAI may submit from time to time.

## 21. Non-U.S. Data Access

Supplier acknowledges that the Final Rule implementing Executive Order 14117 issued by the U.S. Department of Justice prohibits or restricts Access to bulk Covered Data to Countries of Concern or Covered Persons (as such terms and other capitalized terms used in this paragraph are defined in the Final Rule).

* If the services that Supplier provides involve Access to Covered Data of OpenAI or its affiliates, then Supplier represents and warrants that: (i) neither it nor any of its affiliates is or will be organized or chartered in a Country of Concern, has or will have its principal place of business in a Country of Concern, or is or will be 50% or more owned, directly or indirectly, individually or in the aggregate, by one or more Countries of Concern or Covered Persons; and (ii) neither Supplier, nor any of its affiliates, nor any employee or contractor of Supplier who has Access to such Covered Data is or will be located in a Country of Concern, has been determined by the U.S. Attorney General to be a Covered Person, or otherwise qualifies or will qualify as a Covered Person. If (a) or (b) changes, Supplier will immediately notify OpenAI.
* Supplier and its affiliates will not engage in any Covered Data Transaction involving OpenAI’s Covered Data with a Country of Concern or Covered Person. If Supplier engages in a Restricted Transaction related to OpenAI’s Covered Data, then Supplier will provide OpenAI with any information necessary for OpenAI to comply with the requirements of the Final Rule.

## 22. Definitions.

* Covered Data means bulk U.S. sensitive data or U.S. government-related data, as this may be further defined under the Final Rule implementing Executive Order 14117 issued by the U.S. Department of Justice.
* Data Protection Laws means all data protection laws applicable to Supplier’s performance under the Agreement.
* Hosted Service means software-as-a-service, platform-as-a-service, or any similar hosted or online services Supplier provides to OpenAI.
* Information Security Program means a structed framework of policies, procedures, and controls that includes administrative, technical, and physical controls aligned with industry standards, all designed to safeguard the confidentiality, integrity, and availability of OpenAI Data.
* OpenAI Data means information that Supplier has received or collected from or on behalf of OpenAI in connection with Supplier’s performance for OpenAI. OpenAI Data includes but is not limited to Personal Data.
* Personal Data has the meaning assigned to the term “personal data” or “personal information” under applicable Data Protection Laws.
* Processing means any operation performed on data, whether by automated means or not, including collection, recording, organization, storage, use, disclosure, or destruction.
* Security Incident means any actual or suspected event involving the unauthorized access, use, disclosure, alteration, or destruction of OpenAI Data, or disruption to its availability or integrity, within Supplier or subprocessor Systems.
* Supplier Code of Conduct means the OpenAI Supplier Code of Conduct at: [https://openai.com/policies/supplier-code/.⁠](https://openai.com/policies/supplier-code/)
* Supplier Personnel means all personnel who perform any aspect of Supplier’s performance in its engagement with OpenAI, and includes employees, contractors, contingent workers, and subcontractors.
* Systems means information systems used by Supplier or its subprocessors to process, transmit, or store OpenAI Data. This includes the integrated hardware, software, personnel, and procedures supporting those functions.
