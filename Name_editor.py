# AUTHOR: orgkamolbek
# PROJECT: Name Analyzer

name = input("Ismingizni kiriting: ").strip().capitalize()

print(f"\nSalom, {name}! Men sizning ismingizni tahlil qilaman:")

# Ism uzunligini tekshirish
length = len(name)
print(f"- Ismingizda {length} ta harf bor.")

# Ism qanday harf bilan boshlanishini tekshirish
vowels = "AeIuOo' " # Unli harflar
if name[0] in vowels:
    print("- Ismingiz unli harf bilan boshlanadi.")
else:
    print("- Ismingiz undosh harf bilan boshlanadi.")

# Ismni teskari o'girish
reverse_name = name[::-1]
print(f"- Ismingizning teskarisi: {reverse_name}")

print(f"\n--- Tahlil tugadi, {name}! ---")