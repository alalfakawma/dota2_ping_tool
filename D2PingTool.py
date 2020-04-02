import tkinter as tk
from ping3 import ping
from functools import partial

# Constants
WIN_WIDTH=640
WIN_HEIGHT=480
TITLE="Dota2 Ping Tool"

# Root
root = tk.Tk();
root.title(TITLE) # Change the title of the window
root.resizable(False, False)

# Canvas
canvas = tk.Canvas(root, width=WIN_WIDTH, height=WIN_HEIGHT)
canvas.pack()

# Main Frame
mainFrame = tk.Frame(canvas)
mainFrame.place(relwidth=1, relheight=1)

# Dash Frame
dashFrame = tk.Frame(mainFrame)
dashFrame.pack()

# Head label
headLabel = tk.Label(dashFrame, text=TITLE, pady=20, font=("Helvetica", 18, "bold"))
headLabel.grid(row=0, column=0)

# Button Frame
buttonFrame = tk.Frame(mainFrame)
buttonFrame.pack()

# List of the servers and their respective ips
ipList = {
    "Australia (Sydney)": "syd.valve.net",
    "Chile (Santiago)": "200.73.67.1",
    "Dubai (UAE)": "dxb.valve.net",
    "Europe East 1 (Vienna, Austria)": "vie.valve.net",
    "Europe East 2 (Vienna, Austria)": "185.25.182.1",
    "Europe West 1 (Luxembourg)": "lux.valve.net",
    "Europe West 2 (Luxembourg)": "146.66.158.1",
    "India (Kolkata)": "116.202.224.146",
    "Peru (Lima)": "191.98.144.1",
    "Russia 1 (Stockholm, Sweden)": "sto.valve.net",
    "Russia 2 (Stockholm, Sweden)": "185.25.180.1",
    "SE Asia 1 (Singapore)": "sgp-1.valve.net",
    "SE Asia 2 (Singapore)": "sgp-2.valve.net",
    "South Africa 1 (Cape Town)": "cpt-1.valve.net",
    "South Africa 2 (Cape Town)": "197.80.200.1",
    "South Africa 3 (Cape Town)": "197.84.209.1",
    "South Africa 4 (Johannesburg)": "196.38.180.1",
    "South America 1 (Sao Paulo)": "gru.valve.net",
    "South America 2 (Sao Paulo)": "209.197.25.1",
    "South America 3 (Sao Paulo)": "209.197.29.1",
    "US East (Sterling, VA)": "iad.valve.net",
    "US West (Seattle, WA)": "eat.valve.net"
}

# Button click callback function
def buttonClick(server, ip):
    print('%s : %s' % (server, ip))

# Add the buttons according to the list
row = 0
colOffset = 3
for idx, (server, ip) in enumerate(ipList.items()):
    if idx % colOffset == 0:
        row += 1
        col = 0

    buttonFrame.grid_rowconfigure(row, weight=1)
    buttonFrame.grid_columnconfigure(col, weight=1)
    button = tk.Button(buttonFrame, text=server, command=partial(buttonClick, server, ip), font=("Helvetica", 9))
    button.grid(row=row, column=col, sticky="nwse")
    col += 1

# Entry for showing the icmp ping status
# First create a frame for it
pingFrame = tk.Frame(mainFrame, bg="#000000")
pingFrame.place(relwidth=1, relheight=1, rely=0.6)

print(ping('google.com'))

# for i in range(15):
#     pingLabel = tk.Label(pingFrame, text="Ping: 30ms", bg="#000000", fg="lightgreen")
#     pingLabel.grid(row=i)

root.mainloop()
