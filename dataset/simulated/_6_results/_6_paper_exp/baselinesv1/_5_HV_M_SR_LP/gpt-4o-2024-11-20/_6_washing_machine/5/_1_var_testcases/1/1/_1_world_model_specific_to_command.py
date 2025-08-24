# Python comments explaining the features already accurately modeled
# User command is to:
# - Turn on the washing machine
# - Set it to 'Regular' program
# - Choose 'High' water level
# - Allocate 45 minutes for time management
# - Rinse '2 Times'
# - Spin 'Regular'

# Sequence of features to achieve this command:
# 1. Turn on the washing machine
#    Raw user manual text: **1 On/Off button** Product is switched On or Off.
#    Feature name in the code: "on_off"
# 2. Set program to 'Regular'
#    Raw user manual text: **3 Program buttons** Available according to the laundry type.
#    Feature name in the code: "set_program"
# 3. Set water level to 'High'
#    Raw user manual text: **Water Level** Select water level according to clothing categories, degree of soiling and washing habits of customers.
#    Feature name in the code: "set_water_level"
# 4. Allocate 45 minutes for time management
#    Raw user manual text: **Function** Washing time, rinsing times, spinning time and other settings can be selectable.
#    Feature name in the code: "set_time_manager"
# 5. Rinse '2 Times'
#    Raw user manual text: **Function** Washing time, rinsing times, spinning time and other settings can be selectable.
#    Feature name in the code: "set_rinse_times"
# 6. Spin 'Regular'
#    Raw user manual text: **Function** Washing time, rinsing times, spinning time and other settings can be selectable.
#    Feature name in the code: "set_spin_speed"

# Goal variable values:
# - variable_on_off: "on"
# - variable_program: "Regular"
# - variable_water_level: "3" (assuming 'High' corresponds to level 3 in the variable)
# - variable_time_manager: "5" (assuming allocating 45 minutes corresponds to step 5)
# - variable_rinse_times: "2 times"
# - variable_spin_speed: "Medium" (assuming 'Regular' corresponds to 'Medium' spin speed)

class ExtendedSimulator(Simulator):
    pass