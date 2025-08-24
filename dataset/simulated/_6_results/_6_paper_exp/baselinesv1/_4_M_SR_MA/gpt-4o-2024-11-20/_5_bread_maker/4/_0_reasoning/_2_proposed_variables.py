# Variable - menu index
variable_menu_index = DiscreteVariable(
    value_range=[
        "Basic", "French", "Whole Wheat", "Sweet", 
        "Express 680g", "Express 900g", "Yeast Free", 
        "Continental", "Dough", "Gluten Free", "Jam", "Bake"
    ],
    current_value="Basic"
)

# Variable - menu setting 
variable_menu_setting = None

# Variables for menu-specific settings 
variable_menu_setting_basic = TimeVariable(
    value_ranges_steps=[("00:00:00", "23:59:59", 60)],
    current_value="03:25:00"
)
variable_menu_setting_french = TimeVariable(
    value_ranges_steps=[("00:00:00", "23:59:59", 60)],
    current_value="03:40:00"
)
variable_menu_setting_whole_wheat = TimeVariable(
    value_ranges_steps=[("00:00:00", "23:59:59", 60)],
    current_value="03:55:00"
)
variable_menu_setting_sweet = TimeVariable(
    value_ranges_steps=[("00:00:00", "23:59:59", 60)],
    current_value="03:27:00"
)
variable_menu_setting_express_680g = TimeVariable(
    value_ranges_steps=[("01:20:00", "01:20:00", 0)],
    current_value="01:20:00"
)
variable_menu_setting_express_900g = TimeVariable(
    value_ranges_steps=[("01:55:00", "01:55:00", 0)],
    current_value="01:55:00"
)
variable_menu_setting_yeast_free = TimeVariable(
    value_ranges_steps=[("01:50:00", "01:50:00", 0)],
    current_value="01:50:00"
)
variable_menu_setting_continental = TimeVariable(
    value_ranges_steps=[("00:00:00", "23:59:59", 60)],
    current_value="03:25:00"
)
variable_menu_setting_dough = TimeVariable(
    value_ranges_steps=[("01:30:00", "01:30:00", 0)],
    current_value="01:30:00"
)
variable_menu_setting_gluten_free = TimeVariable(
    value_ranges_steps=[("02:45:00", "02:45:00", 0)],
    current_value="02:45:00"
)
variable_menu_setting_jam = TimeVariable(
    value_ranges_steps=[("01:05:00", "01:05:00", 0)],
    current_value="01:05:00"
)
variable_menu_setting_bake = TimeVariable(
    value_ranges_steps=[("00:05:00", "01:30:00", 300)],
    current_value="01:00:00"
)

# Mapping dictionary connecting menu index and settings
menu_setting_dict = {
    "Basic": variable_menu_setting_basic,
    "French": variable_menu_setting_french,
    "Whole Wheat": variable_menu_setting_whole_wheat,
    "Sweet": variable_menu_setting_sweet,
    "Express 680g": variable_menu_setting_express_680g,
    "Express 900g": variable_menu_setting_express_900g,
    "Yeast Free": variable_menu_setting_yeast_free,
    "Continental": variable_menu_setting_continental,
    "Dough": variable_menu_setting_dough,
    "Gluten Free": variable_menu_setting_gluten_free,
    "Jam": variable_menu_setting_jam,
    "Bake": variable_menu_setting_bake
}

# Each time an action is made to adjust menu, variable_menu_setting will have a different initiation from the dictionary.

# Variable - crust color
variable_crust_color = DiscreteVariable(
    value_range=["Light", "Medium", "Dark", "Rapid"],
    current_value="Light"
)

# Variable - loaf size
variable_loaf_size = DiscreteVariable(
    value_range=["450g", "680g", "900g"],
    current_value="450g"
)

# Variable - timer (only for Basic, French, Whole Wheat, Sweet, and Continental menus)
variable_timer = TimeVariable(
    value_ranges_steps=[("00:00:00", "15:00:00", 600)],
    current_value="00:00:00"
)

# Variable - gluten free (direct selection mode)
variable_gluten_free_mode = DiscreteVariable(
    value_range=["on", "off"],
    current_value="off"
)

# Variable - start running
variable_start_running = DiscreteVariable(
    value_range=["on", "off"],
    current_value="off"
)