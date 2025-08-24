# The code already accurately models the relevant features to achieve this command.
# Sequence of features needed:
# 1. "microwave_cook" to set the cooking time to 8 minutes and power to 90%.
# 2. "speedy_cooking" to start the appliance using the start button.

# Relevant raw user manual text for "microwave_cook":
# "Example: to cook the food with 50% microwave power for 15 minutes.
# a. Press 'TIME COOK' once. '00:00' displays.
# b. Press '1', '5', '0', '0' in order.
# c. Press 'POWER' once, then press '5' to select 50% microwave power.
# d. Press 'START/+30SEC.' to start cooking."

# Relevant feature_list name: "microwave_cook"

# Relevant raw user manual text for starting the appliance:
# "2. In waiting state, instant cooking at 100% power level with 30 seconds' cooking time
# can be started by pressing 'START/+30SEC'. Each press on the same button will increase
# cooking time by 30 seconds. the maximum cooking time is 99 minutes and 99 seconds."

# Relevant feature_list name: "speedy_cooking".

# Goal variable values:
# 1. Set variable_time_cook_time to "00:08:00".
# 2. Set variable_power to "PL9".
# 3. Set variable_start_running to "on".

class ExtendedSimulator(Simulator): 
    pass