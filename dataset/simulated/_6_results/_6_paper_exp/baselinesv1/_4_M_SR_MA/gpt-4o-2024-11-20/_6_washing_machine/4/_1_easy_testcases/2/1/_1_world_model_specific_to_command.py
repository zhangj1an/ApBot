# Based on the user manual and given code, the described user command is fully supported. All relevant appliance features involved in the command have been correctly modelled in the code.

# Sequence of features needed to achieve this command:
# 1. Use the "power_on_off" feature to turn the machine on.
# 2. Use the "adjust_program" feature to set the program to "P3 (Speedy)".
# 3. Use the "adjust_water_level" feature to set the water level to 35 L.
# 4. Use the "adjust_wash_time" feature to set the washing time to 6 minutes.
# 5. Use the "adjust_rinse_type" feature to set the rinse type to "No rinsing".
# 6. Use the "start_pause" feature to start the machine running.

# Raw user manual texts describing these features:
# - Power on/off: "Press this button to switch power on and off. The washing machine automatically switches off when operations are finished."
# - Program selection: "Selects programs. The program changes each time the button is pressed."
# - Water level adjustment: "You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L."
# - Washing time adjustment: "Changes the washing time. The washing time can be set between 3 and 18 minutes."
# - Rinse type adjustment: "You can set the number and type of rinses by pressing the Rinse button. Each time you press the Rinse button the setting changes in sequence, from Normal Rinse 2 times, Water-Injection Rinse 2 times, no rinsing, Normal Rinse 1 time, Water-Injection Rinse 1 time."
# - Starting the washing machine: "Starts and pauses operation. When the washing machine is paused for over one hour and no operations are done, it turns off automatically."

# Feature list names in the given code:
# - "power_on_off" for turning on the machine.
# - "adjust_program" for choosing "P3 (Speedy)".
# - "adjust_water_level" for setting the water level to 35 L.
# - "adjust_wash_time" for setting the washing time to 6 minutes.
# - "adjust_rinse_type" for setting no rinsing.
# - "start_pause" for starting the machine running.

# Goal variable values to achieve this command:
# variable_power_on_off = "on"
# variable_program = "P3 (Speedy)"
# variable_water_level = 35
# variable_washing_time = 6
# variable_rinse_type = "No rinsing"
# variable_start_running = "start"

class ExtendedSimulator(Simulator):
    pass