import random
import tkinter as tk
from tkinter import messagebox

recommendations = {

    "English": {
        "Movie": {
            "Happy": ["La La Land", "The Intern"],
            "Sad": ["The Pursuit of Happyness"],
            "Excited": ["Avengers"],
            "Comedy": ["The Mask"],
            "Horror": ["The Conjuring"],
            "Motivational": ["Rocky"]
        },

        "Music": {
            "Happy": ["Happy - Pharrell Williams"],
            "Sad": ["Someone Like You - Adele"],
            "Excited": ["Believer - Imagine Dragons"],
            "Comedy": ["Can't Stop the Feeling"],
            "Motivational": ["Hall of Fame"],
            "Horror": ["Thriller - Michael Jackson"]
        },

        "Book": {
            "Happy": ["Harry Potter"],
            "Sad": ["The Fault in Our Stars"],
            "Excited": ["Sherlock Holmes"],
            "Horror": ["Dracula"],
            "Motivational": ["The Alchemist"],
            "Comedy": ["The Hitchhiker's Guide to the Galaxy"]
        }
    },

    "Hindi": {
        "Movie": {
            "Happy": ["3 Idiots"],
            "Sad": ["Kal Ho Naa Ho"],
            "Excited": ["Pathaan"],
            "Comedy": ["Hera Pheri"],
            "Horror": ["Bhool Bhulaiyaa"],
            "Motivational": ["Dangal"]
        },

        "Music": {
            "Happy": ["Ilahi"],
            "Sad": ["Agar Tum Saath Ho"],
            "Excited": ["Malhari"],
            "Comedy": ["Gallan Goodiyan"],
            "Motivational": ["Kar Har Maidan Fateh"],
            "Horror": ["Ami Je Tomar - Bhool Bhulaiyaa"]
        },

        "Book": {
            "Happy": ["Malgudi Days"],
            "Sad": ["Gaban"],
            "Excited": ["Chanakya Neeti"],
            "Motivational": ["Wings of Fire"],
            "Comedy": ["Panchatantra"],
            "Horror": ["Tales of Supernatural"]
        }
    }
}

quotes = {
    "Happy": "Keep smiling and spread positivity 😊",
    "Sad": "Every storm passes. Stay strong 💪",
    "Excited": "Channel your energy into greatness 🚀",
    "Comedy": "Laughter is the best medicine 😂",
    "Horror": "Enjoy the thrill if you dare 👻",
    "Motivational": "Believe in yourself and achieve greatness 🌟"
}


def recommend():

    name = name_var.get()
    lang = language_var.get()
    interest = interest_var.get()
    mood = mood_var.get()

    suggestion = random.choice(recommendations[lang][interest][mood])
    quote = quotes[mood]

    messagebox.showinfo(
        "Your Recommendation 🎉",
        f"Hello {name}!\n\nInterest: {interest}\nMood: {mood}\n\nRecommendation:\n{suggestion}\n\nQuote:\n{quote}"
    )


def surprise():

    lang = random.choice(["English", "Hindi"])
    interest = random.choice(["Movie", "Music", "Book"])
    mood = random.choice(["Happy", "Sad", "Excited", "Comedy", "Horror", "Motivational"])

    suggestion = random.choice(recommendations[lang][interest][mood])

    messagebox.showinfo(
        "Surprise Recommendation 🎲",
        f"Language: {lang}\nInterest: {interest}\nMood: {mood}\n\nTry this:\n{suggestion}"
    )


app = tk.Tk()
app.title("MoodMatch Recommendation System")
app.geometry("420x400")

tk.Label(app, text="Enter Your Name").pack()

name_var = tk.StringVar()
tk.Entry(app, textvariable=name_var).pack()

tk.Label(app, text="Select Interest").pack()

interest_var = tk.StringVar(value="Movie")
tk.OptionMenu(app, interest_var, "Movie", "Music", "Book").pack()

tk.Label(app, text="Select Language").pack()

language_var = tk.StringVar(value="English")
tk.OptionMenu(app, language_var, "English", "Hindi").pack()

tk.Label(app, text="Select Your Mood").pack()

mood_var = tk.StringVar(value="Happy")
tk.OptionMenu(app, mood_var,
              "Happy", "Sad", "Excited",
              "Comedy", "Horror", "Motivational").pack()

tk.Button(app, text="Get Recommendation", command=recommend).pack(pady=10)

tk.Button(app, text="Surprise Me 🎲", command=surprise).pack()
tk.Label(app, text="MoodMatch 🎯", font=("Arial", 20, "bold")).pack(pady=10)

app.mainloop()