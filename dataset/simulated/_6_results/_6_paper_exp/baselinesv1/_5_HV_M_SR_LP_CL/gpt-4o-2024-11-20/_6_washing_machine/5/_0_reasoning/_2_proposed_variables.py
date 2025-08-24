# User manual: **1 On/Off button** Product is switched On or Off.
variable_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: **2 Start/Pause button** Press the button to start or pause the washing cycle.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: **3 Program buttons** Available according to the laundry type.
variable_program = DiscreteVariable(value_range=["Regular", "Delicates", "Mixed", "Wool", "Heavy Duty", "Bedding", "Quick Wash", "Clean Tub"], current_value="Regular")

# User manual: **Water Level** Select water level according to clothing categories, degree of soiling and washing habits of customers.
variable_water_level = DiscreteVariable(value_range=["1", "2", "3", "4", "5", "6"], current_value="1")

# User manual: **Function** Washing time, rinsing times, spinning time and other settings can be selectable.
# Rinse times
variable_rinse_times = DiscreteVariable(value_range=["1 time", "2 times", "3 times", "4 times"], current_value="1 time")

# Spin speed
variable_spin_speed = DiscreteVariable(value_range=["Off", "Low", "Medium", "High"], current_value="Off")

# Time Manager
variable_time_manager = DiscreteVariable(value_range=["1", "2", "3", "4", "5", "6"], current_value="1")

# User manual: **Clean Tub** Free-cleaning function: when the tub is spinning, The strong water flow will scour the inner/outer tub and reduce the dirt residue.
variable_clean_tub = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: **Child Lock** To avoid operation of functions accidentally pressed by children.
variable_child_lock = DiscreteVariable(value_range=["on", "off"], current_value="off")