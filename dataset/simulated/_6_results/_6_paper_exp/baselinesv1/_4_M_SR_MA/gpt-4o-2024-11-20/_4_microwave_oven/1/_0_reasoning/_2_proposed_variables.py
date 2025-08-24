# variable_start_running
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# variable_power
variable_power = DiscreteVariable(value_range=["PL0", "PL1", "PL2", "PL3", "PL4", "PL5", "PL6", "PL7", "PL8", "PL9", "PL10"], current_value="PL10")

# variable_clock
variable_clock = TimeVariable(
    value_ranges_steps=[("00:00:00", "12:59:59", 1)],
    current_value="00:00:00"
)

# variable_timer
variable_timer = TimeVariable(
    value_ranges_steps=[("00:00:00", "99:99:59", 1)],
    current_value="00:00:00"
)

# variable_time_cook_time
variable_time_cook_time = TimeVariable(
    value_ranges_steps=[("00:00:00", "99:99:59", 1)],
    current_value="00:00:00"
)

# variable_weight_defrost
variable_weight_defrost = ContinuousVariable(
    value_ranges_steps=[(4, 100, 1)],
    current_value=4
)

# variable_time_defrost
variable_time_defrost = TimeVariable(
    value_ranges_steps=[("00:00:01", "99:99:59", 1)],
    current_value="00:00:01"
)

# variable_menu_index
variable_menu_index = DiscreteVariable(
    value_range=["popcorn", "potato", "frozen_vegetable", "beverage", "dinner_plate", "pizza"],
    current_value="popcorn"
)

# variable_menu_setting
variable_menu_setting = None

# variable_menu_setting_popcorn
variable_menu_setting_popcorn = DiscreteVariable(
    value_range=["1.75", "3.0", "3.5"],
    current_value="1.75"
)

# variable_menu_setting_potato
variable_menu_setting_potato = DiscreteVariable(
    value_range=["1", "2", "3"],
    current_value="1"
)

# variable_menu_setting_frozen_vegetable
variable_menu_setting_frozen_vegetable = DiscreteVariable(
    value_range=["4.0", "8.0", "16.0"],
    current_value="4.0"
)

# variable_menu_setting_beverage
variable_menu_setting_beverage = DiscreteVariable(
    value_range=["1", "2", "3"],
    current_value="1"
)

# variable_menu_setting_dinner_plate
variable_menu_setting_dinner_plate = DiscreteVariable(
    value_range=["9.0", "12.0", "18.0"],
    current_value="9.0"
)

# variable_menu_setting_pizza
variable_menu_setting_pizza = DiscreteVariable(
    value_range=["4.0", "8.0", "14.0"],
    current_value="4.0"
)

# menu_setting_dict
menu_setting_dict = {
    "popcorn": variable_menu_setting_popcorn,
    "potato": variable_menu_setting_potato,
    "frozen_vegetable": variable_menu_setting_frozen_vegetable,
    "beverage": variable_menu_setting_beverage,
    "dinner_plate": variable_menu_setting_dinner_plate,
    "pizza": variable_menu_setting_pizza
}

# variable_child_lock
variable_child_lock = DiscreteVariable(value_range=["locked", "unlocked"], current_value="unlocked")