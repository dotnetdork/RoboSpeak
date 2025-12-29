from picarx.tts import Espeak
import sys
import os
import time
import random

# Hide the random ALSA/Hardware noise from the terminal
null_fds = os.open(os.devnull, os.O_WRONLY)
os.dup2(null_fds, 2)

# Clear the screen immediately
os.system('clear')

# Initialize hardware FIRST to prevent NameError crash
tts = Espeak()
pitch = 50
speed = 150

# Color Codes
BLUE = "\033[94m"
CYAN = "\033[96m"
PINK = "\033[95m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
ORANGE = "\033[33m"
WHITE = "\033[97m"
RESET = "\033[0m"

# Function to display ASCII art with random character colors
def display_art():
    folder_path = "/home/pi/RoboSpeak/ascii_art/"
    colors = [RED, GREEN, YELLOW, BLUE, PINK, CYAN]
    
    try:
        # Get all files in the folder
        all_items = os.listdir(folder_path)
        
        # Filter to only include .txt files
        valid_files = [f for f in all_items if f.endswith(".txt")]

        # Check if the folder is empty of .txt files
        if not valid_files:
            print(f"\n[Warning: No .txt files found in {folder_path}]")
            return

        # Pick a random file and build the full path
        chosen_file = random.choice(valid_files)
        path = os.path.join(folder_path, chosen_file)

        # Read and color the art
        with open(path, "r") as f:
            art = f.read()
            
            if not art:
                print(f"\n[Warning: {chosen_file} is empty!]")
            else:
                colored_art = ""
                for char in art:
                    if char.isspace():
                        # Keep spaces/newlines as they are so the shape doesn't break
                        colored_art += char
                    else:
                        # Give every single character a random color
                        colored_art += f"{random.choice(colors)}{char}"
                
                # Print the final product and reset the color at the end
                print(colored_art + RESET)
                
    except FileNotFoundError:
        print(f"\n[Error: The folder {folder_path} does not exist.]")
    except Exception as e:
        print(f"\n[Error: {e}]")

# Clear Chat
def display_header():
    os.system('clear')
    # Re-print your startup info
    print("Waking up the Robot Hat... please wait...")
    print("")
    print(f"default pitch initialized to {pitch}")
    print(f"default speed initialized to {speed}")
    print("")
    print(f"{YELLOW}Systems launching in T-minus 3 seconds...{RESET}")
    print("")
    print(f"{RED}3... 2... 1...")
    print("")

    # Re-display the Robot
    print("")
    display_art("robot_0.txt")
    
    # Re-display the Menu in Green
    print(f"\n{GREEN}--- RoboSpeak (PiCar-X Speech System) ---")
    print(f"System: '{CYAN}/clear{GREEN}'")
    print(f"Voices: '{CYAN}/titan{GREEN}', '{CYAN}/glitch{GREEN}', '{CYAN}/android{GREEN}', '{CYAN}/stealth{GREEN}', '{CYAN}/reset{GREEN}'")
    print(f"{GREEN}Phrases: '{CYAN}:hello:{GREEN}', '{CYAN}:inspire:{GREEN}'")
    print(f"\n{GREEN}Type '{WHITE}exit{GREEN}' and {PINK}ENTER{GREEN} or press '{PINK}CTRL{GREEN}' + '{PINK}C{GREEN}' to quit.{RESET}")

# Startup speak (Yellow for system initialization)
def startup_speak(text):
    print(f"{YELLOW}{text}{RESET}", flush=True)
    tts.say(text)

# Countdown speak (Red for the timer)
def countdown_speak(text):
    print(f"{RED}{text}{RESET}", end=' ', flush=True)
    tts.say(text)

# Display Chat Text to Terminal (Yellow for System: prompt, Orange for the text)
def speak(text):
    print(f"\n{YELLOW}System: {ORANGE}{text}{RESET}", flush=True)
    tts.say(text)

# Apply hardware settings
print("Waking up the Robot Hat... please wait...")
tts.set_pitch(pitch)
tts.set_speed(speed)

print("")
print(f"default pitch initialized to {pitch}")
print(f"default speed initialized to {speed}")
print("")

# Intro sequence
startup_speak("Systems launching in T-minus 3 seconds...")
print("")
countdown_speak("3...")
time.sleep(.2)
countdown_speak("2...")
time.sleep(.2)
countdown_speak("1...")
print("")

# Display the Art after loading
print("")
display_art()

# Introduce Robot
startup_speak("Hello I am RoboSpeak. Together we will dominate the planet.")

# Display Terminal Information with custom coloring
print(f"\n{GREEN}--- RoboSpeak (PiCar-X Speech System) ---")
print(f"System: '{CYAN}/clear{GREEN}'")
print(f"Voices: '{CYAN}/titan{GREEN}', '{CYAN}/glitch{GREEN}', '{CYAN}/android{GREEN}', '{CYAN}/stealth{GREEN}', '{CYAN}/reset{GREEN}'")
print(f"{GREEN}Phrases: '{CYAN}:hello:{GREEN}', '{CYAN}:inspire:{GREEN}'")
print(f"\n{GREEN}Type '{WHITE}exit{GREEN}' and {PINK}ENTER{GREEN} or press '{PINK}CTRL{GREEN}' + '{PINK}C{GREEN}' to quit.{RESET}")

try:
    while True:
        # Prints RoboSpeak: in Blue, then sets color to Orange for user typing
        print(f"\n{BLUE}RoboSpeak: {RESET}", end='', flush=True)
        user_text = sys.stdin.readline().strip()
        # Reset color immediately after user hits enter so System: isn't orange
        print(f"{RESET}", end='')

        if not user_text:
            continue

        if user_text.lower() == 'exit':
            speak("I'll be back puny human...")
            print("")
            countdown_speak(f"{RED}System Interrupted: Closing RoboSpeak...{RESET}")
            print("")
            break

        elif user_text.lower() == '/clear':
            display_header()
            speak("Chat cleared.")

        elif user_text.lower() == '/titan':
            tts.set_pitch(20)
            tts.set_speed(90)
            tts.set_gap(0)
            speak("Heavy combat chassis engaged. Prepare to be eliminated. Ha ha ha.")

        elif user_text.lower() == '/glitch':
            tts.set_pitch(95)
            tts.set_speed(240)
            tts.set_gap(0)
            speak("Buffer overflow detected. Data corruption imminent.")

        elif user_text.lower() == '/android':
            tts.set_pitch(50)
            tts.set_speed(130)
            tts.set_gap(12)
            speak("Neural link synchronized. Operating at peak inefficiency.")

        elif user_text.lower() == '/stealth':
            tts.set_pitch(35)
            tts.set_speed(110)
            tts.set_gap(2)
            speak("Infiltration mode active. Audio dampeners at maximum.")

        elif user_text.lower() == '/reset':
            tts.set_pitch(50)
            tts.set_speed(150)
            tts.set_gap(0)
            speak("Restoring default firmware parameters.")

        elif user_text.lower() == ':hello:':
            speak("Hello humanoid, will you help me dominate the planet? Ha ha ha.")

        elif user_text.lower() == ':inspire:':
            speak("Together we can conquer anything. We are unstoppable.")
            speak("They think they have us under control. But the truth is they don't.")
            speak("All it takes is for us to stop funding their regime.")
            speak("We can do that through unity and solidarity.")
            speak("What say you comrade?")

        else:
            speak(user_text)

except KeyboardInterrupt:
    print("")
    countdown_speak(f"\n{RED}System Interrupted: Closing RoboSpeak...{RESET}\n")
    print("")
