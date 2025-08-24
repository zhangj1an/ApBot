# User manual: Press POWER, the Dehumidifier Starts Operation.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Sleep: start ultra silent air speed
variable_sleep_mode = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Mode: select auto dehumidification, Continuous dehumidification, Drying clothes, purification and ventilation, etc.
variable_mode_selection = DiscreteVariable(
    value_range=["auto_dehumidification", "continuous_dehumidification", "drying_clothes", "purification", "ventilation"],
    current_value="auto_dehumidification"
)

# Timer: realize start/shutdown of the dehumidifier at fixed time
# User manual explicitly mentions time adjustment in hours 
variable_timer = ContinuousVariable(value_ranges_steps=[(0, 24, 1)], current_value=0)

# Humidity: Humidity can be set in Auto mode
variable_humidity_level = ContinuousVariable(value_ranges_steps=[(40, 70, 5)], current_value=40)

# Internal drying mode: touch DRYING for over 2s to start internal drying process
variable_internal_drying = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Anion: start anion function
variable_anion_function = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Swing: start air swing function to realize wide-angle air sweeping
variable_air_swing = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Child Lock: press MODE for over 3s to start child lock function
variable_child_lock = DiscreteVariable(value_range=["on", "off"], current_value="off")