# Project KITSUNE
# URL Feature Extraction Module

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

    return score  
    

url = input("Enter a URL: ")

print("\n----- URL ANALYSIS -----")
print("URL Length      :", url_length(url))
print("Uses HTTPS      :", has_https(url))
print("Number of Dots  :", count_dots(url))
print("Hyphens         :", count_hyphens(url))
print("@ Symbol        :", has_at_symbol(url))
print("Contains Numbers:", has_numbers(url))
print("Suspicious Score :", calculate_score(url))
score = calculate_score(url)

if score >= 3:
    print("Verdict : ⚠️ Potentially Suspicious")
else:
    print("Verdict : ✅ Looks Safe")