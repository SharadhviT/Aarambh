# app.py
import streamlit as st
import random

st.set_page_config(page_title="Aarambh - Advanced Emotional Support App", layout="centered")

st.title("🌈 Aarambh: Advanced Emotional Support App")
st.markdown("Enter how you feel and get guidance and techniques to manage your emotions.")

# ----------------------------
# 100+ Emotions Dictionary
# ----------------------------
EMOTIONS = {
    "happy": {
        "responses": [
            "Yay! Feeling happy! 😄",
            "Joy looks great on you! 🌟",
            "I love your cheerful mood! 🎈"
        ],
        "techniques": [
            "Share your happiness with a friend.",
            "Do something creative or fun.",
            "Write down 3 happy things today."
        ]
    },
    "joyful": {
        "responses": [
            "You're radiating joy! 🥳",
            "Keep that joyful spirit alive! 🌞",
            "Happiness suits you well! ✨"
        ],
        "techniques": [
            "Celebrate small wins.",
            "Listen to uplifting music.",
            "Spread positivity to others."
        ]
    },
    "content": {
        "responses": [
            "Contentment is beautiful 😌",
            "Enjoy this peaceful feeling 🌸",
            "Cherish the moment 💛"
        ],
        "techniques": [
            "Reflect on what makes you content",
            "Meditate",
            "Savor simple joys"
        ]
    },
    "excited": {
        "responses": [
            "Wow! You're thrilled! 🎉",
            "Excitement suits you! ⚡",
            "Yay! Pumped about this! 🚀"
        ],
        "techniques": [
            "Channel excitement into projects",
            "Share your excitement with friends",
            "Write why you feel excited"
        ]
    },
    "hopeful": {
        "responses": [
            "Hope is powerful 🌟",
            "Keep the positive outlook ✨",
            "Your optimism inspires 💛"
        ],
        "techniques": [
            "Visualize positive outcomes",
            "Write goals and steps",
            "Share your hope with someone"
        ]
    },
    "proud": {
        "responses": [
            "You should feel proud! 🏆",
            "Celebrate your success 🎉",
            "Pride looks great on you 🌟"
        ],
        "techniques": [
            "Share accomplishments with friends",
            "Set next goals",
            "Reflect on your journey"
        ]
    },
    "relieved": {
        "responses": [
            "Ah, relief! 😌",
            "Glad things eased 🌿",
            "Take a moment to relax 💛"
        ],
        "techniques": [
            "Take deep breaths",
            "Acknowledge the relief",
            "Share gratitude"
        ]
    },
    "grateful": {
        "responses": [
            "Gratitude is powerful 💛",
            "Your positivity shines 🌞",
            "Keep being thankful 🌸"
        ],
        "techniques": [
            "Write 3 things you are grateful for",
            "Thank someone",
            "Reflect daily"
        ]
    },
    "optimistic": {
        "responses": [
            "Optimism suits you! 🌞",
            "Keep the positive outlook 🌈",
            "Bright days ahead! ✨"
        ],
        "techniques": [
            "Focus on solutions",
            "Visualize positive outcomes",
            "Share positivity"
        ]
    },
    "motivated": {
        "responses": [
            "Motivation is flowing! 🚀",
            "Let's achieve together 🌟",
            "Keep going! 💪"
        ],
        "techniques": [
            "Set small achievable goals",
            "Visualize success",
            "Reward yourself for progress"
        ]
    },
    "confident": {
        "responses": [
            "Confidence looks great on you! 💪",
            "Keep shining 🌟",
            "You got this! 😎"
        ],
        "techniques": [
            "Affirm yourself daily",
            "Take on challenges",
            "Reflect on achievements"
        ]
    },
    "creative": {
        "responses": [
            "Creativity flows! 🎨",
            "Your imagination is amazing 🌈",
            "Keep innovating 💡"
        ],
        "techniques": [
            "Draw, write or design",
            "Brainstorm freely",
            "Try new creative hobbies"
        ]
    },
    "inspired": {
        "responses": [
            "Inspiration strikes! 🌟",
            "Let's turn ideas into action 🚀",
            "You are motivated! 💛"
        ],
        "techniques": [
            "Write down inspirations",
            "Take immediate action",
            "Share with others"
        ]
    },
    "curious": {
        "responses": [
            "Curiosity is wonderful! 🔍",
            "Keep asking questions 🌟",
            "Explore and discover 🧠"
        ],
        "techniques": [
            "Research your interest",
            "Ask experts",
            "Experiment safely"
        ]
    },
    "amused": {
        "responses": [
            "Haha, that's funny 😆",
            "Enjoy the moment of laughter 😂",
            "Humor brightens the day! 🌞"
        ],
        "techniques": [
            "Share the joke",
            "Laugh with friends",
            "Write down funny moments"
        ]
    },
    "relaxed": {
        "responses": [
            "Relaxation is important 😌",
            "Enjoy the calm 🌊",
            "Take deep breaths 🌿"
        ],
        "techniques": [
            "Meditate",
            "Listen to calming music",
            "Spend time in nature"
        ]
    },
    "peaceful": {
        "responses": [
            "Peace is beautiful 🌸",
            "Enjoy the serenity 🕊️",
            "Stay in this calm 🌿"
        ],
        "techniques": [
            "Meditation",
            "Practice mindfulness",
            "Go for a quiet walk"
        ]
    },
    "tired": {
        "responses": [
            "Rest is important 😴",
            "Take it easy 🛌",
            "You deserve a break 🌙"
        ],
        "techniques": [
            "Take a short nap",
            "Do gentle stretches",
            "Drink water and breathe"
        ]
    },
    "sleepy": {
        "responses": [
            "Time to rest 😴",
            "Close your eyes for a moment 🌙",
            "Recharge your energy 💛"
        ],
        "techniques": [
            "Nap for 20-30 mins",
            "Deep breathing",
            "Avoid screens before bed"
        ]
    },
    "bored": {
        "responses": [
            "Boredom is normal 😐",
            "Let's find something fun 🎨",
            "Time to explore! 🧩"
        ],
        "techniques": [
            "Try a hobby",
            "Go for a walk",
            "Learn something new"
        ]
    },
    "lonely": {
        "responses": [
            "You're not alone 💛",
            "Loneliness can be tough 💌",
            "Let's keep each other company 🌼"
        ],
        "techniques": [
            "Reach out to a friend",
            "Join an interest group",
            "Journal your feelings"
        ]
    },
    "sad": {
        "responses": [
            "It's okay to feel sad 😔",
            "I understand, sadness is human 💙",
            "Feeling down is normal 🌧️"
        ],
        "techniques": [
            "Talk to someone you trust",
            "Listen to calming music",
            "Write down your feelings"
        ]
    },
    "depressed": {
        "responses": [
            "Depression is heavy 💔",
            "Reach out for help 🕊️",
            "You are not alone 💛"
        ],
        "techniques": [
            "Seek professional help",
            "Talk to trusted friends",
            "Practice small self-care steps"
        ]
    },
    "heartbroken": {
        "responses": [
            "Heartbreak hurts 💔",
            "Take time to heal 🕊️",
            "Your feelings are valid 💛"
        ],
        "techniques": [
            "Allow yourself to grieve",
            "Talk about it",
            "Engage in comforting activities"
        ]
    },
    "disappointed": {
        "responses": [
            "Disappointment happens 💔",
            "It's okay to feel this 😔",
            "Let's reflect and move forward 🌿"
        ],
        "techniques": [
            "Identify lessons",
            "Adjust expectations",
            "Talk to a friend"
        ]
    },
    "guilty": {
        "responses": [
            "Guilt can be heavy 💔",
            "It's okay to feel remorse 🤲",
            "Let's understand your guilt 🕊️"
        ],
        "techniques": [
            "Acknowledge mistakes",
            "Apologize if needed",
            "Learn and move forward"
        ]
    },
    "shame": {
        "responses": [
            "Shame is a normal emotion 😔",
            "Let's work through it 🪞",
            "You are not alone 💛"
        ],
        "techniques": [
            "Talk to someone you trust",
            "Practice self-compassion",
            "Write down your thoughts"
        ]
    },
    "embarrassed": {
        "responses": [
            "It's okay, we all feel embarrassed 😳",
            "Take a deep breath 🫂",
            "Let's turn this around 😊"
        ],
        "techniques": [
            "Laugh it off",
            "Share with a friend",
            "Reflect on the situation"
        ]
    },
    "anxious": {
        "responses": [
            "I sense your anxiety 😟",
            "Take a moment, breathe 🌿",
            "Let's calm the mind together 💛"
        ],
        "techniques": [
            "Practice deep breathing",
            "Write down worries and tackle them",
            "Try grounding exercises"
        ]
    }
   {
    "nervous": {
        "responses": [
            "It's okay to feel nervous 😬",
            "Take a deep breath, you got this! 🌱",
            "Let's face it together 💪"
        ],
        "techniques": [
            "Prepare in advance",
            "Visualize success",
            "Do calming exercises"
        ]
    },
    "stressed": {
        "responses": [
            "Stress is normal 😣",
            "Let's manage it together 🌱",
            "Take a pause, breathe 🧘"
        ],
        "techniques": [
            "Meditate for 5 mins",
            "Break tasks into smaller parts",
            "Write down priorities"
        ]
    },
    "overwhelmed": {
        "responses": [
            "It's okay to feel overwhelmed 😥",
            "Take one step at a time 🌊",
            "Let's simplify your tasks 📝"
        ],
        "techniques": [
            "Prioritize tasks",
            "Take deep breaths",
            "Ask for help if needed"
        ]
    },
    "frustrated": {
        "responses": [
            "I see your frustration 😤",
            "Take a moment, let's ease it 🔥",
            "Let's calm this frustration 🕊️"
        ],
        "techniques": [
            "Break the problem into smaller steps",
            "Write your thoughts",
            "Do light exercise"
        ]
    },
    "angry": {
        "responses": [
            "Take a deep breath 😡",
            "Anger is powerful, let's manage it 💥",
            "It's okay to feel frustrated 🧘"
        ],
        "techniques": [
            "Count to 10 before reacting",
            "Go for a walk to release tension",
            "Do deep breathing exercises"
        ]
    },
    "resentful": {
        "responses": [
            "Resentment can be heavy ⚡",
            "Let's release it 💧",
            "I hear your frustration 🕊️"
        ],
        "techniques": [
            "Express feelings safely",
            "Forgive if possible",
            "Focus on yourself"
        ]
    },
    "jealous": {
        "responses": [
            "Jealousy is natural 😏",
            "Let's understand it 💭",
            "Feelings of envy happen to everyone 🌱"
        ],
        "techniques": [
            "Focus on your strengths",
            "Practice gratitude",
            "Set personal goals"
        ]
    },
    "insecure": {
        "responses": [
            "It's okay to feel insecure 🤗",
            "You are stronger than you think 💪",
            "Let's boost your confidence 🌟"
        ],
        "techniques": [
            "Affirm your achievements",
            "Practice positive self-talk",
            "Talk to someone supportive"
        ]
    },
    "fearful": {
        "responses": [
            "Fear is natural 😨",
            "Let's approach it gently 🌱",
            "Courage can grow 🌟"
        ],
        "techniques": [
            "Identify fear triggers",
            "Take small actions",
            "Talk to someone supportive"
        ]
    },
    "scared": {
        "responses": [
            "Being scared is okay 😱",
            "Take deep breaths 🌿",
            "Let's handle it carefully 🕊️"
        ],
        "techniques": [
            "Identify the source of fear",
            "Take gradual steps",
            "Seek support"
        ]
    },
    "surprised": {
        "responses": [
            "Surprise! 😲",
            "Unexpected moments happen 🌟",
            "Let's enjoy the moment 🎉"
        ],
        "techniques": [
            "Pause and process",
            "Share your thoughts",
            "Reflect on the experience"
        ]
    },
    "shocked": {
        "responses": [
            "Shocking indeed 😱",
            "Take a moment to breathe 🌬️",
            "Let's process together 🕊️"
        ],
        "techniques": [
            "Ground yourself",
            "Talk it through",
            "Allow emotions to settle"
        ]
    },
    "indifferent": {
        "responses": [
            "Indifference is normal 😐",
            "Sometimes we feel neutral 🌿",
            "Let's explore your thoughts 💭"
        ],
        "techniques": [
            "Engage in meaningful activity",
            "Reflect on feelings",
            "Try mindfulness"
        ]
    },
    "melancholy": {
        "responses": [
            "Melancholy happens 🌧️",
            "It's okay to reflect 😔",
            "Take care of yourself 💛"
        ],
        "techniques": [
            "Write your thoughts",
            "Listen to soothing music",
            "Talk to a friend"
        ]
    },
    "nostalgic": {
        "responses": [
            "Nostalgia hits 🕰️",
            "Memories are precious 🌸",
            "Enjoy the reflections 🌟"
        ],
        "techniques": [
            "Look at old photos",
            "Write memories",
            "Share stories with family"
        ]
    },
    "overjoyed": {
        "responses": [
            "Overjoyed! 😄🎉",
            "Such happiness is contagious 🌟",
            "Let's celebrate 🌈"
        ],
        "techniques": [
            "Share joy with friends",
            "Write about your feelings",
            "Do something kind for others"
        ]
    },
    "disgusted": {
        "responses": [
            "Disgust is okay 🤢",
            "Let's explore it calmly 🌿",
            "Feelings are valid 🌼"
        ],
        "techniques": [
            "Reflect on why you feel this",
            "Avoid negative stimuli",
            "Discuss feelings safely"
        ]
    },
    "prideful": {
        "responses": [
            "Pride is healthy! 🏅",
            "Celebrate yourself 🌟",
            "You did great 💛"
        ],
        "techniques": [
            "Acknowledge achievements",
            "Share with friends",
            "Set next goals"
        ]
    },
    "emboldened": {
        "responses": [
            "Feeling bold! 🦁",
            "Your courage is inspiring 🌟",
            "Step forward with strength 💥"
        ],
        "techniques": [
            "Take calculated risks",
            "Face fears",
            "Celebrate small wins"
        ]
    },
    "confused": {
        "responses": [
            "Feeling confused is okay 🤔",
            "Let's find clarity 🕵️",
            "Take a deep breath 🌿"
        ],
        "techniques": [
            "Write down what confuses you",
            "Break problems into steps",
            "Seek guidance"
        ]
    },
    "lonely_but_strong": {
        "responses": [
            "Even alone, you are strong 💪",
            "Loneliness can teach resilience 🌟",
            "You can shine independently 🌞"
        ],
        "techniques": [
            "Engage in hobbies",
            "Journal your thoughts",
            "Connect with nature"
        ]
    },
    "anxious_about_future": {
        "responses": [
            "The future is uncertain, it's okay 😰",
            "Focus on what you can control 🌱",
            "Breathe and plan 💛"
        ],
        "techniques": [
            "Make small achievable goals",
            "Visualize positive outcomes",
            "Talk to someone supportive"
        ]
    },
    "resentful_of_others": {
        "responses": [
            "Resentment is natural, let's process it 🌊",
            "Focus on your growth 🌟",
            "Release what weighs you down 💧"
        ],
        "techniques": [
            "Write your feelings",
            "Practice forgiveness",
            "Engage in self-care"
        ]
    },
    "ashamed_of_mistakes": {
        "responses": [
            "Mistakes don't define you 💛",
            "Learn and move forward 🌿",
            "Self-compassion heals 🕊️"
        ],
        "techniques": [
            "Acknowledge the mistake",
            "Plan to improve",
            "Talk to someone you trust"
        ]
    },
    "anxious_about_exams": {
        "responses": [
            "Exams are stressful 😟",
            "Let's prepare calmly 🌱",
            "You've got this! 💪"
        ],
        "techniques": [
            "Make a revision plan",
            "Take breaks",
            "Practice mindfulness"
        ]
    },
    "lonely_at_home": {
        "responses": [
            "Home alone can feel lonely 🏡",
            "Let's make this peaceful 🌿",
            "You are safe 💛"
        ],
        "techniques": [
            "Read or write",
            "Call a friend",
            "Do a creative activity"
        ]
    },
    "unmotivated": {
        "responses": [
            "Motivation can ebb 😐",
            "Let's reignite it 🌟",
            "Small steps matter 💛"
        ],
        "techniques": [
            "Set tiny goals",
            "Celebrate progress",
            "Do something enjoyable"
        ]
    },
    "curious_about_life": {
        "responses": [
            "Curiosity is a gift 🔍",
            "Explore new things 🌟",
            "Learn constantly 🧠"
        ],
        "techniques": [
            "Read books",
            "Ask questions",
            "Experiment safely"
        ]
    },
    "thankful": {
        "responses": [
            "Gratitude opens hearts 💛",
            "Keep appreciating 🌸",
            "Your positivity grows 🌞"
        ],
        "techniques": [
            "Write a gratitude list",
            "Say thanks to someone",
            "Reflect daily"
        ]
    }

    "hopeful": {
        "responses": [
            "Hope is powerful 🌟",
            "Keep the positive outlook ✨",
            "Your optimism inspires 💛"
        ],
        "techniques": [
            "Visualize positive outcomes",
            "Write goals and steps",
            "Share your hope with someone"
        ]
    },
    "proud": {
        "responses": [
            "You should feel proud! 🏆",
            "Celebrate your success 🎉",
            "Pride looks great on you 🌟"
        ],
        "techniques": [
            "Share accomplishments with friends",
            "Set next goals",
            "Reflect on your journey"
        ]
    },
    "relieved": {
        "responses": [
            "Ah, relief! 😌",
            "Glad things eased 🌿",
            "Take a moment to relax 💛"
        ],
        "techniques": [
            "Take deep breaths",
            "Acknowledge the relief",
            "Share gratitude"
        ]
    },
    "grateful": {
        "responses": [
            "Gratitude is powerful 💛",
            "Your positivity shines 🌞",
            "Keep being thankful 🌸"
        ],
        "techniques": [
            "Write 3 things you are grateful for",
            "Thank someone",
            "Reflect daily"
        ]
    },
    "optimistic": {
        "responses": [
            "Optimism suits you! 🌞",
            "Keep the positive outlook 🌈",
            "Bright days ahead! ✨"
        ],
        "techniques": [
            "Focus on solutions",
            "Visualize positive outcomes",
            "Share positivity"
        ]
    },
    "motivated": {
        "responses": [
            "Motivation is flowing! 🚀",
            "Let's achieve together 🌟",
            "Keep going! 💪"
        ],
        "techniques": [
            "Set small achievable goals",
            "Visualize success",
            "Reward yourself for progress"
        ]
    },
    "confident": {
        "responses": [
            "Confidence looks great on you! 💪",
            "Keep shining 🌟",
            "You got this! 😎"
        ],
        "techniques": [
            "Affirm yourself daily",
            "Take on challenges",
            "Reflect on achievements"
        ]
    },
    "creative": {
        "responses": [
            "Creativity flows! 🎨",
            "Your imagination is amazing 🌈",
            "Keep innovating 💡"
        ],
        "techniques": [
            "Draw, write or design",
            "Brainstorm freely",
            "Try new creative hobbies"
        ]
    },
    "inspired": {
        "responses": [
            "Inspiration strikes! 🌟",
            "Let's turn ideas into action 🚀",
            "You are motivated! 💛"
        ],
        "techniques": [
            "Write down inspirations",
            "Take immediate action",
            "Share with others"
        ]
    },
    "curious": {
        "responses": [
            "Curiosity is wonderful! 🔍",
            "Keep asking questions 🌟",
            "Explore and discover 🧠"
        ],
        "techniques": [
            "Research your interest",
            "Ask experts",
            "Experiment safely"
        ]
    },
    "amused": {
        "responses": [
            "Haha, that's funny 😆",
            "Enjoy the moment of laughter 😂",
            "Humor brightens the day! 🌞"
        ],
        "techniques": [
            "Share the joke",
            "Laugh with friends",
            "Write down funny moments"
        ]
    },
    "relaxed": {
        "responses": [
            "Relaxation is important 😌",
            "Enjoy the calm 🌊",
            "Take deep breaths 🌿"
        ],
        "techniques": [
            "Meditate",
            "Listen to calming music",
            "Spend time in nature"
        ]
    },
    "peaceful": {
        "responses": [
            "Peace is beautiful 🌸",
            "Enjoy the serenity 🕊️",
            "Stay in this calm 🌿"
        ],
        "techniques": [
            "Meditation",
            "Practice mindfulness",
            "Go for a quiet walk"
        ]
    },
    "tired": {
        "responses": [
            "Rest is important 😴",
            "Take it easy 🛌",
            "You deserve a break 🌙"
        ],
        "techniques": [
            "Take a short nap",
            "Do gentle stretches",
            "Drink water and breathe"
        ]
    },
    "sleepy": {
        "responses": [
            "Time to rest 😴",
            "Close your eyes for a moment 🌙",
            "Recharge your energy 💛"
        ],
        "techniques": [
            "Nap for 20-30 mins",
            "Deep breathing",
            "Avoid screens before bed"
        ]
    },
    "bored": {
        "responses": [
            "Boredom is normal 😐",
            "Let's find something fun 🎨",
            "Time to explore! 🧩"
        ],
        "techniques": [
            "Try a hobby",
            "Go for a walk",
            "Learn something new"
        ]
    },
    "lonely": {
        "responses": [
            "You're not alone 💛",
            "Loneliness can be tough 💌",
            "Let's keep each other company 🌼"
        ],
        "techniques": [
            "Reach out to a friend",
            "Join an interest group",
            "Journal your feelings"
        ]
    },
    "sad": {
        "responses": [
            "It's okay to feel sad 😔",
            "I understand, sadness is human 💙",
            "Feeling down is normal 🌧️"
        ],
        "techniques": [
            "Talk to someone you trust",
            "Listen to calming music",
            "Write down your feelings"
        ]
    },
    "depressed": {
        "responses": [
            "Depression is heavy 💔",
            "Reach out for help 🕊️",
            "You are not alone 💛"
        ],
        "techniques": [
            "Seek professional help",
            "Talk to trusted friends",
            "Practice small self-care steps"
        ]
    },
    "heartbroken": {
        "responses": [
            "Heartbreak hurts 💔",
            "Take time to heal 🕊️",
            "Your feelings are valid 💛"
        ],
        "techniques": [
            "Allow yourself to grieve",
            "Talk about it",
            "Engage in comforting activities"
        ]
    },
    "disappointed": {
        "responses": [
            "Disappointment happens 💔",
            "It's okay to feel this 😔",
            "Let's reflect and move forward 🌿"
        ],
        "techniques": [
            "Identify lessons",
            "Adjust expectations",
            "Talk to a friend"
        ]
    },
    "guilty": {
        "responses": [
            "Guilt can be heavy 💔",
            "It's okay to feel remorse 🤲",
            "Let's understand your guilt 🕊️"
        ],
        "techniques": [
            "Acknowledge mistakes",
            "Apologize if needed",
            "Learn and move forward"
        ]
    },
    "shame": {
        "responses": [
            "Shame is a normal emotion 😔",
            "Let's work through it 🪞",
            "You are not alone 💛"
        ],
        "techniques": [
            "Talk to someone you trust",
            "Practice self-compassion",
            "Write down your thoughts"
        ]
    },
    "embarrassed": {
        "responses": [
            "It's okay, we all feel embarrassed 😳",
            "Take a deep breath 🫂",
            "Let's turn this around 😊"
        ],
        "techniques": [
            "Laugh it off",
            "Share with a friend",
            "Reflect on the situation"
        ]
    },
    "anxious": {
        "responses": [
            "I sense your anxiety 😟",
            "Take a moment, breathe 🌿",
            "Let's calm the mind together 💛"
        ],
        "techniques": [
            "Practice deep breathing",
            "Write down worries and tackle them",
            "Try grounding exercises"
        ]
    },
    "nervous_about_interview": {
        "responses": [
            "Interviews can be nerve-wracking 😬",
            "Stay calm and prepared 🌱",
            "Confidence will help you shine 💪"
        ],
        "techniques": [
            "Practice mock interviews",
            "Research beforehand",
            "Use positive affirmations"
        ]
    },
    "stressed_about_project": {
        "responses": [
            "Project stress is common 😣",
            "Break it into parts 🌿",
            "You can handle it 💛"
        ],
        "techniques": [
            "Divide tasks into smaller steps",
            "Set deadlines for each",
            "Ask for feedback"
        ]
    },
    "overjoyed_with_friends": {
        "responses": [
            "Joy shared is doubled 😄",
            "Friends make happiness brighter 🌟",
            "Celebrate together 🎉"
        ],
        "techniques": [
            "Plan a fun activity",
            "Share a small gift",
            "Express gratitude to friends"
        ]
    },
    "playful_with_siblings": {
        "responses": [
            "Sibling fun! 😜",
            "Laughter is the best 🧩",
            "Enjoy the mischief 😂"
        ],
        "techniques": [
            "Play games together",
            "Share jokes",
            "Do a fun activity"
        ]
    },
    "romantic_excited": {
        "responses": [
            "Love makes the heart flutter 💖",
            "Cherish these feelings 🌹",
            "Enjoy the romance 💛"
        ],
        "techniques": [
            "Write a sweet message",
            "Plan a small surprise",
            "Share a heartfelt conversation"
        ]
    },
    "hopeful_for_future": {
        "responses": [
            "The future is bright 🌞",
            "Keep believing in yourself 🌟",
            "Good things are coming 💛"
        ],
        "techniques": [
            "Set personal goals",
            "Visualize success",
            "Surround yourself with positivity"
        ]
    }

}

# ----------------------------
# Function to detect emotion
# ----------------------------
def detect_emotion(user_input):
    user_input = user_input.lower()
    detected_emotions = []
    for emotion in EMOTIONS:
        if emotion in user_input:
            detected_emotions.append(emotion)
    return detected_emotions

# ----------------------------
# Main App Logic
# ----------------------------
user_input = st.text_area("How are you feeling today? (e.g., happy, sad, anxious, excited, etc.)")

if st.button("Get Support"):
    if not user_input.strip():
        st.warning("Please enter your emotions.")
    else:
        emotions_found = detect_emotion(user_input)
        if emotions_found:
            st.subheader("💬 Responses")
            for emotion in emotions_found:
                response = random.choice(EMOTIONS[emotion]["responses"])
                st.write(f"**{emotion.capitalize()}:** {response}")
                
                technique = random.choice(EMOTIONS[emotion]["techniques"])
                st.write(f"**Technique:** {technique}\n")
        else:
            st.info("Sorry, I couldn't detect a specific emotion. Try mentioning common feelings like happy, sad, anxious, or excited.")
