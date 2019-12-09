"""Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке."""

list_of_words = []
with open("dataset_263150_4.txt") as txt_file:
    for line in txt_file:
        line = line.rstrip()
        list_of_words.append(line)

txt_ans = open("txt_answer.txt", "a")

for i in range(len(list_of_words) - 1, -1, -1):
    txt_ans.write(list_of_words[i] + "\n")

txt_ans.close()
