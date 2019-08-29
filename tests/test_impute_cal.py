import unittest
from unittest.mock import Mock, patch
import impute_cal


@patch('impute_cal.get_current_weight')
class GetWeightsAndCalsTest(unittest.TestCase):

    def test_gets_weights_and_cals(self, mock_get_current_weight):
        workbook = Mock()
        workbook.nrows = 13
        workbook.cell.side_effect = [
            Mock(value=250),
            Mock(value=207),
            Mock(value=206),
            Mock(value=205),
            Mock(value=204),
            Mock(value=203),
            Mock(value=202),
            Mock(value=201),
            Mock(value=2007),
            Mock(value=2006),
            Mock(value=2005),
            Mock(value=2004),
            Mock(value=2003),
            Mock(value=2002),
            Mock(value=2001)
        ]
        impute_cal.get_weights_and_cals(workbook)
        mock_get_current_weight.assert_called_once_with(
            [207, 206, 205, 204, 203, 202, 201],
            [2007, 2006, 2005, 2004, 2003, 2002, 2001],
            250
        )

    def test_breaks_on_blank(self, mock_get_current_weight):
        workbook = Mock()
        workbook.nrows = 13
        workbook.cell.side_effect = [
            Mock(value=250),
            Mock(value=200),
            Mock(value=199),
            Mock(value=''),
            Mock(value=2000),
            Mock(value='')
        ]
        impute_cal.get_weights_and_cals(workbook)  # should not raise
        mock_get_current_weight.assert_called_once_with([200, 199], [2000], 250)


@patch('impute_cal.get_weight_changes')
class GetCurrentWeightTest(unittest.TestCase):

    @patch('builtins.input')
    def test_current_weight_obtained_from_input(
        self, mock_input, mock_get_weight_changes
    ):
        mock_input.return_value = 199
        impute_cal.get_current_weight([200], [2000], 250)
        mock_get_weight_changes.assert_called_once_with([200], [2000], 250, 199)

    def test_current_weight_already_in_workbook(self, mock_get_weight_changes):
        impute_cal.get_current_weight([200, 199], [2000], 250)
        mock_get_weight_changes.assert_called_once_with([200], [2000], 250, 199)

    def test_raises_when_more_cals_than_weights(self, mock_get_weight_changes):
        self.assertRaises(
            Exception, impute_cal.get_current_weight, [200], [2000, 2001], 250,
            msg="Weight-Cal mismatch error"
        )
        mock_get_weight_changes.assert_not_called()


@patch('impute_cal.impute_calories')
class GetWeightChangesTest(unittest.TestCase):

    def test_weight_changes_are_correct(self, mock_impute_calories):
        impute_cal.get_weight_changes([200, 199.4, 198], [2000, 2001], 250, 197)
        mock_impute_calories.assert_called_once_with(
            [2000, 2001], [-50, -0.6, -1.4], 197, 198
        )


@patch('builtins.print')
class ImputeCaloriesTest(unittest.TestCase):

    def test_correct_imputed_calories_are_printed(self, mock_print):
        impute_cal.impute_calories(
            [2000, 2350, 1650], [-0.2, -0.1, -0.3], 200, 200.2)
        mock_print.assert_called_once_with('Imputed Calories: 2000')


if __name__ == '__main__':
    unittest.main()
