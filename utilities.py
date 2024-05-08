"saud4003@gmail.com"

def rawToEmail(rawEmail):
    pass

def emailToRaw(email):
    pass


major_dict = {
    'MATH': 'الرياضيات',
    'AS': 'العلوم الإكتوارية',
    'COE': 'هندسة الحاسب',
    'ICS': 'علوم الحاسب',
    'SWE': 'هندسة البرمجيات',
    'ISE': 'الهندسة الصناعية',
    'EE': 'الهندسة الكهربائية',
    'ME': 'الهندسة الميكانيكية',
    'AE': 'هندسة الطيران والفضاء',
    'PHYS': 'الفيزياء',
    'CIE': 'هندسة التحكم والقياس',
    'FIN': 'المالية',
    'ACCT': 'المحاسبة',
    'MIS': 'نظم المعلومات الإدارية',
    'MGT': 'الإدارة',
    'MKT': 'التسويق',
    'CHEM': 'الكيمياء',
    'CHE': 'الهندسة الكيميائية',
    'MSE': 'هندسة المواد',
    'ARE': 'الهندسة المعمارية',
    'ARC': 'العمارة',
    'CE': 'الهندسة المدنية',
    'PETE': 'هندسة البترول',
    'GEO': 'الجيولوجيا',
    'GEOP': 'الجيوفيزياء',
}

# Dictionary for standings
standing_dict = {
    'prep': 'تحضيري',
    'freshmen': 'السنة الأولى',
    'sophomore': 'السنة الثانية',
    'junior': 'السنة الثالثة',
    'senior': 'السنة الرابعة',
    'graduate': 'خريج'
}

# Dictionary for academic history
history_dict = {
    'low': 'منخفض دائمًا',
    'high_then_low': 'مرتفع ثم منخفض',
    'low_then_high': 'منخفض ثم مرتفع',
    'always_high': 'مرتفع دائمًا'
}

# Dictionary for cities
city_dict = {
    'MCC': 'مكة',
    'MDN': 'المدينة المنورة',
    'RYD': 'الرياض',
    'JED': 'جدة',
    'DMM': 'الدمام',
    'HAS': 'الأحساء',
    'JUB': 'الجبيل',
    'TAF': 'الطائف',
    'ULA': 'العلا',
    'TBK': 'تبوك',
    'AJF': 'الجوف',
    'HAI': 'حائل',
    'HAF': 'حفر الباطن',
    'QSM': 'القصيم',
    'ASR': 'عسير',
    'BAH': 'الباحة',
    'JZN': 'جازان',
    'NJN': 'نجران'
}

# Dictionary for housing
housing_dict = {
    'on-campus': 'داخل الحرم الجامعي',
    'out-of-campus': 'خارج الحرم الجامعي'
}

apearance_dict = {
    'SHOW': 'الظهور',
    'HIDE': 'عدم الظهور'
}

dictOfDicts = {"major": major_dict, "standing": standing_dict, "history": history_dict, "city": city_dict, "housing": housing_dict, "appearance":apearance_dict}
