"""



"""

import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")

### Create US Background Image 
image = r"25_CSV_and_Pandas\US_States_Game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

### Read CSV
CSV = r"25_CSV_and_Pandas\US_States_Game\50_states.csv"
states_df = pd.read_csv(CSV)

### The Game
# correct_guesses = 0
guessed_states = []
data = pd.read_csv(CSV)
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer_state_cap = answer_state.title()
    print(answer_state_cap)
    
    if answer_state == "Exit":
        missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        missing_states = [state for state in missing_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    
    

    if (states_df["state"].eq(answer_state_cap)).any() == True:
        # get the x, y coordinates for the state
        curr_state = states_df[states_df.state == answer_state_cap]
        
        ## Instead could have used .item()
        x_list = (curr_state.x).tolist()
        y_list = (curr_state.y).tolist()
        x_str = int("".join(map(str, x_list)))
        y_str = int("".join(map(str, y_list)))
        
        # write onto the map
        state = turtle.Turtle()
        state.penup()
        state.ht()
        state.goto(x_str, y_str)
        state.write(f"{answer_state_cap}", align="center")








turtle.mainloop()