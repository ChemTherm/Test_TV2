import sys
import os
import logging
from time import sleep
import traceback

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from TinkerForgeHelperLib.tinkerforge_lib import TFH
from TKinter_HelperLib.tkinter_lib import TKH  # Importiere die TKH-Klasse aus deinem tkinter_lib-Modul

from utilities.regler import *

# Setup logging for the script
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("PIL").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

def initialize_tfh():
    try:
        return TFH("localhost", 4223, debug_mode=1)
    except Exception as e:
        logger.error(f"Failed to initialize TFH: {e}")
        sys.exit(1)

def initialize_gui(tfh_obj):
    try:
        tk_obj = TKH(tfh_obj)  # Übergabe von tfh_obj beim Erstellen der Instanz
        return tk_obj
    except Exception as e:
        error_message = traceback.format_exc()
        logger.error(f"Failed to initialize GUI: {error_message}")
        sys.exit(1)

def main():
    
    # Initialize TFH object
    tfh_obj = initialize_tfh()

    # Initialize GUI
    tk_obj = initialize_gui( tfh_obj)

    try:
        # Start the main loop
        tk_obj.start_loop()  
        tk_obj.window.mainloop()
    except Exception as e:
        logger.error(f"An error occurred during the main loop: {e}")
    finally:
        # Ensure resources are cleaned up
        logger.info("Shutting down...")
        tfh_obj.cleanup()
        logger.info("Resources cleaned up. Bye bye!")

if __name__ == "__main__":
    main()