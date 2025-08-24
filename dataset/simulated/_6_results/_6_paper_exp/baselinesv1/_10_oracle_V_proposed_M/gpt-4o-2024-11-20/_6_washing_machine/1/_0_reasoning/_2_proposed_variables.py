# User manual: Press this button once to turn the washing machine on. Then press this button again to turn it off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: Press this button to pause and restart a cycle.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Child Lock: Activating/Deactivating. If you want to activate or deactivate the Child Lock function, hold down the Temp. and Spin buttons at the same time for 3 seconds.
variable_child_lock = DiscreteVariable(value_range=["activated", "deactivated"], current_value="deactivated")

# Temp button: Press this button repeatedly to cycle through the available water temperature options: Cold water 🌡️, 20 °C, 30 °C, 40 °C, 60 °C, and 95 °C.
variable_temperature = DiscreteVariable(value_range=["Cold water", "20°C", "30°C", "40°C", "60°C", "95°C"], current_value="Cold water")

# Spin button: Press the button repeatedly to cycle through the available speeds for the spin cycle.
variable_spin_speed = DiscreteVariable(
    value_range=["Rinse Hold", "No spin", "400", "800", "1200", "1400"],
    current_value="Rinse Hold"
)

# Option button: Press this button repeatedly to cycle through the options. Available options: Soak, Intensive, Prewash, Rinse+, Soak + Rinse+, Intensive + Rinse+, Prewash + Rinse+, Off.
variable_option = DiscreteVariable(
    value_range=["Soak", "Intensive", "Prewash", "Rinse+", "Soak + Rinse+", "Intensive + Rinse+", "Prewash + Rinse+", "Off"],
    current_value="Off"
)

# Cycle Selector: Select the tumble pattern and spin speed for the cycle.
variable_cycle_selector = DiscreteVariable(
    value_range=[
        "Cotton", "Synthetics", "15' Quick Wash", "Baby Care", 
        "Daily Wash", "Stain Away", "Super Eco Wash", "Outdoor Care", 
        "Wool", "Hand Wash", "Spin", "Rinse + Spin"
    ],
    current_value="Cotton"
)

# Delay End: Press this button repeatedly to cycle through the available Delay End options (from 3 hours to 19 hours in one hour increments).
variable_delay_end = ContinuousVariable(
    value_ranges_steps=[(0, 3, 3), (3, 19, 1)],
    current_value=0
)