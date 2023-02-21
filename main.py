import tkinter as tk #Library to create the graphical interface
import codecs #Library to work with UTF-8 encoded files

#Convert data function
def convert_data():
    with codecs.open("data.txt", "r", "utf-8") as dataIn, codecs.open("dataOut.txt", "w", "utf-8") as dataOut:
        lines = dataIn.readlines() #Reading all the document
        for line in lines: #Scrolling through the lines of the text file
            record = line.strip().split(",") #Separating strings in sub-strings with ".split() function"
            hexStr = record[0].split("/") #Discarding the information that won't be needed after the "/" symbol
            hexDec = " : ".join(map(lambda h: str(int(h, 16)), hexStr[0].split(":"))) #Converting the first value from b16 to b10
            stringValue = record[2] #Saving the string value
            decValue = record[5] #Saving the b10 value
            decHex = ".".join(["{:02x}".format(int(d)) for d in decValue.split(".")]) #Converting the third value from b10 to b16
            dataOut.write(f"{stringValue} | {hexDec} | {decHex}\n") #Putting all the information in the dataOut.txt file
            outputText.insert(tk.END, f"{stringValue} | {hexDec} | {decHex}\n") #Showing the process in the graphic interface window
            print(f"{stringValue} | {hexDec} | {decHex}") #Printing the values on the terminal

#Create a window
window = tk.Tk()
window.title("Data Conversion")

#Create a label for input file
inputLabel = tk.Label(window, text="Input file: data.txt")
inputLabel.pack()

#Create a label for output file
outputLabel = tk.Label(window, text="Output file: dataOut.txt")
outputLabel.pack()

#Create a button to convert data
convertButton = tk.Button(window, text="Convert", command=convert_data)
convertButton.pack()

#Create a text box for displaying output
outputText = tk.Text(window, height=30, width=100)
outputText.pack()

#Run the window
window.mainloop()