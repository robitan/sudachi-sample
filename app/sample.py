from sudachipy import tokenizer
from sudachipy import dictionary


tokenizer_obj = dictionary.Dictionary().create()


mode = tokenizer.Tokenizer.SplitMode.C
print([m.surface() for m in tokenizer_obj.tokenize("国家公務員", mode)])

mode = tokenizer.Tokenizer.SplitMode.B
print([m.surface() for m in tokenizer_obj.tokenize("国家公務員", mode)])

mode = tokenizer.Tokenizer.SplitMode.A
print([m.surface() for m in tokenizer_obj.tokenize("国家公務員", mode)])


# Morpheme information

m = tokenizer_obj.tokenize("食べ", mode)[0]

print(m.surface())
print(m.dictionary_form())
print(m.reading_form())
print(m.part_of_speech())


# Normalization

print(tokenizer_obj.tokenize("附属", mode)[0].normalized_form())
# => '付属'
print(tokenizer_obj.tokenize("SUMMER", mode)[0].normalized_form())
# => 'サマー'
print(tokenizer_obj.tokenize("シュミレーション", mode)[0].normalized_form())
# => 'シミュレーション'