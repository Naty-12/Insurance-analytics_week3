from sklearn.model_selection import train_test_split

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split features and target into training and testing sets.

    Parameters:
    - X: pd.DataFrame or np.array of features
    - y: pd.Series or np.array of target variable
    - test_size: float, proportion of data to use as test set (default 0.2)
    - random_state: int, for reproducibility (default 42)

    Returns:
    - X_train, X_test, y_train, y_test
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)