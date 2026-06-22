from groq_helper import (
    generate_project_ideas, # generate project ideas using ai
    generate_project_details #generates complete project blueprint
)

print("=" * 60)
print("🚀 AI PROJECT MENTOR")
print("=" * 60)

domain = input("Enter Domain: ")
difficulty = input("Enter Difficulty: ")
duration = input("Enter Duration: ")

print("\nGenerating Project Ideas...\n")

ideas = generate_project_ideas(domain, difficulty, duration)

print("\n" + "=" * 60)
print("🚀 RECOMMENDED PROJECTS")
print("=" * 60)


for line in ideas.split("\n"): 
    parts = line.split("|")
    if len(parts) == 3:

        number = parts[0].strip() # removes extra space
        name = parts[1].strip()
        desc = parts[2].strip()

        print(f"\n[{number}] {name}")
        print(f"    ➜ {desc}")

print("\n[4] Exit")
print("    ➜ Close the application")
print("\n" + "=" * 60)

choice = input("\n👉 Select Project Number (1-4): ")
if choice == "4":
    print("\n👋 Thank you for using AI Project Mentor!")
    exit()

project_map = {} #creates an empty dictionary

for line in ideas.split("\n"):
    parts = line.split("|")

    if len(parts) == 3:
        project_map[parts[0].strip()] = parts[1].strip()

project_name = project_map.get(choice) 

if not project_name:
    print("❌ Invalid Choice")
    exit()

print("\nGenerating Blueprint...\n")

details = generate_project_details(project_name)

print("=" * 60)
print("🚀 PROJECT BLUEPRINT")
print("=" * 60)

print("\n")
print("🔥 GENERATING COMPLETE PROJECT BLUEPRINT...")
print()

print("=" * 70)
print("🚀 PROJECT MENTOR REPORT")
print("=" * 70)
print(details)

print("\n" + "=" * 70)
print("✅ REPORT GENERATED SUCCESSFULLY")
print("=" * 70)

print("=" * 60)