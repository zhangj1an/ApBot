# The following variables are based on the product's user manual and available control panel elements:

# Variable for selecting menu items (1 to 12).
variable_menu_index = DiscreteVariable(
    value_range=[
        "Basic", 
        "French", 
        "Whole Wheat", 
        "Sweet", 
        "Express 680g", 
        "Express 900g", 
        "Yeast Free", 
        "Continental", 
        "Dough", 
        "Gluten Free", 
        "Jam", 
        "Bake"
    ], 
    current_value="Basic"
)

# Variable for crust color (Light, Medium, Dark, Rapid where applicable)
variable_crust_colour = DiscreteVariable(
    value_range=["Light", "Medium", "Dark", "Rapid"],
    current_value="Light"
)

# Variable for loaf size (450g, 680g, 900g).
# This can only be adjusted for certain menus as mentioned in the user manual.
variable_loaf_size = DiscreteVariable(
    value_range=["450g", "680g", "900g"],
    current_value="450g"
)

# Variable for gluten free setting, directly accessible by Gluten Free button.
# User manual: Press the GLUTEN FREE button on the control panel. GLUTEN FREE will display on the screen.
# Can also be selected by pressing MENU until GLUTEN FREE setting 10 is displayed on the screen.
variable_gluten_free_mode = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for timer adjustment.
# User manual: The time displayed represents the finishing time. Timer can only be adjusted on AUTO MENU selections 1-4.
variable_timer_setting = ContinuousVariable(
    value_ranges_steps=[(0, 15 * 60, 600)],  # Timer adjustment is in 10-minute increments, up to 15 hours.
    current_value=0  # Default initial value.
)

# Variable for start or cancel button.
# User manual: Press START/CANCEL when selections are complete to begin the program.
variable_start_running = DiscreteVariable(
    value_range=["on", "off"],
    current_value="off"
)