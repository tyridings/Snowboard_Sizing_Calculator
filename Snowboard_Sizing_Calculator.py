# Ty Ridings
# CSCI 101 - Section D
# Create Project - Snowboard Size Calculator

'''I used tkinter to create a GUI window that makes the user experience a little nicer'''
import tkinter as tk
from tkinter import *
#from tkinter import ttk
import webbrowser

'''Each of the following function equations are based on regresseion
fit lines I calculated to estimate sizing based off of online
tables I came across. Used to approximate board size.'''
def weightLow (weight):
    size = round(0.1804 * weight + 122.53)
    return size
def weightHigh (weight):
    size = round(0.1941 * weight + 124.56)
    return size
def heightUpperHigh (height):
    size = round(1.5804 * height + 48.58)
    return size
def heightUpperLow (height):
    size = round(1.2413 * height + 66.41)
    return size
def heightLowerHigh (height):
    size = round(1.978 * height + 21.374)
    return size
def heightLowerLow (height):
    size = round(2.0055 * height + 9.1209)
    return size

'''Stored text snippets that are used in the calculator'''
beg = '''\nBEGINNER\nAs a beginner, it's recommended to go with the general height, width, and length requirements. However, gravitating towards the lower end of your range will probably be the safest bet. \n\nYou will definitely want to look into a softer board as well that will be forgiving as you get accustomed to maneuvering on the mountain, but don't get a board that is too soft. Most importantly, don't forget to factor in your own preferences for style and be sure to check out the links that will go into more detail about different board shapes. All-Mountain boards tend to be the best bet for beginners if you don't know what your style is quite yet as well.'''
inter ='''\nINTERMEDIATE\nAs an intermediate rider, you've come a long way from falling over on the bunny slope to testing out some trickier black diamonds and mastering the blue slopes. You've possibly hit some minor jumps and practiced your ollie, and have gotten acustom to racing down the slopes at higher speeds than most. Your acute suggested board length depends largely on your ride style preference at this stage in the game, however you should still hover around this suggested length range.'''
adv = '''\nADVANCED\nYou're a seasoned vet that should be pretty well aware of your appropriate size by now. However, maybe you want some reassurance that you are within a reasonable range, or you want to dig into the finer details of board construction and getting a better edge over other riders when you take off in the park, slope, or backcountry. Use our size guide as a general reference, but do take into account your ride style suggestions and look into the extra provided material as well!'''
allM = '''\nALL-MOUNTAIN\nAll-Mountain is the multi-tool of the snowboard world. Whether you're floating through deep powder in the back bowl, cruising a nice line on the main slope, or testing out boxes and jumps in the park, the All-Mountain board can help get you comfortable with many different riding environments. \n\nThis is a great option for beginners, those without a hard preference, or for someone that wants a board they can take anywhere and be prepared for handling the basics of most terrains. All-Mountain lengths can usually fall towards the middle of your suggested board length range, and can go up or down depending on how you feel when trying the board on and try moving around in it. \n\nBoard shape and construction can range wildly in this style, so it's worth doing some extra research into what board suits you perfectly outside of the apps recommendations. Overall, the versatility in All-Mountains will get you where you are needing to go in a pinch.'''
freeS = '''\nFREESTYLE\nThe freestyle board is intended for park junkies that live for the boxes, rails, kickers, and of course the halfpipe. The length for this board is usually on the lower end for your suggested size range and contains more flex than most boards. The short flexible stature of this design allows for ease of maneuvering the board around for tricks and style points as well. \n\nThe base and edges are usually made with tougher materials to withstand the daily grind of objects in the park to ensure a decent lifetime for the board as well. This can be a good alternative for beginner riders as well for the size and forgiveness, but should still be taken seriously as a tool for the trials and tribulations of a hearty life lived in the pursuit of hardcore tricks and constant abuse.'''
freeR = '''\nFREERIDE\nThe freeride board is solely intended for the powder monkeys and groomer seekers among us. Freeride boards are great for deep untouched powder in the backcountry and for first runs on the slopes after a night of heavy snowfall. These boards tend to live on the lengthier end of your ride size recommendations to help stay afloat in the seas of snow and to give more surface area to displace your weight with. They also tend to have a stiffer flex as well to help with stability when travelling at higher speeds down the slope. Don't be suprised to see these boards come mostly shaped as directional or directional twins in order to optimize your ride stance as well.'''

