# Python Comment:
# The current code correctly models the relevant appliance features needed to achieve the command:
# "Activate the washer, configure to 'Wool' setting, 'High' water selection, set time manager to 25 minutes, '2 Times' rinse, and 'Regular' spin."
# Listed below are the sequence of features required to achieve this user command and the specific actions to adjust the variables.

# Sequence of features needed to achieve the command:
# 1. "on_off": To turn the appliance on.
#    Raw User Manual Text: **1 On/Off button** Product is switched On or Off.
#    Feature List Name: "on_off"
#    Action: "press_on_off_button" — sets `variable_on_off` to `"on"`.

# 2. "set_program": To configure the washer to "Wool" setting.
#    Raw User Manual Text: **3 Program buttons** Available according to the laundry type.
#    Feature List Name: "set_program"
#    Action: "press_program_buttons" — cycles `variable_program` through available programs to set it to "Wool".

# 3. "set_water_level": To set water level to "High".
#    Raw User Manual Text: **Water Level** Select water level according to clothing categories, degree of soiling and washing habits of customers.
#    Feature List Name: "set_water_level"
#    Action: "press_water_level_button" — adjusts `variable_water_level` to `"6"`.

# 4. "set_time_manager": To set time manager to 25 minutes.
#    Raw User Manual Text: **Function - Time Manager** Washing time, rinsing times, spinning time and other settings can be selectable.
#    Feature List Name: "set_time_manager"
#    Action: "press_time_manager_button" — cycles `variable_time_manager` to select `"5"` (preset for 25 minutes).

# 5. "set_rinse_times": To set rinse times to "2 Times".
#    Raw User Manual Text: **Function - Rinse Times** Washing time, rinsing times, spinning time and other settings can be selectable.
#    Feature List Name: "set_rinse_times"
#    Action: "press_rinse_button" — adjusts `variable_rinse_times` to `"2 times"`.

# 6. "set_spin_speed": To set spin speed to "Regular".
#    Raw User Manual Text: **Function - Spin Speed** Washing time, rinsing times, spinning time and other settings can be selectable.
#    Feature List Name: "set_spin_speed"
#    Action: "press_spin_button" — adjusts `variable_spin_speed` to `"Medium"` (Regular represents Medium spin speed).

# Goal variable values to achieve the command:
# variable_on_off = "on"
# variable_program = "Wool"
# variable_water_level = "6"
# variable_time_manager = "5"
# variable_rinse_times = "2 times"
# variable_spin_speed = "Medium"

class ExtendedSimulator(Simulator): 
    pass