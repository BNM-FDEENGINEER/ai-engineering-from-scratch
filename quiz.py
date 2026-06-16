import json

with open("phases/00-setup-and-tooling/01-dev-environment/quiz.json") as f:
    data = json.load(f)

score = 0

print("\n=== AI Engineering Quiz ===\n")

for i, q in enumerate(data["questions"], 1):
    print(f"Q{i}: {q['question']}\n")

    for idx, opt in enumerate(q["options"]):
        print(f"{idx}. {opt}")

    try:
        answer = int(input("\nYour answer: "))
    except:
        print("❌ Invalid input\n")
        continue

    if answer == q["correct"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect")
        print(f"💡 {q['explanation']}\n")

    print("-" * 40)

print(f"\n✅ Final Score: {score}/{len(data['questions'])}")
