from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

import tensorflow as tf

import input_pipeline


class InputPipeLineTest(tf.test.TestCase):

    # def _record(self, label, red, green, blue):
    #     image_size = 32 * 32
    #     record = bytes(bytearray([label] + [red] * image_size +
    #                              [green] * image_size + [blue] * image_size))
    #     expected = [[[red, green, blue]] * 32] * 32
    #     return record, expected

    def testInput(self):
        pass  # TODO
        
        # labels = [1, 1, 0]
        # inputs = []
        # records = [self._record(labels[0], 0, 128, 255),
        #            self._record(labels[1], 255, 0, 1),
        #            self._record(labels[2], 254, 255, 0)]
        # contents = b"".join([record for record, _ in records])
        # expected = [expected for _, expected in records]
        # filename = os.path.join(self.get_temp_dir(), "cifar")
        # open(filename, "wb").write(contents)

        # with self.test_session() as sess:
        #     q = tf.FIFOQueue(99, [tf.string], shapes=())
        #     q.enqueue([filename]).run()
        #     q.close().run()
        #     result = input_pipeline.read_and_decode(q)

        # for i in range(3):
        #     key, label, uint8image = sess.run([
        #         result.key, result.label, result.uint8image])
        #     self.assertEqual("%s:%d" % (filename, i), tf.compat.as_text(key))
        #     self.assertEqual(labels[i], label)
        #     self.assertAllEqual(expected[i], uint8image)

        # with self.assertRaises(tf.errors.OutOfRangeError):
        #     sess.run([result.key, result.uint8image])


if __name__ == "__main__":
    tf.test.main()
