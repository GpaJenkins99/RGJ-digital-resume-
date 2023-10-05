from pathlib import Path

import streamlit as st
from PIL import Image


# ----- PATH SETTINGS -----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "RGJ Resume (2).doc"
profile_pic = current_dir / "assets" / "profile-pic (2).png"

# ----- GENERAL SETTINGS -----
PAGE_TITLE = "Digital Resume | Raniesa Gray-Johnson"
PAGE_ICON = ":⛩:"
NAME = "Raniesa Gray-Johnson"
DESCRIPTION ="""
Retired US Army Soldier | Mother| Entrepreneur  | Cloud engineer 
"""
EMAIL = "raniesaj@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/raniesa-gray-johnson?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B0tMOfYS5S7SPRI8LsJiXSA%3D%3D",
    "GitHub": "https://github.com/GpaJenkins99",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)




# ----- LOAD CSS, PDF &PROFILE PIC -----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# ----- HERO SECTION -----
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# ----- SOCIAL LINKS -----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# ----- EXPERIENCE & QUALIFICATIONS -----
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - ✔️20 years experience with IT as a whole 
    - ✔️CompTIA A+ CE, Network+ CE, Security+ CE, Linux Essentials, CCNA (10/2023), AZ-104 (10/2023)
    - ✔️Western Governors’ University Network Operations and Security, B.S., Oct 2023 
    """
)


# ----- SKILLS -----
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
     - Windows Server 2012/2016,- TCP/IP, - WAN,    - Java,                    - System Administration
     - Microsoft Office 365,    - DNS,    - VoIP,   - django,                  - Network Support 
     - Cisco Router CLI,        - LAN,    - SCCM,   - Remote Access Software , - Docker
     - Adobe Creative Suite,    - VPN,    - WSUS,   - Microsoft Exchange,      - Kubernetes
     - Active Directory,        - DHCP,   - Python, - PowerShell,              - AWS Solutions Architect 
    """
)



# ----- WORK HISTORY -----
st.write("#")
st.subheader("Work History")
st.write("---")

# ----- JOB 1 -----
st.write("🚧", "**Cloud Engineer | Relias**")
st.write("2022-Present")
st.write("Morrisville, North Carolina")
st.write(
    """
   - ► Execute daily system monitoring, meticulously validating the integrity and availability of all server resources, systems, and critical processes. Conduct in-depth reviews of system and application logs, ensuring the successful completion of scheduled tasks, such as backups.
   - ► Champion application performance, uptime, and scalability, upholding stringent standards of code quality and thoughtful design.
   - ► Demonstrate exceptional problem-solving skills, proactively identifying and addressing issues before they impact business productivity.
   - ► Proficiently troubleshoot incidents, systematically identifying root causes, implementing effective solutions, and diligently documenting each problem and its resolution. Enforce preventive measures to minimize future occurrences. 
   - ► Lead the development and execution of technical strategies to design, build, and deploy cloud artifacts at an enterprise scale, contributing to operational efficiency. Maintain and continuously update comprehensive documentation for standard operating procedures to ensure streamlined support.
   - ► Collaborate closely with the software development team, facilitating seamless software releases and fostering cross-functional synergy.
   - ► Work collaboratively with development teams to gain a deep understanding of the application's infrastructure requirements. Collaboratively identify and implement optimal cloud-based solutions to align with the company's objectives.
   - ► Conduct comprehensive research to recommend innovative and, wherever possible, automated approaches for cloud and system administration tasks, enhancing overall operational effectiveness.
   - ► Design and manage cloud infrastructure architecture in strict adherence to company security guidelines, safeguarding sensitive data and assets.
   - ► Contribute actively to the establishment and maintenance of system standards and provide education to teams regarding the implementation of new cloud-based initiatives through tailored training programs.
   - ► Develop Infrastructure as Code (IaC) and other scripts, actively participating in the review process before changes are merged into source control, ensuring code quality and system stability.
   - ► Skillfully develop and maintain software installation and configuration procedures, optimizing system setup and performance.
   - ► Execute the creation, modification, and deletion of Cloud Identity Access Management (IAM) artifacts as needed, encompassing user accounts, service accounts, app registrations, and managed identities, to maintain precise access control and data security.
   - ► Worked closely with development teams to integrate Atlassian tools into workflows, providing guidance and support.
    """
)

