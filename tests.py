import platform
import sys
from guppy import hpy
import ctypes

h = hpy()
a = 'Python-Demo-String'
b = 0xbbbb
c = 0xcccc

def hex_dump_memory(ptr, num):
    s = ''
    n = 0
    lines = []
    data = list((num * ctypes.c_byte).from_address(ptr))

    if len(data) == 0:
        return '<empty>'

    for i in range(0, num, 16):
        line = ''
        line += '%04x | ' % (i)
        n += 16

        for j in range(n - 16, n):
            if j >= len(data): break
            line += '%02x ' % abs(data[j])

        line += ' ' * (3 * 16 + 7 - len(line)) + ' | '

        for j in range(n - 16, n):
            if j >= len(data): break
            c = data[j] if not (data[j] < 0x20 or data[j] > 0x7e) else '.'
            line += '%c' % c

        lines.append(line)
    return '\n'.join(lines)


print(platform.python_implementation())
print(sys.version_info)
print(h.heap().byrcs)

print(hex(id(a)), hex(id(b)), hex(id(c)))

# addr = int('0x' + open('/proc/self/maps', 'r').readlines()[0].split('-')[0], 16)
addr = id(a)
print('Hex dump from 0x%016x' % addr)

print(hex_dump_memory(addr, 256))