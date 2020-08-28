import os
import tkinter as tk
from tkinter import ttk
from tkinter import font,colorchooser,filedialog,messagebox


main_application = tk.Tk()
main_application.geometry('1100x800')
main_application.title('hapty NotePed Editor')


######################################################################### main menu ##############################
main_menu = tk.Menu()

# file icons
file = tk.Menu(main_menu,tearoff=False)
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
saveas_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

#edit Icon
Edit = tk.Menu(main_menu,tearoff=False)
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
Cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')
#view Icon
View = tk.Menu(main_menu,tearoff=False)
toolbar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
statusbar_icon = tk.PhotoImage(file='icons2/status_bar.png')
#color Icon
Color_theme = tk.Menu(main_menu,tearoff=False)
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
light_dark_icon = tk.PhotoImage(file='icons2/dark.png')
light_red_icon = tk.PhotoImage(file='icons2/red.png')
light_monokie_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')


theam_choice = tk.StringVar()
color_icons = (light_default_icon,light_plus_icon,light_dark_icon, light_red_icon, light_monokie_icon,night_blue_icon)
color_dict = {
    'light_default' : ('#000000','#ffffff'),  
    'light_plus' : ('#747474','#e0e0e0'),  
    'dark' : ('#c4c4c4c','#2d2d2d'),  
    'red' : ('#2d2d2d','#ffeBeB'),  
    'monkie' : ('#d3b774','#474747'),  
    'night_blur' : ('#ededed','#6b9dc2'),  

}

#cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=Edit)
main_menu.add_cascade(label='View',menu=View)
main_menu.add_cascade(label='Colou_theme',menu=Color_theme)
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''End Main Menu..............................


######################################################################### Tool Bar ##############################
#tool bar
toolbar = ttk.Label(main_application)
toolbar.pack(side=tk.TOP,fill=tk.X)
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(toolbar,width=30,textvariable=font_family,state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#sizebox
size_var = tk.IntVar()
font_size = ttk.Combobox(toolbar,width=40, textvariable=size_var,state='readonly')
font_size['values'] = tuple(range(8,80,2))
font_size.current(2)
font_size.grid(row=0,column=1,padx=5)

###buttons for bold
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(toolbar,image=bold_icon)
bold_btn.grid(row=0, column=2,padx=5)
###buttons for italic
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(toolbar,image=italic_icon)
italic_btn.grid(row=0, column=3,padx=5)

###buttons for underline
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(toolbar,image=underline_icon)
underline_btn.grid(row=0, column=4,padx=5)

###buttons for color
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(toolbar,image=font_color_icon)
font_color_btn.grid(row=0, column=5,padx=5)

###buttons for aling-left
font_left_align = tk.PhotoImage(file='icons2/align_left.png')
font_left_btn = ttk.Button(toolbar,image=font_left_align)
font_left_btn.grid(row=0, column=6,padx=5)

###buttons for aling-center
font_center_align = tk.PhotoImage(file='icons2/align_center.png')
font_center_btn = ttk.Button(toolbar,image=font_center_align)
font_center_btn.grid(row=0, column=7,padx=5)

###buttons for aling-right
font_right_align = tk.PhotoImage(file='icons2/align_right.png')
font_right_btn = ttk.Button(toolbar,image=font_right_align)
font_right_btn.grid(row=0, column=8,padx=5)
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''End Tool bar''''''''''''''''''''''''''''''


######################################################################### Text Editor ##############################
text_editor = tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)
scroll_bar = tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

####font size and Font Family Functionality
current_font_family = 'Arial'
current_fonT_size = 12

def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_fonT_size))
    
def change_fontsize(event=None):
    global current_fonT_size
    current_fonT_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_fonT_size))
    
font_box.bind('<<ComboboxSelected>>',change_font)
font_size.bind('<<ComboboxSelected>>',change_fontsize)
text_editor.config(font=('Arial',10))


############Buttons Functionality
#bold
def change_to_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family,current_fonT_size,'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family,current_fonT_size,'normal'))
bold_btn.config(command=change_to_bold)

#italic
def change_to_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family,current_fonT_size,'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family,current_fonT_size,'normal'))
italic_btn.config(command=change_to_italic)

##underline
def change_to_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family,current_fonT_size,'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family,current_fonT_size,'normal'))
underline_btn.config(command=change_to_underline)

### change Font color
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])
font_color_btn.configure(command=change_font_color)

### align left
def move_to_left():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')
font_left_btn.configure(command=move_to_left)

### align right
def move_to_right():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')
font_right_btn.configure(command=move_to_right)

### align canter
def move_to_center():
    text_content = text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')
font_center_btn.configure(command=move_to_center)

############ End Buttons Functionality

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''End Text Editor'''''''''''''''''''''''''


######################################################################### main Status Bar ##############################
status_bar = ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
text_changes = False
def change(even=None):
    global text_changes
    text_changes = True
    if text_editor.edit_modified():
       words = len(text_editor.get(1.0,'end-1c').split())
       character =  len(text_editor.get(1.0,'end-1c'))
       status_bar.configure(text=f"character: {character} words: {words}")
    text_editor.edit_modified(False)
