import pendulum
from datetime import datetime

pst = pendulum.timezone('America/Los_Angeles')
ist = pendulum.timezone('Asia/Seoul')

print('LA = ', datetime.now(pst))
print('Seoul = ', datetime.now(ist))
