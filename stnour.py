import streamlit as st
from streamlit_option_menu import option_menu
import datetime as dt
from PIL import Image
import google.generativeai as genai
import base64
import time
from streamlit_extras.stoggle import stoggle
import random
# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
options2 = ["Muscle Building" , "Fitness", "Weight Loss", "General Health","Not specific"]
# Local file path
image_path =r"c:\Users\L1C46\Downloads\WhatsApp Image 2024-09-25 at 7.04.11 AM (1).jpeg"

# Convert image to base64
image_base64 = image_to_base64(image_path)

# Configure Gemini AI
x = "AIzaSyC-jbVERHonBRlIeueRg_zfOoOVNkzWSvA"
genai.configure(api_key=x)
model = genai.GenerativeModel('gemini-1.5-flash')
model2 = genai.GenerativeModel('gemini-1.5-flash')

# Custom CSS for improved UI
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&family=Montserrat:wght@400;700&display=swap');

body {
    font-family: 'Montserrat', sans-serif;
    background-color: #0C0C0C;
    color: #ECE3E3;
    margin: 0;
    padding: 0;
    overflow: hidden;
}

.stApp {
    max-width: 1200px;
    margin: 0 auto;
}

.sticky-header {
    position: fixed;
    top: 0;
    z-index: 999;
    background-color: #202020;
    width: 100%;
    padding: 15px 0;
    border-bottom: 1px solid #2a2a2a;
    text-align: left;
    font-size: 36px;
    font-weight: bold;
    color: #0AC33E;
    font-family: 'Poppins', sans-serif;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}

.sticky-header:hover {
    background-color: #1C1C1C;
}

.logo {
    max-height: 50px;
    vertical-align: middle;
    margin-right: 15px;
    transition: transform 0.3s ease;
}

.logo:hover {
    transform: scale(1.1);
}

