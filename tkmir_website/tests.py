from django.test import TestCase
from datetime import datetime

t1 = '2022-04-14 16:25:17.980921+00:00'
t2 = '2022-04-14 16:18:24.935272+00:00'

print(datetime.strftime(t1, '%Y-%m-%d %H:%M:%S.%f%z'))
# Create your tests here.