choice = [beg, inter, adv, allM, freeS, freeR]

'''Initial Welcome Widget'''
master = tk.Tk()
master1 = tk.Frame(master)
master1.grid(row=0,column=0)
master.title("Snowboard Sizing Application")
master.configure(background='gray54')

welcome = "Welcome to the Snowboard Sizing App!"
info = "This app is designed to help you find out which snowboard size is the best fit for you. \n\nPlease enter your information in the next window and hit Calculate! to get a custom rundown of your rider preference sizing!"
tk.Message(master1, text = welcome,fg='aquamarine2',bg='gray54', font=('arial', 20),width=495).grid(row=0,column=0)
tk.Message(master1, text = info,fg='yellow2',bg='gray54', font=('arial', 14),width=495).grid(row=1,column=0)
tk.Button(master, text='Let''s Go!', font=('arial',15, ), fg='PaleTurquoise1',bg='gray54',command=master.destroy).grid(row=2, column=0, sticky=tk.W, pady=4, padx=200)
tk.mainloop()

'''Main definition used by the Calculator Window'''
def show_entry_fields():
    weight = int(w.get())
    height = int(h.get())
    boots = float(b.get())
    skill = int(v1.get())
    style = int(v2.get())

    '''These if statements limit the upper and
    lower boundaries for size possiblities'''
    if weight > 210:
      weight = 210
    elif weight < 80:
      weight = 80
    if height > 76:
      height = 76
    elif height < 42:
      height = 42
    if boots < 7:
      width = 'Narrow'
    elif boots >= 7 and boots < 10.5:
      width = 'Regular'
    elif boots >= 10.5:
      width = 'Wide'

    '''Height functions split in half (upper and lower height ranges)'''
    if height <= 64:
      h_low = heightLowerLow(height)
      h_high = heightLowerHigh(height)
    elif height > 64:
      h_low = heightUpperLow(height)
      h_high = heightUpperHigh(height)

    '''Weight range calculations'''
    w_low = weightLow(weight)
    w_high = weightHigh(weight)

    '''Here I take an average of the high and lows from
    both the weight estimation and the height estimation'''
    final_low = (w_low + h_low)//2
    final_high = (w_high + h_high)//2

    '''Referencing the stored text snippets from above'''
    if skill == 1:
      sklTxt = choice[0]
    elif skill == 2:
      sklTxt = choice[1]
    elif skill == 3:
      sklTxt = choice[2]

    if style == 1 or style == 4:
      styTxt = choice[3]
      bLabel = 'Site With Top All-Mountain Boards 2019-20'
      url = 'https://www.switchbacktravel.com/best-all-mountain-snowboards'
    elif style == 2:
      styTxt = choice[4]
      bLabel = 'Site With Top Freestyle Boards 2019-20'
      url = 'https://www.tripsavvy.com/best-freestyle-snowboards-3020629'
    elif style == 3:
      styTxt = choice[5]
      bLabel = 'Site With Top Freeride Boards 2019-20'
      url = 'https://snowboardingprofiles.com/the-top-freeride-snowboards-my-top-5'

    '''Size, Skill level, and Ride style message boxes on right hand side after calculation'''
    sze = tk.Frame(master)
    sze.grid(row=0,column=2, columnspan=2)
    szeTxt = ('The Apps General Board Recommendation For You Is: \n      A %s Width %d to %d cm Board Length' % (width,final_low,final_high))
    msg = tk.Message(sze, fg='aquamarine2',bg='gray54',text = szeTxt)
    msg.config( font=('arial', 20),width=950)
    msg.pack()

    skl = tk.Frame(master)
    skl.grid(row=1,column=2, rowspan=3)
    msg = tk.Message(skl, fg='LightCyan2',bg='gray54',text = sklTxt)
    msg.config(font=('arial',13),width=550)
    msg.pack()

    sty = tk.Frame(master)
    sty.grid(row=4,column=2, rowspan = 4)
    msg = tk.Message(sty, fg='LightCyan2',bg='gray54',text = styTxt)
    msg.config(font=('arial',13),width=550)
    msg.pack()

    '''Buttons with links for boards and other sizing options'''
    new = 1
    info_label = "Website with Further Sizing Information!"
    more_info = "https://www.the-house.com/helpdesk/snowboard-sizing/"
    def openweb():
      webbrowser.open(more_info,new=new)
    Btn = Button(master, text = info_label,command=openweb, fg='PaleTurquoise1',bg='gray54',font=('arial',12)).grid(row=2, column=3, padx = 10, pady=10)

    def openweb():
      webbrowser.open(url,new=new)
    Btn = Button(master, text = bLabel,command=openweb, fg='PaleTurquoise1',bg='gray54',font=('arial',12)).grid(row=3, column=3, padx = 10)

    def txtFile():
      with open('Snowboard_Size.txt','w') as txt_file:
        contents = ['Congrats on using the Snowboard Sizing App!','Here are your custom size results: ', '\n'+szeTxt, '\n'+info_label, more_info, '\n'+bLabel, url]
        for i in contents:
          txt_file.write(i+'\n')

    Btn2 = Button(master, text ='Save Results as .txt File!', command=txtFile, fg='PaleTurquoise1',bg='gray54',font=('arial',12)).grid(padx = 10, row=4, column=3, pady=10)

