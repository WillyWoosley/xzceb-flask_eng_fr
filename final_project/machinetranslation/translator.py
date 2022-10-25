"""Module providing translations services using IBMWatson translation API"""
import os

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = "2018-05-01",
    authenticator = authenticator,
)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    """Translates English text to French using the IBMWatson cloud service"""
    if englishText is None:
        raise ValueError("Translation text cannot be None")

    if len(englishText) == 0:
        return ""

    translation = language_translator.translate(
        text = englishText,
        model_id = "en-fr",
    ).get_result()
    french_text = translation["translations"][0]["translation"]

    return french_text

def frenchToEnglish(frenchText):
    """Translates French text to English using the IBMWatson cloud service"""
    if frenchText is None:
        raise ValueError("Translation text cannot be None")

    if len(frenchText) == 0:
        return ""

    translation = language_translator.translate(
        text = frenchText,
        model_id = "fr-en",
    ).get_result()
    english_text = translation["translations"][0]["translation"]

    return english_text
