from calc import Calc_block as c_calc
from log import result_logger as write_log
import transform as d_t
import view as c_ui


def button_click():
    j = d_t.data_formatting(c_ui.input_data())
    calc_result = c_calc(j)
    c_ui.view_data(calc_result, 'Ответ:')
    write_log(j, calc_result)

button_click()