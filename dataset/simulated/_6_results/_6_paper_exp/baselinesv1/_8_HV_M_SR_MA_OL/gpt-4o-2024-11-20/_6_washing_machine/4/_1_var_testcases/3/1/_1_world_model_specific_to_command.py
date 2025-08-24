# Power up the washing machine and use the Fragrance program for 15 minutes at the lowest water level,
# spin 3 minutes, and set rinse to 'Water-Injection Rinse 1 time', then start the machine running.

# Sequence of features needed:
# 1. Turn on the washing machine: "power_on_off"
#    User manual: "Press this button to switch power on and off."
#    feature_list["power_on_off"]
#
# 2. Choose the "Fragrance" program: "adjust_program"
#    User manual: "Selects programs. The program changes each time the button is pressed."
#    feature_list["adjust_program"]
#
# 3. Adjust the water level to the lowest value: "adjust_water_level"
#    User manual: "You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L."
#    feature_list["adjust_water_level"]
#
# 4. Set the washing time to 15 minutes: "adjust_wash_time"
#    User manual: "Changes the washing time. The washing time can be set between 3 and 18 minutes."
#    feature_list["adjust_wash_time"]
#
# 5. Set the spin time to 3 minutes: "adjust_spin_time"
#    User manual: "You can set the spin time each time you press the Spin button in a range of 1 to 9 minutes and no spinning."
#    feature_list["adjust_spin_time"]
#
# 6. Set the rinse to 'Water-Injection Rinse 1 time': "adjust_rinse_type"
#    User manual: "Each time you press the Rinse button the setting changes in sequence, from Normal Rinse 2 times, Water-Injection Rinse 2 times, no rinsing, Normal Rinse 1 time, Water-Injection Rinse 1 time."
#    feature_list["adjust_rinse_type"]
#
# 7. Start the machine running: "start_pause"
#    User manual: "Starts and pauses operation. When the washing machine is paused for over one hour and no operations are done, it turns off automatically."
#    feature_list["start_pause"]

# Goal variable values:
# - Set `variable_power_on_off` to "on"
# - Set `variable_program` to "P4 (Fragrance)"
# - Set `variable_water_level` to 25
# - Set `variable_washing_time` to 15
# - Set `variable_spin_time` to 3
# - Set `variable_rinse_type` to "Water-Injection Rinse 1 time"
# - Set `variable_start_running` to "start"

class ExtendedSimulator(Simulator):
    pass