"""Hyper-Parameters and Configuration"""

import sys

from absl import flags

# ---------- Pre-Processing ----------

# Paths
flags.DEFINE_string("data_path", "", "")
flags.DEFINE_string("train_path", "", "")
flags.DEFINE_string("val_path", "", "")
flags.DEFINE_string("test_path", "", "")
flags.DEFINE_string("meta_path", "", "")
flags.DEFINE_string("output_dir", "", "")
flags.DEFINE_string("stats_path", "", "")
flags.DEFINE_bool("atis", False, "")
flags.DEFINE_bool("slots", False, "")
flags.DEFINE_integer("batch_size", 32, "")
flags.DEFINE_integer("per_intent", 0, "")
flags.DEFINE_integer("epochs", 1, "")

# newly added for prediction in eval_mod.py
flags.DEFINE_string("input_sentence", "", "")
flags.DEFINE_string("input_path", "", "")

params = flags.FLAGS
params(sys.argv)
