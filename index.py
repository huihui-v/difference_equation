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
    for i in range(1, point_count+1):
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

def run_test2(config):
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
    A1 = np.zeros((point_count, point_count))
    A2 = np.zeros((point_count, point_count))
    for j in range(1, point_count+1):
        for i in range(1, point_count+1):
            func1 = lambda x: function.p(x)*function.dphi_i(step, i, x)*function.dphi_i(step,j,x)
            func2 = lambda x: function.q(x)*function.phi_i(step, i, x)*function.phi_i(step,j,x)
            if (abs(j-i) <= 1):
                A1[j-1,i-1] = ite.rectangle(func1, step*(i-1), step*(i+1))
                A2[j-1,i-1] = ite.rectangle(func2, step*(i-1), step*(i+1))
            else:
                A1[j-1,i-1] = 0
                A2[j-1,i-1] = 0
    A = A1+A2
    print (function.phi_i(step, 1, 0.01))

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
    print ('average error: ', sum(e)/e.size)

    plt.show()
    
def run_test3(config):
    # 有限元次数
    k = 1

    left = config["region"]["left"]
    right = config["region"]["right"]
    # 包含左右端点的剖分点计数
    point_count = config["count"] + 1
    # 步长
    step = (right-left)/config["count"]
    
    # Compute x (不包含左右端点的每个剖分点x坐标)
    x = np.linspace(left, right, point_count)

    # 单元刚度矩阵和F的计算
    K_unit = []
    F_unit = []
    for i in range(0,point_count-1):
        A = np.zeros((k+1, k+1))
        F = np.zeros((k+1, 1))
        for t1 in range(0,k+1):
            for t2 in range(0,k+1):
                func1 = lambda u: function.p(u)*function.dphi(x[i],x[i+1],t1,k,u)*function.dphi(x[i],x[i+1],t2,k,u)
                func2 = lambda u: function.q(u)*function.phi(x[i],x[i+1],t1,k,u)*function.phi(x[i],x[i+1],t2,k,u)
                A[t1,t2] = ite.rectangle(func1,x[i],x[i+1]) + ite.rectangle(func2,x[i],x[i+1])
            F[t1] = ite.rectangle(lambda u: function.f(u)*function.phi(x[i],x[i+1],t1,k,u), x[i], x[i+1])
        if (i == 0):
            A = np.delete(A,0,0)
            A = np.delete(A,0,1)
            F = np.delete(F,0,0)
        elif (i == point_count-2):
            A = np.delete(A,k,0)
            A = np.delete(A,k,1)
            F = np.delete(F,k,0)
        K_unit.append(A)
        F_unit.append(F)
        # func1 = phi(c,d,l,k)

    # 总刚度矩阵生成
    A = K_unit[0]
    F = F_unit[0]
    for i in range(1,point_count-1):
        l1 = A.shape[0]
        l2 = K_unit[i].shape[0]
        A2 = np.concatenate((np.zeros((l1-1,l1+l2-1)),
                            np.concatenate((np.zeros((l2,l1-1)),K_unit[i]),1)), 0)
        A1 = np.concatenate((np.concatenate((A,np.zeros((l1,l2-1))),1),
                            np.zeros((l2-1,l1+l2-1))),0)
        A = A1+A2
        F2 = np.concatenate((np.zeros((l1-1,1)),
                            F_unit[i]),0)
        F1 = np.concatenate((F,
                            np.zeros((l2-1,1))),0)
        F = F1+F2
    
    # 计算u值
    A_inv = np.linalg.inv(A)
    u = A_inv*np.asmatrix(F)
    t = []
    t.extend([0])
    t.extend(u)
    t.extend([0])
    u = t

    x = np.linspace(left, right, (point_count-1)*k+1)
    y = function.u_explicit(x)

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
    print ('average error: ', sum(e)/e.size)

    plt.show()

# main calling
# run_test(config["test1"])
# run_test2(config["test1"])
run_test3(config["test1"])