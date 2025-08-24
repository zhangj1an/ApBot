# Verifying the code against the user manual:
# The code already models the relevant features needed to achieve the user command.
# Specifically:
# 1. "Power on": This is modeled under feature "power_adjust".
# 2. "Remove stains from durable clothes, using Stain Away cycle": 
#    This is modeled under "adjust_cycle_selector" (variable_cycle_selector).
#    Raw user manual text quote: "Cycle Selector: Select the tumble pattern and spin speed for the cycle."
# 3. "60 °C temperature": This is modeled under "adjust_temperature" (variable_temperature).
#    Raw user manual text quote: "Temp button: Press this button repeatedly to cycle through the available water temperature options."
# 4. "1400 rpm spin speed": This is modeled under "adjust_spin_speed" (variable_spin_speed).
#    Raw user manual text quote: "Spin button: Press the button repeatedly to cycle through the available speeds for the spin cycle."
# 5. "Soak + Rinse+ option": This is modeled under "adjust_options" (variable_option).
#    Raw user manual text quote: "Option button: Press this button repeatedly to cycle through the options."
# 6. "Set delay to 5 hours": This is modeled under "adjust_delay_end" (variable_delay_end).
#    Raw user manual text quote: "Delay End: Press this button repeatedly to cycle through the available Delay End options."
# 7. "Start the machine": This is modeled under "start_pause_cycle" (variable_start_running).
#    Raw user manual text quote: "Press this button to pause and restart a cycle."

# Sequence of features needed to achieve this command:
# 1. Feature: "power_adjust" to turn on the machine.
# 2. Feature: "adjust_cycle_selector" to set the cycle to "Stain Away".
# 3. Feature: "adjust_temperature" to set the temperature to "60°C".
# 4. Feature: "adjust_spin_speed" to set the spin speed to "1400".
# 5. Feature: "adjust_options" to set the option to "Soak + Rinse+".
# 6. Feature: "adjust_delay_end" to set the delay end to "5 hours".
# 7. Feature: "start_pause_cycle" to start the machine.

# All these steps are accurately modeled in the current code. The goal variable values are:

goal_values = {
    "variable_power_on_off": "on",  # Step 1: Turn on the washing machine
    "variable_cycle_selector": "Stain Away",  # Step 2: Set cycle to Stain Away
    "variable_temperature": "60°C",  # Step 3: Set temperature to 60°C
    "variable_spin_speed": "1400",  # Step 4: Set spin speed to 1400 rpm
    "variable_option": "Soak + Rinse+",  # Step 5: Set option to Soak + Rinse+
    "variable_delay_end": 5,  # Step 6: Set delay to 5 hours
    "variable_start_running": "on",  # Step 7: Start the machine
}

class ExtendedSimulator(Simulator):
    pass