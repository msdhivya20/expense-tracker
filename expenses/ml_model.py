import numpy as np

from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score



def predict_expense(expense_amounts):

    if len(expense_amounts) < 2:
        return 0, 0

    try:

        X = np.array(
            range(
                len(expense_amounts)
            )
        ).reshape(-1, 1)

        y = np.array(
            expense_amounts
        )

        model = LinearRegression()

        model.fit(
            X,
            y
        )

        next_month = np.array([
            [len(expense_amounts)]
        ])

        prediction = model.predict(
            next_month
        )[0]

        score = model.score(
            X,
            y
        )

        confidence = round(
            max(score * 100, 0),
            1
        )

        return (
            round(prediction, 2),
            confidence
        )

    except:

        average = sum(
            expense_amounts
        ) / len(
            expense_amounts
        )

        return (
            round(
                average,
                2
            ),
            50
        )