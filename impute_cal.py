import statsmodels.api as sm
import xlrd


def get_weights_and_cals(workbook):
    start_weight = workbook.cell(5, 5).value
    weights = []
    cals = []
    count = 0
    for row in range(11, workbook.nrows):
        count += 1
        for col in range(3, 10):
            cell_obj = workbook.cell(row, col).value
            try:
                float(cell_obj)
                if count % 2 == 1:
                    weights.append(cell_obj)
                else:
                    cals.append(cell_obj)
            except ValueError:
                break
    get_current_weight(weights, cals, start_weight)


def get_current_weight(weights, cals, start_weight):
    if len(weights) == len(cals):
        current_weight = float(input("Current Weight: "))
    elif len(weights) > len(cals):
        current_weight = weights[len(cals)]
        print("Current Weight: " + str(current_weight))
        weights = weights[:len(cals)]
    else:
        raise Exception("Weight-Cal mismatch error")
    get_weight_changes(weights, cals, start_weight, current_weight)


def get_weight_changes(weights, cals, start_weight, current_weight):
    prev_weight = start_weight
    weight_changes = []
    for item in weights:
        weight_changes.append(round(item - prev_weight, 1))
        prev_weight = item
    impute_calories(cals, weight_changes, current_weight, prev_weight)


def impute_calories(cals, weight_changes, current_weight, prev_weight):
    cals = sm.add_constant(cals)
    model = sm.OLS(weight_changes, cals).fit()
    intercept = model.params[0]
    slope = model.params[1]
    imputed_calories = ((current_weight - prev_weight) - intercept)/slope
    print(f'Imputed Calories: {round(int(imputed_calories))}')


if __name__ == '__main__':
    tdee_30 = xlrd.open_workbook('TDEE 3.0.xlsx').sheet_by_index(0)
    get_weights_and_cals(tdee_30)
