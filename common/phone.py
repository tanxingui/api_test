from faker import Faker
def get_random_phone():
 phone = Faker("zh_CN").phone_number()
 return phone
