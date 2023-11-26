import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def make_model() :
    df = pd.read_csv("./data/cancer_prediction_dataset.csv")
    
    # X, y로 분리
    X = df.iloc[ : , : -1]
    y = df.iloc[ : , -1]
    
    # train, test로 나누기
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
   
    # 로지스틱 선형 회귀 모델 만들기
    model = LogisticRegression()

    # 모델 학습
    model.fit(X_train, y_train)

    # 테스트해서 검증
    y_pred = model.predict(X_test)

    # 정답률 
    ac = accuracy_score(y_test, y_pred)
    
    return model, ac
