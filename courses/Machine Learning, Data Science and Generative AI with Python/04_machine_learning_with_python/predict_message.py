def predict_message(classifer, features, predicts, value):
    msg_0 = f"{classifer} Prediction for \n"
    msg_1 = "{} = {}, \n{} = {}, \n{} = {}, \n".format(
        features[0],
        predicts[0],
        features[1],
        predicts[1],
        features[2],
        predicts[2],
    )
    msg_2 = "{} = {}, \n{} = {}, \n{} = {}: ".format(
        features[3],
        predicts[3],
        features[4],
        predicts[4],
        features[5],
        predicts[5],
    )
    msg = msg_0 + msg_1 + msg_2
    predict = "YES \n" if value == 1 else "NO \n"
    print(msg, predict)
