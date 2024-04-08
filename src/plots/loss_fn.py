import matplotlib.pyplot as plt

def plot_loss_fn(runtime_data):
    data = runtime_data['best_scores']
    data.append((runtime_data['params']['iter'], runtime_data['best_scores'][-1][1]))
    x, y = zip(*data)

    plt.step(x, y, where='post')

    plt.title('Best solution score over time')
    plt.xlabel('Iterations')
    plt.ylabel('Score')

    plt.show()