'''The guts of the instance being created for the whole calculator window'''
master = tk.Tk()
master.title("Snowboard Sizing Application")
master.configure(background='gray54')

'''Input fields for weight, height, boot size'''
tk.Label(master,
         text="Weight (lbs)", fg='yellow2',bg='gray54',font=('arial',15)).grid(row=0, column=0)
tk.Label(master,
         text="Height (inches)", fg='yellow2',bg='gray54',font=('arial',15)).grid(row=1, column=0)
tk.Label(master,
         text="Shoe Size (U.S.)", fg='yellow2',bg='gray54',font=('arial',15)).grid(row=2, column=0)

w = tk.Entry(master)
h = tk.Entry(master)
b = tk.Entry(master)

w.grid(row=0, column=1)
h.grid(row=1, column=1)
b.grid(row=2, column=1)

'''Input Fields for Skill level (radio buttons)'''
v1 = tk.IntVar()
tk.Label(master,
        text="""Choose your skill level:""",justify = tk.LEFT,padx = 20, fg='yellow2',bg='gray54',font=('arial',15)).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.Radiobutton(master,
              text="Beginner",padx = 20,variable=v1,value=1, fg='yellow2',bg='gray54',font=('arial',15), selectcolor='gray30').grid(row=4,column=1,sticky=tk.W,pady=4)
tk.Radiobutton(master,
              text="Intermediate",padx = 20,variable=v1,value=2, fg='yellow2',bg='gray54',font=('arial',15), selectcolor='gray30').grid(row=5,column=1,sticky=tk.W,pady=4)
tk.Radiobutton(master,
              text="Advanced",padx = 20,variable=v1,value=3, fg='yellow2',bg='gray54',font=('arial',15), selectcolor='gray30').grid(row=6,column=1,sticky=tk.W,pady=4)

'''Input Fields for Ride Style (radio buttons)'''
v2 = tk.IntVar()
tk.Label(master,
        text="""Choose your ride style:""",justify = tk.LEFT,padx = 20, fg='yellow2',bg='gray54',font=('arial',15)).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Radiobutton(master,
              text="All-Mountain",padx = 20,variable=v2,value=1, fg='yellow2',bg='gray54',font=('arial',15), selectcolor='gray30').grid(row=4,column=0,sticky=tk.W,pady=4)
tk.Radiobutton(master,
              text="Freestyle",padx = 20,variable=v2,value=2, fg='yellow2',bg='gray54',font=('arial',15), selectcolor='gray30').grid(row=5,column=0,sticky=tk.W,pady=4)
tk.Radiobutton(master,
              text="Freeride",padx = 20,variable=v2,value=3, fg='yellow2',bg='gray54',font=('arial',15), selectcolor='gray30').grid(row=6,column=0,sticky=tk.W,pady=4)
tk.Radiobutton(master,
              text="Not Sure",padx = 20,variable=v2,value=4, fg='yellow2',bg='gray54',font=('arial',15), selectcolor='gray30').grid(row=7,column=0,sticky=tk.W,pady=4)

'''Show and Quit buttons at the bottom of frame'''
tk.Button(master,
        text='Exit App',command=master.destroy, font=10, fg='PaleTurquoise1',bg='gray54',padx=20).grid(row=8,column=0,sticky=tk.W,pady=4, padx=40)
tk.Button(master,
        text='Calculate!',command=show_entry_fields, fg='PaleTurquoise1',bg='gray54',font=10).grid(row=8,column=1,sticky=tk.W,pady=4, padx=40)

tk.mainloop()
