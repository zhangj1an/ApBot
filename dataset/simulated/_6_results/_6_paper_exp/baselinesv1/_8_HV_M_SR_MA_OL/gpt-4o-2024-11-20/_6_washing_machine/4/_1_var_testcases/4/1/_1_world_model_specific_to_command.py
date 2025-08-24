# The current code accurately represents the features necessary to achieve the user's command based on the described user manual. 
# The sequence of relevant features to achieve the command and their corresponding feature_list names are as follows:

# Raw user manual text describing needed actions:
# 1. Power On/Off: "Press this button to switch power on and off. The washing machine automatically switches off when operations are finished."
# Feature_list name: "power_on_off"

# 2. Adjusting washing program to Soak mode: "Selects programs. The program changes each time the button is pressed."
# Feature_list name: "adjust_program"

# 3. Adjusting washing time: "Changes the washing time. The washing time can be set between 3 and 18 minutes."
# Feature_list name: "adjust_wash_time"

# 4. Adjusting water level: "You can set the amount of water each time you press the Water Level button in a range from 25 to 59 L."
# Feature_list name: "adjust_water_level"

# 5. Adjusting spin time: "You can set the spin time each time you press the Spin button in a range of 1 to 9 minutes and no spinning."
# Feature_list name: "adjust_spin_time"

# 6. Adjusting rinse type: "You can set the number and type of rinses by pressing the Rinse button."
# Feature_list name: "adjust_rinse_type"

# 7. Start/Pause the machine: "Starts and pauses operation. When the washing machine is paused for over one hour and no operations are done, it turns off automatically."
# Feature_list name: "start_pause"

# Goal variable values to achieve this command:
# variable_power_on_off -> "on"
# variable_program -> "P5 (Soak)"
# variable_washing_time -> 18
# variable_water_level -> 30
# variable_spin_time -> 3
# variable_rinse_type -> "Normal Rinse 2 times"
# variable_start_running -> "start"

class ExtendedSimulator(Simulator): 
    pass