text_editor.bind('<<Modified>>',change)

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''End Status Bar''''''''''''''''''''''''''''''''''


######################################################################### main menu Functinality ##############################
####file functionality start

#new file
url = ''
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0,tk.END)
    
##open file
def open_file():
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title="select File")
    # , filetypes=({'Text File','*.txt'},{'All files','*.*'})
    try:
        with open(url,'r') as fr:
         text_editor.delete(1.0,tk.END)
         text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))
          
#save File
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
           url = filedialog.asksaveasfile(mode='w' ,defaultextension='.txt')
           content2 = text_editor.get(1.0,tk.END)
           url.write(content2);
           url.close()
    except:
        return

#save as
def saveas_file(event=None):
    global url
    try:
        url = filedialog.asksaveasfile(mode='w' ,defaultextension='.txt')
        content2 = text_editor.get(1.0,tk.END)
        url.write(content2)
        url.close()
    except:
        return
    
##exit
def exit_file(event=None):
    global text_changes
    global url
    try:
        if text_changes:
            mbox = messagebox.askyesnocancel("Warning:",'Do You Want To Save The File')
            if mbox is True:
                if url: 
                   content = text_editor.get(1.0,tk.END)
                   with open(url,'w',encoding='utf-8') as fw:
                       fw.write(content)
                       main_application.destroy()
                else:
                    url = filedialog.asksaveasfile(mode='w' ,defaultextension='.txt')
                    content2 = str(text_editor.get(1.0,tk.END))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                 main_application.destroy()
        else:
            main_application.destroy()
    except:
        return   
####file functionality end

#Edit functionality start
def find_function(event=None):
   def find():
       word = find_input.get()
       text_editor.tag_remove('match','1.0',tk.END)
       matches = 0
       if word:
           start_pos = '1.0'
           while True:
               start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
               if not start_pos:
                   break
               end_pos = f'{start_pos} + {len(word)}c'
               text_editor.tag_add('match',start_pos,end_pos)
               matches += 1
               start_pos = end_pos
               text_editor.tag_config('match',foreground='red',background='yellow')       
       
   def replace():
    word = find_input.get()
    replace_text = replace_input.get()
    context = text_editor.get(1.0,tk.END)
    new_context = context.replace(word,replace_text)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(1.0,new_context)
    
   find_dialog = tk.Toplevel()
   find_dialog.geometry("450x250+500+200")
   find_dialog.title("Find")
   find_dialog.resizable(0,0)
   
   ##frame
   find_frame = ttk.LabelFrame(find_dialog,text="Find And Replace")
   find_frame.pack(pady=20)
   
   ###lable
   text_find_lable = ttk.Label(find_frame,text="Find: ")
   text_replace_lable = ttk.Label(find_frame,text="Replace: ")
   
   ##textboxes
   find_input = ttk.Entry(find_frame,width=30)
   replace_input = ttk.Entry(find_frame,width=30)
   
   ##buttons
   find_button = ttk.Button(find_frame,text="Find ", command=find)
   replace_button = ttk.Button(find_frame,text="Replace ", command=replace)
   
   ####label To Grid
   text_find_lable.grid(row=0,column=0,padx=4, pady=4)
   text_replace_lable.grid(row=1,column=0,padx=4, pady=4)
   find_input.grid(row=0,column=1,padx=4, pady=4)
   replace_input.grid(row=1,column=1,padx=4, pady=4)
   find_button.grid(row=2,column=0,padx=8, pady=4)
   replace_button.grid(row=2,column=1,padx=8, pady=4)
   
   find_dialog.mainloop()

#file Commands 
file.add_command(label='New File',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
file.add_command(label='Open File',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
file.add_command(label='Save File',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)
file.add_command(label='Save as',image=saveas_icon,compound=tk.LEFT,accelerator='Ctrl+alt+s',command=saveas_file)
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=exit_file)

# Edit Commands
Edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda: text_editor.event_generate("<control c>"))
Edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda: text_editor.event_generate("<control v>"))
Edit.add_command(label='Cut',image=Cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda: text_editor.event_generate("<control x>"))
Edit.add_command(label='Clear All',image=clear_icon,compound=tk.LEFT,accelerator='Ctrl+alt+x',command=lambda: text_editor.delete(1.0,tk.END))
Edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_function)

#View commmands
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)
show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
def hide_toobar():
    global show_toolbar
    if show_toolbar:
        toolbar.pack_forget()
        show_toolbar = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        toolbar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True
        
def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True

View.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,image=toolbar_icon,compound=tk.LEFT,command=hide_toobar)
View.add_checkbutton(label='Status Bar',onvalue=1,offvalue=False,variable=show_statusbar,image=statusbar_icon,compound=tk.LEFT,command=hide_statusbar)


#color
def change_theme():
    choice_theam = theam_choice.get()
    color_tuple = color_dict.get(choice_theam)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)

count = 0
for i in color_dict:
    Color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theam_choice , compound=tk.LEFT,command=change_theme)
    count += 1
    
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''End Main menu Functionality''''''''''''''''''''''''''''''''''''''''
main_application.config(menu=main_menu)

## binding Shortcut Key
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",saveas_file)
main_application.bind("<Control-e>",exit_file)
main_application.bind("<Control-f>",find_function)
main_application.mainloop();