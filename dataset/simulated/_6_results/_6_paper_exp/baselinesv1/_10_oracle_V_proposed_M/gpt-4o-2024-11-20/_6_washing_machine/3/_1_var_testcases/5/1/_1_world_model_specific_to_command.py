# The current code successfully models the functionality mentioned in the user command 
# and aligns with the user manual. Below is the reasoning:

# Relevant features:
# 1. Turning on the washing machine:
#    - Feature name: "power"
#    - User manual: Power On/Off - The power turns off automatically if you do not press “Start/Pause” within 10 minutes after power-on.
# 2. Selecting the Blanket program:
#    - Feature name: "select_program"
#    - User manual: Programs - Variety of Programs allows selection from Normal, Delicate, Baby-care, etc. Includes Blanket program.
# 3. Choosing a water level (29 L):
#    - Feature name: "adjust_water_level"
#    - User manual: Change Water Level - During the wash process, press “Water Level” to change the water level.
# 4. Setting timer to finish in 5 hours:
#    - Feature name: "set_preset_timer"
#    - User manual: Preset - Set the time to finish washing (in hours).
# 5. Starting the appliance:
#    - Feature name: "start_operation"
#    - User manual: 3. Start. - Press Start/Pause.
# 6. Activating the child lock:
#    - Feature name: "child_lock"
#    - User manual: Setting Child Lock - To prevent children from falling into the tub and drowning, if the lid is opened while the washing machine is operating, this function sounds a buzzer until it is closed.

# The user command can be fully achieved in the following sequence of features:
# "power" → "select_program" → "adjust_water_level" → "set_preset_timer" → "start_operation" → "child_lock".

# Goal variable values to achieve the command:
# 1. variable_power_on_off: "on"
# 2. variable_program_selection: "5 Blanket"
# 3. variable_water_level: "29 L"
# 4. variable_preset_timer: 5
# 5. variable_start_running: "on"
# 6. variable_child_lock: "on"

class ExtendedSimulator(Simulator): 
    pass