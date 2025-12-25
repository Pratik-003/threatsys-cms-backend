from pymongo import MongoClient

# 1. Connect to MongoDB
client = MongoClient("mongodb+srv://maharanapratik600_db_user:iZpG6TsJjNkH0cfd@threatsyscluster.lgp7wyz.mongodb.net/?retryWrites=true&w=majority&appName=ThreatsysCluster")
db = client["threatsys_cms"]
collection = db["pages"]

# 2. Define the Full Data Structure
data = [
    # ====================================================
    # 1. HOME PAGE (Full Content)
    # ====================================================
    {
        "slug": "home",
        "title": "Threatsys Technologies",
        "sections": {
            # --- Hero Section ---
            "hero_heading": "Securing Your Digital Future Globally",
            "hero_subtext": "Award-winning Cybersecurity & VAPT services trusted by 500+ Enterprises.",
            "banner_image": "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=2070&auto=format&fit=crop", 
            
            # --- Stats Bar ---
            "stats": [
                {"label": "Happy Clients", "value": "500+"},
                {"label": "Vulnerabilities Found", "value": "10k+"},
                {"label": "Countries Served", "value": "15+"}
            ],

            # --- Services Grid (Quick View) ---
            "services_grid": [
                {"title": "Web App Security", "desc": "Comprehensive VAPT for your web applications.", "icon": "globe"},
                {"title": "Mobile App Security", "desc": "Securing Android & iOS apps from runtime threats.", "icon": "smartphone"},
                {"title": "Network Security", "desc": "Internal and External network penetration testing.", "icon": "wifi"},
                {"title": "Cloud Security", "desc": "AWS, Azure, and GCP configuration audits.", "icon": "cloud"},
                {"title": "IoT Security", "desc": "Testing embedded devices and smart infrastructure.", "icon": "cpu"},
                {"title": "Compliance Audit", "desc": "ISO 27001, GDPR, and PCI-DSS compliance.", "icon": "shield"}
            ],

            # --- Client Logos (Trusted By) ---
            "clients": [
                "https://upload.wikimedia.org/wikipedia/commons/a/a9/Amazon_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/5/51/IBM_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/4/44/Microsoft_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg",
                "https://upload.wikimedia.org/wikipedia/commons/b/b1/Tata_Consultancy_Services_Logo.svg"
            ],

            # --- Awards Section ---
            "awards": [
                {
                    "title": "Cyber Safety Summit 2025",
                    "desc": "Recognized as the 'Best VAPT Provider' in Odisha.",
                    "image": "https://images.unsplash.com/photo-1544531586-fde5298cdd40?q=80&w=2070&auto=format&fit=crop"
                },
                {
                    "title": "Global Excellence Award",
                    "desc": "Awarded for innovation in AI-driven Threat Detection.",
                    "image": "https://images.unsplash.com/photo-1511578314322-379afb476865?q=80&w=2069&auto=format&fit=crop"
                }
            ],

            # --- Testimonials ---
            "testimonials": [
                {
                    "name": "Rajesh Kumar",
                    "role": "CTO, FinTech India",
                    "text": "Threatsys identified critical vulnerabilities in our banking app that 3 other vendors missed.",
                    "image": "https://randomuser.me/api/portraits/men/32.jpg"
                },
                {
                    "name": "Sarah Jenkins",
                    "role": "CISO, Global Tech",
                    "text": "Their reporting is detailed, professional, and their team is always available for support.",
                    "image": "https://randomuser.me/api/portraits/women/44.jpg"
                },
                {
                    "name": "Amit Abhisek",
                    "role": "Director, Odisha Power",
                    "text": "The best VAPT partner we have worked with in the last 10 years.",
                    "image": "https://randomuser.me/api/portraits/men/86.jpg"
                }
            ]
        }
    },

    # ====================================================
    # 2. ABOUT PAGE (Mission & Team)
    # ====================================================
    {
        "slug": "about",
        "title": "About Threatsys",
        "sections": {
            "hero_heading": "Who We Are",
            "hero_subtext": "Threatsys is a leading cybersecurity firm based in Bhubaneswar, dedicated to securing the digital future of businesses globally.",
            "banner_image": "https://images.unsplash.com/photo-1522071820081-009f0129c71c?q=80&w=2070&auto=format&fit=crop",
            
            "mission": "To democratize cybersecurity by making enterprise-grade protection accessible to businesses of all sizes.",
            
            "values": [
                {"title": "Integrity", "desc": "We believe in transparency. No fear-mongering, just facts."},
                {"title": "Innovation", "desc": "Hackers evolve every day. So do we."},
                {"title": "Excellence", "desc": "We don't stop at 'compliant'. We aim for 'secure'."}
            ],

            "team": [
                {"name": "Pratik Maharana", "role": "Lead Developer & Researcher", "image": "https://randomuser.me/api/portraits/men/32.jpg"},
                {"name": "Anjali Das", "role": "Head of Compliance", "image": "https://randomuser.me/api/portraits/women/68.jpg"},
                {"name": "Rahul Verma", "role": "Senior Pentester", "image": "https://randomuser.me/api/portraits/men/45.jpg"}
            ]
        }
    },

    # ====================================================
    # 3. SERVICES PAGE (Process & Categories)
    # ====================================================
    {
        "slug": "services",
        "title": "Our Services",
        "sections": {
            "hero_heading": "What We Offer",
            "hero_subtext": "From VAPT to Compliance, we cover every aspect of your security posture.",
            "banner_image": "https://images.unsplash.com/photo-1563986768427-1c591cd66126?q=80&w=2070&auto=format&fit=crop",
            
            "process_steps": [
                {"step": "01", "title": "Reconnaissance", "desc": "We gather intelligence on your assets just like a real attacker would."},
                {"step": "02", "title": "Exploitation", "desc": "Our certified ethical hackers attempt to breach your defenses safely."},
                {"step": "03", "title": "Reporting", "desc": "You get a detailed technical report + an executive summary for leadership."},
                {"step": "04", "title": "Remediation", "desc": "We guide your developers on how to patch every single vulnerability."}
            ],

            "service_categories": [
                "Vulnerability Assessment",
                "Penetration Testing (VAPT)",
                "Red Teaming",
                "Source Code Review",
                "Cloud Configuration Review",
                "API Security Testing",
                "IoT Security"
            ]
        }
    },

    # ====================================================
    # 4. BLOG PAGE (Full Articles)
    # ====================================================
    {
        "slug": "blog",
        "title": "Blog",
        "sections": {
            "hero_heading": "Latest updates from the cyber security universe by Threatsys Technologies",
            "hero_subtext": "",
            "posts": [
                # POST 1: HIPAA
                {
                    "slug": "hipaa-cybersecurity-requirements",
                    "title": "HIPAA Cybersecurity Requirements for Healthcare Startups",
                    "category": "CYBER SECURITY",
                    "date": "Dec 25, 2025",
                    "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?q=80&w=2070&auto=format&fit=crop",
                    "summary": "Healthcare startups are reshaping the future of patient care. However, with digital transformation comes the massive responsibility of securing patient data.",
                    "content": """
                        <p class="lead">Healthcare startups are reshaping the future of patient care through digital platforms, telemedicine, and AI-driven diagnostics. However, with digital transformation comes the massive responsibility of securing patient data.</p>
                        
                        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Why HIPAA Matters</h2>
                        <p class="mb-4">The Health Insurance Portability and Accountability Act (HIPAA) sets the standard for sensitive patient data protection. Companies that deal with protected health information (PHI) must have physical, network, and process security measures in place and follow them to ensure HIPAA Compliance.</p>
                        
                        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Key Technical Safeguards</h2>
                        <ul class="list-disc pl-6 mb-6 space-y-2">
                            <li><strong>Access Control:</strong> Implement unique user IDs, automatic logoff, and encryption to ensure only authorized personnel can access PHI.</li>
                            <li><strong>Audit Controls:</strong> Hardware, software, and procedural mechanisms that record and examine activity in information systems.</li>
                            <li><strong>Integrity:</strong> Implement mechanisms to corroborate that PHI has not been altered or destroyed in an unauthorized manner.</li>
                            <li><strong>Transmission Security:</strong> Encrypt data during transmission over an electronic communications network (e.g., HTTPS/TLS).</li>
                        </ul>

                        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">The Cost of Non-Compliance</h2>
                        <p>Fines for non-compliance can range from $100 to $50,000 per violation (or per record), with a maximum penalty of $1.5 million per year for violations of an identical provision.</p>
                    """
                },

                # POST 2: GDPR vs DPDP
                {
                    "slug": "gdpr-vs-dpdp-key-differences",
                    "title": "GDPR vs DPDP Key Differences for Indian Organisations",
                    "category": "CYBER SECURITY",
                    "date": "Dec 20, 2025",
                    "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?q=80&w=1470&auto=format&fit=crop",
                    "summary": "As data becomes central to business operations, Indian organizations increasingly operate across global data ecosystems.",
                    "content": """
                        <p class="lead">As data becomes central to business operations, Indian organizations increasingly operate across global data ecosystems. With the introduction of the Digital Personal Data Protection (DPDP) Act, 2023, comparisons with the EU's GDPR are inevitable.</p>

                        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Scope of Application</h2>
                        <p class="mb-4"><strong>GDPR:</strong> Applies to the processing of personal data of subjects residing in the EU, regardless of the company's location.</p>
                        <p class="mb-4"><strong>DPDP:</strong> Applies to processing of digital personal data within India, and processing outside India if it is for offering goods or services to Data Principals in India.</p>

                        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Consent Architecture</h2>
                        <p>Under DPDP, consent must be free, specific, informed, unconditional, and unambiguous. Unlike GDPR, which offers 'Legitimate Interest' as a lawful basis, DPDP relies heavily on Consent and 'Certain Legitimate Uses'.</p>
                    """
                },

                # POST 3: DPDP Roadmap
                {
                    "slug": "dpdp-act-90-day-roadmap",
                    "title": "DPDP Act 90-Day Compliance Roadmap",
                    "category": "CYBER SECURITY",
                    "date": "Dec 15, 2025",
                    "image": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?q=80&w=2070&auto=format&fit=crop",
                    "summary": "The Digital Personal Data Protection (DPDP) Act, 2023 marks a major shift in how organizations in India must collect, process, and store personal data.",
                    "content": """
                        <p class="lead">The Digital Personal Data Protection (DPDP) Act, 2023 marks a major shift in how organizations in India must collect, process, store, and protect personal data.</p>

                        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Phase 1: Data Discovery (Days 1-30)</h2>
                        <ul class="list-disc pl-6 mb-6 space-y-2">
                            <li>Map all data flows within the organization.</li>
                            <li>Identify all third-party processors (Data Fiduciaries).</li>
                            <li>Categorize data based on sensitivity.</li>
                        </ul>

                        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Phase 2: Policy Framework (Days 31-60)</h2>
                        <p>Draft new privacy notices that are clear and available in all 22 scheduled languages if required. Update vendor contracts to include DPDP liability clauses.</p>
                        
                        <h2 class="text-2xl font-bold text-gray-900 mt-8 mb-4">Phase 3: Implementation (Days 61-90)</h2>
                        <p>Deploy Consent Managers and set up the Grievance Redressal mechanism as mandated by the Act.</p>
                    """
                }
            ]
        }
    },

    # ====================================================
    # 5. CONTACT PAGE (Locations)
    # ====================================================
    {
        "slug": "contact",
        "title": "Contact Us",
        "sections": {
            "hero_heading": "Get In Touch",
            "hero_subtext": "Reach out for a confidential consultation. Our team is available 24/7 for critical incident response.",
            "banner_image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2070&auto=format&fit=crop",
            
            "locations": [
                {
                    "city": "Bhubaneswar (HQ)",
                    "address": "Ryan Tower, 3rd Floor, Infocity, Patia, Odisha 751024",
                    "phone": "+91 96682 00222",
                    "email": "contact@threatsys.co.in"
                },
                {
                    "city": "Bangalore",
                    "address": "WeWork Galaxy, Residency Road, Bangalore 560025",
                    "phone": "+91 80 4000 5000",
                    "email": "blr@threatsys.co.in"
                }
            ],
            
            "social_links": {
                "linkedin": "https://linkedin.com/company/threatsys",
                "twitter": "https://twitter.com/threatsys",
                "instagram": "https://instagram.com/threatsys"
            }
        }
    }
]

