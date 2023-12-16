credits = {
    "Pyfuscator": {
        "Credits": {"User319183": "Free | Open Source | MIT License"},
        "features": {
            "random_string_generation": "✅",
            "aes_and_rsa_encryption": "✅",
            "string_encryption": "✅",
            "string_decryption": "✅",
            "code_obfuscation": "✅",
            "name_obfuscation": "✅",
            "function_name_obfuscation": "✅",
            "string_obfuscation": "✅",
            "constant_obfuscation": "✅",
            "call_obfuscation": "✅",
            "Advanced_Obfuscation": {
                "code_flattening": "✅",
                "proprietary_logic_insertion": "✅",
                "safeguard_insertion": "✅",
                "dead_code_insertion": "✅",
                "code_substitution": "✅",
                "dummy_code_insertion": "✅",
                "variable_renaming": "✅",
                "advanced_anti_debugger": {
                    "debugger_attachment_detection": "✅",
                    "debugger_process_detection": "✅",
                    "timing_check": "✅",
                    "code_obfuscation": "✅",
                    "debugger_evasion_techniques": "✅",
                    "stealth_techniques": "✅",
                    "environment_checks": "✅",
                    "anti_memory_dumping": "✅",
                    "anti_tampering": "⏳",
                    "anti_virtual_machine": "⏳",
                },
            },
            "SupremeObfuscation": {
                "opaque_predicates": "✅",
                "encrypted_strings": "✅",
                "control_flow_flattening": "✅",
                "parallel_obfuscation": "✅",
            },
        },
    }
}
char_map = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15,
    "g": 16,
    "h": 17,
    "i": 18,
    "j": 19,
    "k": 20,
    "l": 21,
    "m": 22,
    "n": 23,
    "o": 24,
    "p": 25,
    "q": 26,
    "r": 27,
    "s": 28,
    "t": 29,
    "u": 30,
    "v": 31,
    "w": 32,
    "x": 33,
    "y": 34,
    "z": 35,
    "A": 36,
    "B": 37,
    "C": 38,
    "D": 39,
    "E": 40,
    "F": 41,
    "G": 42,
    "H": 43,
    "I": 44,
    "J": 45,
    "K": 46,
    "L": 47,
    "M": 48,
    "N": 49,
    "O": 50,
    "P": 51,
    "Q": 52,
    "R": 53,
    "S": 54,
    "T": 55,
    "U": 56,
    "V": 57,
    "W": 58,
    "X": 59,
    "Y": 60,
    "Z": 61,
    "!": 62,
    '"': 63,
    "#": 64,
    "$": 65,
    "%": 66,
    "&": 67,
    "'": 68,
    "(": 69,
    ")": 70,
    "*": 71,
    "+": 72,
    ",": 73,
    "-": 74,
    ".": 75,
    "/": 76,
    ":": 77,
    ";": 78,
    "<": 79,
    "=": 80,
    ">": 81,
    "?": 82,
    "@": 83,
    "[": 84,
    "\\": 85,
    "]": 86,
    "^": 87,
    "_": 88,
    "`": 89,
    "{": 90,
    "|": 91,
    "}": 92,
    "~": 93,
    " ": 94,
    "\t": 95,
    "\n": 96,
    "\r": 97,
    "\x0b": 98,
    "\x0c": 99,
}
strings_table = []
random = __import__("random")



def print_name_with_something(
    name,
):
    after_name_list = [
        "is awesome!",
        "rocks!",
        "is the best!",
        "is fantastic!",
        "is incredible!",
    ]
    after_name_choice = random.choice(
        after_name_list
    )
    return f"{name} {after_name_choice}"

base64 = __import__("base64")
ctypes = __import__("ctypes")
os = __import__("os")
sys = __import__("sys")

time = __import__("time")

psutil = __import__("psutil")
debug_tool_detected_str = base64.b64decode(
    b"RGVidWdnaW5nIHRvb2wgZGV0ZWN0ZWQuIFByb2dyYW0gd2lsbCB0ZXJtaW5hdGUu"
).decode()

pyfuscator_str = base64.b64decode(
    b"UHlmdXNjYXRvciAtIEFudGktRGVidWdnZXI="
).decode()

