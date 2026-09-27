# ── GRADE BOOK ─────────────────────────────────────────────────

grades = {
    "aaral": 78,
    "lucy": 82,
    "airlie": 87,
    "kailah": 93,
    "amreet": 98
}

print("=" * 38)
print("       📚  STUDENT GRADE BOOK")
print("=" * 38)

# ── CLASS AVERAGE ──────────────────────────────────────────────

total = 0

for value in grades.values():
    total += value

average = total / len(grades)

print(f"Class Average: {average:.1f}")

# ── TOP AND BOTTOM ─────────────────────────────────────────────

top_student = max(grades, key=grades.get)
bottom_student = min(grades, key=grades.get)

print(f"Highest score: {top_student} ({grades[top_student]})")
print(f"Lowest score : {bottom_student} ({grades[bottom_student]})")
print()

# ── STUDENT LOOKUP ─────────────────────────────────────────────

name = input("Look up a student, enter name: ")

score = grades.get(name, None)

if score is not None:
    print(f"{name}'s score: {score}")
else:
    print(f"{name} was not found in the grade book.")