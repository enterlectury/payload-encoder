# Custom Payload Encoder & Obfuscation Framework

**UnifiedMentor Cybersecurity Internship Project**  
Intern ID: `UMID14102561484` | Duration: Nov 2025 – Present (6 Months)  
Course: Cybersecurity Internship

---

## What is this?

This is a Python tool I built as part of my cybersecurity internship at UnifiedMentor. The idea is simple — take a payload (like a shell command), apply different encoding and obfuscation techniques to it, and then test if a simulated antivirus/IDS scanner can still detect it.

It helped me understand how real attackers modify payloads to evade detection, and how defenders can build better detection rules to catch those techniques.

---

## How to run

Make sure Python 3 is installed, then just run:

```bash
python3 payload_encoder.py
```

That's it. The script runs all steps automatically and saves the report.

---

## What it does — step by step

**Step 1** — Load the original test payload  
**Step 2** — Apply encoding (Base64, XOR with key=42, ROT13)  
**Step 3** — Apply obfuscation (reverse string, ASCII char split, hex escape, random junk insertion)  
**Step 4** — Run evasion test against a list of 17 known signatures  
**Step 5** — Generate and save report as `evasion_report.txt`

---

## Modules

### Encoding Module
- `encode_base64()` / `decode_base64()` — converts payload to/from base64
- `encode_xor(key=42)` / `decode_xor()` — XOR cipher, output shown as hex
- `encode_rot13()` / `decode_rot13()` — ROT13 substitution cipher

### Obfuscation Module
- `reverse_payload()` — flips string backwards
- `char_split()` — converts each char to its ASCII number joined by `-`
- `hex_escape()` — converts each char to `\xNN` hex escape format
- `insert_junk()` — inserts random chars between `|` markers every 4 chars

### Evasion Testing
- `check_detection()` — checks payload against 17 known signature strings
- Returns: detected / bypassed + list of matched signatures

### Reporting Engine
- `make_report()` — builds a text report with all results + bypass rate
- Saves output to `evasion_report.txt`

---

## Results

| Method               | Result   |
|----------------------|----------|
| Original Payload     | DETECTED |
| Base64 Encoded       | BYPASSED |
| XOR Encoded          | BYPASSED |
| ROT13 Encoded        | BYPASSED |
| Reversed String      | BYPASSED |
| ASCII Char Split     | BYPASSED |
| Hex Escape Sequence  | BYPASSED |
| Random Junk Inserted | BYPASSED |

**Bypass Rate: 87.5% — 7 out of 8 variants bypassed the scanner**

---

## Files in this repo

```
payload-encoder/
├── payload_encoder.py        # main script
├── evasion_report.txt        # auto-generated after running
├── README.md                 # this file
├── payload-encoder.pptx      # presentation
├── payload-encoder.pdf       # presentation as PDF
├── images/
│   ├── step1_original.png    # screenshot - original payload
│   ├── step2_encoding.png    # screenshot - encoding output
│   ├── step3_obfuscation.png # screenshot - obfuscation output
│   ├── step4_evasion.png     # screenshot - evasion test results
│   └── step5_report.png      # screenshot - full report output
├── offer_letter.pdf          # UnifiedMentor internship offer letter
└── poc_video.mp4             # proof of concept demo video
```

---
## Demonstraion video
<video src="https://github.com/user-attachments/assets/c0f6b632-f08b-4bbb-b09f-ee5400d06486" width="50%" controls>
</video>

## Libraries used

All standard Python libraries — no external installs needed:

- `base64` — Base64 encoding
- `codecs` — ROT13 cipher
- `random`, `string` — junk character generation
- `re` — regex to remove junk markers
- `datetime` — report timestamp

---

## What I learned

- How payloads are modified to evade signature-based detection
- Why static scanners alone aren't enough — they only match exact strings
- Difference between encoding (reversible format change) and encryption (needs a key)
- How red teams use these techniques in offensive workflows
- How blue teams can write better YARA rules and detection logic

---

## Repo

**https://github.com/enterlectury/payload-encoder/**

---

## Disclaimer

This project is for **educational purposes only** and was built in a **lab environment**. No real malware or malicious code was used or created. All detection testing is against a simulated signature database written by me for learning purposes.

Built during my cybersecurity internship at **UnifiedMentor**.  
Contact: rank1aditya@gmail.com
