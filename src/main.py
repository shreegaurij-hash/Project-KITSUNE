from url_features import *

url = input("Enter a URL: ")

results = analyze_url(url)

print("\n========== PROJECT KITSUNE ==========")

for feature, value in results.items():
    print(f"{feature:<20}: {value}")

score = calculate_score(url)

print("\nSuspicious Score  :", score)

if score <= 2:
    print("Verdict           : ✅ Low Risk")

elif score <= 5:
    print("Verdict           : ⚠️ Medium Risk")

else:
    print("Verdict           : 🚨 High Risk (Possible Phishing)")

print("\nWhy?")
print("-" * 40)

for reason in explain_risk(url):
    print("•", reason)