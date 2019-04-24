#!/usr/bin/python3
# coding: utf-8

# /home/gswyhq/data/people-2014

# 字向量来源： https://github.com/Embedding/Chinese-Word-Vectors
# https://pan.baidu.com/s/1c9yiosHKNIZwRlLzD_F1ig
WORD_EMBDDING_FILE_PATH = '/home/gswyhq/data/word-vectors/sgns.target.word-character.char1-1.dynwin5.thr10.neg5.dim300.iter5'

import json
import os

def load_embdding():
    INDEX_WORDS = []
    _index = 0
    with open(WORD_EMBDDING_FILE_PATH)as f:
        line = f.readline()

        while line:
            _index += 1
            line = f.readline()
            if not line or not line.strip():
                break
            word, embddings = line.split(maxsplit=1)
            INDEX_WORDS.append(word)
            if _index % 5000 == 0:
                print(_index)
        print("总词数", len(INDEX_WORDS))
    save_word_index_file = './word_index.json'
    print('文件保存在：{}'.format(os.path.abspath(save_word_index_file)))
    with open(save_word_index_file, 'w')as f:
        json.dump(INDEX_WORDS, f, ensure_ascii=False)

def main():
    load_embdding()


if __name__ == '__main__':
    main()