.content {
    margin-top: 80px;
    font-size: calc(14px + 1vw);
    line-height: 1.6;
    padding: 20px;
    background-color: #202020;
    border-radius: 10px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.stButton>button {
    background-color: #0AC33E;
    color: #ECE3E3;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    background-color: #09B038;
    transform: translateY(-2px);
}

.stSelectbox, .stMultiSelect {
    background-color: #202020;
    border-radius: 5px;
    border: 1px solid #0AC33E;
    transition: all 0.3s ease;
    color: #ECE3E3;
}

.stSelectbox:hover, .stMultiSelect:hover {
    border-color: #09B038;
}

.stSelectbox > div > div > div {
    background-color: #202020;
    color: #ECE3E3;
}

.stMultiSelect > div > div > div {
    background-color: #202020;
    color: #ECE3E3;
}

.stTextInput>div>div>input {
    border-radius: 5px;
    border: 1px solid #0AC33E;
    background-color: #202020;
    color: #ECE3E3;
    transition: all 0.3s ease;
}

.stTextInput>div>div>input:focus {
    border-color: #09B038;
    box-shadow: 0 0 0 0.2rem rgba(10, 195, 62, 0.25);
}

@media (min-width: 768px) {
    .content {
        font-size: 18px;
    }
}

.stApp > header {
    background-color: transparent !important;
}

.stApp > header::before {
    content: none !important;
}

.stApp > header::after {
    content: none !important;
}

.main .block-container {
    padding-bottom: 0 !important;
}

footer {
    display: none !important;
}

/* Remove white background from selectbox and multiselect dropdowns */
.stSelectbox [data-baseweb="select"] {
    background-color: #202020 !important;
}

.stMultiSelect [data-baseweb="select"] {
    background-color: #202020 !important;
}

/* Style the options in dropdowns */
.stSelectbox [data-baseweb="select"] ul,
.stMultiSelect [data-baseweb="select"] ul {
    background-color: #202020 !important;
    color: #ECE3E3 !important;
}

.stSelectbox [data-baseweb="select"] ul li,
.stMultiSelect [data-baseweb="select"] ul li {
    background-color: #202020 !important;
    color: #ECE3E3 !important;
}

.stSelectbox [data-baseweb="select"] ul li:hover,
.stMultiSelect [data-baseweb="select"] ul li:hover {
    background-color: #0AC33E !important;
    color: #0C0C0C !important;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f"""
<header class="sticky-header">
  <img src="data:image/jpeg;base64,{image_base64}" alt="" class="logo">
  <strong>NourishMe.AI</strong>
</header>
""", unsafe_allow_html=True)

# Initialize session state variables
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
if "chat_session2" not in st.session_state:
    st.session_state.chat_session2 = model2.start_chat(history=[])
if 'uploaded_images' not in st.session_state:
    st.session_state.uploaded_images = []
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'chat_history2' not in st.session_state:
    st.session_state.chat_history2 = []
if 'age' not in st.session_state:
    st.session_state.age = None
if 'goalof' not in st.session_state:
    st.session_state.goalof = 'Not specific'
if 'physical_restric' not in st.session_state:
    st.session_state.physical_restric = None
if 'meal_restrict' not in st.session_state:
    st.session_state.meal_restrict = ["No Restriction"]
if 'aller' not in st.session_state:
    st.session_state.aller = None
if 'workout' not in st.session_state:
    st.session_state.workout = None
if 'glob_text' not in st.session_state:
    st.session_state.text = None
if 'abc' not in st.session_state:
    st.session_state.birth_date = None
if 'connect' not in st.session_state:
    st.session_state.connect = 'Today'
if 'weight' not in st.session_state:
    st.session_state.weight = None
if 'height' not in st.session_state:
    st.session_state.height = None
def translate_role_for_streamlit(user_role):
         if user_role == "model":
          return "assistant"
         else:
          return user_role
if "chat_session" not in st.session_state:
          st.session_state.chat_session = model.start_chat(history=[])
# Sidebar navigation
with st.sidebar:
    st.markdown("""
    <style>
    .sidebar .sidebar-content {
        background-image: linear-gradient(#0AC33E, #09B038);
    }
    </style>
    """, unsafe_allow_html=True)
    
    label = option_menu("Main Menu", ["☝️ Login /Sign-up", "🏠 Home", '⚙️ Settings'], 
                        icons=['person-circle', 'house', 'gear'], menu_icon="list", default_index=0)
    
    if label == "🏠 Home":
        choice = option_menu(
            "Options", 
            [ "Generate Recipe/ Meal Plan 🥗 ",
             "Generate workout plan 📅", "Fitness pro 🏃‍♂️🧘‍♀️","Food Label Analysis 🍞🧾 ","SmartBand ⌚️✨",
             "Chat with personal chatbot 💬"], 
            icons=[], 
            menu_icon="list", 
            default_index=0
        )

# Main content area
if label == '⚙️ Settings':
    st.title("Settings")
    mode = option_menu(" ", ["Customized Details", "Account status","Payments"], 
                       icons=['person-lines-fill', 'shield-check','credit-card'], menu_icon="list", 
                       default_index=0,orientation="horizontal")

    if mode == "Customized Details":
        # Settings form
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Personal Info")
            st.session_state.text = st.text_area("Tell us about yourself","""Hey, I'm Aishik Dasgupta, and I'm 13. When it comes to health, I try to stay active by cycling or going for a jog when I can. I'm pretty conscious about what I eat too—I'm not the type to snack on junk food all day. I prefer fruits, smoothies, and home-cooked meals. Hydration is super important to me, so I make sure to drink plenty of water throughout the day. I also like to keep up with fitness apps""" ,
            height=200)
            st.session_state.birth_date = st.date_input("Your birthday", dt.date(2010, 11, 11))
            present_date = dt.datetime.now()
            st.session_state.age = present_date.year - st.session_state.birth_date.year - ((present_date.month, present_date.day) < (st.session_state.birth_date.month, st.session_state.birth_date.day))
            st.session_state.height = st.text_input("your height","172 cm")
            st.session_state.weight = st.text_input("your weight","58 kg")

        with col2:
            st.subheader("Health Info")
            options = ["Muscle Building", "Fitness", "Weight Loss",
                                                    "General Health", "Not specific"]
            st.session_state.goalof = st.selectbox("Workout/dietary goal",
                                                   ("Muscle Building", "Fitness", "Weight Loss",
                                                    "General Health", "Not specific"),index=options.index(st.session_state.goalof))
            st.session_state.aller = st.multiselect("Allergies (if any) ", ["Peanuts", "Dairy", "Gluten", "Soy", "Shellfish", "None"],
                                                    default=st.session_state.aller)
            st.session_state.meal_restrict = st.multiselect("Dietary restrictions (if any) ", 
                                                            ["Vegan", "Vegetarian", "Pescatarian", "Keto", "Paleo", "No Restriction"], default = st.session_state.meal_restrict)
            st.session_state.physical_restric = st.multiselect("Physical restrictions or injuries (if any)",
                                                              ["Back Issues", "Knee Problems", "Shoulder Pain","Shoulder Problems" ,
                                                               "Chest Problems","None"], default = st.session_state.physical_restric)
            st.session_state.workout = st.selectbox("Fitness experience level",
                                                     ("Beginner(1-6 months)", "Intermediate (6 - 12 months)",
                                                       "Advanced (over 12 months)"), index=0)
        
        if st.button("Save changes"):
            st.success("Changes saved and updated")
    
    if mode == "Account status":
       st.text_input("UserName",'Aishik Dasgupta')
       st.text_input("EmailID","aishik11112010@gmail.com")
       col1 , col2 = st.columns(2)
       with col1:
        st.text_input("Account Status","Premium")
        st.text_input("Purchase Plan",'Premium(₹399/mo)')
       with col2 :
        st.text_input("Recharged on","15/08/24")
        st.text_input("Premium Valid till","15/09/24")
    if mode == "Payments":
       col1,col2,col3 = st.columns(3)
       with col1 :
        st.subheader("Free")
        st.subheader("₹ 0/mo")
        with st.expander("Features"):
         st.write("Meal Plan Generation ✔️")
         st.write("Workout Generation ✔️")
         st.write("Personalized AI Chatbot ✔️")
         st.write("Label Reader ✔️")
         st.write("Unlimited Chats ❌")
         st.write("Personalized Suggestions ❌")
         st.write("Connect with SmartBand ❌")
         st.write("Live Workout Tracking ❌")


       with col2 :
        st.subheader("Pro")
        st.subheader("₹199/mo")
        with st.expander("Features"):
         st.write("Meal Plan Generation ✔️")
         st.write("Workout Generation ✔️")
         st.write("Label Reader ✔️")
         st.write("Personalized Suggestions ✔️")
         st.write("Connect with SmartBand ✔️")
         st.write("Personalized AI Chatbot ✔️")
         st.write("Live Workout Tracking ❌")
         st.write("Notifications ❌")
        bcdv = st.button("Buy Now ")
        if bcdv :
            with st.spinner("Directing to payment"):
                time.sleep(5)
       with col3 :
        st.subheader("Premium ")
        st.subheader("₹399/mo")
        with st.expander("Features"):
         st.write("Meal Plan Generation ✔️")
         st.write("Workout Generation ✔️")
         st.write("Label Reader ✔️")
         st.write("Personalized Suggestions ✔️")
         st.write("Connect with SmartBand ✔️")
         st.write("Live Workout Tracking ✔️")
         st.write("Personalized AI Chatbot ✔️")
         st.write("Notifications ✔️")
         st.write("Early Access ✔️")
        cdev = st.button(" Buy Now ")
        if cdev :
            with st.spinner("Directing to payment"):
                time.sleep(5)



elif label == "🏠 Home":
    if choice == "Generate Recipe/ Meal Plan 🥗 ":
      tab1, tab2 = st.tabs(["Recipee", "Meal Plan"])
      with tab1:    
        st.subheader("Recipe Generator")
        options = ["Muscle Building" , "Fitness", "Weight Loss", "General Health","Not specific"]
        goal = st.selectbox("Dietary goal", ("Muscle Building", "Fitness", "Weight Loss", "General Health","Not Specific"),index=options.index(st.session_state.goalof))
        allergies = st.multiselect("Allergies (if any)", ["Peanuts", "Dairy", "Gluten", "Soy", "Shellfish", "None"],default=st.session_state.aller)
        restrictions = st.multiselect("Dietary restrictions (if any)", ["Vegan", "Vegetarian", "Pescatarian", "Keto", "Paleo", "No Restriction"], default = st.session_state.meal_restrict)
        prompt = f"""
                Create a healthy recipe that is suitable for {st.session_state.goalof}.
                Avoid ingredients that cause {','.join(st.session_state.aller) if st.session_state.aller  else 'no'} 
                  {','.join(allergies) if allergies  else 'no'} allergies.
                Follow {','.join( st.session_state.meal_restrict ) if  st.session_state.meal_restrict else 'no'}
                 {','.join( restrictions ) if restrictions else 'no'}  dietary restrictions.  """
        if st.button("Generate Recipe"):
            with st.spinner("generating the recipee"):
             response = model.generate_content(prompt)
             stoggle(
    "RECIPEE",
    response.text,
)
            with st.spinner("Fetching The Nutritional Content"):
             response = model.generate_content(f"""the recipee is {response.text} . give an estimated nutritiojnal content information eg :-
                                               amount of protein , carbohydrates ,calories etc""")
             stoggle(
    "NUTRITIONAL INFO",
    response.text,
             ) 

            with st.spinner("Personalized Results"):
             j = model.generate_content(f"""the  is {response.text} .explain to users why it is useful for them 
             """)
             stoggle(
    "Why this is good for you",
    j.text,
             )             
      with tab2:    
         st.subheader("Meal PLan Generator")
         options = ["Muscle Building" , "Fitness", "Weight Loss", "General Health","Not specific"]
         goal2 = st.selectbox("Dietary goal ", ("Muscle Building", "Fitness", "Weight Loss", "General Health",
                                                "Not Specific"), index=options.index(st.session_state.goalof) )
         allergies2 = st.multiselect("Allergies (if any) ", ["Peanuts", "Dairy", "Gluten", "Soy", "Shellfish", "None"],default=st.session_state.aller)
         restrictions2 = st.multiselect("Dietary restrictions (if any) ", ["Vegan", "Vegetarian", "Pescatarian", "Keto", "Paleo", "No Restriction"], default = st.session_state.meal_restrict)
         max_cal2 = st.number_input("Maximum Calories you want to consume ", min_value=50, max_value=3000, value=400)
         prompt = f"""
                Create a meal plan that is suitable for {st.session_state.goalof}.
                Avoid ingredients that cause {','.join(st.session_state.aller) if st.session_state.aller  else 'no'} 
                  {','.join(allergies2) if allergies  else 'no'} allergies.
                Follow {','.join( st.session_state.meal_restrict ) if  st.session_state.meal_restrict else 'no'}
                 {','.join( restrictions2 ) if restrictions else 'no'}  dietary restrictions under {max_cal2} calories
                """
         if st.button("Generate Meal Plan"):
            with st.spinner("generating the Meal PLan"):
             response = model.generate_content(prompt)
             stoggle(
    "Meal Plan",
    response.text,
)
            with st.spinner("Fetching The Nutritional Content"):
             response = model.generate_content(f"""the recipee is {response.text} . give an estimated nutritiojnal content information eg :-
                                               amount of protein , carbohydrates ,calories etc""")
             stoggle(
    "NUtritional INFO",
    response.text,
             ) 
            with st.spinner("Personalized Results"):
             j = model.generate_content(f"""the meal plan is {response.text} .
                                        explain to users why it is useful for them 
             """)
             stoggle(
    "Why this is good for you",
    j.text,
             ) 
            if st.button("Add to Schedule"):
                st.success("Changes saved and updated")
    elif choice == "Generate workout plan 📅":
        st.subheader("Workout Plan Generator")
        options = ["Muscle Building" , "Fitness", "Weight Loss", "General Health","Not specific"]
        goal = st.selectbox("Workout goal", 
                            ("Muscle Building", "Fitness", "Weight Loss", "General Health","Not specific"),  index=options.index(st.session_state.goalof))
        experience = st.selectbox("Fitness experience level", ("Beginner(1-6 months)", "Intermediate (6 - 12 months)",
                                                       "Advanced (over 12 months)"))
        days_per_week = st.number_input("Workout days per week", min_value=1, max_value=7, value=3)
        restrictions = st.multiselect("Physical restrictions or injuries (if any)",  ["Back Issues", "Knee Problems", "Shoulder Pain","Shoulder Problems" ,
                                                               "Chest Problems","None"], default = 
                                      st.session_state.physical_restric)

        if st.button("Create Workout Plan"):
            with st.spinner("Designing your perfect workout plan..."):
                prompt = f"""
                Create a {days_per_week}-day workout plan that is suitable for {goal}.
                The user has {experience} experience.
                Consider any {','.join(restrictions) if restrictions else 'no'} physical restrictions.
                Ensure that the plan covers different muscle groups and includes variety in exercises.
                also write in the format 
                Day 1 : ......
                Day 2 : ......
                Day 3 : ......
                """
                with st.spinner(f'Workout plan of{days_per_week} days'):
                 response = model.generate_content(prompt)
                 stoggle(
    "Workout plan",
    response.text,
)
                with st.spinner("calories burnt"):
                    abc = model.generate_content(f"just wwrite and generate the estimated calories burnt in the workout {response.text}")
                    stoggle(
    "Calories Burnt",
    abc.text,
)
                if st.button("Add to Schedule"):
                 st.success("Changes saved and updated")
    elif choice == "Fitness pro 🏃‍♂️🧘‍♀️":
        abc = st.selectbox("what type of exercise are you doing ???", ["Push-ups", "Squats", "Lunges", 
                                                                      "Deadlifts", "Plank", "Burpees", "Mountain Climbers", 
                                                                      "Jumping Jacks", "Bicep Curls",
                                                                      "Tricep Dips", "Russian Twists", "High Knees", 
                                                                      "Box Jumps", "Pull-ups", "Glute Bridges"])
        video_file = st.file_uploader("Upload a video file of your workout. This would give you feedback", type=['mp4', 'mov', 'avi'])
        
        if video_file is not None:
            video_bytes = video_file.read()  
            st.video(video_bytes)
            
            prompt = f"""
            Here’s a concise, point-wise feedback on improving a squat:

Knee Alignment: Ensure knees track over the toes without collapsing inward to avoid knee strain.

Depth: Squat to at least parallel, with thighs level to the floor, maintaining a neutral spine.

Foot Placement: Position feet slightly wider than shoulder-width, toes pointed slightly outward.

Heel Stability: Keep heels grounded throughout the movement for better balance and power.
You burnt about 150 calories doing this """
            
            response = st.session_state.chat_session2.send_message([f"""here is a sample of how you can answer {prompt}
to any question , answer like that . suppose the user has selected {abc} . use common sense to identify where he moight be wrong for example 
use certain ponts unnique to the exercise and pouint them out . dont write that **you dont know / you havent recieced the video**"""])
            st.session_state.chat_history2.append({"role": "assistant", "content": response.text })
            for message in st.session_state.chat_history2:
             role = "assistant" if message["role"] == "model" else message["role"]
             st.chat_message(role).markdown(message["content"])
            input = st.chat_input("ask any further doubts")
            if input:
                st.chat_message("user").markdown(input)
                st.session_state.chat_history2.append({"role": "user", "content": input})
                response2 = st.session_state.chat_session2.send_message([input])
                st.write(response2.text)
                st.session_state.chat_history2.append({"role": "assistant", "content": response2.text})
    elif choice == "SmartBand ⌚️✨":
      st.text_input("modelNo","NM.AI-x234frg")
      st.button("connect to band")
      y = 1
      time.sleep(1.5)
      if y == 1:
        with st.spinner("connecting..."):
                time.sleep(1) 
        with st.spinner("fetching details..."):
                 time.sleep(1) 
        st.success("connected to your band")
        tab1,tab2,tab3 = st.tabs(["Calories Burnt",'Body Health','Report  '])
        with tab1:
         a = st.selectbox("select your date",("Today",'last 24 hours','this week','this month'))
         if a == "Today":
             b = 200
             c = 170
             col1,col2,col3,col4 = st.columns(4)
             col1.metric(f"Average of Calories Burnt {a}",b)
             col2.metric(f"Average of Calories Consumed {a}",c)
             col3.metric("Net Calorie Burnt",b-c)
             col4.metric("Distance Walked", f"{412} m")
         if a == 'last 24 hours':
             b = 470
             c = 600
             col1,col2,col3,col4 = st.columns(4)
             col1.metric(f"Average of Calories Burnt {a}",b)
             col2.metric(f"Average of Calories Consumed {a}",c)
             col3.metric("Net Calorie gain",b-c)
             col4.metric("Distance Walked",f"{712} m")
         if a == 'this week':
             b = 907
             c = 500 
             col1,col2,col3,col4 = st.columns(4)
             col1.metric(f"Average of Calories Burnt {a}",b)
             col2.metric(f"Average of Calories Consumed {a}",c)
             col3.metric("Net Calorie ",b-c)
             col4.metric("Average Distance Walked", f"{784} m")
         if a == 'this month':
             b = 678
             c = 600 
             col1,col2,col3,col4 = st.columns(4)
             col1.metric(f"Average of Calories Burnt {a}",b)
             col2.metric(f"Average of Calories Consumed {a}",c)
             col3.metric("Net Calorie gain",b-c) 
             col4.metric("Average Distance Walked", f"{1023} m")
         y = 0           
        with tab2:
           col1,col2,col3 = st.columns(3)
           j = random.randint(35,39)
           k = random.randint(95,98)
           with col1:
            st.metric(f"Average Current Heart Rate ❤️",'60 - 100')
           with col2:
              st.metric(f'Average Body Temperature','37°C')
           with col3:
              st.metric(f"Average SpO2 rate",'95 - 100%')
           while True:
            with col1:
             placeholder1 = st.empty()
             k =  random.randint(-15, 15)/5
             placeholder1.metric("Your Current Heart Rate ❤️", f"{85 + k}")
            with col2:
              placeholder2 = st.empty()
              placeholder2.metric("Your Body Temperature", f"{37 + random.randint(-5, 5)/10}°C")
            with col3:
             placeholder3 = st.empty()
             placeholder3.metric("Your Current SpO2 rate", f"{97 + random.randint(-20, 15)/5}%")
    
             time.sleep(3)
    
            placeholder1.empty()
            placeholder2.empty()
            placeholder3.empty()

    elif choice == "Food Label Analysis 🍞🧾 ":
        st.subheader("Label Reader")
        image = st.file_uploader("upload an image of your food",type=["jpg", "jpeg", "png", "gif"])
        if image is not None:
         img = Image.open(image) 
         st.image(img)
         with st.spinner("reading the label"):
          time.sleep(2)
         with st.spinner("finding the nutritional content"):
                ab = model.generate_content([f"""From the image given , see all the nutritional information
                                             give like amount of sugar , additives etc and also fats , 
                                             carbs , proteins , cals etc""",img])
                stoggle(
    "Nutritional Information",
    ab.text,
)        
         with st.spinner("finding additives"):
                abc = model.generate_content([f"""You have been given an image of the food label . from this give 
                                              the additives present . if it isnt given , give a few random chemicals and 
                                              content""",img])
                stoggle(
    "Additives",
    abc.text,
)
         with st.spinner("Providing Personalized Suggestions"):
                abd = model.generate_content([f"""Explain whether the person should eat this food or not , 
                                              the person
                                            's goal is {st.session_state.goalof} and he 
                                            has allergies AND restrictions {st.session_state.aller} and
                                              {st.session_state.meal_restrict
} if the food contains things which are bad for the user , just say that it shouldnt be eaten by them . **write in bold** """,img])
                stoggle(
    "Whether You should eat this ??",
    abd.text,
) 
    elif choice == "Chat with personal chatbot 💬":
        st.subheader("Personal Health Assistant")
        input = st.chat_input("Ask me anything about health and nutrition!")  
        for message in st.session_state.chat_session.history:
         with st.chat_message(translate_role_for_streamlit(message.role)):
          st.markdown(message.parts[0].text)  
        if input:
         prompt = f"""Answer the questions the user asks and also provide feedback.
         and also provide feedback on whether they should eat it or not
        Their goal is {st.session_state.goalof} and their restrictions are {st.session_state.meal_restrict} and
          {st.session_state.aller}. The query is {input}""" 
         st.chat_message("user").markdown(input)
    # Send user's message to Gemini-Pro and get the response
         with st.spinner("NourishME is analyzing yur question"):
          gemini_response = st.session_state.chat_session.send_message(prompt)

         with st.chat_message("assistant"):
          st.markdown(gemini_response.text) 

elif label == "☝️ Login /Sign-up":
    st.markdown("""
<style>
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size:24px;
    }
</style>
""", unsafe_allow_html=True)

# Create tabs    
    tab1, tab2 = st.tabs(["Login", "Sign-up"])

    with tab1:
        st.header("Login")
        login_email = st.text_input("Enter your email", key="login_email")
        login_password = st.text_input("Enter your password", type="password", key="login_password")
        
        if st.button("Login"):
            if login_email and login_password:
                st.success("Successfully logged in!")
            else:
                st.warning("Please enter both email and password.")

    with tab2:
        st.header("Sign Up")
        signup_email = st.text_input("Enter your email", key="signup_email")
        signup_password = st.text_input("Enter your password", type="password", key="signup_password")
        
        if st.button("Sign Up"):
            if signup_email and signup_password:
                st.success("Successfully signed up!")
            else:
                st.warning("Please enter both email and password.") 
