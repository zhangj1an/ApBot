# User command: Power on and wash outdoor sportswear, using Outdoor Care cycle, 40 °C temperature, 1200 rpm spin speed, Soak + Rinse+ option, set delay to 5 hours, and start the machine.

# Sequence of features needed:
# 1. "power_on_off": Turn on the appliance.
# User manual: "Press this button once to turn the washing machine on."
# Feature in code: "power_on_off"
#
# 2. "adjust_cycle_selector": Select the Outdoor Care cycle.
# User manual: "Select the tumble pattern and spin speed for the cycle. Refer to the Cycle Selector."
# Feature in code: "adjust_cycle_selector"
#
# 3. "adjust_temperature": Set the temperature to 40°C.
# User manual: "Press this button repeatedly to cycle through the available water temperature options: Cold water 🌡️, 20°C, 30°C, 40°C, 60°C, and 95°C."
# Feature in code: "adjust_temperature"
#
# 4. "adjust_spin_speed": Set the spin speed to 1200 rpm.
# User manual: "Press the button repeatedly to cycle through the available speeds for the spin cycle."
# Feature in code: "adjust_spin_speed"
#
# 5. "adjust_options": Select the Soak + Rinse+ option.
# User manual: "Press this button repeatedly to cycle through the options: Soak, Intensive, Prewash, Rinse+, Soak + Rinse+, Intensive + Rinse+, Prewash + Rinse+, Off."
# Feature in code: "adjust_options"
#
# 6. "adjust_delay_end": Set the delay time to 5 hours.
# User manual: "Press this button repeatedly to cycle through the available Delay End options (from 3 hours to 19 hours in one-hour increments)."
# Feature in code: "adjust_delay_end"
#
# 7. "start_pause_cycle": Start the washing machine cycle.
# User manual: "Press this button to pause and restart a cycle."
# Feature in code: "start_pause_cycle"

# Goal variable values:
# variable_power_on_off = "on" (turn on the machine)
# variable_cycle_selector = "Outdoor Care" (select Outdoor Care cycle)
# variable_temperature = "40°C" (set temperature to 40°C)
# variable_spin_speed = "1200" (set spin speed to 1200 rpm)
# variable_option = "Soak + Rinse+" (select Soak + Rinse+ option)
# variable_delay_end = 5 (set delay time to 5 hours)
# variable_start_running = "on" (start the washing machine)

class ExtendedSimulator(Simulator):
    pass