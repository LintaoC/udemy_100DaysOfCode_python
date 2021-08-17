import turtle
import pandas

# Turtle setup
screen = turtle.Screen()
screen.title("U.S States Games")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

# Pandas setup
states_data = pandas.read_csv("50_states.csv")
states_data_list = states_data["state"].to_list()


def write_state(name, x, y):
    """ Function to write states name on the screen at the correct position """
    new_state = turtle.Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.goto(x, y)
    new_state.write(name)


def user_won():
    """ Function to write states name on the screen at the correct position """
    new_state = turtle.Turtle()
    new_state.penup()
    new_state.hideturtle()
    new_state.write("You best the game, Gratz!!!", align="center", font=("", 28, ""))


# Variable
guessed_state = []
state_to_learn_list = []
game_is_on = True

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"States Correct: {len(guessed_state)}/{len(states_data_list)}",
                                    prompt="Enter state name: ")

    if answer_state.title() == "Exit":
        # Create file states_to_learn.csv containing all the states that the player did not guess
        for states in states_data_list:
            if states not in guessed_state:
                state_to_learn_list.append(states)

        state_to_learn_dict = {
            "State to learn": state_to_learn_list,
        }

        state_to_learn = pandas.DataFrame(state_to_learn_dict)  # Create the DataFrame
        state_to_learn.to_csv("states_to_learn.csv")  # Save the DataFrame into a new file
        break

    if answer_state.title() in states_data_list:
        # If the guess is in the list, retrieve the state name , x, y data
        get_raw_data = states_data[states_data["state"] == answer_state.title()]
        state_name = get_raw_data["state"].item()
        x_coordinate = int(get_raw_data["x"])
        y_coordinate = int(get_raw_data["y"])
        write_state(state_name, x_coordinate, y_coordinate)
        guessed_state.append(state_name)
        print(guessed_state)

user_won()

screen.exitonclick()
