import os
import csv
import time
import pickle
import numpy as np
import pandas as pd
from datetime import datetime
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from scipy.sparse import csr_matrix, save_npz, load_npz

folder = os.getcwd()


class SVM:
    """
    Supported Vector Machines
    """

    def get_words():
        t0 = time.time()
        file1 = open(f"{folder}/scripts/svm/all_words.txt", "r")
        lines = file1.readlines()
        file1.close()
        lines = [line.replace("\n", "") for line in lines]
        new1 = [lines[0]]
        for i in range(len(lines)):
            item = lines[i]
            last = new1[-1]
            len_last = len(last)
            len_item = len(item)
            get = False
            if len_last < len_item:
                for j in range(len_last, 2, -1):
                    if item[:j] == last[:j]:
                        new1[-1] = item[:j]
                        get = True
                if not get:
                    new1.append(item)
            else:
                for j in range(len_item, 2, -1):
                    if item[:j] == last[:j]:
                        new1[-1] = item[:j]
                        get = True
                if not get:
                    new1.append(item)
        w_file = open(f"{folder}/scripts/svm/training_words.txt", "w")
        for item in new1:
            w_file.write(item + "\n")
        w_file.close()
        t1 = time.time()
        result = "Total time to get words: %s" % (t1 - t0)
        print(result)
        return result

    def get_xarray(num, up, down):
        t0 = time.time()
        feature = []
        csv.field_size_limit(100000000)
        file1 = open("training_words.txt", "r")
        lines = file1.readlines()
        file1.close()
        lines = [line.replace("\n", "") for line in lines]
        with open("dataset.csv", newline="") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=" ", quotechar="|")
            a = 0
            for row in spamreader:
                new_row = " ".join([item.lower() for item in row])
                fetch = []
                for item in lines:
                    (
                        fetch.append(str(up))
                        if item in new_row
                        else fetch.append(str(down))
                    )
                feature.append(
                    {
                        "c": fetch,
                        "label": -1 if "spam" in new_row[-1] else 1,
                    }
                )
                a += 1
                if a > num - 1:
                    break
        b = 1
        while b > 0:
            c = "0%s" % (b) if b < 100 else str(b)
            if b < 10:
                c = "00%s" % (b) if b < 10 else "0%s" % (b)
            exist = os.path.exists("trained_{0}.txt".format(c))
            if exist:
                b += 1
            else:
                break
        w_file = open("trained_{0}.txt".format(c), "w")
        for item in feature:
            w_file.write(",".join(item["c"]) + "||" + str(item["label"]) + "\n")
        w_file.close()
        t1 = time.time()

        print("Total time to get x array: %s" % (t1 - t0))
        result = "trained_{0}.txt".format(c)
        return result

    def get_train():
        t0 = time.time()
        b = 1
        while b > 0:
            c = "0%s" % (b) if b < 100 else str(b)
            if b < 10:
                c = "00%s" % (b)
            exist = os.path.exists("trained_{0}.txt".format(c))
            if exist:
                pass
            else:
                doc = "0%s" % (b - 1) if b < 100 else str(b - 1)
                if b < 10:
                    doc = "00%s" % (b - 1)
                break
            b += 1
        file1 = open("trained_{0}.txt".format(doc), "r")
        lines = file1.readlines()
        file1.close()
        lines = [line.replace("\n", "") for line in lines]
        new_file = "trained_{0}_mat_{1}.txt".format(doc, len(lines))
        if not os.path.exists(new_file):
            w_file = open(new_file, "w")
            for item in lines:
                w_file.write(item)
            w_file.close()
        arr1 = [l.split("||")[0] for l in lines]
        arr2 = [a.split(",") for a in arr1]
        arr3 = []
        brr1 = [l.split("||")[1] for l in lines]
        brr2 = [int(t) for t in brr1]
        for item in arr2:
            arr3.append([float(k) for k in item])

        dim_D = len(arr3[0])
        dim_l = len(lines)

        b = np.array([0 for i in range(dim_D)])
        d = 0
        for i in range(dim_D):
            b[i] = brr2[d]
            d += 1
            if d + 1 == dim_l:
                d = 0
        wx = np.ones(dim_D)
        A = np.vstack([wx, np.ones(len(wx))]).T
        m, c = np.linalg.lstsq(A, b, rcond=None)[0]
        r = [m, c]

        # use least squares (c) in wx = +/- 1 + b
        a = np.array([np.zeros(dim_D) for i in range(dim_D)])
        b = np.array([c for i in range(dim_D)])
        d = 0
        for i in range(dim_D):
            a[i] = arr3[d]
            b[i] = b[i] + brr2[d]
            d += 1
            if d + 1 == dim_l:
                d = 0

        Apinv = np.linalg.pinv(a)
        w = Apinv.dot(b)
        w_file = open("w_{0}_mat_{1}.txt".format(doc, dim_l), "w")
        for item in w:
            w_file.write(str(item) + "\n")
        w_file.close()
        b_file = open("b_{0}_mat_{1}.txt".format(doc, dim_l), "w")
        for item in b:
            b_file.write(str(item) + "\n")
        b_file.close()
        r_file = open("r_{0}_mat_{1}.txt".format(doc, dim_l), "w")
        for item in r:
            r_file.write(str(round(item, 4)) + "\n")
        r_file.close()

        t1 = time.time()
        result = "Total time to get train: %s" % (t1 - t0)
        print(result)
        return result

    def test(input):
        file1 = open("001_w_mat_2410.txt", "r")
        w = file1.readlines()
        file1.close()
        file1 = open("001_b_mat_2410.txt", "r")
        b = file1.readlines()
        file1.close()
        file1 = open("001_r_mat_2410.txt", "r")
        r = file1.readlines()
        file1.close()
        file1 = open("001_t_mat_2410.txt", "r")
        t = file1.readlines()
        file1.close()

        w = [line.replace("\n", "") for line in w]
        b = [line.replace("\n", "") for line in b]
        r = [line.replace("\n", "") for line in r]
        t = [line.replace("\n", "") for line in t]

        input = "Subject: " + input
        fetch = []
        for item in t:
            fetch.append(1) if item in input else fetch.append(0)
        w = np.array([float(item) for item in w])
        v = np.array(fetch)
        y = w.dot(v)
        print("y: ", y)
        result = "spam"
        if round(y, 4) == round(float(r[1]), 4):
            result = "ham"
        print("result: ", result)
        return result

    def get_df_words():
        t1 = time.time()
        class_1 = "spam"
        class_2 = "ham"
        # # Load a CSV file from a local path
        # file_path = f"{folder}/scripts/svm/dataset.csv"
        file_path = f"{folder}/scripts/svm/dataset.xlsx"
        # df_excel = f"{folder}/scripts/svm/dataset.xlsx"
        # print(df_excel)
        messages = []
        classes = []
        indices = []
        df = pd.read_excel(file_path)
        # Check for correct dimension in dataset
        try:
            if df.shape[1] == 2:
                print("ok")
            else:
                print("Dataset must have two columns.")
        except IndexError:
            print("Incorrect dataset column index.")

        is_excel_file = True
        if is_excel_file:
            column_names = df.columns.tolist()
            names = []
            for name in column_names:
                if "Unnamed" not in name:
                    names.append(name)
            if len(names) > 2:
                print("error")

            key1 = names[0]
            key2 = names[1]
            for index, row in df.iterrows():
                if class_1 in row[key1] or class_2 in row[key1]:
                    if class_1 in row[key1]:
                        classes.append(class_1)
                        messages.append(row[key2])
                        indices.append(index)
                    elif class_2 in row[key1]:
                        classes.append(class_2)
                        messages.append(row[key2])
                        indices.append(index)
                else:
                    if class_1 in row[key2]:
                        classes.append(class_1)
                        messages.append(row[key1])
                        indices.append(index)
                    elif class_2 in row[key2]:
                        classes.append(class_2)
                        messages.append(row[key1])
                        indices.append(index)

        if not is_excel_file:
            for index, row in df.iterrows():
                # message is row.iloc[0]
                # class is row.iloc[1]
                if class_1 in row.iloc[0] or class_2 in row.iloc[0]:
                    if class_1 in row.iloc[0]:
                        classes.append(class_1)
                        messages.append(row.iloc[1])
                        indices.append(index)
                    elif class_2 in row.iloc[0]:
                        classes.append(class_2)
                        messages.append(row.iloc[1])
                        indices.append(index)
                else:
                    if class_1 in row.iloc[1]:
                        classes.append(class_1)
                        messages.append(row.iloc[0])
                        indices.append(index)
                    elif class_2 in row.iloc[1]:
                        classes.append(class_2)
                        messages.append(row.iloc[0])
                        indices.append(index)

        # Check for more than three classes in the
        data = DataFrame({"message": messages, "class": classes}, index=indices)

        vectorizer = CountVectorizer()
        counts = vectorizer.fit_transform(data["message"].values)

        now = datetime.now().strftime("%Y%m%d%H%M%S")
        count_vectorizer_file = f"{folder}/scripts/svm/{now}.pkl"
        with open(count_vectorizer_file, "wb") as f:
            pickle.dump(vectorizer, f)

        classifier = MultinomialNB()
        targets = data["class"].values
        target_values_file = f"{folder}/scripts/svm/{now}.txt"
        write_file = open(target_values_file, "w")
        for item in targets:
            write_file.write(item + "\n")
        write_file.close()

        classifier.fit(counts, targets)

        examples = ["Free Viagra now!!!", "Hi Bob, how about a game of golf tomorrow?"]
        example_counts = vectorizer.transform(examples)
        predictions = classifier.predict(example_counts)
        print("predictions: ", predictions)
        t2 = time.time()
        print("elapsed: ", t2 - t1)
        # Save this result to Redis
        result = {
            "count": count_vectorizer_file,
            "target": target_values_file,
            "session": "12345678",
            "classes": [class_1, class_2],
        }
        print(result)
        return result


if __name__ == "__main__":
    # SVM.get_words()
    # get_xarray(a, 1, 0)
    # get_train()
    # input = "What is your jidei? "
    SVM.get_df_words()
    # SVM.test(input)
