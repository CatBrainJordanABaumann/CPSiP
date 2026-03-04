import hashlib

desired_hash = 'd077f244def8a70e5ea758bd8352fcd8'

base_word = 'ca'

for l1 in base_word:
    for l2 in base_word:
        base_test_word = l1 + l2
        h = hashlib.new('md5', base_test_word.encode('ASCII')).hexdigest()
        print(f'initial hash is {h} for word {base_test_word}')

        for l in 'abcdefghijklmnopqrstuvwxyz':
            test_word = base_test_word + l
            h = hashlib.new('md5', test_word.encode('ASCII')).hexdigest()
            if h == desired_hash:
                print(f'desired hash found is {h} with word {test_word}')
            else:
                print(f'potential hash is {h} for word {test_word}')