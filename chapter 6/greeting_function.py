
def greeting_function(**kargs):
    for k,v in kargs.items():
        print(f'{k+'님 안녕하세요' if {v} == 'korean' else  'hello ' + k }')

greeting_function(이영희 = 'korean',김철수 = 'korean',박민수 = 'korean',john_doe = 'english')

    