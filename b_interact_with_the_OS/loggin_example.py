#!/usr/bin/env python3
import logging
import sys
import os
import pprint
from functools import partial, partialmethod

logging.TRACE = 15
logging.addLevelName(logging.TRACE, 'TRACE')
logging.Logger.trace = partialmethod(logging.Logger.log, logging.TRACE)
logging.trace = partial(logging.log, logging.TRACE)

logging.MLLLOGLEVEL = 25
logging.addLevelName(logging.MLLLOGLEVEL, 'MLLLOGLEVEL')
logging.Logger.mllloglevel = partialmethod(logging.Logger.log, logging.MLLLOGLEVEL)
logging.mllloglevel = partial(logging.log, logging.MLLLOGLEVEL)

src_dir = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(
    filename=os.path.join(src_dir, 'loggin_example.log'),
    format=
    # '%(levelname)-8s: %(asctime)s: %(process)d: %(message)s',
    '%(levelname)-8s: %(asctime)s: %(process)d: %(filename)s: %(funcName)s: %(message)s',
    # -8 means alignt up to 8 spaces to the left
    level=logging.CRITICAL,
)
# create a logger to add logging to terminal at the same time
logger1 = logging.getLogger()
logger1.addHandler(logging.StreamHandler(sys.stdout))

# levels = [10, 15, 20, 30, 40, 50]
# levels.sort(reverse=True)
# levels = sorted([10, 15, 20, 25, 30, 40, 50], reverse=False)

levelsWithName = [
    l for l in range(101) if not logging.getLevelName(l).startswith('Level')
]
print(levelsWithName)

levelsDict1 = {}
for l in levelsWithName:
    levelsDict1[l] = logging.getLevelName(l)
print(levelsDict1)
pprint.pprint(levelsDict1)
for l in levelsWithName:
    print(l)
    logger1.setLevel(l)
    logging.critical(f'\tcritical')
    logging.error(f'\terror')
    logging.warning(f'\twarning')
    logging.mllloglevel(f'\tmllloglevel')
    logging.info(f'\tinfo')
    logging.trace(f'\ttrace')
    logging.debug(f'\tdebug')
    #break
print('end loop')