# ----- JOB 2 -----
st.write("🚧", "**Cloud Security Engineer/Systems Administrator | Solutions Granted Inc**")
st.write("2020-2022")
st.write("Woodbridge, Virginia")
st.write(
    """
   - ► Orchestrated seamless operation of on-site technology infrastructure, ensuring uninterrupted functionality.
   - ► Vigilantly managed and monitored server backup processes to safeguard critical data and systems.
   - ► Expertly installed and configured specialized software to meet organizational needs, optimizing system performance.
   - ► Diligently applied software and operating system patches, maintaining system security and reliability. 
   - ► Assumed responsibility for managing user accounts, permissions, and password policies, ensuring data integrity and security.
   - ► Collaborated efficiently with third-party support entities to swiftly resolve technical issues and implement effective solutions.
   - ► Spearheaded the installation and configuration of new hardware components, enhancing the overall infrastructure.
   - ► Demonstrated adept troubleshooting skills, resolving technical issues promptly to support both on-site and remote customers.
   - ► Proficiently administered Active Directory (AD), Office 365, and Cloud Storage systems, facilitating efficient user management and data access.
   - ► Demonstrated expertise in engineering and maintaining shared corporate infrastructure.
   - ► Proficiently executed and supervised PowerShell scripts for image updates, enhancing system functionality.
   - ► Developed and programmed Python scripts to streamline task sequences, augmenting operational efficiency.
   - ► Collaborated seamlessly with cross-functional teams to define, document, and align system requirements with business objectives.
   - ► Worked closely with development teams to integrate Atlassian tools into workflows, providing guidance and support.
    """
)

# ----- JOB 3 -----
st.write("🚧", "**Technology Support Analyst (TSG) | United Parcel Services (UPS)**")
st.write("2019 - 2020")
st.write("Newport News, Virginia")
st.write(
    """
   - ► Meticulously maintained Windows Server 2016 to ensure optimal patch management, enhancing system security and reliability.
   - ► Swiftly responded to and effectively resolved all escalated network issues for internal users, minimizing downtime and disruptions.
   - ► Played a pivotal role in configuring and fortifying corporate network connections for over 600 workstations, employing Cisco switches and routers to bolster network security and performance.
   - ► Skillfully programmed, maintained, and allocated VOIP extensions using Avaya PBX systems for active vendor agents, streamlining communication processes.
   - ► Managed and scheduled essential software maintenance and upgrades for over 900 Windows-based workstations and servers, ensuring software integrity and performance optimization.
   - ► Expertly configured security settings and access permissions for both user groups and individuals using Active Directory, fortifying data security and access control.
   - ► Assumed the role of project manager, overseeing the delivery of defined business requirements with a focus on timeliness. This encompassed managing stakeholder expectations, facilitating communication of critical decisions, presenting project milestones, and conducting comprehensive risk assessments to inform management decisions.
    """
)

