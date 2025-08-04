#===============這些是LINE提供的功能套組，先用import叫出來=============
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
#===============LINEAPI=============================================



import torch
import pickle
from Q_A.core import to_bert_ids, use_model


def predict_message(str_1):
    
    # load and init
    pkl_file = open('Q_A/bert_part/data_features.pkl', 'rb')
    data_features = pickle.load(pkl_file)
    answer_dic = data_features['answer_dic']
        
    # BERT
    model_setting = {
        "model_name":"bert", 
        "config_file_path":"Q_A/bert_part/config.json", 
        "model_file_path":"Q_A/bert_part/pytorch_model.bin", 
        "vocab_file_path":"Q_A/bert_part/bert-base-chinese-vocab.txt",
        "num_labels":149  # 分幾類 
    }    
    
    model, tokenizer = use_model(**model_setting)
    model.eval()

   
    bert_ids = to_bert_ids(tokenizer,str_1)
    assert len(bert_ids) <= 512
    input_ids = torch.LongTensor(bert_ids).unsqueeze(0)

    # predict
    outputs = model(input_ids)
    predicts = outputs[:2]
    predicts = predicts[0]
    max_val = torch.max(predicts)
    label = (predicts == max_val).nonzero().numpy()[0][1]
    ans_label = answer_dic.to_text(label)
    
    return ans_label

# print(predict_message('淡江大學通識課'))

# import os
# if os.path.isfile('Q_A/bert_part/config.json'):
#   print("檔案存在。")
# else:
#   print("檔案不存在。")