messageboxW = getattr(
    ctypes.windll.user32, base64.b64decode(b"TWVzc2FnZUJveFc=").decode()
)

os_exit = getattr(
    os, base64.b64decode(b"X2V4aXQ=").decode()
)

isdebuggerpresent = getattr(
    ctypes.windll.kernel32, base64.b64decode(b"SXNEZWJ1Z2dlclByZXNlbnQ=").decode()
)

if getattr(sys, base64.b64decode(b"Z2V0dHJhY2U=").decode())() is not None:
    messageboxW(
        0,
        debug_tool_detected_str,
        pyfuscator_str,
        1,
    )
    # if_you_put_a_buck_in_my_cup_i_will_suck_you_off = "Another day, another victory for the OGs"
    os_exit(
        1
    )
# we_suck_poo = "sacrifice loves skidding"

if (
    isdebuggerpresent()
):
    messageboxW(
        0,
        debug_tool_detected_str,
        pyfuscator_str,
        1,
    )
    os_exit(
        1
    )

debugger_name_list = [
    base64.b64decode(b"Z2Ri").decode(),
    base64.b64decode(b"bGxkYg==").decode(),
    base64.b64decode(b"d2luZGJn").decode(),
    base64.b64decode(b"aWRhcQ==").decode(),
    base64.b64decode(b"aWRhcTY0").decode(),
    base64.b64decode(b"eDY0X2RiZw==").decode(),
    base64.b64decode(b"b2xseWRiZw==").decode(),
    base64.b64decode(b"aW1tdW5pdHlkZWJ1Z2dlcg==").decode(),
    base64.b64decode(b"ZWNsaXBzZQ==").decode(),
    base64.b64decode(b"cHlyYWhybQ==").decode(),
    base64.b64decode(b"bmV0YmVhbnM=").decode(),
    base64.b64decode(b"Y29kZWJsb2Nrcw==").decode(),
    base64.b64decode(b"dmlzdWFsbHN0dWRpbyE=").decode(),
    base64.b64decode(b"cmFkYXJlMg==").decode(),
]
process_list = [
    var2.info[
        "name"
    ]
    for var2 in psutil.process_iter(
        attrs=["name"]
    )
]
for debugger_name in debugger_name_list:
    if (
        debugger_name
        in process_list
    ):
        messageboxW(
            0,
            debug_tool_detected_str,
            pyfuscator_str,
            1,
        )
        os_exit(
            1
        )

start_time = (
    time.time()
)
time.sleep(0.001)

end_time = (
    time.time()
)

if (
    end_time
    - start_time
) > 0.005000000000109139:
    messageboxW(
        0,
        debug_tool_detected_str,
        pyfuscator_str,
        1,
    )
    os_exit(
        1
    )

os = __import__("os")
ctypes = __import__("ctypes")

base64 = __import__("base64")

vm_detected_str = base64.b64decode(
    b"VmlydHVhbCBNYWNoaW5lIGRldGVjdGVkLiBQcm9ncmFtIHdpbGwgdGVybWluYXRlLg=="
).decode()

pyfuscator_str = base64.b64decode(
    b"UHlmdXNjYXRvciAtIEFudGktVk0="
).decode()

messageboxW = getattr(
    ctypes.windll.user32, base64.b64decode(b"TWVzc2FnZUJveFc=").decode()
)

os_exit = getattr(
    os, base64.b64decode(b"X2V4aXQ=").decode()
)

# pooron = "User319183 was here!"
vm_name_list = [
    base64.b64decode(b"dm13YXJl").decode(),
    base64.b64decode(b"dmlydHVhbGJveA==").decode(),
]
sysinfo_str = (
    os.popen("systeminfo").read().lower()
)
for sys_info_entry in vm_name_list:
    if (
        sys_info_entry
        in sysinfo_str
    ):
        messageboxW(
            0,
            vm_detected_str,
            pyfuscator_str,
            1,
        )
        os_exit(
            1
        )

def main():
    name = input(
        "What's your name? "
    )
    print_i_suppose = print_name_with_something(
        name
    )
    print(
        print_i_suppose
    )

if __name__ == "__main__":
    main()
