import turtle
import pandas

screen = turtle.Screen()
turtle.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
state_data = data.state.to_list()

score = 0
correct_guesses = []

while len(correct_guesses) < 50:
    answer_state = screen.textinput(f"{score}/50 States Correct", "What's another state's name?").title()

    if answer_state == "Exit":
        break

    if answer_state in state_data:
        writer = turtle.Turtle()
        writer.speed("fastest")
        writer.hideturtle()
        writer.penup()
        state_row = data[data.state == answer_state]
        writer.goto(state_row.x.item(), state_row.y.item())
        writer.write(answer_state)
        correct_guesses.append(answer_state)
        state_data.remove(answer_state)
        score += 1

    else:
        pass

states_to_learn = pandas.DataFrame(state_data)

states_to_learn.to_csv("states_to_learn")

    # for i in state_data:
    #     if i == answer_state and answer_state not in correct_guesses:
            # state_row_dict = data[data.state == i].to_dict()
            # key = 0
            # for k in state_row_dict['x']:
            #     key = k
            # x_data = state_row_dict['x'][key]
            # y_data = state_row_dict['y'][key]


            # x_data = state_row_dict['x'][state_data.index(i)]
            # y_data = state_row_dict['y'][state_data.index(i)]
            # writer.setpos(x_data, y_data)

            # writer.setpos(state_data.x, state_data.y)
            # score+=1
            # correct_guesses.append(answer_state)
            # writer.write(answer_state)
        # else:
        #     pass



