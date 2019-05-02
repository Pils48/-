"""
����� �������, ������ ���������� Ti, ������� � i = 2, �������� �� ����������������� ���������� ���������� Ti - 2 � Ti - 1. ��� ���������������� ���������� ���������� ����� ���� �������� ��������� �����, 
��� ��� ����� ����� ��� ������������ �������������� �� �����.
� ������ ������� �������������� ������ ����������: ��������, ��� ���������� ������ ��������� ����� ������ ��� ���������� ���������� ���, 
����� ��� ���� S, ������������� ��� ������� � ����� �� �������� ����, ���� ����������� ����� K ���.
����������� ���������� � ��� � ��������: ���� ��������� �������� ����� A � B, ��� ���� S, 
������������� � ����� ��� ����� �� ���, � ����� ����� K, ���������� ����� N � ���������� ����� ���������� TN, � ������� ����� S ����������� ����� K ���.
"""
def contain(s = str, c = str):
    sep = ""
    idx = 0
    while ord(s[idx]) > 32 and ord(s[idx]) < 127 and idx < len(s) - 1:
        idx+=1
    else: sep = s[idx]
    cnt = 0
    s = s.lower()
    c = c.lower()
    words = list(s.split(sep))
    for word in words:
        if (word == c):
            cnt+=1
    return cnt



def write_to_file(c):
    f = open('output.txt', 'w')
    f.write(c)
    f.close()

f = open('input.txt', 'r')
fc = f.read().split("\n")
f.close()

res = ""
a = b = q = 0
a+=contain(fc[0], fc[2])
b+=contain(fc[1], fc[2])

pr2 = a
pr1 = b
it = 1
while q < int(fc[3]):
    it+=1
    q = pr2 + pr1
    pr2 = pr1
    pr1 = q
if q == int(fc[3]):
    res = str(it)
    write_to_file(res)
else:
    res = "Impossible"
    write_to_file(res)
