from tkinter import *
import trigram_a1 as trigram_code

root = Tk()
root.title('A1_NLP - Autofill Search')
root.geometry("500x300")


# Update the listbox
def update(data):
    # Clear the listbox
    my_list.delete(0, END)

    # Add toppings to listbox
    for item in data:
        my_list.insert(END, item)


# Create function to check entry vs listbox
def check(e):
    # grab what was typed
    typed = my_entry.get()
    entryList = typed.lower().split()
    predictedList = []
    if len(entryList) >= 2:
        predictedList = trigram_code.predict_word(entryList[-2], entryList[-1])
        # print(predictedList)

    # update our listbox with selected items
    update(predictedList)


# Create a label
my_label = Label(root, text="Search...",
                 font=("Helvetica", 14), fg="grey")

my_label.pack(pady=20)

# Create an entry box
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()

# Create a listbox
my_list = Listbox(root, width=50)
my_list.pack(pady=40)

# Create a binding on the entry box
my_entry.bind("<KeyRelease>", check)

root.mainloop()

