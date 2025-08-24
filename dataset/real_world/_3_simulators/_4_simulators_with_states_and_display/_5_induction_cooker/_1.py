import os

# Variable for power on/off
# User manual: Press the Power button to power on the induction cooker. It will display “On” on the LED panel.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for cooking function
variable_cooking_function = DiscreteVariable(
    value_range=["Water", "Soup", "Rice", "Milk", "BBQ", "Hot pot", "Fry", "S.Fry" ],
    current_value="Hot pot"
)

# Variable for power/temperature setting
variable_power_temperature_setting = None

# Variables for power/temperature setting in different modes
variable_power_temperature_setting_bbq = ContinuousVariable(
    value_ranges_steps=[(60, 240, 20)],
    current_value=60
)
variable_power_temperature_setting_hotpot = ContinuousVariable(
    value_ranges_steps=[(200, 2000, 200)],
    current_value=1400
)
variable_power_temperature_setting_s_fry = ContinuousVariable(
    value_ranges_steps=[(200, 2000, 200)],
    current_value=1400
)
variable_power_temperature_setting_fry = ContinuousVariable(
    value_ranges_steps=[(60, 240, 20)],
    current_value=60
)

# The mapping dictionary for power/temperature setting
power_temperature_setting_dict = {
    "BBQ": variable_power_temperature_setting_bbq,
    "Hot pot": variable_power_temperature_setting_hotpot,
    "S.Fry": variable_power_temperature_setting_s_fry,
    "Fry": variable_power_temperature_setting_fry
}

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_button"], "variable": "variable_power_on_off"}
]

feature_list["cooking_function"] = [
    {"step": 1, "actions": ["press_function_button"], "variable": "variable_cooking_function"}
]

feature_list["adjust_power_temperature_hotpot"] = [
    {"step": 1, "actions": ["press_power_temperature_up_button", "press_power_temperature_down_button"], "variable": "variable_power_temperature_setting_hotpot"}
]

"""
feature_list["adjust_power_temperature_bbq"] = [
    {"step": 1, "actions": ["press_power_temperature_up_button", "press_power_temperature_down_button"], "variable": "variable_power_temperature_setting_bbq"}
]

feature_list["adjust_power_temperature_s_fry"] = [
    {"step": 1, "actions": ["press_power_temperature_up_button", "press_power_temperature_down_button"], "variable": "variable_power_temperature_setting_s_fry"}
]

feature_list["adjust_power_temperature_fry"] = [
    {"step": 1, "actions": ["press_power_temperature_up_button", "press_power_temperature_down_button"], "variable": "variable_power_temperature_setting_fry"}
]
"""

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.text = False
        self.variable_power_on_off = variable_power_on_off
        self.variable_cooking_function = variable_cooking_function
        self.variable_power_temperature_setting_bbq = variable_power_temperature_setting_bbq
        self.variable_power_temperature_setting_hotpot = variable_power_temperature_setting_hotpot
        self.variable_power_temperature_setting_s_fry = variable_power_temperature_setting_s_fry
        self.variable_power_temperature_setting_fry = variable_power_temperature_setting_fry
        self.power_temperature_setting_dict = power_temperature_setting_dict
        self.variable_image_map = {
            "variable_power_on_off":{
                "on": "power=on.JPG",
                "off": "power=off.JPG"
            },
            "variable_cooking_function":{
                "Hot pot": "hotpot_1400.JPG",
                "Fry": "fry.JPG",
                "S.Fry": "stir_fry.JPG",
                "BBQ": "bbq.JPG",
                "Soup": "soup.JPG",
                "Rice": "rice.JPG",
                "Milk": "milk.JPG",
                "Water": "water.JPG"
            },
            "variable_power_temperature_setting_hotpot":{
                "200": "hotpot_200.JPG",
                "400": "hotpot_400.JPG",
                "600": "hotpot_600.JPG",
                "800": "hotpot_800.JPG",
                "1000": "hotpot_1000.JPG",
                "1200": "hotpot_1200.JPG",
                "1400": "hotpot_1400.JPG",
                "1600": "hotpot_1600.JPG",
                "1800": "hotpot_1800.JPG",
                "2000": "hotpot_2000.JPG"
            },
        }

    def press_power_button(self, feature_name="turn_on_off"):
        self.feature.update_progress("press_power_button")
        # Toggle power on/off
        if self.variable_power_on_off.get_current_value() == "off":
            self.variable_power_on_off.set_current_value("on")
        else:
            self.variable_power_on_off.set_current_value("off")

    def press_function_button(self, feature_name="select_cooking_function"):
        self.feature.update_progress("press_function_button")
        # Change cooking function
        self.execute_action_and_set_next("press_function_button")
        # Update the power/temperature setting variable based on the selected cooking function
        current_function = self.variable_cooking_function.get_current_value()
        if current_function in self.power_temperature_setting_dict:
            self.variable_power_temperature_setting = self.power_temperature_setting_dict[current_function]

    def press_power_temperature_up_button(self, feature_name):
        self.feature.update_progress("press_power_temperature_up_button")
        # Adjust power/temperature setting upwards
        self.execute_action_and_set_next("press_power_temperature_up_button")

    def press_power_temperature_down_button(self, feature_name):
        # Set the feature and update progress
        self.feature.update_progress("press_power_temperature_down_button")
        # Adjust power/temperature setting downwards
        self.execute_action_and_set_prev("press_power_temperature_down_button")
    
    def update_display(self, variable=None):
        #feedback = {"feature": self.feature.current_value}
        feedback = {}
        def get_image_for(variable_name, value):
            image_name = self.variable_image_map[variable_name][value]
            #image_name = image_dict[value]
            print("image_name: ", image_name)
            #print("image_dict: ", image_dict)
            if image_name != "" and self.text == False:
                return os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_3_simulators/_4_simulators_with_states_and_display/_5_induction_cooker/feedbacks/{image_name}")
            else:
                return ""

        if variable is not None:
            variable_name = self.find_attribute_name(variable)#.replace("variable_", "")
            value = variable.current_value
            value = str(value)
            print("image_file test2: ", variable_name, value)
            image_file = get_image_for(variable_name, value)
            
            if image_file != "" and self.text == False:
                feedback[variable_name] = (1, image_file)
            else:
                feedback[variable_name] = (0, f"{variable_name}={value}")
        else:
            appliance_state = self.get_state()
            current_feature_name, current_feature_step = self.feature.current_value
            print("current_feature_name: ", current_feature_name)
            print("current_feature_step: ", current_feature_step)

            for offset in [-1, 0, 1]:
                detail = self.feature.get_feature_step_detail(current_feature_name, current_feature_step + offset)
                if detail and "variable" in detail:
                    var_name = detail["variable"]
                    value = self.get_variable_by_name(var_name).current_value
                    value=str(value)
                    print("image_file test1: ", var_name, value)
                    image_file = get_image_for(var_name, value)
                    
                    if image_file != "" and self.text == False:
                        feedback[var_name] = (1, image_file)
                    else:
                        feedback[var_name] = (0, f"{var_name}={value}")
                

        if len(feedback) == 1:  # feature only
            for special_var in ["power", "on_off"]:
                special_variable = self.get_variable_by_name(f"variable_{special_var}")
                if special_variable is not None:
                    value = special_variable.get_current_value()
                    print("image_file test3: ", special_var, value)
                    image_file = get_image_for(special_var, value)
                    
                    if image_file != "" and self.text == False:
                        feedback[special_var] = (1, image_file)
                    else:
                        feedback[special_var] = (0, f"{special_var}={value}")

        self.display = feedback