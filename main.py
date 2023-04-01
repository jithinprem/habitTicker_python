'''
    TODO: use database
    TODO : instead of new window use newpage when addtask is called
    TODO : remove tick functionality
    TODO : handle ticks with monthly(30 ticks) or hourly(24 ticks) format according to task
    TODO : auto add ❌ when a hour is passed or when a day is passed in respective task
    TODO : implement a notification when day about to end, hour about to end
    TODO : accomplishment should display the efficiency of tasks
    TODO : improve UI
    TODO : daily the ticks are not reset, try something to reset
'''

import tkinter as tk
from functools import partial   # to pass arguments to command

# constants
font_style_title = ('Verdana', 20)

# variables
tasks = [{'my_task': 'wakeup', 'ticks': 2}, {'my_task': 'run', 'ticks': 4}] # dict with 'my_task' and 'ticks' update it in addtask
task_lab = []  # list of Label to display task
task_ent = []  # list of Label to display tick
is_checked = []
check_buttons = [] # list of radio buttons

# button click functions
def addHabit():
    tasks.append({'my_task': taskenter.get(), 'ticks':0})


def seeAccomplish():
    print('new page is opening')

def addTick(i):
    print('adding a tick')
    tasks[i]['ticks'] +=1
    task_ent[i].config(text='✅' * tasks[i]['ticks'], anchor='w')

def refresh():
    task_ent.clear()
    task_lab.clear()
    check_buttons.clear()
    for i in range(len(tasks)):
        val = tasks[i]
        task_lab.append(tk.Label(text=val['my_task'], anchor='w'))
        task_lab[i].grid(row=4+i, column=0)
        check_buttons.append(tk.Button(window,text='finished ', command=partial(addTick, i)))
        check_buttons[i].grid(row= 4+i, column=1)
        task_ent.append(tk.Label(text='✅' * val['ticks'], anchor='w'))
        task_ent[i].grid(row=4+i, column=2)


window = tk.Tk()
window.title('habit ticker')
window.geometry("700x500")
app_title = tk.Label(window, text='Habit Ticker', font=font_style_title)
app_title.grid(column=1, row=1, columnspan=3)

add_habit_btn = tk.Button(text='Add Habit', command=addHabit)
add_habit_btn.grid(column=1, row=2, columnspan=1)
accomplish_btn = tk.Button(text='Accomplishments', command=seeAccomplish)
accomplish_btn.grid(column=2, row=2, columnspan=1)
refresh_btn = tk.Button(text='Refresh', command=refresh)
refresh_btn.grid(column=3, row=2, columnspan=1)
taskenter = tk.Entry(window)
taskenter.grid(column=0, row=2)

refresh()

window.mainloop()


