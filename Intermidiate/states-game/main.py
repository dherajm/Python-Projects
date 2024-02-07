import turtle
import pandas

# Ensure correct image and CSV file paths
image = "blank_states_img.gif"
data_file = "50_states.csv"

screen = turtle.Screen()
screen.title("U.S States Game")
screen.addshape(image)
turtle.shape(image)

try:
    data = pandas.read_csv(data_file)
except FileNotFoundError:
    print("Error: CSV file not found.")
    exit()

all_states = data.state.to_list()
states_guessed = []

while len(states_guessed) < 50 and len(states_guessed) < len(all_states):  # Exit loop if all states guessed
    answer_state = screen.textinput(title=f"Guess the State ({len(states_guessed) + 1}/50)",
                                    prompt="What's another state name?").title()

    if answer_state in all_states:
        if answer_state not in states_guessed:
            state_data = data[data["state"] == answer_state]
            states_guessed.append(answer_state)

            turtle.hideturtle()
            turtle.penup()
            turtle.goto(int(state_data["x"].iloc[0]), int(state_data["y"].iloc[0]))
            turtle.write(answer_state)

    elif answer_state == "Exit":
        break

    else:
        pass

# Generate missing states list only if not all states guessed
if len(states_guessed) < len(all_states):
    missing_states = [state for state in all_states if state not in states_guessed]
    missing_data = pandas.DataFrame(missing_states)
    missing_data.to_csv("missing_states.csv")
