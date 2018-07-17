from keras.models import Model
from keras.layers import Dense, Embedding, Conv1D, multiply, GlobalMaxPool1D, Input, Reshape, Activation

def Malconv(max_len=200000, win_size=500, vocab_size=257):
    
    inp = Input((max_len,))
    emb = Embedding(vocab_size, 8)(inp)
    
    conv1 = Conv1D(kernel_size = (win_size), filters = 128, strides=(win_size), padding='same')(emb)
    conv2 = Conv1D(kernel_size = (win_size), filters = 128, strides=(win_size), padding='same')(emb)
    a = Activation('sigmoid')(conv2)
    
    mul = multiply([conv1, a])
    p = GlobalMaxPool1D()(mul)
    d = Dense(64)(p)
    out = Dense(1, activation='sigmoid')(d)

    return Model(inp, out)