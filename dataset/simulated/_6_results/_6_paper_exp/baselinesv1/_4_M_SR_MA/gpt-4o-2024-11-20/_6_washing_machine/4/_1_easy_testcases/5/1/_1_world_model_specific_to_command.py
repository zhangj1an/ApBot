# Python Comments:
# For the requested user command: "Turn on the machine and choose the Tub Clean program for a maximum water level with rinse setting to be 'Normal Rinse 1 time' and a wash time of 3 minutes, then start the machine running."
# The features and variables in the current code are modeled accurately to achieve this command. Below is the sequence of features needed, the raw user manual text, and goal variable values to complete this command.

# **Sequence of Features Needed:**
# 1. "power_on_off" feature to turn the machine on.
# 2. "adjust_program" feature to choose the "Tub Clean" program.
# 3. "adjust_water_level" feature to set the water level to maximum ("59 L").
# 4. "adjust_rinse_type" feature to set "Normal Rinse 1 time".
# 5. "adjust_wash_time" feature to set wash time to "3 minutes".
# 6. "start_pause" feature to start the machine running.

# **Relevant User Manual Text:**
# - Power button: "Press this button to switch power on and off."
# - Selecting program: "Selects programs. The program changes each time the button is pressed."
# - Water level: "You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L."
# - Rinse: "You can set the number and type of rinses by pressing the Rinse button."
# - Wash time: "Changes the washing time. The washing time can be set between 3 and 18 minutes."
# - Starting operation: "Starts and pauses operation."

# **Corresponding Feature List Names:**
# 1. "power_on_off" for turning the machine on.
# 2. "adjust_program" for choosing the Tub Clean program.
# 3. "adjust_water_level" for setting the water level.
# 4. "adjust_rinse_type" for setting rinse type.
# 5. "adjust_wash_time" for wash time.
# 6. "start_pause" to start the machine.

# **Goal Variable Values:**
# - variable_power_on_off: "on"
# - variable_program: "P6 (Tub Clean)"
# - variable_water_level: 59
# - variable_rinse_type: "Normal Rinse 1 time"
# - variable_washing_time: 3
# - variable_start_running: "start"

class ExtendedSimulator(Simulator): 
    pass