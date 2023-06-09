TITANIC_DATA_URL = (
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
)
X_COLS = [
    "Age",
    "Fare",
    "Parch",
    "Pclass",
    "SibSp",
]
Y_COLS = [
    "Survived",
]
COLS = X_COLS + Y_COLS
BATCH_SIZE = 64
LEARNING_RATE = 1e-3
EPOCHS = 100
