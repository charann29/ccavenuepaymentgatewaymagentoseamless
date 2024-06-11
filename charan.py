def split(df):
    y = df.type
    x = df.drop(columns=['type'])
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
    # Ensure arrays are writable
    return x_train.copy(), x_test.copy(), y_train.copy(), y_test.copy()  
