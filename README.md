# vdateutils

This is my datetime utils, share with everyone needed.

### install

```
git clone https://github.com/luffy51k/vdateutils.git
cd vdateutils/
python setup.py install
```

### example

```python
from vdateutils import format_timestamp_to_str_time, date_add_from_now, date_sub_from_now, date_add, compare_2date,\
    sub_2date


print(date_add_from_now('Asia/Ho_Chi_Minh', 7))
print(date_sub_from_now('Asia/Ho_Chi_Minh', 7))
print(format_timestamp_to_str_time())

date_in = '2020-07-03 09:49:28'
print(date_add(date_in, 7))

d1 = '2020-07-03 09:49:28'
d2 = '2020-08-03 09:49:28'

print(compare_2date(d1, d2))
print(str(sub_2date(d1, d2)))
```
