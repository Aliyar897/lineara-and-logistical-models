import numpy as np

def gradien_descent(x,y):
    m_occur = b_occur = 0
    iterations = 1000
    n =  len(x)
    learning_rate = 0.001

    for i in range(iterations):
        y_pridicted = m_occur * x + b_occur
        cost = (1/n)*sum( [val**2 for val in (y-y_pridicted)])
        md = -(2/n)*sum(x*(y-y_pridicted))
        bd = -(2/n)*sum(y-y_pridicted)
        m_occur = m_occur - learning_rate * md
        b_occur = b_occur - learning_rate * bd
        print('m {} b {} iterations {}'.format(m_occur, b_occur, i))




x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])