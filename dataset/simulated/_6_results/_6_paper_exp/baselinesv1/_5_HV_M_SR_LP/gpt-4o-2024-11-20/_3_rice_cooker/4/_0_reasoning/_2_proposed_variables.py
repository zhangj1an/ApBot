# Variable to start the appliance 
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for keep warm or cancel
variable_keep_warm = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for delay cooking (reservation time)
variable_delay_time = ContinuousVariable(value_ranges_steps=[(0, 12, 1)], current_value=0)

# Variable for menu selection index
variable_menu_index = DiscreteVariable(value_range=["quick_rice", "white_rice", "brown", "porridge", "grains", "mixed", "steam", "soup", "stew"], current_value="quick_rice")

# Placeholder for menu setting initialization
variable_menu_setting = None

# Variable menu-specific settings
variable_menu_setting_quick_rice = DiscreteVariable(["default"], "default")  # Quick Rice has a fixed 30-minute duration
variable_menu_setting_white_rice = DiscreteVariable(["default"], "default")  # White Rice is pre-set, specifics not detailed in manual
variable_menu_setting_brown = ContinuousVariable(value_ranges_steps=[(0, 2, 0.1)], current_value=0)  # Brown has approximately 1 hour 20 min cooking time, adjust per manual guidelines
variable_menu_setting_porridge = ContinuousVariable(value_ranges_steps=[(0, 2, 0.1)], current_value=0)  # For porridge cooking, default is 1 hour 30 min
variable_menu_setting_grains = ContinuousVariable(value_ranges_steps=[(0, 2, 0.1)], current_value=0)  # Grains cooking, 1 hour 10 min approx
variable_menu_setting_mixed = ContinuousVariable(value_ranges_steps=[(0, 2, 0.1)], current_value=0)  # Mixed rice cooking with customization
variable_menu_setting_steam = ContinuousVariable(value_ranges_steps=[(0, 3, 0.1)], current_value=0)  # Steam default is 30 min but adjustable
variable_menu_setting_soup = ContinuousVariable(value_ranges_steps=[(0, 3, 0.1)], current_value=0)  # Soup cooking default 2 hours
variable_menu_setting_stew = ContinuousVariable(value_ranges_steps=[(0, 3, 0.1)], current_value=0)  # Stew cooking similar to soup's 2-hour default

# Dictionary mapping menu index to respective settings
menu_setting_dict = {
    "quick_rice": variable_menu_setting_quick_rice,
    "white_rice": variable_menu_setting_white_rice,
    "brown": variable_menu_setting_brown,
    "porridge": variable_menu_setting_porridge,
    "grains": variable_menu_setting_grains,
    "mixed": variable_menu_setting_mixed,
    "steam": variable_menu_setting_steam,
    "soup": variable_menu_setting_soup,
    "stew": variable_menu_setting_stew
}