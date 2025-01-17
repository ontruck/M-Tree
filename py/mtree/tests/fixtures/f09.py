from .generator import ADD, REMOVE, QUERY

"""
actions = '9a9r9a9r'
dimensions = 4
remove_chance = 0.1
"""

DIMENSIONS = 4


def PERFORM(callback):
    callback(ADD((68, 44, 73, 57), QUERY((17, 97, 81, 83), 42.784442863746406, 5)))
    callback(ADD((42, 87, 68, 6), QUERY((10, 61, 88, 25), 73.93310431102259, 1)))
    callback(ADD((79, 7, 73, 18), QUERY((73, 19, 7, 34), 19.205573387935146, 5)))
    callback(ADD((45, 58, 20, 13), QUERY((97, 98, 55, 83), 26.76471679640736, 3)))
    callback(ADD((58, 6, 79, 52), QUERY((57, 12, 66, 0), 71.38694037383586, 6)))
    callback(ADD((70, 0, 56, 12), QUERY((48, 66, 10, 76), 43.80171544347283, 12)))
    callback(ADD((5, 0, 13, 34), QUERY((91, 20, 83, 13), 37.919455043424094, 12)))
    callback(ADD((39, 72, 33, 17), QUERY((23, 48, 92, 19), 54.78071067280567, 4)))
    callback(ADD((87, 55, 19, 22), QUERY((93, 97, 95, 37), 25.560790461542044, 14)))
    callback(REMOVE((5, 0, 13, 34), QUERY((9, 25, 88, 22), 37.66636491817968, 9)))
    callback(REMOVE((87, 55, 19, 22), QUERY((65, 2, 38, 30), 9.369935475863338, 9)))
    callback(REMOVE((70, 0, 56, 12), QUERY((13, 66, 60, 78), 65.15221976846887, 3)))
    callback(REMOVE((45, 58, 20, 13), QUERY((3, 20, 10, 29), 25.937573358112438, 4)))
    callback(REMOVE((58, 6, 79, 52), QUERY((19, 80, 70, 92), 42.94860504599718, 9)))
    callback(REMOVE((39, 72, 33, 17), QUERY((56, 19, 1, 11), 5.264807286707596, 6)))
    callback(REMOVE((68, 44, 73, 57), QUERY((72, 77, 3, 96), 60.572073077310506, 7)))
    callback(REMOVE((79, 7, 73, 18), QUERY((88, 45, 4, 31), 53.85840171887337, 1)))
    callback(REMOVE((42, 87, 68, 6), QUERY((89, 35, 29, 61), 0.9244156692733707, 3)))
    callback(ADD((47, 84, 71, 86), QUERY((76, 95, 97, 18), 34.290691053989875, 2)))
    callback(ADD((49, 3, 39, 57), QUERY((61, 65, 12, 80), 1.937394159739032, 3)))
    callback(ADD((63, 66, 68, 50), QUERY((56, 43, 4, 62), 18.687738989551903, 5)))
    callback(ADD((47, 77, 73, 48), QUERY((100, 60, 72, 50), 52.29319570377506, 1)))
    callback(ADD((5, 47, 31, 97), QUERY((6, 77, 54, 71), 19.48341283310528, 9)))
    callback(ADD((46, 75, 89, 51), QUERY((58, 89, 76, 39), 34.76741996350512, 3)))
    callback(ADD((31, 53, 26, 47), QUERY((0, 40, 47, 23), 16.921204977514233, 12)))
    callback(ADD((30, 41, 99, 83), QUERY((87, 12, 78, 86), 30.2934225040193, 5)))
    callback(ADD((7, 44, 18, 71), QUERY((50, 85, 9, 88), 5.111369978819784, 10)))
    callback(REMOVE((47, 84, 71, 86), QUERY((73, 3, 61, 27), 66.71341825678114, 11)))
    callback(REMOVE((46, 75, 89, 51), QUERY((56, 14, 40, 59), 69.77090723811857, 12)))
    callback(REMOVE((5, 47, 31, 97), QUERY((31, 84, 11, 49), 48.25997801607295, 4)))
    callback(REMOVE((49, 3, 39, 57), QUERY((30, 13, 11, 85), 8.569859754324751, 9)))
    callback(REMOVE((47, 77, 73, 48), QUERY((94, 44, 17, 41), 57.38667609637716, 1)))
    callback(REMOVE((7, 44, 18, 71), QUERY((26, 87, 4, 69), 73.7114765530958, 4)))
    callback(REMOVE((31, 53, 26, 47), QUERY((71, 69, 6, 15), 5.990022623900524, 5)))
    callback(REMOVE((63, 66, 68, 50), QUERY((24, 19, 72, 77), 69.95605525860272, 4)))
    callback(REMOVE((30, 41, 99, 83), QUERY((71, 79, 55, 33), 4.664416550638117, 3)))
