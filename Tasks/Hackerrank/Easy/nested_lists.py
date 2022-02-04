# Nested Lists
# ------------------------------------------------------------------------------



student_lst = []
scr_lst = []
final_scr = []
final_lst = []
for _ in range(int(input())):
    name = input()
    score = float(input())

    student_lst.append([name, score])
    scr_lst.append(score)
    std_lst = sorted(student_lst)

for scr in scr_lst:
    if scr > min(scr_lst):
        final_scr.append(scr)
sec_low_scr = min(final_scr)

for std in range(len(std_lst)):
    if std_lst[std][1] == sec_low_scr:
        final_lst.append(std_lst[std][0])

for fin in final_lst:
    print(fin)