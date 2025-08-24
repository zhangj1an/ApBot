# variable_start_running indicates whether the cooking process has started or not.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# variable_on_off represents the power state of the machine.
# User manual: Plug the rice cooker into an available 120V AC outlet.
variable_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# variable_delay_timer represents the delay timer before the cooking starts.
variable_delay_timer = ContinuousVariable(value_ranges_steps=[(0, 24, 0.5)], current_value=0, round_over=True)

# variable_keep_warm represents whether the machine is in Keep Warm mode.
variable_keep_warm = DiscreteVariable(value_range=["on", "off"], current_value="off")

# variable_menu_index indicates the selected cooking menu.
variable_menu_index = DiscreteVariable(
    value_range=["White Rice", "Brown Rice", "Quinoa", "Steel Cut Oats"], 
    current_value="White Rice"
)

# variable_menu_setting is a placeholder for the menu-specific variable.
variable_menu_setting = None

# variable_menu_setting_white_rice, variable_menu_setting_brown_rice, etc., represent cooking times for respective menus.
variable_menu_setting_white_rice = ContinuousVariable(value_ranges_steps=[(0, 60, 1)], current_value=0, round_over=True)
variable_menu_setting_brown_rice = ContinuousVariable(value_ranges_steps=[(0, 90, 1)], current_value=0, round_over=True)
variable_menu_setting_quinoa = ContinuousVariable(value_ranges_steps=[(0, 40, 1)], current_value=0, round_over=True)
variable_menu_setting_steel_cut_oats = ContinuousVariable(value_ranges_steps=[(0, 40, 1)], current_value=0, round_over=True)

# The mapping dictionary for menu-specific variables.
menu_setting_dict = {
    "White Rice": variable_menu_setting_white_rice,
    "Brown Rice": variable_menu_setting_brown_rice,
    "Quinoa": variable_menu_setting_quinoa,
    "Steel Cut Oats": variable_menu_setting_steel_cut_oats
}