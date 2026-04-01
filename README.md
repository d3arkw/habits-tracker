📈 Habit Tracker

A simple backend-oriented Python project for tracking daily habits with JSON-based storage.

⸻

📌 Description

This project allows you to create habits, track daily completion, and maintain streaks.
All data is stored locally in a JSON file, simulating a simple backend persistence layer.

⸻

⚙️ Features
 • Add and delete habits
 • Mark habits as completed
 • Automatic streak calculation
 • JSON-based data storage
 • Error handling (invalid input, edge cases)
 • Basic date tracking

⸻

🧠 How It Works
 • Each habit is stored in a JSON structure
 • When a habit is completed:
 • If it’s the next day → streak increases
 • If skipped → streak resets
 • The system tracks last completion date

⸻

🛠 Tech Stack
 • Python
 • JSON

 ⸻

🖼 Screenshots

 ⸻

📄 Example Data

{
  "habits": [
    {
      "name": "Training",
      "streak": 6,
      "last_done": "2026.04.01"
    }
  ]
}

⸻

▶️ How to Run

git clone https://github.com/d3arkw/habit-tracker
cd habit-tracker
python main.py

⸻

📁 Project Structure

habit-tracker/
│── main.py
│── example.json
│── assets/

⸻

🚀 Future Improvements
 • CLI improvements
 • Better data validation
 • Transition to database (SQLite)