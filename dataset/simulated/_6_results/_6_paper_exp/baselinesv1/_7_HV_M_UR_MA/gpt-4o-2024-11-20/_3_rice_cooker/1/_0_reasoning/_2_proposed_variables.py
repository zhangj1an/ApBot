# variable_start_running: starts the appliance by pressing the "Start" button
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off") 

# variable_cooking_mode: represents the cooking mode (menu) selected with the "Menu" button
variable_cooking_mode = DiscreteVariable(
    value_range=[
        "Glutinous rice", 
        "Porridge", 
        "Bean", 
        "Soup", 
        "Steam", 
        "Reheat"
    ],
    current_value="Glutinous rice"
)

# variable_cooking_time_hr: represents the hour setting for cooking time adjustment
variable_cooking_time_hr = ContinuousVariable(value_ranges_steps=[[0, 59, 1]], current_value=0)

# variable_cooking_time_min: represents the minute setting for cooking time adjustment
variable_cooking_time_min = ContinuousVariable(value_ranges_steps=[[0, 59, 1]], current_value=0)

# variable_preset_time_hr: sets the preset hour for delayed cooking using the "Preset timer" button
variable_preset_time_hr = ContinuousVariable(value_ranges_steps=[[0, 23, 1]], current_value=0)

# variable_preset_time_min: sets the preset minutes for delayed cooking using the "Preset timer" button
variable_preset_time_min = ContinuousVariable(value_ranges_steps=[[0, 59, 1]], current_value=0)

# variable_keep_warm_cancel: represents the appliance state for keeping warm or cancelling the operation
variable_keep_warm_cancel = DiscreteVariable(value_range=["keep_warm", "cancel"], current_value="keep_warm")

# variable_rice_type: selects between the white and brown rice cooking functions
variable_rice_type = DiscreteVariable(value_range=["white", "brown"], current_value="white")