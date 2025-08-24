# Python Comments:
# The current code accurately models the relevant appliance features needed to achieve the user command. 
# Sequence of features needed:
# 1. "on_off" - Turn the power on.
# 2. "set_program" - Set the program to "Bedding".
# 3. "set_water_level" - Set the water level to "High".
# 4. "set_time_manager" - Allocate 40 minutes.
# 5. "set_rinse_times" - Set rinse to "3 Times".
# 6. "set_spin_speed" - Set spin to "Short".

# **Relevant user manual text**:
# - **On/Off button:** Product is switched On or Off.
# - **Program buttons:** Available according to the laundry type.
# - **Water Level:** Select water level according to clothing categories, degree of soiling and washing habits of customers.
# - **Function (Time Manager):** Washing time, rinsing times, spinning time and other settings can be selectable.
# - **Spin and Rinse:** Settings selectable for rinse times ("Rinse Hold", "Extended", "3 Times", etc.) and spin speed ("Short", "Regular", etc.).

# **Relevant feature_list names in code**:
# - Feature: `on_off`
# - Feature: `set_program`
# - Feature: `set_water_level`
# - Feature: `set_time_manager`
# - Feature: `set_rinse_times`
# - Feature: `set_spin_speed`

# Goal variable values to achieve this command:
# 1. `variable_on_off`: "on".
# 2. `variable_program`: "Bedding".
# 3. `variable_water_level`: "High".
# 4. `variable_time_manager`: "40".
# 5. `variable_rinse_times`: "3 Times".
# 6. `variable_spin_speed`: "Short".

class ExtendedSimulator(Simulator): 
    pass