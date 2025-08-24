import os
# User manual: Press this button to switch power on and off. The washing machine automatically switches off when operations are finished. The washing machine also turns off automatically if it is not operated or no button is pressed for 10 minutes after the power has been turned on.
variable_power_on_off = DiscreteVariable(value_range=["on", "off"], current_value="off")

# User manual: Starts and pauses operation. When the washing machine is paused for over one hour and no operations are done, it turns off automatically.
variable_start_running = DiscreteVariable(value_range=["on", "off"], current_value="off")

# Program selection
variable_program = DiscreteVariable(value_range=["Fuzzy", "Jeans", "Delicate", "Blanket", "Wool", "Speedy", "Economy", "Soak", "Tub Dry"], current_value="Fuzzy")

# Wash time setting
variable_wash_time = DiscreteVariable(value_range=[ "3", "9", "12", "15", "18"], current_value="18")

# Rinse type setting
variable_rinse_type = DiscreteVariable(value_range=["1", "2", "ex&1", "ex&2"], current_value="2")

# Spin time setting
variable_spin_time = DiscreteVariable(value_range=[ "1", "3", "6", "9"], current_value="9")

# Water level setting
variable_water_level = DiscreteVariable(value_range=["20", "27", "35", "45", "55", "60"], current_value="20")

# Delay timer setting
variable_delay_timer = ContinuousVariable(value_ranges_steps=[(0, 3, 3), (3, 12, 1)], current_value=0)

feature_list = {}

feature_list["turn_on_off"] = [
    {"step": 1, "actions": ["press_power_on_off_button"], "variable": "variable_power_on_off"}
]

feature_list["start_pause"] = [
    {"step": 1, "actions": ["press_start_pause_button"], "variable": "variable_start_running"}
]

feature_list["program_selection"] = [
    {"step": 1, "actions": ["press_program_button"], "variable": "variable_program"}
]

feature_list["adjust_wash_time"] = [
    {"step": 1, "actions": ["press_wash_button"], "variable": "variable_wash_time"}
]

feature_list["adjust_rinse_type"] = [
    {"step": 1, "actions": ["press_rinse_button"], "variable": "variable_rinse_type"}
]

feature_list["adjust_spin_time"] = [
    {"step": 1, "actions": ["press_spin_button"], "variable": "variable_spin_time"}
]

feature_list["adjust_water_level"] = [
    {"step": 1, "actions": ["press_water_level_button"], "variable": "variable_water_level"}
]

feature_list["set_delay_timer"] = [
    {"step": 1, "actions": ["press_delay_start_button"], "variable": "variable_delay_timer"}
]

feature_list["null"] = [
    {"step": 1, "actions": ["press_airjet_button"]}
]

simulator_feature = Feature(feature_list=feature_list, current_value=("empty", 1))

class Simulator(Appliance):

    def reset(self):
        self.feature = simulator_feature
        self.variable_power_on_off = variable_power_on_off
        self.variable_start_running = variable_start_running
        self.variable_program = variable_program
        self.variable_wash_time = variable_wash_time
        self.variable_rinse_type = variable_rinse_type
        self.variable_spin_time = variable_spin_time
        self.variable_water_level = variable_water_level
        self.variable_delay_timer = variable_delay_timer
        self.variable_image_map = {
            "variable_power_on_off":{
                "on": "power=on.JPG",
                "off": "power=off.JPG"
            },
            "variable_start_running":{
                "on": "start=on.JPG",
                "off": "start=off.png"
            },
            "variable_program":{
                "Fuzzy": "program=fuzzy.JPG",
                "Jeans": "program=jeans.JPG",
                "Delicate": "program=delicate.JPG",
                "Blanket": "program=blanket.JPG",
                "Wool": "program=wool.JPG",
                "Speedy": "program=speedy.JPG",
                "Economy": "program=economy.JPG",
                "Soak": "program=soak.JPG",
                "Tub Dry": "program=tubdry.JPG"
            },
            "variable_wash_time":{
                "off": "wash=0.png",
                "3": "wash=3.JPG",
                "9": "wash=9.JPG",
                "12": "wash=12.JPG",
                "15": "wash=15.JPG",
                "18": "wash=18.JPG"
            },
            "variable_rinse_type":{
                "off": "rinse=off.png",
                "1": "rinse=1.JPG",
                "2": "rinse=2.JPG",
                "ex&1": "rinse=ex&1.JPG",
                "ex&2": "rinse=ex&2.JPG"
            },
            "variable_spin_time":{
                "0": "spin=0.png",
                "1": "spin=1.JPG",
                "3": "spin=3.JPG",
                "6": "spin=6.JPG",
                "9": "spin=9.JPG"
            },
            "variable_water_level":{
                "20": "waterlevel=20.JPG",
                "27": "waterlevel=27.JPG",
                "35": "waterlevel=35.JPG",
                "45": "waterlevel=45.JPG",
                "55": "waterlevel=55.JPG",
                "60": "waterlevel=60.JPG"
            },
            "variable_delay_timer":{
                "0": "delay=0.png",
                "3": "delay=3.JPG",
                "4": "delay=4.JPG",
                "5": "delay=5.JPG",
                "6": "delay=6.JPG",
                "7": "delay=7.JPG",
                "8": "delay=8.JPG",
                "9": "delay=9.JPG",
                "10": "delay=10.JPG",
                "11": "delay=11.JPG",
                "12": "delay=12.JPG"
            },
        }

    def press_power_on_off_button(self):
        # This action toggles the power state of the washing machine.
        self.feature.update_progress("press_power_on_off_button")
        self.execute_action_and_set_next("press_power_on_off_button")

    def press_start_pause_button(self):
        # This action toggles the start/pause state of the washing machine.
        self.feature.update_progress("press_start_pause_button")
        current_feature = self.feature.current_value[0]
        if current_feature == "start_pause":
            self.variable_start_running.set_current_value("on")

    def press_program_button(self):
        # This action cycles through the available washing programs.
        self.feature.update_progress("press_program_button")
        self.execute_action_and_set_next("press_program_button")

    def press_wash_button(self):
        # This action adjusts the wash time.
        self.feature.update_progress("press_wash_button")
        self.execute_action_and_set_next("press_wash_button")

    def press_rinse_button(self):
        # This action adjusts the rinse type.
        self.feature.update_progress("press_rinse_button")
        self.execute_action_and_set_next("press_rinse_button")

    def press_spin_button(self):
        # This action adjusts the spin time.
        self.feature.update_progress("press_spin_button")
        self.execute_action_and_set_next("press_spin_button")

    def press_water_level_button(self):
        # This action adjusts the water level.
        self.feature.update_progress("press_water_level_button")
        self.execute_action_and_set_next("press_water_level_button")

    def press_delay_start_button(self):
        # This action sets the delay timer for the washing machine.
        self.feature.update_progress("press_delay_start_button")
        self.execute_action_and_set_next("press_delay_start_button")
    
    def update_display(self, variable=None):
        #feedback = {"feature": self.feature.current_value}
        feedback = {}
        def get_image_for(variable_name, value):
            image_name = self.variable_image_map[variable_name][value]
            #image_name = image_dict[value]
            print("image_name: ", image_name)
            #print("image_dict: ", image_dict)
            if image_name != "":
                return os.path.expanduser(f"~/TextToActions/datasetv2/real_world/_3_simulators/_4_simulators_with_states_and_display/_1_washing_machine/feedbacks/{image_name}")
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
