import csv
import os
import glob

from statistics import mean

def hietool():
    target_dir_path = './data_test'
    files = os.listdir(target_dir_path)
    folders = [f for f in files if os.path.isdir(os.path.join(target_dir_path, f))]
    for folder in folders:
        folder_path = os.path.join(target_dir_path, folder)
        precision_1_list = []
        precision_2_list = []
        precision_3_list = []
        recall_1_list = []
        recall_2_list = []
        recall_3_list = []
        accuracy_1_list = []
        accuracy_2_list = []
        accuracy_3_list = []
        for file in glob.glob('{}/*.csv'.format(folder_path)):
            list_4, list_5 = unko(file)
            precision_1_list.append(list_4[1])
            precision_2_list.append(list_4[3])
            precision_3_list.append(list_4[5])
            recall_1_list.append(list_4[2])
            recall_2_list.append(list_4[4])
            recall_3_list.append(list_4[6])
            accuracy_1_list.append(list_5[1])
            accuracy_2_list.append(list_5[3])
            accuracy_3_list.append(list_5[5])
        with open('{}./output.txt'.format(folder_path), 'w') as f:
            output_string = "precision1-mean:{}\n".format(mean(precision_1_list))
            f.write(output_string)
            output_string = "precision2-mean:{}\n".format(mean(precision_2_list))
            f.write(output_string)
            output_string = "precision3-mean:{}\n".format(mean(precision_3_list))
            f.write(output_string)
            output_string = "recall1-mean:{}\n".format(mean(recall_1_list))
            f.write(output_string)
            output_string = "recall2-mean:{}\n".format(mean(recall_2_list))
            f.write(output_string)
            output_string = "recall3-mean:{}\n".format(mean(recall_3_list))
            f.write(output_string)
            output_string = "accuracy1-mean:{}\n".format(mean(accuracy_1_list))
            f.write(output_string)
            output_string = "accuracy2-mean:{}\n".format(mean(accuracy_2_list))
            f.write(output_string)
            output_string = "accuracy3-mean:{}\n".format(mean(accuracy_3_list))
            f.write(output_string)


def unko(csv_file_path):
    #csvを読み込みモードで開く
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        next(f)
        L = []
        # カッコつけたいお年頃なので，本当は2重ループのリスト内包表記で書きたい．
        for row in reader:
            row = row[1:]
            num_list = [int(num) for num in row]
            L.append(num_list)
        #各値を計算
        precision_1 = L[1][1]/(L[1][1]+L[0][1])
        precision_2 = L[0][2]/(L[0][2]+L[1][2])
        precision_3 = L[0][4]/(L[0][4]+L[1][4])
        recall_1 = L[1][1]/(L[1][1]+L[1][0])
        recall_2 = L[0][2]/(L[0][2]+L[0][3])
        recall_3 = L[0][4]/(L[0][4]+L[0][5])
        accuracy_1 = L[1][1]+L[0][0]/L[1][1]+L[0][1]+L[0][0]+L[1][0]
        accuracy_2 = L[0][2]+L[0][3]/L[0][2]+L[1][2]+L[1][3]+L[0][3]
        accuracy_3 = L[0][4]+L[0][5]/L[0][4]+L[1][4]+L[1][5]+L[0][5]
        #書き込み用のリストを作成
        writein_list_4 = ['', precision_1, recall_1, precision_2, recall_2, precision_3, recall_3]
        writein_list_5 = ['', accuracy_1, '', accuracy_2, '', accuracy_3, '']
    
    with open(csv_file_path, 'a') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(writein_list_4)
        writer.writerow(writein_list_5)

    return writein_list_4, writein_list_5

def main():
    hietool()


if __name__ == '__main__':
    main()  