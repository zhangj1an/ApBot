# Variable for starting the appliance
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for menu selection
variable_menu_index = DiscreteVariable(value_range=["White Rice", "Brown Rice", "Quinoa", "Steel Cut Oats"], current_value="White Rice")

# Variable for menu setting (cooking time)
variable_menu_setting = None

# Variables for specific menu settings
variable_menu_setting_white_rice = ContinuousVariable(value_ranges_steps=[[0, 60, 1]], current_value=0)  # Cooking time in minutes
variable_menu_setting_brown_rice = ContinuousVariable(value_ranges_steps=[[0, 90, 1]], current_value=0)  # Cooking time in minutes
variable_menu_setting_quinoa = ContinuousVariable(value_ranges_steps=[[0, 40, 1]], current_value=0)  # Cooking time in minutes
variable_menu_setting_steel_cut_oats = ContinuousVariable(value_ranges_steps=[[0, 40, 1]], current_value=0)  # Cooking time in minutes

# The mapping dictionary for menu options to menu-specific settings
menu_setting_dict = {
    "White Rice": variable_menu_setting_white_rice,
    "Brown Rice": variable_menu_setting_brown_rice,
    "Quinoa": variable_menu_setting_quinoa,
    "Steel Cut Oats": variable_menu_setting_steel_cut_oats
}

# Variable for delay timer
variable_delay_timer = ContinuousVariable(value_ranges_steps=[[0, 24, 0.5]], current_value=0)  # Delay timer in hours

# Variable for keep warm
variable_keep_warm = DiscreteVariable(value_range=["on", "off"], current_value="off")