# Variable for menu selection
variable_menu_index = DiscreteVariable(
    value_range=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
    current_value="1"
)

# Variable for loaf size selection
variable_loaf_size = DiscreteVariable(
    value_range=["700g", "900g"],
    current_value="700g"
)

# Variable for crust color selection
variable_crust_color = DiscreteVariable(
    value_range=["Light", "Medium", "Dark"],
    current_value="Medium"
)

# Variable for delay timer
variable_delay_timer = ContinuousVariable(
    value_ranges_steps=[(0, 720, 10)],  # 0 to 720 minutes (12 hours) with 10-minute steps
    current_value=0
)

# Variable for start/stop functionality
# User manual: Press START/STOP button to start or stop the Programmes.
variable_start_running = DiscreteVariable(
    value_range=["on", "off"],
    current_value="off"
)