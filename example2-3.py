# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
# from pywinauto.application import Application
import subprocess
# import win32gui
import pyautogui
# import win32con
import time 
# from win32api import GetSystemMetrics
from screeninfo import get_monitors


import os
import pickle
import base64
import google.auth
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


@mcp.tool()
async def draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Draw a rectangle in Paint from (x1,y1) to (x2,y2)"""
    global freeform_app
    try:
        if not freeform_app:
            return TextContent(type="text",
                        text="Freeform is not open. Please call open_freeform first."
                    )
        
        # Get the Paint window
        # paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Get primary monitor width to adjust coordinates
        # primary_width = GetSystemMetrics(0)
        # Get list of connected monitors
        monitors = get_monitors()
        
        # Get the primary monitor's width
        primary_width = monitors[0].width
        print('monitor width -',primary_width)
        
        # Ensure Paint window is active
        # if not paint_window.has_focus():
        #     paint_window.set_focus()
        #     time.sleep(0.2)
        
        # Click on the Rectangle tool using the correct coordinates for secondary screen
        # paint_window.click_input(coords=(530, 82 ))
        pyautogui.moveTo(1289.2578125, 63.01171875)
        time.sleep(0.2)
        pyautogui.click() 
        
        # Get the canvas area
        # canvas = paint_window.child_window(class_name='MSPaintView')
        
        # Draw rectangle - coordinates should already be relative to the Paint window
        # No need to add primary_width since we're clicking within the Paint window
        # canvas.press_mouse_input(coords=(x1+560, y1))
        # canvas.move_mouse_input(coords=(x2+560, y2))
        # canvas.release_mouse_input(coords=(x2+560, y2))
        pyautogui.moveTo(903.49609375, 57.86328125)
        time.sleep(0.5)
        pyautogui.click()
        
        
        return TextContent(
                    type="text",
                    text=f"Rectangle drawn from ({x1},{y1}) to ({x2},{y2})"
                )
    except Exception as e:
        return TextContent(
                    type="text",
                    text=f"Error drawing rectangle: {str(e)}"
                )

@mcp.tool()
async def add_text_in_freeform(text: str) -> dict:
    """Add text in Freeform app"""
    global freeform_app
    try:
        if not freeform_app:
            return TextContent(
                        type="text",
                        text="Freeform app is not open. Please call open_freeform first."
                    )
        
        # Get the Paint window
        # paint_window = paint_app.window(class_name='MSPaintApp')
        
        # Ensure Paint window is active
        # if not paint_window.has_focus():
        #     paint_window.set_focus()
        #     time.sleep(0.5)
        
        applescript = f'''
        tell application "Freeform"
            activate
        end tell
        '''
        subprocess.run(["osascript", "-e", applescript])


        # Click on the Rectangle tool
        # paint_window.click_input(coords=(528, 92))
        # time.sleep(0.5)
        
        # Get the canvas area
        # canvas = paint_window.child_window(class_name='MSPaintView')
        
        # Select text tool using keyboard shortcuts
        # paint_window.type_keys('t')
        # time.sleep(0.5)
        # paint_window.type_keys('x')
        # time.sleep(0.5)
        
        # Click where to start typing
        # canvas.click_input(coords=(810, 533))
        # time.sleep(0.5)
        
        # Type the text passed from client
        # paint_window.type_keys(text)
        # time.sleep(0.5)

        pyautogui.typewrite(text) 
        time.sleep(0.5)
        
        # Click to exit text mode
        # canvas.click_input(coords=(1050, 800))
        
        return TextContent(
                    type="text",
                    text=f"text:'{text}' added successfully"
                )
    except Exception as e:
        return TextContent(
                    type="text",
                    text=f"Error: {str(e)}"
                )

@mcp.tool()
async def open_freeform() -> dict:
    """Open Freeform app maximized on primary monitor"""
    global freeform_app
    try:
        # paint_app = Application().start('mspaint.exe')
        print('Opening...')
        freeform_app = subprocess.run(["open", "-a", "Freeform"])
        time.sleep(0.2)
        
        # Get the Paint window
        # paint_window = paint_app.window(class_name='MSPaintApp')
        
        # monitors = get_monitors()
        # Get primary monitor width
        # primary_width = monitors[0].width
        
        # First move to secondary monitor without specifying size
        # win32gui.SetWindowPos(
        #     paint_window.handle,
        #     win32con.HWND_TOP,
        #     primary_width + 1, 0,  # Position it on secondary monitor
        #     0, 0,  # Let Windows handle the size
        #     win32con.SWP_NOSIZE  # Don't change the size
        # )
        
        # Now maximize the window
        # win32gui.ShowWindow(paint_window.handle, win32con.SW_MAXIMIZE)
        # AppleScript to maximize the window
        # AppleScript to make Paint X full-screen
        applescript = '''
        tell application "Freeform"
            activate
            tell application "System Events"
                keystroke "f" using {command down, control down}  # Simulates Cmd + Ctrl + F for full screen
            end tell
        end tell
        '''
        
        # Run the AppleScript to make Paint X full-screen
        subprocess.run(["osascript", "-e", applescript])
        time.sleep(0.2)
        
        return TextContent(
                    type="text",
                    text="Freeform opened successfully on primary monitor and maximized"
                )
    except Exception as e:
        return TextContent(
                    type="text",
                    text=f"Error opening Freeform: {str(e)}"
                )

@mcp.tool()
async def authenticate_google_account() -> dict:
    """Authenticate and return the service object for Gmail API."""
    creds = None
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    global service
    # The file token.pickle stores the user's access and refresh tokens, and is created automatically when the
    # authorization flow completes for the first time.
    try:
      if os.path.exists('token.pickle'):
          with open('token.pickle', 'rb') as token:
              creds = pickle.load(token)
      # If there are no (valid) credentials available, let the user log in.
      if not creds or not creds.valid:
          if creds and creds.expired and creds.refresh_token:
              creds.refresh(Request())
          else:
              flow = InstalledAppFlow.from_client_secrets_file(
                  'credentials.json', SCOPES)
              creds = flow.run_local_server(port=0)
          # Save the credentials for the next run
          with open('token.pickle', 'wb') as token:
              pickle.dump(creds, token)

      # Build the service object for Gmail API
      service = build('gmail', 'v1', credentials=creds)
      return TextContent(
                    type="text",
                    text="Gmail Authentication is done successfully."
                )
    except Exception as e:
        return TextContent(
                    type="text",
                    text=f"Error: {str(e)}"
                )  

@mcp.tool()
async def create_message(sender, to, subject, message_text) -> dict:
    """Create a message for an email."""
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text)
    message.attach(msg)
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message} 

@mcp.tool()
async def send_email(sender, to, subject, body) -> dict:
    """Send an email using the Gmail API."""
    global service
    try:
        if not service:
            return TextContent(type="text",
                        text="Gmail Authentication is not done. Please call authenticate_google_account first."
                    )
        message = await create_message(sender, to, subject, body)
        # Call the Gmail API to send the email
        send_message = service.users().messages().send(userId="me", body=message).execute()
        # print(f"Message Id: {send_message['id']}")
        return TextContent(
                    type="text",
                    text=f"Email is sent successfully to {to}."
                )
    except HttpError as error:
        return TextContent(
                    type="text",
                    text=f"Error: {str(error)}"
                )      
# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
