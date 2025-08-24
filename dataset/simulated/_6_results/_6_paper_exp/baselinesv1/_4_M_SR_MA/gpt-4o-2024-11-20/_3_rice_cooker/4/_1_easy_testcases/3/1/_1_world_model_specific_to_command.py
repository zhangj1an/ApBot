# Python comments explaining relevant features for the task

# Raw user manual text:
# **Reservation**
# 3. Set the timer for cooking completion
# Press the “DELAY” button, the Time Display flashes, and then press the button “DELAY” again to adjust the displayed reservation time.
# 4. Start cooking
# Press the “START” button, the cooking will be finished at the appointed time.
# Relevant feature: "set_delay_time" for setting the reservation time and "start_cooking" for starting the machine.

# Raw user manual text:
# **Operation Instructions**
# Display Screen
# MENU Button
# MENU ▶ PORRIDGE ▶ START
# 1. Measure and wash rice
# 2. Add water with reference to the water level of the Porridge.
# 3. Cooking
# Press the “MENU” button.  
# Select the "PORRIDGE" function. 
# Relevant feature: "set_menu" for selecting the cooking menu.

# Features required for user command:
# 1. "set_menu" to select the "PORRIDGE" menu.
# 2. "set_delay_time" to set the reservation time to 1 hour.
# 3. "start_cooking" to start the machine.

# Checking the code provided:
# Feature "set_menu" correctly models the step for selecting the menu.
# Feature "set_delay_time" correctly models the step for setting the timer.
# Feature "start_cooking" correctly models the step for starting the appliance.

# Required variable values to achieve the command:
# 1. variable_menu_index = "porridge" (set via "set_menu")
# 2. variable_delay_time = 1 (set via "set_delay_time")
# 3. variable_start_running = "on" (set via "start_cooking")

class ExtendedSimulator(Simulator): 
    pass