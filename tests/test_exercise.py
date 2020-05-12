import pytest
import src.exercise

def test_exercise():
    input_values = ["chelsea,2017","luke,2017","lily,2014","hanna,2010",""]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert output == ["","","","","","Longest name: chelsea","Average of the birth years: 2014.5"]
