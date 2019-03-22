from enum import Enum
from enum import IntEnum,unique
#加了之后则不可以相同
@unique
class VIP(IntEnum):
    YELLOW=1
    GREEN=12
    BLACK=3
    RED=4
class VIP1(Enum):
    YELLOW=1
    GREEN=1
    BLACK=3
    RED=4
class Common():
    YELLOW=1

# print(type(VIP.YELLOW))
# print(type(VIP.GREEN.name))
# print(VIP['YELLOW'])

#枚举类型 枚举的值 枚举的名字
# VIP.YELLOW=6 
# for v in VIP:
#      print(v)
# for v in VIP.__members__.items():
#      print(v)
# for v in VIP.__members__:
#      print(v)
# result=VIP.GREEN>VIP.YELLOW
# result1=VIP.GREEN is VIP1.GREEN
# print(result1)

# print(VIP.GREEN)

# a=1
# print(VIP(a))

print(VIP.YELLOW)