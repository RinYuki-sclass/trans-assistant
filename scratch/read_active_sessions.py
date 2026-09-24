import ctypes
from ctypes import wintypes
import os
import re

GENERIC_READ = 0x80000000
FILE_SHARE_READ = 0x00000001
FILE_SHARE_WRITE = 0x00000002
FILE_SHARE_DELETE = 0x00000004
OPEN_EXISTING = 3
FILE_ATTRIBUTE_NORMAL = 0x80
INVALID_HANDLE_VALUE = -1

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

def read_locked(path):
    h = kernel32.CreateFileW(
        path,
        GENERIC_READ,
        FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE,
        None,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        None
    )
    if h == INVALID_HANDLE_VALUE:
        print(f"Failed to open {path}, error: {ctypes.get_last_error()}")
        return b""
    try:
        size = os.path.getsize(path)
        buf = ctypes.create_string_buffer(size)
        read = wintypes.DWORD()
        success = kernel32.ReadFile(h, buf, size, ctypes.byref(read), None)
        if success:
            return buf.raw[:read.value]
        else:
            print("ReadFile failed:", ctypes.get_last_error())
            return b""
    finally:
        kernel32.CloseHandle(h)

p = r'C:\Users\Innotech\AppData\Local\Google\Chrome\User Data\Default\Sessions'
for fname in os.listdir(p):
    fpath = os.path.join(p, fname)
    data = read_locked(fpath)
    if data:
        print(f"=== {fname} ({len(data)} bytes) ===")
        matches = re.findall(rb'https?://[^\x00-\x1f\x7f-\xff]*novelupdates[^\x00-\x1f\x7f-\xff]*', data)
        seen = set()
        for m in matches:
            s = m.decode('utf-8', errors='ignore')
            if s not in seen:
                seen.add(s)
                print("  ", s)
