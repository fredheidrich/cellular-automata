"""Test the Dataset class"""

import tensorflow as tf
import numpy as np
from pprint import pprint
import os
import random

# from src.models.dataset import create_datasets
from data.random_walker import create_grids, check_repeats
from data.random_walker import draw_grid

from data.make_dataset import Saver


class DatasetTests(tf.test.TestCase):

    def testBlobs(self):

        path = '~/Developer/machine-learning/cellular-automata/data/blobs_10_8x8.h5'
        saver = Saver(path)
        a,b = saver.load_hdf5()
        print (a[random.randint(0, len(a))])
        print (b[random.randint(0, len(b))])
        # print (a, b)

    # def testSliceData(self):

    #     h = 8
    #     w = 4
    #     n = 5
    #     grids, _, _ = create_grids(h, w, n, 0.5)
    #     grid = grids[0]
    #     draw_grid(grid)
    #     print ("0,0: %d" % grid[0,0])
    #     print ("3,0: %d" % grid[3,0])
    #     print ("0,3: %d" % grid[0,3])
    #     print ("top: ", grids[0, 0, :])

    # def testRepeatingGrids(self):

        # should repeat
        # path = tf.test.get_temp_dir() + "/dset.h5"
        # h = 8
        # w = 8
        # n = 10000
        # grids, _, _ = create_grids(h, w, n, 0.5)
        # check_repeats(grids)


if __name__ == "__main__":
    tf.test.main()
