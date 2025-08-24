# Variable to initiate the cooking process
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for timer setting during the reservation (set timer for cooking completion)
variable_reservation_time = ContinuousVariable(value_ranges_steps=[(0, 12, 1)], current_value=0)

# Variable for function mode/menu selection
variable_menu_index = DiscreteVariable(
    value_range=["QUICK RICE", "WHITE RICE", "BROWN", "PORRIDGE", "MIXED", "STEAM", "SOUP", "STEW"], 
    current_value="QUICK RICE"
)

# Variable menu setting (placeholder)
variable_menu_setting = None

# Individual menu variable settings where the cooking time differs by menu
variable_menu_setting_quick_rice = ContinuousVariable(value_ranges_steps=[(0, 30, 1)], current_value=0)
variable_menu_setting_white_rice = ContinuousVariable(value_ranges_steps=[(0, 60, 1)], current_value=0)
variable_menu_setting_brown = ContinuousVariable(value_ranges_steps=[(0, 80, 1)], current_value=0)
variable_menu_setting_porridge = ContinuousVariable(value_ranges_steps=[(0, 90, 1)], current_value=0)
variable_menu_setting_mixed = ContinuousVariable(value_ranges_steps=[(0, 40, 1)], current_value=0)
variable_menu_setting_steam = ContinuousVariable(value_ranges_steps=[(0, 30, 1)], current_value=0)
variable_menu_setting_soup = ContinuousVariable(value_ranges_steps=[(0, 120, 1)], current_value=0)
variable_menu_setting_stew = ContinuousVariable(value_ranges_steps=[(0, 120, 1)], current_value=0)

# Mapping dictionary for menu modes
menu_setting_dict = {
    "QUICK RICE": variable_menu_setting_quick_rice,
    "WHITE RICE": variable_menu_setting_white_rice,
    "BROWN": variable_menu_setting_brown,
    "PORRIDGE": variable_menu_setting_porridge,
    "MIXED": variable_menu_setting_mixed,
    "STEAM": variable_menu_setting_steam,
    "SOUP": variable_menu_setting_soup,
    "STEW": variable_menu_setting_stew
}