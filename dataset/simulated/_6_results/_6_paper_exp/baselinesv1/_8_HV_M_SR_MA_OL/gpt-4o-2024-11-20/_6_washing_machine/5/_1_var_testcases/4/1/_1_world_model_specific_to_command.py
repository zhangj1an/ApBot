# The current code accurately represents the user commands based on the user manual. 
# Here is why:
# The features needed to achieve the command are properly modeled:
# 1. **Activate the washer**: This corresponds to the feature "on_off". The user manual mentions: 
#    **1 On/Off button** Product is switched On or Off. This is correctly captured in the feature_list["on_off"].
# 2. **Configure to 'Wool' setting**: This corresponds to the feature "set_program". 
#    User manual: **3 Program buttons** Available according to the laundry type.
# 3. **'High' water selection**: This corresponds to the feature "set_water_level". 
#    User manual: **Water Level** Select water level according to clothing categories, degree of soiling and washing habits of customers.
# 4. **Set time manager to 25 minutes**: 
#    Although the user mentions a time (25 minutes), this item is modeled as a discrete selection through the feature "set_time_manager", e.g., "1, 2, 3..., 6".
#    User manual refers: **Function** Washing time, rinsing times, spinning time, and other settings can be selectable.
# 5. **'2 Times' rinse**: This is already included in the feature "set_rinse_times".
#    User manual: **Function** Rinsing times can be selected (e.g., 1 time, 2 times, etc.).
# 6. **'Regular' spin**: This is captured in the feature "set_spin_speed". 
#    User manual: **Function** Spinning speeds can be selected (e.g., low, medium, high, etc.).

# Based on the current feature list, the following sequence of features needs to be executed to satisfy the command:
# - Feature: "on_off" to set variable_on_off to "on".
# - Feature: "set_program" to set variable_program to "Wool".
# - Feature: "set_water_level" to set variable_water_level to "5" (corresponding to a "High" water level).
# - Feature: "set_time_manager" to set variable_time_manager to "2" (assuming 25 minutes correlates to this discrete option).
# - Feature: "set_rinse_times" to set variable_rinse_times to "2 times".
# - Feature: "set_spin_speed" to set variable_spin_speed to "Medium" (interpreted as "Regular" by the user command).

goal_variable_values = {
    "variable_on_off": "on",
    "variable_program": "Wool",
    "variable_water_level": "5",
    "variable_time_manager": "2",
    "variable_rinse_times": "2 times",
    "variable_spin_speed": "Medium",
}

class ExtendedSimulator(Simulator): 
    pass