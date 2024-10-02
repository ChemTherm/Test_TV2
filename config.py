config = {
    "Verdampfer": { 
        "type": "ExtOutput",
        "output_device": "TiX",
        "output_channel": 1,
        "unit": "ml/min",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 940,
    },
    
    "p_1": { 
        "type": "pressure",
        "input_device": "23UK",
        "input_channel": 0,
        "unit": "mbar",
        "gradient": 0.4,
        "y-axis":   0,
        "x": 370,
        "y": 540,
    },
    
    "p_2": { 
        "type": "pressure",
        "input_device": "23UK",
        "input_channel": 1,
        "unit": "mbar",
        "gradient":1,
        "y-axis":   0,
        "x": 955,
        "y": 890,
    },
    
    "p_3": { 
        "type": "pressure",
        "input_device": "TiX",
        "input_channel": 0,
        "unit": "mbar",
        "gradient":1,
        "y-axis":   0,
        "x": 955,
        "y": 890,
    },
    
       
    "T_1": { 
        "type": "thermocouple",
        "tc_type": "K",
        "input_device": "WPP",
        "input_channel": 0,
        "unit": "°1C",
        "x": 890,
        "y": 690,
    },
    
    "T_2": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WQ3",
        "input_channel": 0,
        "unit": "°2",
        "x": 130,
        "y": 450,
    },
    
    "T_3": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "WjR",
        "input_channel": 0,
        "unit": "°3",
        "x": 610,
        "y": 320,
    } ,
    
    "T_4": { 
        "type": "thermocouple",
        "tc_type": "N",
        "input_device": "Wj2",
        "input_channel": 0,
        "unit": "°4",
        "x": 770,
        "y": 270,
    }      
}
