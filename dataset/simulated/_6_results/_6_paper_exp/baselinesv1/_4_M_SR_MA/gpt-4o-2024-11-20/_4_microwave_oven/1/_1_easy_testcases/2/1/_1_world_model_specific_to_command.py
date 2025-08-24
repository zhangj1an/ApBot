# The provided code accurately models the relevant appliance features needed to achieve the user command.
# Sequence of features needed: "microwave_cook"
# Relevant user manual text:
# **4. MICROWAVE COOK**
# Example: to cook the food with 50% microwave power for 15 minutes.
# a. Press "TIME COOK" once."00:00" displays.
# b. Press "1","5","0","0" in order.
# c. Press "POWER" once, then press "5" to select 50% microwave power.
# d. Press "START/+30SEC." to start cooking.
# Relevant feature_list name: "microwave_cook"
# Goal variable values: 
# - Set `variable_time_cook_time` to "00:06:00"
# - Set `variable_power` to "PL8" (80% power)
# - Set `variable_start_running` to "on"

class ExtendedSimulator(Simulator): 
    pass