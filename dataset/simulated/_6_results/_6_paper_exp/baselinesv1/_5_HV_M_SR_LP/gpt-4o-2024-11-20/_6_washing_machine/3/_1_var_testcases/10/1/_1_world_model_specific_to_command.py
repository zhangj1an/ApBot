# User manual: Power On/Off - The power turns off automatically if you do not press “Start/Pause” within 10 minutes after power-on.
# User manual: Variety of Programs - Normal program and adjusting water level and set timer for finish operation.

# Features utilized:
# - "toggle_power" is used to power on the washing machine.
# - "select_program" is used to set the program to Normal.
# - "adjust_water_level" is used to select a water level of 20 L.
# - "adjust_preset_timer" is used to finish operation in 9 hours.
# - "start_operation" starts the appliance.
# - "set_child_lock" activates the child lock.

# Sequence of actions required to achieve the user command:
# 1. Feature: "toggle_power" - Action: "press_power_button" to turn on the washing machine. (Variable: variable_power_on_off)
# 2. Feature: "select_program" - Action: "press_program_button" until "1 Normal" is selected. (Variable: variable_program_selection)
# 3. Feature: "adjust_water_level" - Action: "press_water_level_button" until "20 L" is selected. (Variable: variable_water_level)
# 4. Feature: "adjust_preset_timer" - Action: "press_preset_button" until "9" is selected. (Variable: variable_preset_timer)
# 5. Feature: "start_operation" - Action: "press_start_pause_button" to start the appliance. (Variable: variable_start_running)
# 6. Feature: "set_child_lock" - Action: "press_and_hold_program_button" for 5 seconds to activate child lock. (Variable: variable_child_lock)

# The current feature_list and variables correctly allow for the execution of the steps to carry out the user command as per the user manual.
# Goal variable values:
# - variable_power_on_off: "on" (to power on the washing machine)
# - variable_program_selection: "1 Normal" (to set the Normal program)
# - variable_water_level: "20 L" (to select a water level of 20 L)
# - variable_preset_timer: 9 (to set timer for finishing operation in 9 hours)
# - variable_start_running: "on" (to start the appliance)
# - variable_child_lock: "on" (to activate child lock)

class ExtendedSimulator(Simulator): 
    pass