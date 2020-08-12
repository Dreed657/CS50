s = set()

s.add(3)
s.add(1)
s.add(2)

print(f"Elements {s} with length {len(s)}")

s.add(3 )

print(f"Elements {s} with length {len(s)}")

s.remove(3)

print(f"Elements {s} with length {len(s)}")