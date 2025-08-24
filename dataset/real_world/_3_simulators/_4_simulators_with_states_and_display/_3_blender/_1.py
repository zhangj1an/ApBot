import os

# Variable for speed setting
variable_speed_setting = DiscreteVariable(value_range=["slow", "turbo"], current_value="slow")

feature_list = {}

feature_list["speed_setting"] = [
    {"step": 1, "actions": ["press_and_hold_a1_button", "press_and_hold_a2_turbo_button"], "variable": "variable_speed_setting"}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_speed_setting = variable_speed_setting
        self.variable_image_map = {
            "variable_speed_setting":{
                "slow": "state.JPG",
                "turbo": "state.JPG"
            },
            }

    def press_and_hold_a1_button(self, feature_name="", duration=1):
        # This action sets the speed setting to "slow" if held for any duration
        self.feature.current_value = ("speed_setting", self.feature.current_value[1])
        self.feature.update_progress("press_and_hold_a1_button")
        if duration >= 1:
            self.variable_speed_setting.set_current_value("slow")

    def press_and_hold_a2_turbo_button(self, feature_name="", duration=1):
        # This action sets the speed setting to "turbo" if held for any duration
        self.feature.current_value = ("speed_setting", self.feature.current_value[1])
        self.feature.update_progress("press_and_hold_a2_turbo_button")
        if duration >= 1:
            self.variable_speed_setting.set_current_value("turbo")
    
    def update_display(self, variable=None):
        #feedback = {"feature": self.feature.current_value}
        feedback = {}
        def get_image_for(variable_name, value):
            image_name = self.variable_image_map[variable_name][value]
            #image_name = image_dict[value]
            print("image_name: ", image_name)
            #print("image_dict: ", image_dict)
            if image_name != "":
                return os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_3_simulators/_4_simulators_with_states_and_display/_3_blender/feedbacks/{image_name}")
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