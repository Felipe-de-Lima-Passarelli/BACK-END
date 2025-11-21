import struct

a, b = map(float ,input().split())

a1 = struct.unpack('f', struct.pack('f', a))[0]
b1 = struct.unpack('f', struct.pack('f', b))[0]

c, d = map(float, input().split())

c1 = struct.unpack('f', struct.pack('f', c))[0]
d1 = struct.unpack('f', struct.pack('f', d))[0]

print('A = {:.6f}, B = {:.6f}'.format(a1, b1))
print('C = {:.6f}, D = {:.6f}'.format(c1, d1))
print('A = {:.1f}, B = {:.1f}'.format(a, b))
print('C = {:.1f}, D = {:.1f}'.format(c, d))
print('A = {:.2f}, B = {:.2f}'.format(a, b))
print('C = {:.2f}, D = {:.2f}'.format(c, d))
print('A = {:.3f}, B = {:.3f}'.format(a, b))
print('C = {:.3f}, D = {:.3f}'.format(c, d))
print('A = {:.3E}, B = {:.3E}'.format(a, b))
print('C = {:.3E}, D = {:.3E}'.format(c, d))
print('A = {:.0f}, B = {:.0f}'.format(a, b))
print('C = {:.0f}, D = {:.0f}'.format(c, d))
