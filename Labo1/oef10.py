temperatuur = float(input("Geef een temperatuur in Celsius: "))
temperatuur_in_fahrenheir = (temperatuur * 9/5) + 32
temperatuur_in_kelvin = temperatuur + 273.15

print(f"""
{temperatuur}°C komt overeen met:
- {temperatuur_in_fahrenheir}°F (Fahrenheit)
- {temperatuur_in_kelvin} K (Kelvin)
""")