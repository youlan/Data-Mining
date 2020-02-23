import numpy as np


def page_rank(V, E, init, debug=False):
    # construct the graph
    graph = np.zeros([V, V])
    for edge in E:
        start = edge[0]
        end = edge[1]
        graph[start - 1, end - 1] = 1

    T = np.zeros([V, V])

    for i in range(V):
        if np.sum(graph[i, :]) == 0.0:
            T[i, :] = 1 / V
        else:
            T[i, :] = graph[i, :] / np.sum(graph[i, :])
    print(T)
    alpha = 0.2
    maxIter = 100
    epsi = 1e-9
    print(epsi)
    pcurr = init

    for t in range(maxIter):
        pnext = np.matmul(np.transpose(alpha * np.identity(V) + (1 - alpha) * T), pcurr)
        err = np.sum(np.abs(pnext - pcurr))
        if debug:
            print('iter %d - err = %.5f' % (t + 1, err))

        if err < epsi:
            break
        pcurr = pnext

    return pcurr


def main():
    # num of vertices
    V = 7
    # egdes
    E = [[1, 5], [1, 2], [2, 1], [3, 6], [4, 5], [4, 7], [5, 4], [5, 1], [6, 5], [6, 4], [7, 2], [7, 5]]

    n_trials = 100
    res = np.zeros(shape=[n_trials, V])

    for i in range(n_trials):
        init = np.random.uniform(0, 1, size=V)
        #init = np.ones(V)
        #         init = np.ones(V)/V
        p = page_rank(V, E, init, debug=False)
        res[i, :] = p

    pavg = np.mean(res, axis=0)
    print(pavg)


if __name__ == '__main__':
    main()