import ctypes
from ctypes import wintypes
import os

GENERIC_READ = 0x80000000
FILE_SHARE_READ = 0x00000001
FILE_SHARE_WRITE = 0x00000002
FILE_SHARE_DELETE = 0x00000004
OPEN_EXISTING = 3
FILE_ATTRIBUTE_NORMAL = 0x80
INVALID_HANDLE_VALUE = -1

kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

CreateFileW = kernel32.CreateFileW
CreateFileW.argtypes = [
    wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
    ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE
]
CreateFileW.restype = wintypes.HANDLE

ReadFile = kernel32.ReadFile
ReadFile.argtypes = [
    wintypes.HANDLE, wintypes.LPVOID, wintypes.DWORD,
    ctypes.POINTER(wintypes.DWORD), ctypes.c_void_p
]
ReadFile.restype = wintypes.BOOL

CloseHandle = kernel32.CloseHandle
CloseHandle.argtypes = [wintypes.HANDLE]
CloseHandle.restype = wintypes.BOOL

def copy_locked_file(src, dst):
    h_file = CreateFileW(
        src,
        GENERIC_READ,
        FILE_SHARE_READ | FILE_SHARE_WRITE | FILE_SHARE_DELETE,
        None,
        OPEN_EXISTING,
        FILE_ATTRIBUTE_NORMAL,
        None
    )
    if h_file == INVALID_HANDLE_VALUE:
        err = ctypes.get_last_error()
        raise OSError(f"CreateFile failed with error {err}")
    
    try:
        buffer_size = 64 * 1024
        buf = ctypes.create_string_buffer(buffer_size)
        bytes_read = wintypes.DWORD()
        with open(dst, 'wb') as out_f:
            while True:
                success = ReadFile(h_file, buf, buffer_size, ctypes.byref(bytes_read), None)
                if not success or bytes_read.value == 0:
                    break
                out_f.write(buf.raw[:bytes_read.value])
        print(f"Successfully copied locked file {src} -> {dst} ({os.path.getsize(dst)} bytes)")
    finally:
        CloseHandle(h_file)

src_cookies = r'C:\Users\Innotech\AppData\Local\Google\Chrome\User Data\Default\Network\Cookies'
dst_cookies = r'd:\Nhung\RIDI\trans-assistant\scratch\chrome_profile\Default\Network\Cookies'
copy_locked_file(src_cookies, dst_cookies)
