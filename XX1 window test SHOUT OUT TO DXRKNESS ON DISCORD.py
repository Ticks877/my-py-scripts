made by dxrkness on discord


import tkinter as tk

window=tk.Tk()
window.overrideredirect(1)
window.attributes("-topmost", 1)
window.attributes("-alpha", 0.9)

screenWidth=window.winfo_screenwidth()
screenHeight=window.winfo_screenheight()

def tryClose(win):
  if confirm("Are you YUH HUH OR NUH HUH?", "red", "green"):
    win.destroy()

def confirm(m, c1, c2):
  confirmWindow = tk.Toplevel()
  confirmWindow.overrideredirect(1)
  confirmWindow.attributes("-topmost", 1)

  confirmWindow.focus()

  result = {"value": None}

  def onYes():
    result["value"] = 1
    confirmWindow.destroy()

  def onNo():
    result["value"] = 0
    confirmWindow.destroy()

  windowWidth = screenWidth // 4
  windowHeight = screenHeight // 8
  xPosition = (screenWidth - windowWidth) // 2
  yPosition = (screenHeight - windowHeight) // 2
  confirmWindow.geometry(f"{windowWidth}x{windowHeight}+{xPosition}+{yPosition}")

  frame = tk.Frame(confirmWindow, bg="white")
  frame.pack(fill="both", expand=True)

  messageLabel = tk.Label(
    frame,
    text=m,
    fg="white",
    bg="black",
    font=("Arial", 10, "bold"),
    wraplength=windowWidth - 20,
  )
  messageLabel.pack(pady=10)

  noButton = tk.Button(
    frame,
    text="nuh uh",
    bg=c1,
    relief="flat",
    cursor="hand2",
    command=lambda: onNo(),
    font=("Arial", 8, "bold")
  )
  noButton.pack(side="right", anchor="s", padx=10, pady=10)

  yesButton = tk.Button(
    frame,
    text="yuh huh",
    bg=c2,
    relief="flat",
    cursor="hand2",
    command=lambda: onYes(),
    font=("Arial", 8, "bold")
  )
  yesButton.pack(side="right", anchor="s", pady=10)

  confirmWindow.bind("<Return>", lambda event: onYes())
  confirmWindow.bind("<Escape>", lambda event: onNo())

  confirmWindow.grab_set()
  confirmWindow.wait_window()

  print(f"{m} {result['value']}")
  return result["value"]

windowWidth=screenWidth // 6
windowHeight=screenHeight // 3

xPosition=screenWidth - windowWidth
yPosition=screenHeight - windowHeight

window.geometry(f"{windowWidth}x{windowHeight}+{xPosition}+{yPosition}")

frame=tk.Frame(window, bg="black")
frame.pack(fill="both", expand=1)

closeButton=tk.Button(
  frame,
  text="X",
  fg="white",
  bg="black",
  relief="flat",
  cursor="hand2",
  command=lambda: tryClose(window),
  font=("Arial", 8, "bold")
)
closeButton.pack(side="right", anchor="n")
closeButton.bind("<Enter>", lambda event: closeButton.config(bg="red"))
closeButton.bind("<Leave>", lambda event: closeButton.config(bg="black"))

section1=tk.Text(
  frame,
  height=10,
  fg="white",
  bg="black",
  font=("Arial", 8, "bold"),
  border=0,
  padx=5,
  pady=5
)
section1.pack(fill="x", side="left", anchor="n")

section1.config(state="normal")
section1.delete("1.0", "end")
section1.insert("end", "Hi")
section1.config(state="disabled")

window.mainloop()
