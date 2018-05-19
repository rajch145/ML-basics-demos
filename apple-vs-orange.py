from sklearn import tree

class FruitPredictor():
    '''Below code will identify the fruit type between apple and orange.
    feature are the classification data for both fruits
    '''
    def predict(self):
        features = [[140,1],[138,1],[150,0],[160,1]]
        labels = [0,0,1,1]
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        print(clf.predict([[150,0]]))


if __name__=="__main__":
    predictor = FruitPredictor()
    predictor.predict()
