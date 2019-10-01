import uuid
import random


for idx in range(1000):
    uid = uuid.uuid4()
    eudaimonia = random.randint(0, 999999999)
    print('<tr>\n<td>{}</td>\n<td>{}</td>\n<td><button class="button">!PLACE BID!</button></td>\n</tr>'.format(uid, eudaimonia))
