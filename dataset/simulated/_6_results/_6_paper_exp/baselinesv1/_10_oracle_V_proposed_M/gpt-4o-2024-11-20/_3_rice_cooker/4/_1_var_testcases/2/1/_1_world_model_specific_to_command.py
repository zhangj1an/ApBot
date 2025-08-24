# The raw User Manual provides descriptions of features related to setting rice cooking modes, reservation timing, and starting the machine.
# The provided code correctly models all required variables and features to achieve the user command efficiently.
# Detailed feature and command alignment:
# 1. Choose 'BROWN' rice mode → Feature: "set_menu", variable: `variable_menu_index`, Relevant raw text: "**Display screen: | BROWN |...| MENU Button**"
# 2. Set reservation timer to 5 hours → Feature: "set_reservation_time", variable: `variable_reservation_time`, Relevant raw text: "**Press the “DELAY” button...Press DELAY again to adjust the displayed reservation time.**"
# 3. Start the machine → Feature: "start_cooking", variable: `variable_start_running`, Relevant raw text: "**Press the “START” button, the cooking will be finished at the appointed time.**"

# Sequence of features needed to execute the user instruction:
# - Feature: "set_menu" → Select the 'BROWN' mode.
# - Feature: "set_reservation_time" → Set timer to 5 hours.
# - Feature: "start_cooking" → Begin the process.

# Goal variable values to fulfill the user command:
# variable_menu_index: "BROWN"
# variable_reservation_time: 5
# variable_start_running: "on"

class ExtendedSimulator(Simulator): 
    pass