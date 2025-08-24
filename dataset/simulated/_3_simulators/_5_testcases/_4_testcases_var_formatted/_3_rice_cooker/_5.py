[
    {
        "command": "Please turn on the rice cooker and set it to cook jasmine rice for a total time of 4 hours using the preset option. Then start the machine.",
        "id": 1,
        "important_target_states": {
            "variable_cooking_program": "jasmine_rice",
            "variable_preset_time": "04:00:00",
            "variable_start_running": "on"
        },
        "optimal_step_size": 26,
        "target_state": {
            "variable_cooking_program": "jasmine_rice",
            "variable_keep_warm": "off",
            "variable_preset_time": "04:00:00",
            "variable_start_running": "on",
            "variable_timer": "00:00:00"
        }
    },
    {
        "command": "Set the rice cooker to slow cook stew mode for 3 hours using the variable_timer. Then start the machine.",
        "id": 2,
        "important_target_states": {
            "variable_cooking_program": "slow_cook_stew",
            "variable_start_running": "on",
            "variable_timer": "03:00:00"
        },
        "optimal_step_size": 21,
        "target_state": {
            "variable_cooking_program": "slow_cook_stew",
            "variable_keep_warm": "off",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "on",
            "variable_timer": "03:00:00"
        }
    },
    {
        "command": "Turn on the cooker and set it to brown rice mode for a preset time of 5 hours. Then start the machine.",
        "id": 3,
        "important_target_states": {
            "variable_cooking_program": "brown_rice",
            "variable_preset_time": "05:00:00",
            "variable_start_running": "on"
        },
        "optimal_step_size": 33,
        "target_state": {
            "variable_cooking_program": "brown_rice",
            "variable_keep_warm": "off",
            "variable_preset_time": "05:00:00",
            "variable_start_running": "on",
            "variable_timer": "00:00:00"
        }
    },
    {
        "command": "Please turn on and set the rice cooker to cook congee for 2 hours. Then start the machine.",
        "id": 4,
        "important_target_states": {
            "variable_cooking_program": "soup_congee",
            "variable_start_running": "on",
            "variable_timer": "02:00:00"
        },
        "optimal_step_size": 15,
        "target_state": {
            "variable_cooking_program": "soup_congee",
            "variable_keep_warm": "off",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "on",
            "variable_timer": "02:00:00"
        }
    },
    {
        "command": "Set the rice cooker in glutinous rice mode with a preset time of 6 hours. Then start the machine.",
        "id": 5,
        "important_target_states": {
            "variable_cooking_program": "glutinous_rice",
            "variable_preset_time": "06:00:00",
            "variable_start_running": "on"
        },
        "optimal_step_size": 39,
        "target_state": {
            "variable_cooking_program": "glutinous_rice",
            "variable_keep_warm": "off",
            "variable_preset_time": "06:00:00",
            "variable_start_running": "on",
            "variable_timer": "00:00:00"
        }
    },
    {
        "command": "Please cook jasmine rice with a preset time of 7 hours. Remember to start the machine.",
        "id": 6,
        "important_target_states": {
            "variable_cooking_program": "jasmine_rice",
            "variable_preset_time": "07:00:00",
            "variable_start_running": "on"
        },
        "optimal_step_size": 44,
        "target_state": {
            "variable_cooking_program": "jasmine_rice",
            "variable_keep_warm": "off",
            "variable_preset_time": "07:00:00",
            "variable_start_running": "on",
            "variable_timer": "00:00:00"
        }
    },
    {
        "command": "Set the cooker for white rice preparation with a preset finishing time in 8 hours. Then start the machine.",
        "id": 7,
        "important_target_states": {
            "variable_cooking_program": "white_rice",
            "variable_preset_time": "08:00:00",
            "variable_start_running": "on"
        },
        "optimal_step_size": 51,
        "target_state": {
            "variable_cooking_program": "white_rice",
            "variable_keep_warm": "off",
            "variable_preset_time": "08:00:00",
            "variable_start_running": "on",
            "variable_timer": "00:00:00"
        }
    },
    {
        "command": "Turn on and cook brown rice with a preset finish time in 9 hours. Then start the machine.",
        "id": 8,
        "important_target_states": {
            "variable_cooking_program": "brown_rice",
            "variable_preset_time": "09:00:00",
            "variable_start_running": "on"
        },
        "optimal_step_size": 57,
        "target_state": {
            "variable_cooking_program": "brown_rice",
            "variable_keep_warm": "off",
            "variable_preset_time": "09:00:00",
            "variable_start_running": "on",
            "variable_timer": "00:00:00"
        }
    },
    {
        "command": "Turn on the rice cooker in quick cooking steam mode with variable_timer set to 20 minutes. Then start the machine.",
        "id": 9,
        "important_target_states": {
            "variable_cooking_program": "quick_cooking_steam",
            "variable_start_running": "on",
            "variable_timer": "00:20:00"
        },
        "optimal_step_size": 5,
        "target_state": {
            "variable_cooking_program": "quick_cooking_steam",
            "variable_keep_warm": "off",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "on",
            "variable_timer": "00:20:00"
        }
    },
    {
        "command": "Turn on the rice cooker and set to congee mode with a variable_timer set for 1.5 hours. Then start the machine.",
        "id": 10,
        "important_target_states": {
            "variable_cooking_program": "soup_congee",
            "variable_start_running": "on",
            "variable_timer": "01:30:00"
        },
        "optimal_step_size": 12,
        "target_state": {
            "variable_cooking_program": "soup_congee",
            "variable_keep_warm": "off",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "on",
            "variable_timer": "01:30:00"
        }
    }
]
