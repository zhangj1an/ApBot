# Power on and wash synthetic shirts for a quick wash, using synthetics cycle, cold water temperature, 
# 1200 rpm spin speed, rinse+ option, set delay to 5 hours, and start the machine.

# Listed sequence of features needed to achieve this command:
# 1. Power on the machine (feature_list["power_on_off"]).
# Raw user manual text: "*Press this button once to turn the washing machine on. Then press this button again to turn it off.*"
# 2. Set Synthetics cycle using Cycle Selector (feature_list["adjust_cycle_selector"]).
# Raw user manual text: "*Cycle Selector - Select the tumble pattern and spin speed for the cycle.*"
# 3. Set cold water temperature using Temp button (feature_list["adjust_temperature"]).
# Raw user manual text: "*Press this button repeatedly to cycle through the available water temperature options: Cold water 🌡️, 20 °C, 30 °C, 40 °C, 60 °C and 95 °C.*"
# 4. Set 1200 RPM spin speed using Spin button (feature_list["adjust_spin_speed"]).
# Raw user manual text: "*Press the button repeatedly to cycle through the available speeds for the spin cycle.*"
# 5. Set Rinse+ option using Option button (feature_list["adjust_options"]).
# Raw user manual text: "*Press this button repeatedly to cycle through the options: Soak > Intensive > Prewash > Rinse+.*"
# 6. Set Delay End to 5 hours (feature_list["adjust_delay_end"]).
# Raw user manual text: "*Press this button repeatedly to cycle through the available Delay End options (from 3 hours to 19 hours in one hour increments).*"
# 7. Start the machine (feature_list["start_pause_cycle"]).
# Raw user manual text: "*Press this button to pause and restart a cycle.*"

# Goal variable values to achieve this command:
# - variable_power_on_off = "on"
# - variable_cycle_selector = "Synthetics"
# - variable_temperature = "Cold water"
# - variable_spin_speed = "1200"
# - variable_option = "Rinse+"
# - variable_delay_end = 5
# - variable_start_running = "on"

class ExtendedSimulator(Simulator): 
    pass