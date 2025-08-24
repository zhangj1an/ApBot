# The existing code already accurately models the appliance features described in the user manual.
# Here's the sequence of features needed to achieve this command:
# 1. Turn on the washing machine using the "on_off" feature.
#       - User manual: **1 On/Off button** Product is switched On or Off.
#       - feature_list["on_off"]
# 2. Set the washing program to 'Regular' using the "set_program" feature.
#       - User manual: **3 Program buttons** Available according to the laundry type.
#       - feature_list["set_program"]
# 3. Set the water level to 'High' using the "set_water_level" feature. 
#       - User manual: **Water Level** Select water level according to clothing categories, degree of soiling and washing habits of customers.
#       - feature_list["set_water_level"]
# 4. Set the time manager to allocate 45 minutes. Although it does not specify in the user manual what specific values can be stored, we will approximate using the variable_time_manager.
#       - User manual: **Function** Washing time, rinsing times, spinning time and other settings can be selectable.
#       - feature_list["set_time_manager"]
# 5. Set rinse times to '2 Times' using the "set_rinse_times" feature.
#       - User manual: **Function** Washing time, rinsing times, spinning time and other settings can be selectable.
#       - feature_list["set_rinse_times"]
# 6. Set spin speed to 'Regular' using the "set_spin_speed" feature.
#       - User manual: **Function** Washing time, rinsing times, spinning time and other settings can be selectable.
#       - feature_list["set_spin_speed"]

goal_variable_values = {
    "variable_on_off": "on",                 # Step 1: Turn on
    "variable_program": "Regular",          # Step 2: Set program
    "variable_water_level": "6",            # Step 3: Set water level to 'High'
    "variable_time_manager": "5",           # Step 4: Allocate time
    "variable_rinse_times": "2 times",      # Step 5: Rinse '2 Times'
    "variable_spin_speed": "Medium"         # Step 6: Spin 'Regular' approximated as Medium
}

class ExtendedSimulator(Simulator): 
    pass