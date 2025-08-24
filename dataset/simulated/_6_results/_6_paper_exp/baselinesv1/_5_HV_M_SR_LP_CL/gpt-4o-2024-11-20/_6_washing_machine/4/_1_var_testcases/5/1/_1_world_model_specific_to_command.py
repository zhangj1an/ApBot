# The command is to turn on the washing machine, select the Tub Clean program, set the water level to maximum, set rinse type to "Normal Rinse 1 time", set washing time to 3 minutes, and then start the machine.
# This seems accurately modeled in the given Simulator class code. Below highlights the sequence of features needed and the goal variable values.

# Sequence of features needed to achieve the command:
# 1. Turn on the machine.
#   - Feature: "power_on_off" 
#   - User manual text: "Press this button to switch power on and off."
#
# 2. Choose the Tub Clean program.
#   - Feature: "adjust_program"
#   - User manual text: "Selects programs. The program changes each time the button is pressed."
#
# 3. Set the water level to the maximum.
#   - Feature: "adjust_water_level"
#   - User manual text: "You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L."
#
# 4. Set the rinse setting to "Normal Rinse 1 time."
#   - Feature: "adjust_rinse_type"
#   - User manual text: "You can set the number and type of rinses by pressing the Rinse button. Each time you press the Rinse button, the setting changes in sequence, from Normal Rinse 2 times, Water-Injection Rinse 2 times, no rinsing, Normal Rinse 1 time, Water-Injection Rinse 1 time."
#
# 5. Set the washing time to 3 minutes.
#   - Feature: "adjust_wash_time"
#   - User manual text: "Changes the washing time. The washing time can be set between 3 and 18 minutes."
#
# 6. Start the machine.
#   - Feature: "start_pause"
#   - User manual text: "Starts and pauses operation. When the washing machine is paused for over one hour and no operations are done, it turns off automatically."

# Goal variable values to achieve this:
#   variable_power_on_off: "on"  (turn the machine on)
#   variable_program: "P6 (Tub Clean)"  (select Tub Clean Program)
#   variable_water_level: 59  (set water level to maximum)
#   variable_rinse_type: "Normal Rinse 1 time"  (set rinse type)
#   variable_washing_time: 3  (set washing time to 3 minutes)
#   variable_start_running: "start"  (start the washing machine)

class ExtendedSimulator(Simulator): 
    pass