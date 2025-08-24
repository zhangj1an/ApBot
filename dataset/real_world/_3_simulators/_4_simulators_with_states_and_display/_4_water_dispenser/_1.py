import os

# Variable for temperature setting
variable_temperature_setting = DiscreteVariable(value_range=["clean", "60", "85", "98"], current_value="clean")

# Variable for cleaning mode
variable_cleaning_mode = DiscreteVariable(value_range=["off", "on"], current_value="on")

# Variable for unlock status
variable_unlock_status = DiscreteVariable(value_range=["locked", "unlocked"], current_value="locked")
# Variable for reducing chlorine
variable_reduce_chlorine = DiscreteVariable(value_range=["timer", "chlorine", "off"], current_value="off")

# Variable for timer setting
variable_timer_setting = DiscreteVariable(value_range=["off", "on"], current_value="off")

feature_list = {}

feature_list["temperature_setting"] = [
    {"step": 1, "actions": ["press_temp_clean_button"], "variable": "variable_temperature_setting"}
]

#feature_list["cleaning_mode"] = [
#    {"step": 1, "actions": ["press_temp_clean_button"], "variable": "variable_cleaning_mode"}
#]

feature_list["unlock_status"] = [
    {"step": 1, "actions": ["press_unlock_button"], "variable": "variable_unlock_status"}
]

feature_list["reduce_chlorine"] = [
    {"step": 1, "actions": ["press_reboil_timer_button"], "variable": "variable_reduce_chlorine"}
]

#feature_list["timer_setting"] = [
#    {"step": 1, "actions": ["press_reboil_timer_button"], "variable": "variable_timer_setting"}
#]

feature_list["pour_water"] = [
    {"step": 1, "actions": ["press_pump_button"]}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.text= True
        self.variable_temperature_setting = variable_temperature_setting
        self.variable_cleaning_mode = variable_cleaning_mode
        self.variable_unlock_status = variable_unlock_status
        self.variable_reduce_chlorine = variable_reduce_chlorine
        self.variable_timer_setting = variable_timer_setting
        self.variable_image_map = {
            "variable_temperature_setting":{
                "clean": "clean.JPG",
                "60": "temp=60.JPG",
                "85": "temp=85.JPG",
                "98": "temp=98.JPG"
            },
            "variable_cleaning_mode":{
                "off": "temp=98.JPG",
                "on": "clean.JPG"
            },
            "variable_unlock_status":{
                "locked": "temp=98.JPG",
                "unlocked": "unlock=true.JPG"
            },
            "variable_reduce_chlorine":{
                "timer": "timer=on.JPG",
                "chlorine": "reduce_chlorine.JPG",
                "off": "reduce_chlorine.JPG"
            },
            "variable_timer_setting":{
                "off": "reduce_chlorine.JPG",
                "on": "timer=on.JPG"
            }
        }
    # Action: press_temp_clean_button
    def press_temp_clean_button(self, feature_name):
        self.feature.update_progress("press_temp_clean_button")
        self.execute_action_and_set_next("press_temp_clean_button")
        

    # Action: press_unlock_button
    def press_unlock_button(self, feature_name):
        self.feature.update_progress("press_unlock_button")
        self.execute_action_and_set_next("press_unlock_button")

    # Action: press_pump_button
    def press_pump_button(self, feature_name):
        self.feature.update_progress("press_pump_button")
        self.execute_action_and_set_next("press_pump_button")

    # Action: press_reboil_timer_button
    def press_reboil_timer_button(self, feature_name):
        self.feature.update_progress("press_reboil_timer_button")
        self.execute_action_and_set_next("press_reboil_timer_button")
        
    
    def update_display(self, variable=None):
        #feedback = {"feature": self.feature.current_value}
        feedback = {}
        def get_image_for(variable_name, value):
            image_name = self.variable_image_map[variable_name][value]
            #image_name = image_dict[value]
            print("image_name: ", image_name)
            #print("image_dict: ", image_dict)
            if image_name != "":
                return os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_3_simulators/_4_simulators_with_states_and_display/_4_water_dispenser/feedbacks/{image_name}")
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
                    
                    if image_file != "" and self.text==False:
                        feedback[special_var] = (1, image_file, f"{special_var}={value}")
                    else:
                        feedback[special_var] = (0, f"{special_var}={value}")

        self.display = feedback