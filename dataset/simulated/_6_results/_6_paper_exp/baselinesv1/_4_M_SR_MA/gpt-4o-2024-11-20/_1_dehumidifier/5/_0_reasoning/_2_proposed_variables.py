# User manual: Turns the unit on and off.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: Fan/Air Speed (SPEED): 1. Low 2. Mid 3. High
variable_fan_speed = DiscreteVariable(value_range=["1", "2", "3"], current_value="1")

# User manual: Turns the negative Ion generator on and off
variable_ion_generator = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: Sets an Auto-On or Shut-Off timer, 1H, 2H or 4H.
variable_timer = DiscreteVariable(value_range=["0", "1", "2", "4"], current_value="0")

# User manual: Press to send the display to sleep. The unit will continue working on the low fan mode but the lights will turn off.
variable_sleep_mode = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: After 5000 hours of use, the sleep button will flash continuously as a reminder to replace the filter. After you have fitted a new filter, hold the sleep button down for 5 seconds to reset the timer.
variable_filter_timer_reset = DiscreteVariable(value_range=["reset", "not_reset"], current_value="not_reset")