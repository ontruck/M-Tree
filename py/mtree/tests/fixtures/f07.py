from ...tests.fixtures.generator import ADD, REMOVE, QUERY

"""
actions = '7a7r7a7r'
dimensions = 3
remove_chance = 0.1
"""

DIMENSIONS = 3


def PERFORM(callback):
    callback(ADD((51, 3, 58), QUERY((95, 21, 60), 69.32670153503543, 3)))
    callback(ADD((71, 50, 3), QUERY((26, 19, 85), 63.059398537105345, 4)))
    callback(ADD((55, 43, 54), QUERY((84, 39, 74), 59.79041780570793, 3)))
    callback(ADD((24, 96, 96), QUERY((27, 83, 30), 42.79267677088545, 2)))
    callback(ADD((55, 99, 14), QUERY((54, 92, 5), 79.29962142613402, 9)))
    callback(ADD((60, 50, 72), QUERY((34, 77, 26), 5.0697555265270555, 3)))
    callback(ADD((50, 24, 3), QUERY((96, 52, 97), 10.922290203972134, 1)))
    callback(REMOVE((71, 50, 3), QUERY((73, 44, 68), 64.59894916046194, 11)))
    callback(REMOVE((55, 43, 54), QUERY((72, 18, 60), 45.160922442438284, 4)))
    callback(REMOVE((50, 24, 3), QUERY((31, 0, 50), 34.53510019728081, 5)))
    callback(REMOVE((51, 3, 58), QUERY((37, 74, 66), 68.97613539772058, 7)))
    callback(REMOVE((55, 99, 14), QUERY((93, 14, 9), 50.97986579925154, 1)))
    callback(REMOVE((60, 50, 72), QUERY((34, 72, 24), 28.154382433954204, 1)))
    callback(REMOVE((24, 96, 96), QUERY((41, 92, 88), 31.91033800897489, 5)))
    callback(ADD((55, 64, 28), QUERY((97, 96, 39), 79.69903498836767, 2)))
    callback(ADD((36, 48, 23), QUERY((73, 98, 74), 78.47640052538631, 5)))
    callback(ADD((49, 79, 32), QUERY((79, 76, 79), 18.279981673193433, 8)))
    callback(ADD((22, 97, 58), QUERY((70, 54, 9), 51.77659016861129, 2)))
    callback(ADD((53, 39, 7), QUERY((45, 0, 72), 65.8151966292113, 11)))
    callback(ADD((90, 61, 72), QUERY((48, 65, 81), 8.58232542684278, 11)))
    callback(ADD((60, 82, 88), QUERY((72, 12, 96), 19.189115684003415, 3)))
    callback(REMOVE((60, 82, 88), QUERY((78, 80, 98), 56.27211343849702, 2)))
    callback(REMOVE((90, 61, 72), QUERY((53, 92, 59), 22.97164245980296, 7)))
    callback(REMOVE((49, 79, 32), QUERY((67, 64, 75), 24.005541537473107, 9)))
    callback(REMOVE((22, 97, 58), QUERY((32, 77, 25), 57.57893853234587, 3)))
    callback(REMOVE((55, 64, 28), QUERY((91, 34, 12), 0.757066404546638, 3)))
    callback(REMOVE((36, 48, 23), QUERY((61, 99, 85), 78.41497511960426, 2)))
    callback(REMOVE((53, 39, 7), QUERY((53, 8, 35), 17.050371057818285, 1)))
