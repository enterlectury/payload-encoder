# Payload Encoder and Obfuscation Framework
# This project is for studying how payloads can be encoded
# and obfuscated to test evasion against basic signature detection.
# Made for educational purpose only - lab environment

import base64
import codecs
import random
import string
import re
import datetime


# -----------------------------------------------
# ENCODING FUNCTIONS
# -----------------------------------------------

# base64 encoding - converts payload to base64 string
def encode_base64(payload):
    result = base64.b64encode(payload.encode()).decode()
    return result

# base64 decoding
def decode_base64(encoded_text):
    result = base64.b64decode(encoded_text.encode()).decode()
    return result


# XOR encoding - each character is XORed with the key
def encode_xor(payload, key=42):
    xor_result = ""
    for char in payload:
        xor_result += chr(ord(char) ^ key)
    # converting to hex so output is readable
    hex_output = xor_result.encode().hex()
    return hex_output

# XOR decoding - same key reverses it
def decode_xor(hex_payload, key=42):
    raw_bytes = bytes.fromhex(hex_payload).decode(errors="replace")
    original = ""
    for char in raw_bytes:
        original += chr(ord(char) ^ key)
    return original


# ROT13 - simple letter substitution cipher (shifts by 13)
def encode_rot13(payload):
    return codecs.encode(payload, "rot_13")

# ROT13 decode - applying rot13 again gives back original
def decode_rot13(encoded_text):
    return codecs.decode(encoded_text, "rot_13")


# -----------------------------------------------
# OBFUSCATION FUNCTIONS
# -----------------------------------------------

# reverse the whole payload string
def reverse_payload(payload):
    return payload[::-1]

def reverse_back(payload):
    return payload[::-1]


# convert every character to its ASCII number separated by -
def char_split(payload):
    parts = []
    for ch in payload:
        parts.append(str(ord(ch)))
    return "-".join(parts)

def char_split_decode(obfuscated):
    numbers = obfuscated.split("-")
    original = ""
    for n in numbers:
        original += chr(int(n))
    return original


# convert each character to hex escape like \x70
def hex_escape(payload):
    result = ""
    for ch in payload:
        result += "\\x{:02x}".format(ord(ch))
    return result

def hex_escape_decode(obfuscated):
    hex_string = obfuscated.replace("\\x", "")
    return bytes.fromhex(hex_string).decode()


# insert random junk characters every few chars using | as marker
def insert_junk(payload, every=4):
    output = ""
    for i, ch in enumerate(payload):
        output += ch
        if (i + 1) % every == 0:
            junk_char = random.choice(string.ascii_lowercase)
            output += "|" + junk_char + "|"
    return output

def remove_junk(obfuscated):
    # remove anything between | | markers
    return re.sub(r"\|.\|", "", obfuscated)


# -----------------------------------------------
# DETECTION / EVASION TESTING
# -----------------------------------------------

# this is a simulated signature list - like a basic AV or IDS would use
KNOWN_SIGNATURES = [
    "cmd.exe",
    "/bin/sh",
    "exec(",
    "eval(",
    "powershell",
    "wget ",
    "curl ",
    "nc -e",
    "ncat",
    "shellcode",
    "msfvenom",
    "payload",
    "reverse_shell",
    "bind_shell",
    "os.system",
    "subprocess",
    "Invoke-Expression"
]

def check_detection(payload, name="test"):
    found_sigs = []
    for sig in KNOWN_SIGNATURES:
        if sig.lower() in payload.lower():
            found_sigs.append(sig)

    is_detected = len(found_sigs) > 0

    return {
        "name": name,
        "detected": is_detected,
        "result": "DETECTED" if is_detected else "BYPASSED",
        "matched": found_sigs,
        "preview": payload[:80]
    }


# -----------------------------------------------
# REPORT GENERATOR
# -----------------------------------------------