# 3. Clear and Insert
collection.delete_many({})
collection.insert_many(data)
print("✅ Database successfully seeded with ALL pages (Home, About, Services, Blog, Contact)!")

certificates_data = [
    {
        "cert_id": "TS-2025-001",
        "company_name": "TechFlow Solutions Pvt Ltd",
        "address": "Plot 45, Silicon Valley, Bangalore, India",
        "scope": "ISO 27001:2013 Information Security Management System",
        "issue_date": "2024-01-15",
        "expiry_date": "2027-01-15", 
        "status": "Active"
    },
    {
        "cert_id": "TS-2023-889",
        "company_name": "OldGuard Logistics",
        "address": "12 Industrial Area, Mumbai, India",
        "scope": "VAPT of Core Banking Solution",
        "issue_date": "2023-01-10",
        "expiry_date": "2024-01-10", # EXPIRED
        "status": "Expired"
    },
    {
        "cert_id": "TS-2025-102",
        "company_name": "Alpha Nexus Health",
        "address": "Sector 5, Salt Lake, Kolkata, India",
        "scope": "HIPAA Compliance Audit",
        "issue_date": "2024-06-20",
        "expiry_date": "2025-06-20",
        "status": "Active"
    },
    {
        "cert_id": "TS-2025-105",
        "company_name": "CyberDefense Odisha",
        "address": "Patia, Bhubaneswar, Odisha",
        "scope": "GDPR Data Processing Audit",
        "issue_date": "2024-11-01",
        "expiry_date": "2025-11-01",
        "status": "Active"
    },
    {
        "cert_id": "TS-2022-500",
        "company_name": "RedBrick Construction",
        "address": "Civil Lines, Delhi, India",
        "scope": "ISO 9001:2015 Quality Management",
        "issue_date": "2022-05-15",
        "expiry_date": "2023-05-15", # EXPIRED
        "status": "Expired"
    },
    {
        "cert_id": "TS-2025-200",
        "company_name": "Innovate AI Labs",
        "address": "Hitech City, Hyderabad, India",
        "scope": "SOC 2 Type II Audit",
        "issue_date": "2025-01-01",
        "expiry_date": "2026-01-01",
        "status": "Active"
    }
]

cert_col = db["certificates"]
cert_col.delete_many({})
cert_col.insert_many(certificates_data)

print("✅ Database populated: Pages & Certificates!")