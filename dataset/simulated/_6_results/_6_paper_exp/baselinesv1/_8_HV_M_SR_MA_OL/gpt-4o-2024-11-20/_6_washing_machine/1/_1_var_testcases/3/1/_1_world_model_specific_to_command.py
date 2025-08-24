# The sequence of features needed to achieve the user command:
# 1. Power on the machine (feature_list["power_adjust"])
# 2. Adjust cycle selector to use "15' Quick Wash" (feature_list["adjust_cycle_selector"])
# 3. Adjust temperature to "Cold water" (feature_list["adjust_temperature"])
# 4. Adjust spin speed to "400 rpm" (feature_list["adjust_spin_speed"])
# 5. Adjust options to "Rinse+" (feature_list["adjust_options"])
# 6. Adjust delay end to 5 hours (feature_list["adjust_delay_end"])
# 7. Start the machine (feature_list["start_pause_cycle"])

# Raw user manual text references:
# - "Press this button once to turn the washing machine on. Then press this button again to turn it off."
# - "Cycle Selector: Select the tumble pattern and spin speed for the cycle."
# - "Temp. button: Press this button repeatedly to cycle through the available water temperature options: Cold water 🌡️, 20 °C, 30 °C, 40 °C, 60 °C and 95 °C."
# - "Spin button: Press the button repeatedly to cycle through the available speeds for the spin cycle."
# - "Option button: Press this button repeatedly to cycle through the options: Soak > Intensive > Prewash > Rinse+ > Soak + Rinse+ > Intensive + Rinse+ > Prewash + Rinse+ > off."
# - "Delay End: Press this button repeatedly to cycle through the available Delay End options (from 3 hours to 19 hours in one hour increments)."
# - "Press this button to pause and restart a cycle."

# Relevant feature_list names:
# - "power_adjust"
# - "adjust_cycle_selector"
# - "adjust_temperature"
# - "adjust_spin_speed"
# - "adjust_options"
# - "adjust_delay_end"
# - "start_pause_cycle"

# Goal variable values to achieve this command:
# - Set variable_power_on_off to "on"
# - Set variable_cycle_selector to "15' Quick Wash"
# - Set variable_temperature to "Cold water"
# - Set variable_spin_speed to "400"
# - Set variable_option to "Rinse+"
# - Set variable_delay_end to 5
# - Set variable_start_running to "on"

class ExtendedSimulator(Simulator): 
    pass