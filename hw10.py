import os
import pickle


filename = 'score.bin'


if os.path.exists(filename) :
    print('[파일 읽기]\n\n[점수 출력]')
    with open(filename, 'rb') as file :
        result = pickle.load(file)
        average = pickle.load(file)
    print(f'개인점수: {result}')
    print(f'평균: {average:0.1f}')
    
else :
    def input_scores() :
        print('[점수 입력]')
        lst = []
        n = 0
        while True :
            n += 1
            score = int(input(f'#{n}? '))
            if score < 0 :
                print()
                return lst
            lst.append(score)
    
    def get_average(lst) :
        total = 0
        for i in lst :
            total += i
        return total / len(lst) 
    
    def show_scores(lst) :
        result = ''
        for i in lst :
            result += f'{i} '
        
        print('[점수 출력]')
        print('개인점수: ', result)
        return result

    scores = input_scores()
    result = show_scores(scores)
    average = get_average(scores)
    print(f'평균: {average:0.1f}')

    with open(filename, 'wb') as file :
        pickle.dump(result, file)
        pickle.dump(average, file)
