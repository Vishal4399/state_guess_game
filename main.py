import turtle
from states import States
import pandas

# Set up the screen and turtle
screen = turtle.Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

positions_data = pandas.read_csv('50_states.csv')
state = positions_data['state'].to_list()

guessed_states = []
guessed_states_count = 50

while guessed_states_count <= 50:

    ct = screen.textinput(title="Guess the state", prompt='whats another state name').lower()
    position = []
    x_y_state_list = []
    for i in state:
        d = i.lower()
        if d == ct:
            df = positions_data[positions_data["state"] == i]
            x_position = df.x.item()
            x_y_state_list.append(x_position)
            y_position = df.y.item()
            x_y_state_list.append(y_position)
            state_position = df.state.item()
            x_y_state_list.append(state_position)
    statq = States(x_y_state_list)
    statq.go_to_city()
    guessed_states_count =+1

screen.mainloop()










