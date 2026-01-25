# File for 2.3 2.4 2.5

PERSONAL_ID = "sc22bm2"
target_id = "sc22bm2" 

def change_target(new_target):
    """
    Updates the global target_id to switch who we are messaging.
    Ref: Task 2.5 Step 1 [cite: 288]
    """
    global target_id
    target_id = new_target
    print(f"--> Target Switched: Now talking to {target_id}")

def create_message(input_string):
    """
    Takes a string and wraps it into a dictionary protocol with IDs.
    Ref: Task 2.4 Step 1 [cite: 209]
    """
    message = {
        'msg': input_string,
        'sender_id': PERSONAL_ID,
        'receiver_id': target_id
    }
    return str(message)

def validate_message(message_dict):
    """
    Checks if a dictionary has all the required protocol keys.
    Ref: Task 2.4 Step 2 [cite: 215]
    """
    expected_keys = ['msg', 'sender_id', 'receiver_id']
    
    for key in expected_keys:
        if key not in message_dict:
            return False 
    return True 

if __name__ == "__main__":
    print("--- Testing Protocol Logic ---")
    
    print(f"Current Target: {target_id}")
    packet = create_message("Hello World")
    print(f"Generated Packet: {packet}")
    
    print("\nValidating Packet...")
    received_dict = eval(packet) 
    if validate_message(received_dict):
        print("✅ Message is Valid")
    else:
        print("❌ Message Invalid")

    print("\nTesting Target Switch...")
    change_target("TEACHER_PC")
    packet2 = create_message("New Message")
    print(f"New Packet: {packet2}")
