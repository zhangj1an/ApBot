import os

# Variable for start running
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Variable for cooking mode
variable_cooking_mode = DiscreteVariable(
    value_range=[
        "rice", 
        "brown_rice", 
        "porridge", 
        "multi-grain_porridge", 
        "multi-grain_rice", 
        "reheat", 
        "braise", 
        "yogurt", 
        "cake", 
        "steam", 
        "soup"
    ], 
    current_value="rice"
)

# Variable for preset time
variable_preset_time = TimeVariable(
    value_ranges_steps=[("00:00:00", "12:00:00", 30)], 
    current_value="00:00:00"
)

feature_list = {}

feature_list["start_function"] = [
    {"step": 1, "actions": ["press_start_button"], "variable": "variable_start_running"}
]

feature_list["cooking_mode_selection"] = [
    {"step": 1, "actions": ["press_rice_button", "press_brown_rice_button", "press_porridge_button", "press_func_select_button"], "variable": "variable_cooking_mode"}
]

feature_list["preset_time"] = [
    {"step": 1, "actions": ["press_preset_button"], "variable": "variable_preset_time"} # requires parsing from variable_input_string
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_start_running = variable_start_running
        self.variable_cooking_mode = variable_cooking_mode
        self.variable_preset_time = variable_preset_time
        self.variable_image_map = {
            "variable_start_running":{
                "on": "start=on.JPG",
                "off": "start=off.JPG"
            },
            "variable_cooking_mode":{
                "rice": "func=rice.JPG",
                "brown_rice": "func=brown_rice.jpeg",
                "porridge": "func=porridge.JPG",
                "multi-grain_porridge": "func=multi_grain_porridge.JPG",
                "multi-grain_rice": "func=multi_grain_rice.JPG",
                "reheat": "func=reheat.JPG",
                "braise": "func=braise.JPG",
                "yogurt": "func=yogurt.JPG",
                "cake": "func=cake.JPG",
                "steam": "func=steam.JPG",
                "soup": "func=soup.JPG"
            },
            "variable_preset_time":{
                "00:00:00": "preset=0000.png",
                "00:00:30": "preset=0030.JPG",
                "00:01:00": "preset=0100.JPG",
                "00:01:30": "preset=0130.JPG",
                "00:02:00": "preset=0200.JPG",
                "00:02:30": "preset=0230.JPG",
                "00:03:00": "preset=0300.JPG",
                "00:03:30": "preset=0330.JPG",
                "00:04:00": "preset=0400.JPG",
                "00:04:30": "preset=0430.JPG",
                "00:05:00": "preset=0500.JPG",
                "00:05:30": "preset=0530.JPG",
                "00:06:00": "preset=0600.JPG",
                "00:06:30": "preset=0630.JPG",
                "00:07:00": "preset=0700.JPG",
                "00:07:30": "preset=0730.JPG",
                "00:08:00": "preset=0800.JPG",
                "00:08:30": "preset=0830.JPG",
                "00:09:00": "preset=0900.JPG",
                "00:09:30": "preset=0930.JPG",
                "00:10:00": "preset=1000.JPG",
                "00:10:30": "preset=1030.JPG",
                "00:11:00": "preset=1100.JPG",
                "00:11:30": "preset=1130.JPG",
                "00:12:00": "preset=1200.JPG"
            }
        }

    def press_start_button(self):
        # This action sets the variable_start_running to "on" in the start_function feature
        self.feature.update_progress("press_start_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_function":
            self.variable_start_running.set_current_value("on")

    def press_rice_button(self):
        # This action changes the cooking mode to "rice" in the cooking_mode_selection feature
        self.feature.update_progress("press_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_mode_selection":
            self.variable_cooking_mode.set_current_value("rice")

    def press_brown_rice_button(self):
        # This action changes the cooking mode to "brown_rice" in the cooking_mode_selection feature
        self.feature.update_progress("press_brown_rice_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_mode_selection":
            self.variable_cooking_mode.set_current_value("brown_rice")

    def press_porridge_button(self):
        # This action changes the cooking mode to "porridge" in the cooking_mode_selection feature
        self.feature.update_progress("press_porridge_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_mode_selection":
            self.variable_cooking_mode.set_current_value("porridge")

    def press_func_select_button(self):
        # This action cycles through the cooking modes in the cooking_mode_selection feature
        self.feature.update_progress("press_func_select_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "cooking_mode_selection":
            self.execute_action_and_set_next("press_func_select_button")

    def press_preset_button(self):
        # This action allows setting the preset time in the preset_time feature
        self.feature.update_progress("press_preset_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "preset_time":
            self.execute_action_and_set_next("press_preset_button")
    
    def update_display(self, variable=None):
        #feedback = {"feature": self.feature.current_value}
        feedback = {}
        def get_image_for(variable_name, value):
            image_name = self.variable_image_map[variable_name][value]
            #image_name = image_dict[value]
            print("image_name: ", image_name)
            #print("image_dict: ", image_dict)
            if image_name != "":
                return os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_3_simulators/_4_simulators_with_states_and_display/_2_rice_cooker/feedbacks/{image_name}")
            else:
                return ""

        if variable is not None:
            variable_name = self.find_attribute_name(variable)#.replace("variable_", "")
            value = variable.current_value
            value = str(value)
            print("image_file test2: ", variable_name, value)
            image_file = get_image_for(variable_name, value)
            
            if image_file != "":
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
                    
                    if image_file != "":
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
                    
                    if image_file != "":
                        feedback[special_var] = (1, image_file)
                    else:
                        feedback[special_var] = (0, f"{special_var}={value}")

        self.display = feedback