# ----- JOB 4 -----
st.write("🚧", "**Network Support Analyst | PSI Pax, Inc**")
st.write("2017 – 2019")
st.write("Yorktown, Virginia")
st.write(
    """
   - ► Assumed responsibility for the meticulous management of backup, administration, and security measures for Navy time and attendance software, ensuring data integrity and availability.
   - ► Enforced backup procedures through vigilant monitoring and meticulous logging of backup storage, guaranteeing seamless data recovery capabilities.
   - ► Demonstrated expertise in proactively identifying and addressing network virus attacks, actively maintaining up-to-date virus definitions to fortify the organization's cybersecurity posture.
   - ► Proficiently configured security settings and access permissions, leveraging Active Directory and Navy proprietary software to uphold robust data security and controlled access.
   - ► Conducted continuous monitoring of the network infrastructure, analyzing computer network security breaches or attempted breaches to swiftly mitigate risks and bolster network security.
   - ► Strategically planned and executed scheduled network upgrades, minimizing disruptions and enhancing capabilities. 
   - ► Conducted thorough investigations into network faults, swiftly resolving issues to maintain seamless operations.
   - ► Ensured network equipment was up-to-date with the latest firmware releases, enhancing security and functionality.
   - ► Delivered concise network status reports to key stakeholders, enabling informed decision-making.
   - ► Provided comprehensive training to marine personnel, empowering them with troubleshooting skills to resolve network-related challenges.
    """
)

# ----- JOB 5 -----
st.write("🚧", "**IOT Solutions Support | Apple, Inc**")
st.write("2015 - 2017")
st.write("Remote")
st.write(
    """
   - ► Conducted a meticulous review and analysis of computer printouts and performance indicators to pinpoint code problems, systematically identifying errors and rectifying them through precise code correction.
   - ► Demonstrated a commitment to continuous learning and professional growth by diligently studying manuals, periodicals, and technical reports. This enabled the development of programs that seamlessly aligned with staff and user requirements.
   - ► Facilitated open and effective communication by engaging with network users to collaboratively address and resolve existing system problems, fostering a culture of proactive issue resolution
   - ► Effectively managed, created, escalated, and concluded tickets utilizing HP Service Manager, maintaining meticulous records.
   - ► Orchestrated seamless installation and upkeep of personal computers and mainframe terminals, ensuring optimal functionality.
   - ► Efficiently accepted and managed work orders from customers, maintaining comprehensive daily operational logs.
   - ► Exhibited expertise in PC (desktop & laptop) upgrades, configuration, maintenance, troubleshooting, and repairs.
   - ► Employed remote access tools to deliver remote assistance to end-users, enhancing problem resolution efficiency.
   - ► Conducted weekly and monthly statistical analysis and metrics of helpdesk activities, contributing to performance evaluation.
   - ► Methodically documented technical issues reported by customers using Remedy, ensuring clear communication.
   - ► Maintained a professional demeanor and consistently delivered excellent customer service, fostering positive interactions.
   - ► Collaborated with end-users to facilitate password setup and user account activation, ensuring seamless access to systems.
    """
)

# ----- JOB 5 -----
st.write("🚧", "**Computer Specialist | 633d Logistics Readiness Squadron, US. Air Force.**")
st.write("2008 - 2014")
st.write("Hampton, Virginia")
st.write(
    """
   - ► Spearheaded the proactive monitoring of network performance, conducting comprehensive assessments to determine the necessity of adjustments and forecast future changes.
   - ► Upheld significant responsibilities as the Equipment Custodian and Software Licensing Manager, overseeing assets valued at over $200,000, meticulously ensuring their proper maintenance and compliance with licensing requirements.
   - ► Demonstrated technical prowess in the installation, testing, and maintenance of base-wide Radio Frequency ID Scanners, playing a pivotal role in supporting logistic and supply operations.
   - ► Expertly addressed network connectivity issues, encompassing troubleshooting and resolution of TCP/IP, DHCP, and DNS-related challenges, ensuring uninterrupted network functionality.
   - ► Executed the creation of accreditation packages for the SIPRNet office, meticulously preparing them for inspection and approval by the Base Information Assurance Office, reinforcing data security protocols.
   - ► Assumed responsibility for the management of 800+ user accounts within the domain, leveraging Active Directory's Web Active Roles Server to streamline user administration processes.
   - ► Contributed significantly to system upgrades and revisions, demonstrating precision and efficiency by consistently achieving a 100% accuracy rate and completing installations within three days of receiving new programs and equipment. 
    """
)

# ----- PROJECTS & ACCOMPLISHMENTS -----