def make_report(all_results, original):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_lines = []
    report_lines.append("=" * 60)
    report_lines.append("  PAYLOAD OBFUSCATION FRAMEWORK - EVASION REPORT")
    report_lines.append("  Date: " + now)
    report_lines.append("=" * 60)
    report_lines.append("")
    report_lines.append("Original Payload:")
    report_lines.append("  " + original)
    report_lines.append("")

    total = len(all_results)
    detected = sum(1 for r in all_results if r["detected"])
    bypassed = total - detected
    bypass_rate = (bypassed / total) * 100

    report_lines.append("Summary:")
    report_lines.append("  Total tested  : " + str(total))
    report_lines.append("  Detected      : " + str(detected))
    report_lines.append("  Bypassed      : " + str(bypassed))
    report_lines.append("  Bypass Rate   : " + str(round(bypass_rate, 1)) + "%")
    report_lines.append("")
    report_lines.append("-" * 60)

    for r in all_results:
        report_lines.append("")
        report_lines.append("  Method  : " + r["name"])
        report_lines.append("  Result  : " + r["result"])
        report_lines.append("  Preview : " + r["preview"])
        if r["matched"]:
            report_lines.append("  Matched : " + ", ".join(r["matched"]))

    report_lines.append("")
    report_lines.append("=" * 60)
    report_lines.append("  END OF REPORT")
    report_lines.append("=" * 60)

    return "\n".join(report_lines)


# -----------------------------------------------
# MAIN - runs all steps
# -----------------------------------------------

def main():
    print("=" * 60)
    print("  Custom Payload Encoder & Obfuscation Framework")
    print("=" * 60)
    print()

    # Step 1 - define the test payload
    original = "powershell -nop -c exec(payload); /bin/sh reverse_shell"
    print("[Step 1] Original Payload:")
    print("  " + original)
    print()

    # Step 2 - apply encodings
    print("[Step 2] Encoding the payload...")
    print()

    b64 = encode_base64(original)
    print("  Base64 encoded:")
    print("  " + b64)
    print()

    xor_out = encode_xor(original, key=42)
    print("  XOR encoded (key=42, shown as hex):")
    print("  " + xor_out[:60] + "...")
    print()

    rot_out = encode_rot13(original)
    print("  ROT13 encoded:")
    print("  " + rot_out)
    print()

    # Step 3 - apply obfuscations
    print("[Step 3] Applying obfuscation techniques...")
    print()

    rev = reverse_payload(original)
    print("  Reversed string:")
    print("  " + rev)
    print()

    split_out = char_split(original)
    print("  ASCII char split (first 60 chars):")
    print("  " + split_out[:60] + "...")
    print()

    esc_out = hex_escape(original)
    print("  Hex escape sequence (first 60 chars):")
    print("  " + esc_out[:60] + "...")
    print()

    junk_out = insert_junk(original, every=4)
    print("  Random junk inserted:")
    print("  " + junk_out[:60] + "...")
    print()

    # Step 4 - run evasion tests on each variant
    print("[Step 4] Running evasion tests against signature list...")
    print()

    test_cases = [
        ("Original Payload",       original),
        ("Base64 Encoded",         b64),
        ("XOR Encoded",            xor_out),
        ("ROT13 Encoded",          rot_out),
        ("Reversed String",        rev),
        ("ASCII Char Split",       split_out),
        ("Hex Escape Sequence",    esc_out),
        ("Random Junk Inserted",   junk_out),
    ]

    results = []
    for label, variant in test_cases:
        res = check_detection(variant, name=label)
        results.append(res)
        status = "[DETECTED]" if res["detected"] else "[BYPASSED]"
        print("  " + status + " " + label)

    print()

    # Step 5 - generate and save report
    print("[Step 5] Generating report...")
    print()

    report = make_report(results, original)
    print(report)

    with open("evasion_report.txt", "w") as f:
        f.write(report)

    print()
    print("[Done] Report saved to evasion_report.txt")
    print()

    # quick decode verification
    print("[Verification] Checking decoding works correctly:")
    print("  Base64 decoded : " + decode_base64(b64)[:50])
    print("  XOR decoded    : " + decode_xor(xor_out, 42)[:50])
    print("  ROT13 decoded  : " + decode_rot13(rot_out)[:50])
    print("  Reversed back  : " + reverse_back(rev)[:50])
    print("  Char split back: " + char_split_decode(split_out)[:50])
    print("  Junk removed   : " + remove_junk(junk_out)[:50])
    print()


if __name__ == "__main__":
    main()
