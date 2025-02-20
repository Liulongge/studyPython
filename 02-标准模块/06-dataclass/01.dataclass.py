from dataclasses import dataclass, field
from typing import List, Optional
# 1. typing 基本类型
# 用于表示简单的数据类型。
# 类型	    说明
# int	    整数类型
# float	    浮点数类型
# str	    字符串类型
# bool	    布尔类型
# bytes	    字节类型
# None	    表示空值，通常与 Optional 结合使用

# 2. typing容器类型
# 用于表示容器（如列表、字典、集合等）的类型。
# 类型	                 说明
# List[T]	            列表，元素类型为 T（例如 List[int] 表示整数列表）
# Dict[K, V]	        字典，键类型为 K，值类型为 V（例如 Dict[str, int] 表示键为字符串、值为整数的字典）
# Set[T]	            集合，元素类型为 T（例如 Set[str] 表示字符串集合）
# Tuple[T1, T2, ...]	元组，元素类型分别为 T1, T2, ...（例如 Tuple[int, str] 表示一个整数和一个字符串的元组）
# Sequence[T]	        序列（如列表、元组等），元素类型为 T
# Mapping[K, V]	        映射（如字典），键类型为 K，值类型为 V
# Iterable[T]	        可迭代对象，元素类型为 T

@dataclass
class Address:
    street: str
    city: str
    zip_code: str

@dataclass
class PhoneNumber:
    type: str
    number: str

@dataclass
# List[PhoneNumber] = field(default_factory=list) 的含义是：
# 声明一个类型为 List[PhoneNumber] 的字段。
# 使用 field(default_factory=list) 为该字段设置默认值，确保每次创建对象时都会生成一个新的空列表。
# 避免多个实例共享同一个列表对象，防止意外的副作用。
# 这种方式是 dataclass 中处理可变默认值（如列表、字典等）的推荐做法。
class Person:
    name: str
    age: int
    address: Address
    phone_numbers: List[PhoneNumber] = field(default_factory=list)

@dataclass
class Company:
    name: str
    employees: List[Person] = field(default_factory=list)

# C++ 风格的赋值
def assign_person():
    address = Address(street="123 Main St", city="Anytown", zip_code="12345")
    phone_numbers = [
        PhoneNumber(type="home", number="555-1234"),
        PhoneNumber(type="work", number="555-5678")
    ]
    person = Person(name="John Doe", age=30, address=address, phone_numbers=phone_numbers)
    return person

# C++ 风格的读取
def read_person(person: Person): # ‘: Person’ 是类型注解（Type Annotation），它的作用是显式地指明函数参数 person 的预期类型是 Person 类。
    print(f"Name: {person.name}")
    print(f"Age: {person.age}")
    print(f"Address: {person.address.street}, {person.address.city}, {person.address.zip_code}")
    for phone in person.phone_numbers:
        print(f"{phone.type} Phone: {phone.number}")

# 使用示例
person = assign_person()
read_person(person)