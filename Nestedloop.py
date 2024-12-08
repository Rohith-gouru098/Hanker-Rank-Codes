if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    score = sorted(set(student [1]for student in students))
    second_lowest_score = score[1]
    second_lowest_score = [student[0] for student in students if student[1] == second_lowest_score]
    second_lowest_score.sort()
    for name in second_lowest_score:
        print(name)    
        
        
