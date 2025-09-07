# 5 harften kısa olanları UPPERCASE yap, diğerlerini aynen bırak

words = ["sun", "planet", "sky", "galaxy", "moon"]
result = [w.upper() if len(w) < 5 else w for w in words ]

print(result)
