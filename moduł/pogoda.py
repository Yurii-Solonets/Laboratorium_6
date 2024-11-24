import temperatura

temp_c = 21
temp_f = 89

print(f"{temp_c}°C to {temperatura.c_to_f(temp_c):.2f}°F")
print(f"{temp_f}°F to {temperatura.f_to_c(temp_f):.2f}°F")
print(f"35°F to {temperatura.c_to_k(35):.2f}°K")