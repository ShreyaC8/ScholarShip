# scholarship.py

schol_type = {
    "generic": {
        "GREAT Scholarships": {
            "desc": "Scholarships for one-year master's courses across a range of subjects at a variety of UK universities. It covers partial or full tuition fees.",
            "eligibility": '''Available to students from:
                Bangladesh, China, Egypt, Ghana, Greece, Kenya, India, Indonesia, Malaysia, Mexico, Nigeria, Pakistan, Thailand, Turkey, Vietnam. 
                Check online to see which universities provide scholarships to your nation and how to apply.''',
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://study-uk.britishcouncil.org/scholarships-funding/great-scholarships"
        },
        "Commonwealth Scholarships": {
            "desc": "UK university scholarships given to talented individuals with the potential to make a positive impact on the global stage. It covers full funding including tuition fees, living expenses, and airfare.",
            "eligibility": "Students from Commonwealth countries who have (at least) an upper second class (2:1) undergraduate degree and are unable to afford to study in the UK.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://cscuk.fcdo.gov.uk/apply/"
        },
        "Chevening Scholarships": {
            "desc": "Fully funded master's degrees in the UK for individuals with leadership potential. It covers full funding including tuition fees, living expenses, and airfare.",
            "eligibility": '''Open to individuals: with an undergraduate degree that qualifies them for a UK master's programme,
                who are a citizen of a Chevening-eligible country or territory,
                who have at least two years of work experience (2,800 hours),
                who commit to returning to their home country for at least two years after their scholarship ends.''',
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.chevening.org"
        },
        "Erasmus Mundus Joint Master Degrees": {
            "desc": "A prestigious, integrated, international study programme, jointly delivered by an international consortium of higher education institutions.",
            "eligibility": "Available to students worldwide who hold a Bachelor's degree and meet specific academic requirements of the programme.",
            "lvl_study": "Masters",
            "location": "Various European Countries",
            "website": "https://ec.europa.eu/programmes/erasmus-plus/opportunities/individuals/students/erasmus-mundus-joint-master-degrees_en"
        },
        "Rhodes Scholarships at Oxford University": {
            "desc": "The Rhodes Scholarship is the oldest and perhaps the most prestigious international scholarship programme in the world.",
            "eligibility": "Open to outstanding students from certain countries, based on academic achievements and leadership potential.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.rhodeshouse.ox.ac.uk"
        }
    },
    "agri_vet": {
        "Newcastle University": {
            "name": "John Pain Scholarship",
            "desc": "Scholarship for students pursuing agriculture at Newcastle University.",
            "eligibility": "Open to undergraduate students pursuing agriculture at Newcastle University.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.ncl.ac.uk/undergraduate/fees-funding/scholarships-bursaries/subject-scholarships/agriculture/"
        },
        "University of Edinburgh": {
            "name": "Royal (Dick) School of Veterinary Studies International Scholarship",
            "desc": "Scholarship for international students studying veterinary medicine at the University of Edinburgh.",
            "eligibility": "Available for international students applying to the Royal (Dick) School of Veterinary Studies.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.ed.ac.uk/student-funding/undergraduate/international/vet"
        },
        "Harper Adams University": {
            "name": "Douglas Bomford Trust Scholarship",
            "desc": "Scholarship for undergraduate students in agriculture at Harper Adams University.",
            "eligibility": "Open to undergraduate students pursuing agriculture at Harper Adams University.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.harper-adams.ac.uk/apply/finance/scholarships/scholarship/17/douglas-bomford-trust-scholarship"
        },
        "Aberystwyth University": {
            "name": "CLA and Aberystwyth University Agriculture Scholarships",
            "desc": "Scholarships offered by CLA and Aberystwyth University for agriculture students.",
            "eligibility": "Available for undergraduate students entering Aberystwyth University in agriculture-related fields.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.aber.ac.uk/en/study-with-us/ug-studies/scholarships/departmental/cla/#:~:text=CLA%20and%20Aberystwyth%20University%20Agriculture,for%20entry%20in%20September%202024."
        },
        "Writtle University College": {
            "name": "Elinor Roper Scholarship",
            "desc": "Scholarship for Masters students at Writtle University College.",
            "eligibility": "Available for Masters students studying agriculture at Writtle University College.",
            "lvl_study": "Masters",
            "location": "United Kingdom",
            "website": "https://writtle.ac.uk/scholarships.cfm?Scholarship=147&nohead=1&nofooter=1"
        },
        "Royal Agricultural University": {
            "name": "Clyde Higgs Postgraduate Scholarship",
            "desc": "Scholarship for postgraduate students at the Royal Agricultural University.",
            "eligibility": "Open to postgraduate students in agriculture at the Royal Agricultural University.",
            "lvl_study": "Masters",
            "location": "United Kingdom",
            "website": "https://www.rau.ac.uk/student-life/finance-scholarships-and-bursaries/clyde-higgs-postgraduate-scholarship"
        },
        "University of Leeds": {
            "name": "Faculty of Biological Sciences International Excellence Scholarships",
            "desc": "Scholarships for international students in biological sciences, including agriculture, at the University of Leeds.",
            "eligibility": "Open to international students demonstrating excellence in biological sciences, including agriculture.",
            "lvl_study": "Masters",
            "location": "United Kingdom",
            "website": "https://biologicalsciences.leeds.ac.uk/directory_record/523/faculty-of-biological-sciences-international-excellence-scholarships"
        },
        "University of East Anglia": {
            "name": "The Chadacre Trust Scholarship",
            "desc": "Scholarship for Masters students at the University of East Anglia.",
            "eligibility": "Available for Masters students studying agriculture or related fields at the University of East Anglia.",
            "lvl_study": "Masters",
            "location": "United Kingdom",
            "website": "https://www.uea.ac.uk/study/fees-and-funding/scholarships/the-chadacre-trust-scholarship"
        },
        "University of Nottingham": {
            "name": "Nottingham Trent University Agriculture Scholarship",
            "desc": "Scholarships for international students in agriculture and related fields at Nottingham Trent University.",
            "eligibility": "Open to students demonstrating academic excellence and a commitment to agriculture, with an offer from Nottingham Trent University.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.ntu.ac.uk/study-and-courses/courses/our-schools/animal-rural-and-environmental-sciences"
        },
    },
    "comp_math": {
        "University of Oxford": {
            "name": "Oxford-Weidenfeld and Hoffmann Scholarships",
            "desc": "Scholarships for outstanding students in computer science and mathematics from developing countries.",
            "eligibility": '''Students must demonstrate a commitment to improving society in their home countries, 
                              be willing to return to their home country after studies, and have a record of leadership achievement.''',
            "lvl_study": "Masters",
            "location": "United Kingdom",
            "website": "https://www.ox.ac.uk/admissions/graduate/fees-and-funding/scholarships/university-wide/oxford-weidenfeld-and-hoffmann-scholarships-and-leadership-programme"
        },
        "University of Cambridge": {
            "name": "Gates Cambridge Scholarship",
            "desc": "Full-cost scholarships for exceptional students in any discipline, including computer science.",
            "eligibility": "Open to non-UK citizens applying to a full-time postgraduate degree in any subject available at the University of Cambridge.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.gatescambridge.org"
        },
        "University of Edinburgh": {
            "name": "Edinburgh Global Research Scholarships",
            "desc": "Scholarships aimed at attracting the best and brightest PhD students from around the world.",
            "eligibility": "Open to overseas students starting a PhD program in computer science or mathematics.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.ed.ac.uk/student-funding/postgraduate/international/global/research"
        },
        "Imperial College London": {
            "name": "Imperial College PhD Scholarship Scheme",
            "desc": "Offers a large number of fully funded PhD scholarships for students with outstanding academic records and potential.",
            "eligibility": "Available to students worldwide, based on academic merit and potential for research excellence.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.imperial.ac.uk/study/pg/fees-and-funding/scholarships/phd-scholarship/"
        },
        "University of Manchester": {
            "name": "President's Doctoral Scholar Awards",
            "desc": "Scholarships for outstanding students who wish to undertake postgraduate research study at the University of Manchester.",
            "eligibility": "Open to all nationalities, with strong academic records and research potential.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.manchester.ac.uk/study/postgraduate-research/funding/opportunities/display/?id=00000273"
        }
    },   
    "sci": {
        "Imperial College London": {
            "name": "President's PhD Scholarships",
            "desc": "Opportunities for the most talented students to receive funding for a PhD in science and engineering.",
            "eligibility": "Open to all students who can demonstrate exceptional academic achievement and research potential.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.imperial.ac.uk/study/pg/fees-and-funding/scholarships/phd-scholarship/"
        },
        "University of Cambridge": {
            "name": "Cambridge International Scholarships",
            "desc": "For high-achieving international students pursuing a PhD at the University of Cambridge.",
            "eligibility": "Available to outstanding international students from any country who are accepted into a PhD programme.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.graduate.study.cam.ac.uk/finance/funding"
        },
        "University of Oxford": {
            "name": "Oxford Doctoral Training Partnership Scholarships",
            "desc": "Funded positions for high-achieving PhD students in science and engineering.",
            "eligibility": "Open to all international students who meet the entry requirements for the DTP program.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.ox.ac.uk/admissions/graduate/fees-and-funding/graduate-scholarships"
        },
        "University of Edinburgh": {
            "name": "Edinburgh Global Research Scholarships",
            "desc": "For PhD students demonstrating exceptional academic achievements.",
            "eligibility": "Available to overseas students who have applied for a PhD programme in science.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.ed.ac.uk/student-funding/postgraduate/international/global/research"
        },
        "University of Bristol": {
            "name": "Bristol International Fellowships",
            "desc": "For international researchers undertaking PhD studies in science and related fields.",
            "eligibility": "Available to international students who hold a relevant undergraduate or master's degree.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.bristol.ac.uk/fees-funding/postgraduate/international/"
        }
    },
    "art_design": {
        "Royal College of Art": {
            "name": "RCA Bursaries",
            "desc": "Financial support for students pursuing postgraduate degrees in art and design.",
            "eligibility": "Based on financial need and academic merit.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.rca.ac.uk/study/scholarships/"
        },
        "Central Saint Martins": {
            "name": "UAL Postgraduate Scholarships",
            "desc": "Support for students undertaking postgraduate study in art and design.",
            "eligibility": "Open to UK/EU students with a strong academic record.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.arts.ac.uk/study-at-ual/student-fees-and-funding/scholarships-search"
        },
        "Glasgow School of Art": {
            "name": "GSA International Scholarships",
            "desc": "Scholarships for international students applying to postgraduate programs in art and design.",
            "eligibility": "Based on academic excellence and financial need.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.gsa.ac.uk/about/our-schools/school-of-fine-art/funding/"
        },
        "University of the Arts London": {
            "name": "UAL International Postgraduate Scholarships",
            "desc": "Support for exceptional international students pursuing postgraduate programs in art and design.",
            "eligibility": "Open to international students with excellent academic records.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.arts.ac.uk/study-at-ual/student-fees-and-funding/scholarships-search"
        },
        "University of Brighton": {
            "name": "International Scholarships for Art and Design",
            "desc": "Funding for international students in art and design programs.",
            "eligibility": "Open to international students demonstrating academic excellence.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.brighton.ac.uk/international/scholarships/index.aspx"
        }
    },
    "engin_tech": {
        "University of Bristol": {
            "name": "Engineering International Scholarships",
            "desc": "Scholarships for international students applying to engineering programs.",
            "eligibility": "Open to non-UK/EU students with academic excellence in engineering.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.bristol.ac.uk/study/undergraduate/fees-funding/scholarships/engineering-international-scholarships/"
        },
        "University of Southampton": {
            "name": "Engineering and Physical Sciences Scholarships",
            "desc": "Scholarships for postgraduate students in engineering fields.",
            "eligibility": "Outstanding academic achievement in engineering disciplines.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.southampton.ac.uk/scholarships/engineering-and-physical-sciences.page"
        },
        "University of Leeds": {
            "name": "Faculty of Engineering International Scholarships",
            "desc": "Funding for international students pursuing undergraduate degrees in engineering.",
            "eligibility": "Available to non-UK students with excellent academic records.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.engineering.leeds.ac.uk/undergraduate/fees-funding/scholarships/"
        },
        "University of Sheffield": {
            "name": "Sheffield International Engineering Scholarship",
            "desc": "Scholarships for international students enrolling in engineering programs.",
            "eligibility": "Based on academic merit, open to all nationalities.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.sheffield.ac.uk/international/finance/scholarships"
        },
        "University of Strathclyde": {
            "name": "Strathclyde Excellence Scholarship",
            "desc": "Scholarships for international students in engineering programs.",
            "eligibility": "Available to high-achieving international students.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.strath.ac.uk/study/scholarships/undergraduate/"
        }
    },
    "health_med": {
        "King's College London": {
            "name": "Global Health & Social Medicine Scholarships",
            "desc": "Scholarships for students in global health and social medicine programs.",
            "eligibility": "Open to international students with a strong academic record.",
            "lvl_study": "Masters",
            "location": "United Kingdom",
            "website": "https://www.kcl.ac.uk/study/postgraduate/fees-and-funding/scholarships/global-health-social-medicine-scholarships"
        },
        "University of Birmingham": {
            "name": "Medical and Dental Sciences Scholarships",
            "desc": "Support for students pursuing medical and dental programs.",
            "eligibility": "Based on academic merit, open to all nationalities.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.birmingham.ac.uk/schools/medical-dental/scholarships.aspx"
        },
        "University of Glasgow": {
            "name": "Medical School Scholarships",
            "desc": "Scholarships for students pursuing medical degrees.",
            "eligibility": "Available to students with outstanding academic records and financial need.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.gla.ac.uk/scholarships/"
        },
        "University of Manchester": {
            "name": "Manchester Medical School Scholarships",
            "desc": "Financial support for students enrolled in medical programs.",
            "eligibility": "Open to all students based on academic merit and financial need.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.manchester.ac.uk/undergraduate/fees-funding/scholarships/"
        },
        "University of Nottingham": {
            "name": "Nottingham Medical School Scholarships",
            "desc": "Scholarships for exceptional medical students.",
            "eligibility": "Available to students with high academic achievement.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.nottingham.ac.uk/ugstudy/fees-and-funding/scholarships.aspx"
        }
    },
    "humanities": {
        "University of York": {
            "name": "Wolfson Postgraduate Scholarships in Humanities",
            "desc": "Scholarships for students in history, literature, and languages.",
            "eligibility": "Open to UK/EU students demonstrating academic excellence.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.york.ac.uk/study/postgraduate-research/funding/wolfson-scholarships/"
        },
        "University of St Andrews": {
            "name": "St Andrews International Postgraduate Scholarships",
            "desc": "Support for international postgraduate students in humanities.",
            "eligibility": "Based on academic merit and financial need.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.st-andrews.ac.uk/study/fees-and-funding/scholarships/"
        },
        "University of Edinburgh": {
            "name": "Edinburgh Global Research Scholarships",
            "desc": "Funding for outstanding PhD students in humanities.",
            "eligibility": "Open to international students with strong academic records.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.ed.ac.uk/student-funding/postgraduate/international/global/research"
        },
        "University of Cambridge": {
            "name": "Cambridge International Scholarships",
            "desc": "Scholarships for international students undertaking a PhD in humanities.",
            "eligibility": "Available to students with an outstanding academic record.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.graduate.study.cam.ac.uk/finance/funding"
        },
        "University of Oxford": {
            "name": "Oxford University Humanities Scholarships",
            "desc": "Scholarships for PhD students in the humanities.",
            "eligibility": "Open to all students demonstrating high academic potential.",
            "lvl_study": "PhD",
            "location": "United Kingdom",
            "website": "https://www.ox.ac.uk/admissions/graduate/fees-and-funding/graduate-scholarships"
        }
    },
    "law": {
        "University of London": {
            "name": "University of London International Scholarships",
            "desc": "Funding for international students pursuing law degrees.",
            "eligibility": "Available to students with strong academic records and financial need.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.london.ac.uk/scholarships"
        },
        "University of Edinburgh": {
            "name": "Edinburgh Law School Scholarships",
            "desc": "Scholarships for students pursuing undergraduate and postgraduate law degrees.",
            "eligibility": "Open to students with strong academic achievements.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.ed.ac.uk/student-funding/undergraduate/law"
        },
        "University of Cambridge": {
            "name": "Cambridge Law Faculty Scholarships",
            "desc": "Scholarships for exceptional students in law programs.",
            "eligibility": "Available to students with excellent academic records.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.law.cam.ac.uk/study/undergraduate/scholarships"
        },
        "University of Oxford": {
            "name": "Oxford Law Scholarships",
            "desc": "Funding for undergraduate and postgraduate law students.",
            "eligibility": "Open to all nationalities, based on academic merit.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.law.ox.ac.uk/admissions/graduate/scholarships"
        },
        "King's College London": {
            "name": "King's College Law Scholarships",
            "desc": "Scholarships for students studying law at King's College London.",
            "eligibility": "Available to high-achieving students with financial need.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.kcl.ac.uk/study/undergraduate/fees-and-funding/scholarships/law"
        }
    },
    "fitness": {
        "University of Stirling": {
            "name": "Sport and Exercise Scholarships",
            "desc": "Support for students who excel in sports and exercise science.",
            "eligibility": "Open to students with demonstrated excellence in sports or academic achievements.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.stir.ac.uk/sport/exercise-scholarships/"
        },
        "University of Leeds": {
            "name": "Sport Scholarships",
            "desc": "Scholarships for exceptional student-athletes.",
            "eligibility": "Available to students with high performance in their respective sports.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.leeds.ac.uk/scholarships/sport"
        },
        "University of Birmingham": {
            "name": "Sports Scholarships",
            "desc": "Funding for students excelling in sports.",
            "eligibility": "Open to student-athletes with demonstrated success in their sport.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.birmingham.ac.uk/scholarships/sport.aspx"
        },
        "Loughborough University": {
            "name": "Loughborough Sports Scholarships",
            "desc": "Support for students with outstanding sporting talent.",
            "eligibility": "Available to students with significant achievements in their sport.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.lboro.ac.uk/sport/scholarships/"
        },
        "University of Bath": {
            "name": "Sport and Exercise Science Scholarships",
            "desc": "Scholarships for students in sport and exercise science programs.",
            "eligibility": "Open to students with high academic and athletic achievements.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.bath.ac.uk/campaigns/scholarships-for-sport-and-exercise-science/"
        }
    },
    "social_comms": {
        "University of Westminster": {
            "name": "Westminster International Scholarships",
            "desc": "Scholarships for international students in social sciences and communications.",
            "eligibility": "Based on academic merit and financial need.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.westminster.ac.uk/international-scholarships"
        },
        "London School of Economics and Political Science": {
            "name": "LSE Graduate Support Scheme",
            "desc": "Scholarships for students undertaking graduate studies in social sciences.",
            "eligibility": "Available to students with excellent academic records and financial need.",
            "lvl_study": "Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.lse.ac.uk/study-at-lse/graduate/fees-and-funding"
        },
        "University of Bristol": {
            "name": "Bristol International Office Scholarships",
            "desc": "Support for international students in social sciences and communications.",
            "eligibility": "Open to international students demonstrating academic excellence.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.bristol.ac.uk/international/fees-funding/"
        },
        "University of Glasgow": {
            "name": "International Leadership Scholarships",
            "desc": "Scholarships for outstanding international students in social sciences.",
            "eligibility": "Available to high-achieving students with leadership potential.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.gla.ac.uk/scholarships/international/"
        },
        "University of Edinburgh": {
            "name": "Edinburgh Global Undergraduate Maths Scholarships",
            "desc": "Scholarships for undergraduate students in social sciences, including communications.",
            "eligibility": "Open to international students demonstrating academic merit.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.ed.ac.uk/student-funding/undergraduate/international/global"
        }
    },
    "trav_tourism": {
        "University of Brighton": {
            "name": "International Scholarships for Travel and Tourism",
            "desc": "Funding for international students pursuing travel and tourism programs.",
            "eligibility": "Available to students with strong academic achievements and financial need.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.brighton.ac.uk/international/scholarships/index.aspx"
        },
        "University of Strathclyde": {
            "name": "Travel and Tourism Scholarships",
            "desc": "Support for students in travel and tourism programs.",
            "eligibility": "Open to students demonstrating high academic performance.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.strath.ac.uk/study/scholarships/"
        },
        "University of Sunderland": {
            "name": "Sunderland Travel and Tourism Scholarships",
            "desc": "Scholarships for students pursuing undergraduate and postgraduate travel and tourism studies.",
            "eligibility": "Based on academic merit and financial need.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.sunderland.ac.uk/study/fees-and-funding/scholarships/"
        },
        "University of Plymouth": {
            "name": "Plymouth International Scholarships for Travel and Tourism",
            "desc": "Support for international students in travel and tourism programs.",
            "eligibility": "Available to students with strong academic records.",
            "lvl_study": "Undergraduate/Postgraduate",
            "location": "United Kingdom",
            "website": "https://www.plymouth.ac.uk/scholarships"
        },
        "University of Leeds": {
            "name": "Leeds International Scholarships for Travel and Tourism",
            "desc": "Scholarships for exceptional international students in travel and tourism programs.",
            "eligibility": "Open to students with excellent academic achievements.",
            "lvl_study": "Undergraduate",
            "location": "United Kingdom",
            "website": "https://www.leeds.ac.uk/scholarships/"
        }
    }
}

def get_generic_scholarships():
    return schol_type['generic']