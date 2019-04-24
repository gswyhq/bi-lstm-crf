
root@d5b66b9f5ffa:/bi-lstm-crf$ 7z e people-2014.7z
~$ bzip2 -kd sgns.target.word-character.char1-1.dynwin5.thr10.neg5.dim300.iter5.bz2 

gswyhq@gswyhq-pc:~/github_projects/bi-lstm-crf$ python3 tools/ner_data_preprocess.py people-2014/train 2014_processed -c True -s True

gswyhq@gswyhq-pc:~/github_projects/bi-lstm-crf$ python3 tools/make_dicts.py 2014_processed -s src_dict.json -t tgt_dict.json
Using TensorFlow backend.

gswyhq@gswyhq-pc:~/github_projects/bi-lstm-crf$ python3 tools/convert_to_h5.py 2014_processed 2014_processed.h5 -s src_dict.json -t tgt_dict.json
Using TensorFlow backend.
