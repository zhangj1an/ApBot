[
    {
        "id": 1,
        "command": "Cook rice with the name 'rice' mode and start running. Start running: 'on', Cooking mode: 'rice', Preset time: '00:00:00'",
        "target_state": {
            "variable_cooking_mode": "rice",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "on"
        },
        "important_target_states": {
            "variable_cooking_mode": "rice",
            "variable_start_running": "on"
        }
    },
    {
        "id": 2,
        "command": "Cook brown rice and start running. Start running: 'on', Cooking mode: 'brown_rice', Preset time: '00:00:00'",
        "target_state": {
            "variable_cooking_mode": "brown_rice",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "on"
        },
        "important_target_states": {
            "variable_cooking_mode": "brown_rice",
            "variable_start_running": "on"
        }
    },
    {
        "id": 3,
        "command": "Make porridge for breakfast with a 30-minute preset and start running. Start running: 'on', Cooking mode: 'porridge', Preset time: '00:00:30'",
        "target_state": {
            "variable_cooking_mode": "porridge",
            "variable_preset_time": "00:00:30",
            "variable_start_running": "on"
        },
        "important_target_states": {
            "variable_cooking_mode": "porridge",
            "variable_start_running": "on"
        }
    },
    {
        "id": 4,
        "command": "Prepare yogurt and start running. The command does not specify a preset time, so it defaults to '00:00:00'. The cooking mode 'yogurt' is not directly accessible through a button press.",
        "target_state": {
            "variable_cooking_mode": "rice",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "off"
        },
        "important_target_states": {
            "variable_start_running": "off"
        }
    },
    {
        "id": 5,
        "command": "Braise meat for dinner in 1 hour and start running. Start running: 'on', Cooking mode: 'braise', Preset time: '00:01:00'",
        "target_state": {
            "variable_cooking_mode": "rice",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "off"
        },
        "important_target_states": {
            "variable_start_running": "off"
        }
    },
    {
        "id": 6,
        "command": "Make a cake for this evening’s treat and start running. Start running: 'on', Cooking mode: 'cake', Preset time: '00:00:00'",
        "target_state": {
            "variable_cooking_mode": "rice",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "off"
        },
        "important_target_states": {
            "variable_start_running": "off"
        }
    },
    {
        "id": 7,
        "command": "Steaming vegetables for a healthy lunch and start running. Start running: 'on', Cooking mode: 'steam', Preset time: '00:00:00'",
        "target_state": {
            "variable_cooking_mode": "rice",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "off"
        },
        "important_target_states": {
            "variable_start_running": "off"
        }
    },
    {
        "id": 8,
        "command": "Slow-cook soup for the family dinner and start running. Start running: 'on', Cooking mode: 'soup', Preset time: '00:00:00'",
        "target_state": {
            "variable_cooking_mode": "rice",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "off"
        },
        "important_target_states": {
            "variable_start_running": "off"
        }
    },
    {
        "id": 9,
        "command": "Set to multi-grain rice for a nutritious meal and start running. Start running: 'on', Cooking mode: 'multi-grain_rice', Preset time: '00:00:00'",
        "target_state": {
            "variable_cooking_mode": "rice",
            "variable_preset_time": "00:00:00",
            "variable_start_running": "off"
        },
        "important_target_states": {
            "variable_start_running": "off"
        }
    }
]