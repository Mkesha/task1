time = int(input("Enter your time in sec "))
hours = time // 3600
residue = time % 3600
minutes = residue // 60
sec = residue % 60
print(f"{hours}:{minutes}:{sec} ")