import tensorflow as tf

import dataset_reader  # pylint: disable=g-bad-import-order, g-import-not-at-top

# Task config
tf.flags.DEFINE_string(
    'task_dataset_info', 
    'square_room',
    'Name of the room in which the experiment is performed.'
)

tf.flags.DEFINE_string(
    'task_root', 
    None,
    'Dataset path.'
)

# Require flags
tf.flags.mark_flag_as_required('task_root')
tf.flags.mark_flag_as_required('saver_results_directory')
FLAGS = tf.flags.FLAGS

print( f'FLAGS: {FLAGS}' )

def train():

    """Training loop."""

    tf.reset_default_graph()

    # Create the motion models for training and evaluation
    data_reader = dataset_reader.DataReader( 
        FLAGS.task_dataset_info, 
        root=FLAGS.task_root, 
        num_threads=4
    )

def main(unused_argv):

    tf.logging.set_verbosity(3)  # Print INFO log messages.
    train()

if __name__ == '__main__':
    tf.app.run()