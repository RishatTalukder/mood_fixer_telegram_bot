from random import choice

happy = [
    "Believe you can and you're halfway there.",
    "You are stronger than you think.",
    "Keep pushing forward, no matter what."
]

sad = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why was the math book sad? Because it had too many problems.",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats!"
]

angry = [
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!"
]

def get_mood_response(mood):
    """
    This function maps moods to responses and returns an appropriate response.
    """
    mood_dict = {
        'happy': choice(happy),
        'sad': choice(sad),
        'angry': choice(angry)
    }
    return mood_dict.get(mood, "I am sorry! I am not trained to understand that!😊")
