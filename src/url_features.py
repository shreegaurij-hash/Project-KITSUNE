# Project KITSUNE
# URL Feature Extraction Module
import re
from urllib.parse import urlparse

def url_length(url):
    return len(url)

def has_https(url):
    return url.startswith("https://")

def count_dots(url):
    return url.count(".")

def count_hyphens(url):
    return url.count("-")

def has_at_symbol(url):
    return "@" in url

def has_numbers(url):
    for character in url:
        if character.isdigit():
            return True
    return False  
 
def count_slashes(url):
    return url.count("/")


def count_underscores(url):
    return url.count("_")


def count_question_marks(url):
    return url.count("?")


def count_equals(url):
    return url.count("=")


def count_percent(url):
    return url.count("%")


def count_ampersands(url):
    return url.count("&")


def has_ip_address(url):
    pattern = r'(\d{1,3}\.){3}\d{1,3}'
    return bool(re.search(pattern, url))


def subdomain_count(url):
    domain = urlparse(url).netloc
    return max(0, domain.count(".") - 1)

def calculate_score(url):
    score = 0

    if not has_https(url):
        score += 1

    if has_at_symbol(url):
        score += 2

    if count_hyphens(url) > 2:
        score += 1

    if has_numbers(url):
        score += 1

    if has_ip_address(url):
        score += 3

    if subdomain_count(url) > 2:
        score += 2

    if count_question_marks(url) > 1:
        score += 1

    if count_equals(url) > 2:
        score += 1

    if count_percent(url) > 0:
        score += 1

    return score
    
def analyze_url(url):
    return {
        "URL Length": url_length(url),
        "HTTPS": has_https(url),
        "Dots": count_dots(url),
        "Hyphens": count_hyphens(url),
        "@ Symbol": has_at_symbol(url),
        "Numbers": has_numbers(url),
        "Slashes": count_slashes(url),
        "Underscores": count_underscores(url),
        "Question Marks": count_question_marks(url),
        "Equal Signs": count_equals(url),
        "Percent Signs": count_percent(url),
        "Ampersands": count_ampersands(url),
        "IP Address": has_ip_address(url),
        "Subdomains": subdomain_count(url),
        "Risk Score": calculate_score(url)
    }

def explain_risk(url): #explainability
    reasons = []

    if not has_https(url):
        reasons.append("Website is not using HTTPS.")

    if has_ip_address(url):
        reasons.append("URL uses an IP address instead of a domain name.")

    if has_at_symbol(url):
        reasons.append("URL contains '@', which can hide the real destination.")

    if count_hyphens(url) > 2:
        reasons.append("URL contains many hyphens.")

    if subdomain_count(url) > 2:
        reasons.append("Too many subdomains detected.")

    if has_numbers(url):
        reasons.append("URL contains numbers.")

    if url_length(url) > 75:
        reasons.append("URL is unusually long.")

    if count_question_marks(url) > 1:
        reasons.append("URL contains multiple query parameters.")

    if not reasons:
        reasons.append("No major suspicious characteristics detected.")

    return reasons
