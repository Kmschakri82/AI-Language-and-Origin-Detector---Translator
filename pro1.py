from langdetect import detect
import pycountry
from deep_translator import GoogleTranslator

# Manual mapping for common languages → countries
lang_to_country = {
    "en": "United States, UK, India, Australia",
    "te": "India (Andhra Pradesh, Telangana)",
    "hi": "India",
    "fr": "France, Canada, Belgium",
    "es": "Spain, Mexico, Latin America",
    "de": "Germany, Austria, Switzerland",
    "zh": "China, Taiwan",
    "ar": "Middle East, North Africa",
    "ru": "Russia, Belarus, Kazakhstan",
    "ja": "Japan",
    "ko": "South Korea",
}

# Input text
text = input("Enter a sentence: ")

# Detect language code
lang_code = detect(text)

# Fix codes
code_fix = {"jw": "jv", "zh-cn": "zh", "zh-tw": "zh"}
lang_code = code_fix.get(lang_code, lang_code)

# Get full language name
try:
    lang_name = pycountry.languages.get(alpha_2=lang_code).name
except:
    try:
        lang_name = pycountry.languages.get(alpha_3=lang_code).name
    except:
        lang_name = "Unknown Language"

# Get country/region info
country_info = lang_to_country.get(lang_code, "Region info not available")

# Translate using deep-translator
try:
    translation = GoogleTranslator(source='auto', target='en').translate(text)
except:
    translation = "Translation not available"

# Output
print("\n--- Language Detection Result ---")
print(f"Input Text: {text}")
print(f"Detected Language Code: {lang_code}")
print(f"Language Name: {lang_name}")
print(f"Commonly Used In: {country_info}")
print(f"Translation to English: {translation}")
