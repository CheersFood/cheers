from load_data import data
from reccommender import algo

trainingSet = data.build_full_trainset()

algo.fit(trainingSet)


prediction = algo.predict('E', 2)
print(prediction.est)
print("Hiya! Supdogvdsdlkfv")