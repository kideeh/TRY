# herbs_data.py
# 52 conditions dataset (English + Kiswahili). 

HERBS_DATA = {
    "Common Cold": {
        "keywords": ["sneezing", "runny nose", "sore throat", "cough"],
        "herbs": {"English": ["Ginger", "Lemon", "Honey"], "Kiswahili": ["Tangawizi", "Ndimu", "Asali"]},
        "actions": ["Drink warm herbal tea", "Rest", "Stay hydrated"],
        "safety": "If fever persists >3 days, see a doctor."
    },
    "Flu": {
        "keywords": ["fever", "body ache", "cough", "chills"],
        "herbs": {"English": ["Ginger", "Garlic", "Lemon"], "Kiswahili": ["Tangawizi", "Kitunguu saumu", "Ndimu"]},
        "actions": ["Rest", "Fluids", "Warm teas"],
        "safety": "Seek care for breathing difficulty or very high fever."
    },
    "Malaria": {
        "keywords": ["fever", "chills", "sweating", "rigors"],
        "herbs": {"English": ["Artemisia", "Neem", "Lemongrass"], "Kiswahili": ["Artemisia", "Mwarobaini", "Lemongrass"]},
        "actions": ["Test for malaria", "Rest", "Hydration"],
        "safety": "High fever needs prompt hospital care."
    },
    "Typhoid": {
        "keywords": ["abdominal pain", "fever", "weakness", "loss of appetite"],
        "herbs": {"English": ["Neem", "Clove", "Garlic"], "Kiswahili": ["Mwarobaini", "Karafuu", "Kitunguu saumu"]},
        "actions": ["Maintain hygiene", "Hydration", "Seek medical care if severe"],
        "safety": "Seek hospital care for prolonged high fever."
    },
    "Diarrhea": {
        "keywords": ["loose stool", "stomach cramps", "dehydration"],
        "herbs": {"English": ["Guava leaves", "Ginger", "Banana"], "Kiswahili": ["Majani ya mpera", "Tangawizi", "Ndizi"]},
        "actions": ["Oral rehydration", "Soft foods", "Guava leaf tea"],
        "safety": "If lasts >2 days or blood in stool, seek care."
    },
    "Dysentery": {
        "keywords": ["bloody stool", "severe abdominal pain", "fever"],
        "herbs": {"English": ["Guava leaf", "Neem"], "Kiswahili": ["Majani ya mpera", "Mwarobaini"]},
        "actions": ["Hydration", "Seek medical attention"],
        "safety": "Urgent care if severe dehydration or bloody stool."
    },
    "Indigestion": {
        "keywords": ["bloating", "heartburn", "acid", "sour taste"],
        "herbs": {"English": ["Ginger", "Chamomile", "Fennel"], "Kiswahili": ["Tangawizi", "Chamomile", "Mfenel"]},
        "actions": ["Avoid spicy foods", "Small meals", "Ginger tea"],
        "safety": "Seek care if severe pain or vomiting blood."
    },
    "Acid Reflux": {
        "keywords": ["heartburn", "burning chest", "regurgitation"],
        "herbs": {"English": ["Aloe vera", "Chamomile", "Ginger"], "Kiswahili": ["Mshubiri", "Chamomile", "Tangawizi"]},
        "actions": ["Elevate head when sleeping", "Avoid trigger foods"],
        "safety": "Severe symptoms require medical review."
    },
    "Ulcer": {
        "keywords": ["stomach pain", "burning stomach", "ulcer"],
        "herbs": {"English": ["Aloe vera", "Licorice", "Banana"], "Kiswahili": ["Mshubiri", "Licorice", "Ndizi"]},
        "actions": ["Avoid NSAIDs", "Eat small meals"],
        "safety": "Black stools or severe pain — seek care."
    },
    "Headache": {
        "keywords": ["headache", "migraine", "throbbing head"],
        "herbs": {"English": ["Peppermint", "Feverfew", "Lavender"], "Kiswahili": ["Mint", "Feverfew", "Lavender"]},
        "actions": ["Rest", "Hydration", "Peppermint inhalation"],
        "safety": "Seek urgent care for sudden severe headache."
    },
    "Migraine": {
        "keywords": ["migraine", "aura", "sensitive to light"],
        "herbs": {"English": ["Feverfew", "Butterbur", "Peppermint"], "Kiswahili": ["Feverfew", "Butterbur", "Mint"]},
        "actions": ["Rest in dark room", "Hydrate", "Cold compress"],
        "safety": "See doctor for persistent migraines."
    },
    "Hypertension": {
        "keywords": ["high blood pressure", "dizziness", "headache"],
        "herbs": {"English": ["Garlic", "Hibiscus", "Celery"], "Kiswahili": ["Kitunguu saumu", "Hibiscus", "Celery"]},
        "actions": ["Reduce salt", "Exercise", "Monitor BP"],
        "safety": "Follow prescribed medications from a clinician."
    },
    "Hypotension": {
        "keywords": ["low blood pressure", "fainting", "lightheaded"],
        "herbs": {"English": ["Licorice (cautious)"], "Kiswahili": ["Licorice"]},
        "actions": ["Increase fluids", "Slow position changes"],
        "safety": "Persistent fainting — see a clinician."
    },
    "Diabetes": {
        "keywords": ["thirst", "frequent urination", "blurred vision"],
        "herbs": {"English": ["Moringa", "Bitter gourd", "Cinnamon"], "Kiswahili": ["Mlonge", "Karela", "Mdalasini"]},
        "actions": ["Monitor sugar", "Exercise", "Diet control"],
        "safety": "Regular medical monitoring required."
    },
    "Asthma": {
        "keywords": ["wheezing", "shortness of breath", "chest tightness"],
        "herbs": {"English": ["Ginger", "Peppermint", "Licorice"], "Kiswahili": ["Tangawizi", "Mint", "Licorice"]},
        "actions": ["Avoid triggers", "Steam inhalation", "Follow inhaler plan"],
        "safety": "Severe attack — seek emergency care."
    },
    "Bronchitis": {
        "keywords": ["productive cough", "chest congestion", "phlegm"],
        "herbs": {"English": ["Honey", "Ginger", "Thyme"], "Kiswahili": ["Asali", "Tangawizi", "Thyme"]},
        "actions": ["Steam", "Hydration", "Warm teas"],
        "safety": "High fever or breathing difficulty — see a doctor."
    },
    "Pneumonia": {
        "keywords": ["difficulty breathing", "chest pain", "high fever"],
        "herbs": {"English": ["Eucalyptus", "Garlic", "Ginger"], "Kiswahili": ["Eucalyptus", "Kitunguu saumu", "Tangawizi"]},
        "actions": ["Seek medical care", "Keep warm", "Hydration"],
        "safety": "Medical attention urgently recommended."
    },
    "Sinusitis": {
        "keywords": ["sinus pain", "facial pressure", "blocked nose"],
        "herbs": {"English": ["Peppermint", "Eucalyptus", "Ginger"], "Kiswahili": ["Mint", "Eucalyptus", "Tangawizi"]},
        "actions": ["Steam inhalation", "Saline rinses"],
        "safety": "Persistent pain or vision changes — see clinician."
    },
    "Allergy": {
        "keywords": ["itchy eyes", "sneezing", "hives"],
        "herbs": {"English": ["Nettle", "Butterbur", "Chamomile"], "Kiswahili": ["Nettle", "Butterbur", "Chamomile"]},
        "actions": ["Avoid allergen", "Antihistamines (if advised)"],
        "safety": "Anaphylaxis requires emergency care."
    },
    "Skin Rash": {
        "keywords": ["rash", "itching", "redness"],
        "herbs": {"English": ["Aloe vera", "Neem", "Turmeric"], "Kiswahili": ["Mshubiri", "Mwarobaini", "Manjano"]},
        "actions": ["Keep clean", "Apply aloe vera gel"],
        "safety": "Rapid spreading or fever — seek care."
    },
    "Eczema": {
        "keywords": ["dry skin", "itchy patches", "eczema"],
        "herbs": {"English": ["Oatmeal baths", "Aloe vera", "Chamomile"], "Kiswahili": ["Oatmeal", "Mshubiri", "Chamomile"]},
        "actions": ["Moisturize", "Avoid irritants"],
        "safety": "Seek dermatologist for severe cases."
    },
    "Psoriasis": {
        "keywords": ["silvery scales", "thick patches"],
        "herbs": {"English": ["Aloe vera", "Turmeric"], "Kiswahili": ["Mshubiri", "Manjano"]},
        "actions": ["Moisturize", "Avoid triggers"],
        "safety": "Chronic condition — specialist care advised."
    },
    "Acne": {
        "keywords": ["pimples", "blackheads", "whiteheads"],
        "herbs": {"English": ["Tea tree oil (diluted)", "Neem"], "Kiswahili": ["Tea tree", "Mwarobaini"]},
        "actions": ["Gentle cleansing", "Avoid heavy cosmetics"],
        "safety": "Severe cystic acne — see clinician."
    },
    "UTI": {
        "keywords": ["burning urination", "frequent urination", "urine smell"],
        "herbs": {"English": ["Cranberry", "Garlic", "Parsley"], "Kiswahili": ["Cranberry", "Kitunguu saumu", "Parsley"]},
        "actions": ["Hydration", "See clinician for antibiotics if needed"],
        "safety": "Fever or back pain — urgent care."
    },
    "Kidney Stones": {
        "keywords": ["severe flank pain", "blood in urine", "colic pain"],
        "herbs": {"English": ["Lemon water", "Nettle"], "Kiswahili": ["Ndimu", "Nettle"]},
        "actions": ["Hydration", "Seek medical imaging if severe"],
        "safety": "Severe pain or inability to pass urine — emergency."
    },
    "Arthritis": {
        "keywords": ["joint pain", "stiffness", "swelling"],
        "herbs": {"English": ["Turmeric", "Ginger", "Boswellia"], "Kiswahili": ["Manjano", "Tangawizi", "Boswellia"]},
        "actions": ["Warm compress", "Gentle exercise"],
        "safety": "Chronic swelling needs clinician review."
    },
    "Gout": {
        "keywords": ["sudden joint pain", "big toe pain", "red swollen joint"],
        "herbs": {"English": ["Cherry", "Turmeric"], "Kiswahili": ["Cherry", "Manjano"]},
        "actions": ["Limit purine foods", "Hydration"],
        "safety": "Severe attacks — see clinician."
    },
    "Back Pain": {
        "keywords": ["lower back pain", "stiff back", "sciatica"],
        "herbs": {"English": ["Turmeric", "Ginger", "Arnica (topical)"], "Kiswahili": ["Manjano", "Tangawizi", "Arnica"]},
        "actions": ["Gentle stretching", "Heat therapy"],
        "safety": "Numbness, weakness or bowel/bladder changes — urgent care."
    },
    "Toothache": {
        "keywords": ["tooth pain", "toothache", "sensitive tooth"],
        "herbs": {"English": ["Clove oil", "Garlic"], "Kiswahili": ["Karafuu", "Kitunguu saumu"]},
        "actions": ["Saltwater rinse", "See dentist"],
        "safety": "Severe swelling or fever — urgent dental care."
    },
    "Sore Throat": {
        "keywords": ["sore throat", "painful swallow", "pharyngitis"],
        "herbs": {"English": ["Honey", "Gargle salt water", "Ginger"], "Kiswahili": ["Asali", "Chumvi ya kumwagika", "Tangawizi"]},
        "actions": ["Warm drinks", "Salt gargle"],
        "safety": "Trouble breathing — seek emergency care."
    },
    "Tonsillitis": {
        "keywords": ["swollen tonsils", "sore throat", "fever"],
        "herbs": {"English": ["Garlic", "Honey"], "Kiswahili": ["Kitunguu saumu", "Asali"]},
        "actions": ["Hydration", "See clinician if persistent"],
        "safety": "Difficulty breathing or severe fever — urgent."
    },
    "Ear Infection": {
        "keywords": ["ear pain", "ear discharge", "hearing loss"],
        "herbs": {"English": ["Garlic oil (careful)", "Warm compress"], "Kiswahili": ["Kitunguu saumu", "Compress ya joto"]},
        "actions": ["See clinician for ear exam"],
        "safety": "High fever or severe pain — urgent."
    },
    "Conjunctivitis": {
        "keywords": ["red eye", "eye discharge", "itchy eyes"],
        "herbs": {"English": ["Chamomile compress", "Clean water rinses"], "Kiswahili": ["Chamomile", "Maji safi"]},
        "actions": ["Avoid touching eyes", "Cleanliness"],
        "safety": "Severe pain or vision change — see clinician."
    },
    "Insomnia": {
        "keywords": ["can't sleep", "sleeplessness", "restless night"],
        "herbs": {"English": ["Chamomile", "Valerian", "Lavender"], "Kiswahili": ["Chamomile", "Valerian", "Lavender"]},
        "actions": ["Sleep routine", "Avoid caffeine"],
        "safety": "Chronic insomnia — seek medical advice."
    },
    "Anxiety": {
        "keywords": ["anxiety", "nervousness", "panic"],
        "herbs": {"English": ["Lemon balm", "Chamomile", "Lavender"], "Kiswahili": ["Lemon balm", "Chamomile", "Lavender"]},
        "actions": ["Breathing exercises", "Counseling"],
        "safety": "Severe panic or self-harm thoughts — seek immediate help."
    },
    "Depression": {
        "keywords": ["low mood", "hopelessness", "loss of interest"],
        "herbs": {"English": ["St. John's Wort (interacts with meds)", "Rhodiola"], "Kiswahili": ["St. John's Wort", "Rhodiola"]},
        "actions": ["Social support", "Professional help"],
        "safety": "Suicidal thoughts — seek urgent help."
    },
    "Menstrual Cramps": {
        "keywords": ["period pain", "cramps", "dysmenorrhea"],
        "herbs": {"English": ["Ginger", "Cinnamon", "Chamomile"], "Kiswahili": ["Tangawizi", "Mdalasini", "Chamomile"]},
        "actions": ["Heat pad", "Gentle exercise"],
        "safety": "Heavy bleeding or severe pain — see clinician."
    },
    "Infertility (general)": {
        "keywords": ["fertility issues", "can't conceive"],
        "herbs": {"English": ["Maca (consult clinician)", "Vitex"], "Kiswahili": ["Maca", "Vitex"]},
        "actions": ["Medical evaluation", "Healthy lifestyle"],
        "safety": "See fertility specialist for investigation."
    },
    "Vaginal Infection": {
        "keywords": ["vaginal discharge", "itching", "odor"],
        "herbs": {"English": ["Yogurt (probiotics)", "Tea tree oil (diluted)"], "Kiswahili": ["Yogurt", "Tea tree"]},
        "actions": ["See clinician for diagnosis", "Avoid self-medication"],
        "safety": "Pain or fever — seek care."
    },
    "Prostatitis": {
        "keywords": ["pelvic pain", "urinary symptoms", "fever"],
        "herbs": {"English": ["Saw palmetto", "Pumpkin seed"], "Kiswahili": ["Saw palmetto", "Pumpkin seed"]},
        "actions": ["See clinician", "Hydration"],
        "safety": "Fever or severe pain — urgent care."
    },
    "Cold Sores": {
        "keywords": ["blisters on lip", "tingling lip", "cold sore"],
        "herbs": {"English": ["Lemon balm", "Aloe vera"], "Kiswahili": ["Lemon balm", "Mshubiri"]},
        "actions": ["Topical care", "Avoid sharing utensils"],
        "safety": "Severe spreading — see clinician."
    },
    "Fungal Nail": {
        "keywords": ["thick nail", "discolored nail", "fungal nail"],
        "herbs": {"English": ["Tea tree oil (diluted)", "Vinegar soaks"], "Kiswahili": ["Tea tree", "Siki"]},
        "actions": ["Keep nails dry", "Topical treatments"],
        "safety": "See podiatrist for severe cases."
    },
    "Ringworm": {
        "keywords": ["ring-shaped rash", "scaly patch"],
        "herbs": {"English": ["Turmeric paste", "Neem"], "Kiswahili": ["Manjano", "Mwarobaini"]},
        "actions": ["Keep area clean", "Topical remedies"],
        "safety": "Spreading rash — see clinician."
    },
    "Contact Dermatitis": {
        "keywords": ["itchy rash after contact", "blisters"],
        "herbs": {"English": ["Oatmeal baths", "Aloe vera"], "Kiswahili": ["Oatmeal", "Mshubiri"]},
        "actions": ["Wash area", "Avoid scratching"],
        "safety": "Severe swelling or breathing trouble — emergency."
    },
    "Motion Sickness": {
        "keywords": ["nausea in vehicle", "dizziness on travel"],
        "herbs": {"English": ["Ginger", "Peppermint"], "Kiswahili": ["Tangawizi", "Mint"]},
        "actions": ["Fresh air", "Ginger candy or tea"],
        "safety": "Severe vomiting — see clinician."
    },
    "Nausea": {
        "keywords": ["nausea", "feeling sick", "want to vomit"],
        "herbs": {"English": ["Ginger", "Peppermint"], "Kiswahili": ["Tangawizi", "Mint"]},
        "actions": ["Small sips of clear fluids", "Ginger tea"],
        "safety": "Persistent vomiting — seek care."
    },
    "Hemorrhoids": {
        "keywords": ["bleeding from anus", "painful lump", "hemorrhoid"],
        "herbs": {"English": ["Witch hazel", "Aloe vera"], "Kiswahili": ["Witch hazel", "Mshubiri"]},
        "actions": ["Sitz baths", "Fiber and fluids"],
        "safety": "Heavy bleeding — seek medical attention."
    },
    "Anemia": {
        "keywords": ["fatigue", "pale", "weakness"],
        "herbs": {"English": ["Iron-rich foods", "Moringa"], "Kiswahili": ["Vyenye chuma", "Mlonge"]},
        "actions": ["Dietary iron", "See clinician for testing"],
        "safety": "Severe symptoms — urgent evaluation."
    },
    "Cold Hands/Feet": {
        "keywords": ["cold hands", "cold feet", "poor circulation"],
        "herbs": {"English": ["Ginger", "Cayenne (cautious)"], "Kiswahili": ["Tangawizi", "Cayenne"]},
        "actions": ["Keep warm", "Exercise"],
        "safety": "Persistent ischemia — seek clinician."
    },
    "Nosebleed": {
        "keywords": ["nose bleed", "epistaxis"],
        "herbs": {"English": ["Apply pressure", "Keep head forward"], "Kiswahili": ["Shinikiza pua", "Kaa mbele"]},
        "actions": ["Pinch nose for 10-15 minutes", "Seek care if recurrent"],
        "safety": "Heavy bleeding or after head injury — emergency."
    },
    "Hypoglycemia": {
        "keywords": ["sweating", "shakiness", "low blood sugar"],
        "herbs": {"English": ["Quick sugar (juice)"], "Kiswahili": ["Juisi ya sukari"]},
        "actions": ["Give fast-acting sugar", "Seek medical help if severe"],
        "safety": "Loss of consciousness — emergency."
    }
}
