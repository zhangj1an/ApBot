# Variable: variable_menu_index
variable_menu_index = DiscreteVariable(
    value_range=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
    current_value="1"
)

# Variable: variable_menu_setting
variable_menu_setting = None

# Variable: variable_menu_setting_1 (Basic White)
variable_menu_setting_1 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("3:00:00", "3:00:00", 1), ("2:53:00", "2:53:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_2 (French)
variable_menu_setting_2 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("3:50:00", "3:50:00", 1), ("3:40:00", "3:40:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_3 (Wholewheat)
variable_menu_setting_3 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("3:40:00", "3:40:00", 1), ("3:32:00", "3:32:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_4 (Quick)
variable_menu_setting_4 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("1:40:00", "1:40:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_5 (Sweet)
variable_menu_setting_5 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("2:55:00", "2:55:00", 1), ("2:50:00", "2:50:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_6 (Fastbake I)
variable_menu_setting_6 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("0:58:00", "0:58:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_7 (Fastbake II)
variable_menu_setting_7 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("0:58:00", "0:58:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_8 (Dough)
variable_menu_setting_8 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("1:30:00", "1:30:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_9 (Jam)
variable_menu_setting_9 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("1:20:00", "1:20:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_10 (Cake)
variable_menu_setting_10 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("2:50:00", "2:50:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_11 (Sandwich)
variable_menu_setting_11 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("3:00:00", "3:00:00", 1), ("2:55:00", "2:55:00", 1)],
    current_value="0:00:00"
)

# Variable: variable_menu_setting_12 (Extrabake)
variable_menu_setting_12 = TimeVariable(
    value_ranges_steps=[("0:00:00", "0:00:00", 1), ("1:00:00", "1:00:00", 10)],
    current_value="0:00:00"
)

# The mapping dictionary
menu_setting_dict = {
    "1": variable_menu_setting_1,
    "2": variable_menu_setting_2,
    "3": variable_menu_setting_3,
    "4": variable_menu_setting_4,
    "5": variable_menu_setting_5,
    "6": variable_menu_setting_6,
    "7": variable_menu_setting_7,
    "8": variable_menu_setting_8,
    "9": variable_menu_setting_9,
    "10": variable_menu_setting_10,
    "11": variable_menu_setting_11,
    "12": variable_menu_setting_12
}

# Crust Color Variable
variable_crust_color = DiscreteVariable(
    value_range=["light", "medium", "dark"],
    current_value="light"
)

# Loaf Size Variable
variable_loaf_size = DiscreteVariable(
    value_range=["1.5LB", "2LB"],
    current_value="1.5LB"
)

# Start Running Variable
variable_start_running = DiscreteVariable(
    value_range=["on", "off"],
    current_value="off"
)

# Timer Delay
variable_timer_delay = TimeVariable(
    value_ranges_steps=[("00:00:00", "13:00:00", 600)],
    current_value="00:00:00"
)