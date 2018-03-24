# import librarys needed
import numpy as np
import function
import config_parser
import integration as ite
import matplotlib.pyplot as plt

# configurations 
CONFIG_NAME = "config.conf"
config = config_parser.parse(CONFIG_NAME)

def plotter(ax, data1, data2):
    out = ax.plot(data1, data2)
    return out

# test routine
def run_test(config):
    left = config["region"]["left"]
    right = config["region"]["right"]
    point_count = config["count"] - 1
    step = (right-left)/config["count"]
    
    # Compute x
    x = np.linspace(left, right, point_count)
    y = function.u_explicit(x)

    # Compute (f, Phi_i)
    F = np.zeros((point_count, 1))
    for i in range(1, point_count):
        func_to_ite = lambda x: function.f(x)*function.phi_i(step, i, x)
        F[i-1] = ite.rectangle(func_to_ite, step*(i-1), step*(i+1))
    
    # Compute A
    A = np.eye(point_count)*2
    P1 = np.eye(point_count, k=1)*(-1)
    P2 = np.eye(point_count, k=-1)*(-1)
    A = A + P1 + P2
    A = A*(1/step)

    # Solve equation Au = F
    A_inv = np.linalg.inv(A)
    u = A_inv*np.asmatrix(F)

    # Plot
    fig, ax_list = plt.subplots(2, 2, sharex=True)
    ax_list[0, 0].set_title('u_explicit')
    ax_list[0, 0].plot(x, y)

    ax_list[0, 1].set_title('u_computed')
    ax_list[0, 1].plot(x, u)
    
    ax_list[1, 0].set_title('comparison')
    ax_list[1, 0].plot(x, u, label='u_computed')
    ax_list[1, 0].plot(x, y, label='u_explicit')
    ax_list[1, 0].legend()

    ax_list[1, 1].set_title('error')
    e = np.transpose(np.asmatrix(y)-np.transpose(u))
    ax_list[1, 1].plot(x, e, label="u-y")
    ax_list[1, 1].plot(x, 0*x, label='baseline')
    ax_list[1, 1].set_ylim(-0.5, 0.5)
    ax_list[1, 1].legend()
    
    plt.show()

    
# main calling
run_test(config["test1"])