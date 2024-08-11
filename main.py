import pandas as pd
from sklearn.tree import DecisionTreeRegressor


melbourne_file_path = 'melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
melbourne_data = melbourne_data.dropna(axis=0)
y = melbourne_data.Price
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = melbourne_data[melbourne_features]


melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X, y)


def predict_price():
    print("Enter the details for the house:")

    rooms = float(input("Number of rooms: "))
    bathroom = float(input("Number of bathrooms: "))
    landsize = float(input("Landsize (in square meters): "))
    lattitude = float(input("Latitude: "))
    longtitude = float(input("Longitude: "))
    

    user_input = pd.DataFrame({
        'Rooms': [rooms],
        'Bathroom': [bathroom],
        'Landsize': [landsize],
        'Lattitude': [lattitude],
        'Longtitude': [longtitude]
    })
    

    predicted_price = melbourne_model.predict(user_input)
    
    print(f"The predicted price for the house is: ${predicted_price[0]:,.2f}")


predict_price()
